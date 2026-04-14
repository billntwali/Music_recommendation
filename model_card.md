# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibePilot 1.0**

---

## 2. Goal / Task  

This recommender suggests the top 5 songs from a small catalog.
It tries to match a user's vibe using genre, mood, and numeric music features.
It is a ranking system, not a prediction of what a user will "definitely" love.

---

## 3. Data Used  

The dataset has 18 songs in `data/songs.csv`.
Each song has `genre`, `mood`, `energy`, `tempo_bpm`, `valence`, `danceability`, and `acousticness`.
I expanded the starter catalog to include more genres and moods.
The data is still small and hand-curated, so it does not represent all music tastes.

---

## 4. Algorithm Summary  

Each song starts at score `0`.
The model adds points for an exact genre match and an exact mood match.
Then it adds similarity points when energy, valence, and tempo are close to the user target.
If the user likes acoustic music, songs with high acousticness get a small bonus.
After scoring all songs, it sorts from highest to lowest and returns top `k`.

---

## 5. Strengths  

The system works well for clear profiles like "Chill Lofi" and "Deep Intense Rock."
Recommendations are easy to explain because every score includes human-readable reasons.
The behavior is consistent when profiles are similar.

---

## 6. Observed Behavior / Biases  

The model can create a filter bubble because exact genre and mood matches get strong rewards.
In an edge-case profile, `Ocean Lantern` ranked first even though its energy was far from the target, because category matches were strong.
With only 18 songs, some tracks appear in many profiles, so diversity is limited.
The system also ignores lyrics, language, and personal history.

---

## 7. Evaluation Process  

I tested four profiles: `High-Energy Pop`, `Chill Lofi`, `Deep Intense Rock`, and one adversarial profile (`Calm + Very High Energy`).
For each profile, I reviewed the top 5 songs and the reason strings.
I compared outputs to my own musical intuition.
I also ran one experiment: doubled energy weight and halved genre weight.
That change brought in more high-energy cross-genre songs, which showed the model is sensitive to weights.

---

## 8. Intended Use and Non-Intended Use

Intended use:
- Classroom exploration of recommender logic.
- Small demo of how scoring and ranking work.

Non-intended use:
- Not for real production recommendations.
- Not for high-stakes decisions.
- Not a full model of a person's music identity.

---

## 9. Ideas for Improvement  

1. Add more songs and better balance across genres and moods.
2. Add diversity rules so top 5 is not dominated by one genre or one artist.
3. Learn weights from user feedback instead of fixed manual values.

---

## 10. Personal Reflection  

My biggest learning moment was seeing how one weight change can reorder the whole top 5.
AI tools helped me scaffold code and generate test ideas quickly, but I still had to run the program and check if outputs made sense.
I was surprised that a simple point system can still feel like "real recommendations" when the reasons are clear.
If I extend this project, I want to add user history and a diversity-aware reranking step.
