from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler


METADATA_COLUMNS = ["track_name", "artists", "album_name", "track_genre"]
AUDIO_FEATURES = [
    "danceability",
    "energy",
    "loudness",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence",
    "tempo",
    "duration_ms",
]
REQUIRED_COLUMNS = METADATA_COLUMNS + AUDIO_FEATURES + ["key", "mode"]


def validate_schema(frame: pd.DataFrame) -> None:
    missing = [column for column in REQUIRED_COLUMNS if column not in frame.columns]
    if missing:
        raise ValueError(
            "The CSV is missing required columns: " + ", ".join(missing)
        )


@st.cache_data(show_spinner="Loading Spotify tracks...")
def load_tracks(csv_path: str) -> pd.DataFrame:
    path = Path(csv_path).expanduser()
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")

    frame = pd.read_csv(path)
    validate_schema(frame)
    return frame


@st.cache_data(show_spinner="Preparing recommendation features...")
def prepare_features(frame: pd.DataFrame) -> tuple[np.ndarray, StandardScaler, list[str]]:
    numeric = frame[AUDIO_FEATURES + ["key", "mode"]].apply(
        pd.to_numeric, errors="coerce"
    )
    numeric = numeric.fillna(numeric.median(numeric_only=True))

    key_radians = numeric["key"].fillna(0).mod(12) * (2 * np.pi / 12)
    features = numeric[AUDIO_FEATURES].copy()
    features["key_sin"] = np.sin(key_radians)
    features["key_cos"] = np.cos(key_radians)
    features["mode"] = numeric["mode"].fillna(0)

    scaler = StandardScaler()
    matrix = scaler.fit_transform(features)
    return matrix, scaler, list(features.columns)


def make_preference_vector(
    preferences: dict[str, Optional[float]],
    scaler: StandardScaler,
    feature_columns: list[str],
) -> np.ndarray:
    values = {feature: float(preferences.get(feature, 0.0)) for feature in AUDIO_FEATURES}
    key = preferences.get("key")
    if key is None:
        values["key_sin"] = scaler.mean_[feature_columns.index("key_sin")]
        values["key_cos"] = scaler.mean_[feature_columns.index("key_cos")]
    else:
        key_radians = float(key) % 12 * (2 * np.pi / 12)
        values["key_sin"] = np.sin(key_radians)
        values["key_cos"] = np.cos(key_radians)

    mode = preferences.get("mode")
    values["mode"] = (
        scaler.mean_[feature_columns.index("mode")]
        if mode is None
        else float(mode)
    )

    raw_vector = pd.DataFrame([[values[column] for column in feature_columns]], columns=feature_columns)
    return scaler.transform(raw_vector)