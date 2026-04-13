# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

This recommender can create a small filter bubble because exact `genre` and `mood` matches are rewarded strongly and repeatedly. During stress tests, songs with perfect categorical matches often stayed near the top even when their numeric vibe (especially energy) was not ideal. The edge-case profile (`calm` mood with very high energy) exposed this: a calm classical song still ranked first mostly due to category matching, even though its energy was far from the target. Another limitation is catalog coverage: with only 18 songs, a few tracks appear in multiple profiles simply because there are not many alternatives at each mood/energy combination. Finally, the model ignores lyrical themes, language, and cultural context, so it may miss what users actually mean by a "deep" or "intense" track.

---

## 7. Evaluation  

I evaluated the system by running four profiles: `High-Energy Pop`, `Chill Lofi`, `Deep Intense Rock`, and an adversarial profile (`Edge Case: Calm + Very High Energy`). For each run, I inspected the top 5 songs and checked whether the reasons matched the expected vibe. Results mostly made sense: `Library Rain` and `Midnight Coding` rose to the top for `Chill Lofi`, while `Storm Runner` ranked first for `Deep Intense Rock` due to strong genre+mood+energy alignment. The most surprising output came from the edge case, where `Ocean Lantern` ranked first despite low energy, showing that categorical matches can dominate numeric mismatch. I also ran a sensitivity experiment (double energy weight, half genre weight) and saw `Barrio Neon` enter the `High-Energy Pop` top 5, confirming the model is sensitive to weighting choices rather than fixed song identity.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
