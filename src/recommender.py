import csv
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top-k songs sorted by descending score."""
        user_prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }

        scored_songs: List[Tuple[Song, float]] = []
        for song in self.songs:
            score, _ = score_song(user_prefs, song.__dict__)
            scored_songs.append((song, score))

        scored_songs.sort(key=lambda pair: pair[1], reverse=True)
        return [song for song, _ in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Generate a short human-readable reason string for one song."""
        user_prefs = {
            "favorite_genre": user.favorite_genre,
            "favorite_mood": user.favorite_mood,
            "target_energy": user.target_energy,
            "likes_acoustic": user.likes_acoustic,
        }
        _, reasons = score_song(user_prefs, song.__dict__)
        return "; ".join(reasons)


def _to_float(value: object, default: float = 0.0) -> float:
    """Safely convert a value to float."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _to_bool(value: object) -> bool:
    """Convert common truthy strings and values to bool."""
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "y"}
    return bool(value)

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from CSV and convert numeric columns to numeric types."""
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            songs.append(
                {
                    "id": int(row["id"]),
                    "title": row["title"],
                    "artist": row["artist"],
                    "genre": row["genre"],
                    "mood": row["mood"],
                    "energy": float(row["energy"]),
                    "tempo_bpm": int(float(row["tempo_bpm"])),
                    "valence": float(row["valence"]),
                    "danceability": float(row["danceability"]),
                    "acousticness": float(row["acousticness"]),
                }
            )
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Compute one song's weighted score and explanation reasons."""
    score = 0.0
    reasons: List[str] = []
    weights = user_prefs.get("weights", {})

    genre_weight = _to_float(weights.get("genre", 2.0), default=2.0)
    mood_weight = _to_float(weights.get("mood", 1.0), default=1.0)
    energy_weight = _to_float(weights.get("energy", 2.0), default=2.0)
    valence_weight = _to_float(weights.get("valence", 1.0), default=1.0)
    tempo_weight = _to_float(weights.get("tempo", 0.75), default=0.75)
    acoustic_bonus = _to_float(weights.get("acoustic_bonus", 0.5), default=0.5)

    favorite_genre = (user_prefs.get("favorite_genre") or user_prefs.get("genre") or "").strip().lower()
    favorite_mood = (user_prefs.get("favorite_mood") or user_prefs.get("mood") or "").strip().lower()
    song_genre = str(song.get("genre", "")).strip().lower()
    song_mood = str(song.get("mood", "")).strip().lower()

    if favorite_genre and song_genre == favorite_genre:
        score += genre_weight
        reasons.append(f"genre match (+{genre_weight:.2f})")

    if favorite_mood and song_mood == favorite_mood:
        score += mood_weight
        reasons.append(f"mood match (+{mood_weight:.2f})")

    target_energy = _to_float(user_prefs.get("target_energy", user_prefs.get("energy", 0.5)), default=0.5)
    energy = _to_float(song.get("energy"), default=0.5)
    energy_similarity = max(0.0, 1.0 - abs(energy - target_energy))
    energy_points = energy_weight * energy_similarity
    score += energy_points
    reasons.append(f"energy closeness (+{energy_points:.2f})")

    if "target_valence" in user_prefs or "valence" in user_prefs:
        target_valence = _to_float(user_prefs.get("target_valence", user_prefs.get("valence", 0.5)), default=0.5)
        valence = _to_float(song.get("valence"), default=0.5)
        valence_similarity = max(0.0, 1.0 - abs(valence - target_valence))
        valence_points = valence_weight * valence_similarity
        score += valence_points
        reasons.append(f"valence closeness (+{valence_points:.2f})")

    if "preferred_tempo_bpm" in user_prefs or "tempo_bpm" in user_prefs:
        preferred_tempo = _to_float(user_prefs.get("preferred_tempo_bpm", user_prefs.get("tempo_bpm", 110)), default=110.0)
        tempo = _to_float(song.get("tempo_bpm"), default=110.0)
        tempo_similarity = max(0.0, 1.0 - min(abs(tempo - preferred_tempo) / 110.0, 1.0))
        tempo_points = tempo_weight * tempo_similarity
        score += tempo_points
        reasons.append(f"tempo closeness (+{tempo_points:.2f})")

    likes_acoustic = _to_bool(user_prefs.get("likes_acoustic", False))
    if likes_acoustic and _to_float(song.get("acousticness"), default=0.0) >= 0.60:
        score += acoustic_bonus
        reasons.append(f"acoustic preference match (+{acoustic_bonus:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song, rank by score, and return the top-k results."""
    scored: List[Tuple[Dict, float, str]] = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons)
        scored.append((song, score, explanation))

    ranked = sorted(scored, key=lambda item: item[1], reverse=True)
    return ranked[:k]
