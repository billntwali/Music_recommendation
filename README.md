# Music Recommender Simulation

A transparent, rule-based music recommender built for learning and experimentation.
The project ranks songs by how well they match a user profile using interpretable features like genre, mood, energy, tempo, valence, and acousticness.

## Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Testing](#testing)
- [Sample Output](#sample-output)
- [Current Limitations](#current-limitations)
- [Documentation](#documentation)

## Overview

This project demonstrates a content-based recommendation pipeline:

1. Load a small catalog of songs from `data/songs.csv`.
2. Score each song against a user taste profile.
3. Rank songs by score and return the top `k` recommendations.
4. Provide human-readable reasons for each recommendation.

The implementation intentionally favors explainability over model complexity, making it suitable for classroom use, prototyping, and algorithm walkthroughs.

## How It Works

The recommender combines exact-match and similarity-based scoring.

### Input Signals

- Categorical: `genre`, `mood`
- Numeric: `energy`, `tempo_bpm`, `valence`
- Preference flag: `likes_acoustic` (bonus when `acousticness >= 0.60`)

### Default Scoring Weights

- Genre match: `+2.0`
- Mood match: `+1.0`
- Energy closeness: `+2.0 * similarity`
- Valence closeness: `+1.0 * similarity`
- Tempo closeness: `+0.75 * similarity`
- Acoustic bonus: `+0.5`

Similarity values are normalized to the range `[0, 1]`.

### Output

For each recommended song, the system returns:

- Song metadata
- Final score
- Explanation string (for example: `genre match`, `energy closeness`, `tempo closeness`)

## Repository Structure

```text
.
├── data/
│   └── songs.csv
├── src/
│   ├── main.py            # CLI entry point and stress-test profiles
│   └── recommender.py     # Core scoring + ranking logic
├── tests/
│   └── test_recommender.py
├── assets/                # Saved outputs and visuals
├── model_card.md
├── reflection.md
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Create and activate a virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the CLI recommender:

```bash
python3 -m src.main
```

The script will:

- Load the song catalog
- Evaluate multiple stress-test profiles
- Print ranked recommendations with explanation traces
- Run an experimental weight-shift scenario

## Testing

Run the test suite:

```bash
python3 -m pytest -q
```

Current tests validate:

- Recommendation ordering by score
- Presence of non-empty explanation output

## Sample Output

The `assets/` directory includes saved examples from CLI experiments:

- High-Energy Pop recommendations
- Chill Lofi recommendations
- Deep Intense Rock recommendations
- Edge-case profile output
- Weight-shift experiment output

## Current Limitations

- Small, hand-curated catalog (`18` songs)
- No collaborative filtering or user-history learning
- No diversity or novelty constraints in reranking
- Fixed heuristic weights (unless manually overridden)

## Documentation

- Model card: [model_card.md](model_card.md)
- Reflection notes: [reflection.md](reflection.md)

