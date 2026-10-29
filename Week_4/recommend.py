import numpy as np
import pandas as pd
from typing import List, Optional
from sklearn.metrics.pairwise import cosine_similarity


def _rank_results(
    frame: pd.DataFrame,
    scores: np.ndarray,
    top_n: int,
    genres: Optional[List[str]] = None,
    excluded_index: Optional[int] = None,
) -> pd.DataFrame:
    ranked = frame.copy()
    ranked["similarity"] = scores

    if genres:
        ranked = ranked[ranked["track_genre"].isin(genres)]
    if excluded_index is not None and excluded_index in ranked.index:
        ranked = ranked.drop(index=excluded_index)

    return ranked.sort_values("similarity", ascending=False).head(top_n)


def recommend_from_vector(
    frame: pd.DataFrame,
    feature_matrix: np.ndarray,
    query_vector: np.ndarray,
    top_n: int = 10,
    genres: Optional[List[str]] = None,
    excluded_index: Optional[int] = None,
) -> pd.DataFrame:
    scores = cosine_similarity(query_vector, feature_matrix).ravel()
    return _rank_results(frame, scores, top_n, genres, excluded_index)


def recommend_from_track(
    frame: pd.DataFrame,
    feature_matrix: np.ndarray,
    track_index: int,
    top_n: int = 10,
    genres: Optional[List[str]] = None,
) -> pd.DataFrame:
    return recommend_from_vector(
        frame,
        feature_matrix,
        feature_matrix[track_index].reshape(1, -1),
        top_n=top_n,
        genres=genres,
        excluded_index=track_index,
    )