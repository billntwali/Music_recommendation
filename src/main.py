"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

try:
    from .recommender import load_songs, recommend_songs
except ImportError:  # Allows running as: python3 src/main.py
    from recommender import load_songs, recommend_songs


def print_profile_results(profile_name: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    """Print top-k recommendations for one profile in a readable CLI block."""
    print(f"\n=== {profile_name} ===")
    recommendations = recommend_songs(user_prefs, songs, k=k)
    for index, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print(f"{index}. {song['title']} - {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Reasons: {explanation}")
        print("-" * 72)


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    stress_test_profiles = [
        (
            "High-Energy Pop",
            {
                "favorite_genre": "pop",
                "favorite_mood": "happy",
                "target_energy": 0.88,
                "target_valence": 0.84,
                "preferred_tempo_bpm": 126,
                "likes_acoustic": False,
            },
        ),
        (
            "Chill Lofi",
            {
                "favorite_genre": "lofi",
                "favorite_mood": "chill",
                "target_energy": 0.38,
                "target_valence": 0.62,
                "preferred_tempo_bpm": 78,
                "likes_acoustic": True,
            },
        ),
        (
            "Deep Intense Rock",
            {
                "favorite_genre": "rock",
                "favorite_mood": "intense",
                "target_energy": 0.92,
                "target_valence": 0.45,
                "preferred_tempo_bpm": 150,
                "likes_acoustic": False,
            },
        ),
        (
            "Edge Case: Calm + Very High Energy",
            {
                "favorite_genre": "classical",
                "favorite_mood": "calm",
                "target_energy": 0.92,
                "target_valence": 0.40,
                "preferred_tempo_bpm": 160,
                "likes_acoustic": True,
            },
        ),
    ]

    print("\nStress Test Recommendations:")
    for profile_name, profile in stress_test_profiles:
        print_profile_results(profile_name, profile, songs, k=5)

    experimental_profile = dict(stress_test_profiles[0][1])
    experimental_profile["weights"] = {
        "genre": 1.0,   # half of baseline genre weight (2.0 -> 1.0)
        "mood": 1.0,
        "energy": 4.0,  # double baseline energy weight (2.0 -> 4.0)
        "valence": 1.0,
        "tempo": 0.75,
        "acoustic_bonus": 0.5,
    }
    print("\nExperiment: High-Energy Pop with weight shift (energy x2, genre x0.5)")
    print_profile_results("High-Energy Pop (Experimental Weights)", experimental_profile, songs, k=5)


if __name__ == "__main__":
    main()
