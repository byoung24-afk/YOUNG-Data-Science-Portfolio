from pathlib import Path

import streamlit as st

from data import load_tracks, make_preference_vector, prepare_features
from recommend import recommend_from_track, recommend_from_vector


DEFAULT_CSV_PATH = str(Path(__file__).parent / "Data" / "spotifytracks.csv")
PREFERENCE_FEATURES = [
    ("danceability", "Danceability", 0.0, 1.0, 0.01),
    ("energy", "Energy", 0.0, 1.0, 0.01),
    ("valence", "Valence", 0.0, 1.0, 0.01),
    ("acousticness", "Acousticness", 0.0, 1.0, 0.01),
    ("instrumentalness", "Instrumentalness", 0.0, 1.0, 0.01),
    ("tempo", "Tempo", 40.0, 220.0, 1.0),
]
KEY_OPTIONS = ["Any key", "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]


def display_results(results) -> None:
    columns = [
        "track_name",
        "artists",
        "album_name",
        "track_genre",
        "similarity",
        "danceability",
        "energy",
        "valence",
        "tempo",
    ]
    available_columns = [column for column in columns if column in results.columns]
    table = results[available_columns].copy()
    if "similarity" in table:
        table["similarity"] = table["similarity"].round(3)
    st.dataframe(table, use_container_width=True, hide_index=True)


def main() -> None:
    st.set_page_config(page_title="Spotify Track Recommender", page_icon="🎵", layout="wide")
    st.title("Spotify Track Recommender")
    st.caption("Find tracks with similar audio characteristics from your Spotify dataset.")

    with st.sidebar:
        st.header("Dataset")
        csv_path = st.text_input("CSV path", value=DEFAULT_CSV_PATH)
        top_n = st.slider("Recommendations", min_value=5, max_value=30, value=10)

    try:
        tracks = load_tracks(csv_path)
        feature_matrix, scaler, feature_columns = prepare_features(tracks)
    except (FileNotFoundError, ValueError) as error:
        st.error(str(error))
        st.stop()

    st.sidebar.success(f"Loaded {len(tracks):,} tracks")
    input_mode = st.radio(
        "How would you like to start?",
        ["Seed track", "Audio preferences"],
        horizontal=True,
    )
    genres = sorted(tracks["track_genre"].dropna().unique().tolist())
    selected_genres = st.multiselect("Optional genre filter", genres)

    if input_mode == "Seed track":
        track_labels = tracks.apply(
            lambda row: f"{row['track_name']} - {row['artists']}", axis=1
        ).tolist()
        selected_label = st.selectbox("Choose a seed track", track_labels)
        selected_index = track_labels.index(selected_label)

        if st.button("Recommend similar tracks", type="primary"):
            results = recommend_from_track(
                tracks,
                feature_matrix,
                selected_index,
                top_n=top_n,
                genres=selected_genres or None,
            )
            st.subheader("Recommended tracks")
            display_results(results)
    else:
        left, right = st.columns(2)
        preferences = {}
        for position, (feature, label, minimum, maximum, step) in enumerate(
            PREFERENCE_FEATURES
        ):
            target = left if position % 2 == 0 else right
            with target:
                preferences[feature] = st.slider(
                    label, minimum, maximum, (minimum + maximum) / 2, step=step
                )

        mode_label = st.selectbox("Preferred mode", ["Any", "Major", "Minor"])
        preferences["mode"] = {"Any": None, "Major": 1.0, "Minor": 0.0}[mode_label]
        key_label = st.selectbox("Preferred key", KEY_OPTIONS)
        preferences["key"] = None if key_label == "Any key" else KEY_OPTIONS.index(key_label) - 1

        if st.button("Find tracks", type="primary"):
            query_vector = make_preference_vector(preferences, scaler, feature_columns)
            results = recommend_from_vector(
                tracks,
                feature_matrix,
                query_vector,
                top_n=top_n,
                genres=selected_genres or None,
            )
            st.subheader("Recommended tracks")
            display_results(results)


if __name__ == "__main__":
    main()