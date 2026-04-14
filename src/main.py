"""
Command line runner for the Music Recommender Simulation.
"""

from recommender import load_songs, recommend_songs

SEPARATOR = "-" * 60


def show_recommendations(label: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    print(f"\n{'=' * 60}")
    print(f"  Profile: {label}")
    print(f"{'=' * 60}")

    recommendations = recommend_songs(user_prefs, songs, k=k)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"\n  #{rank}  {song['title']:<35} {score:>2.0f} / 12")
        print(f"       {SEPARATOR}")
        for reason in explanation.split("; "):
            print(f"       {reason}")


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded {len(songs)} songs.")

    profiles = [
        {
            "label": "lofi / chill  |  energy 0.38  |  valence 0.58",
            "prefs": {
                "genre": "lofi",
                "mood":  "chill",
                "energy":  0.38,
                "valence": 0.58,
            },
        },
        {
            "label": "pop / happy  |  energy 0.80  |  valence 0.82",
            "prefs": {
                "genre": "pop",
                "mood":  "happy",
                "energy":  0.80,
                "valence": 0.82,
            },
        },
    ]

    for profile in profiles:
        show_recommendations(profile["label"], profile["prefs"], songs)

    print()


if __name__ == "__main__":
    main()
