# Profile Pair Reflections

Profiles tested:
- High-Energy Pop
- Chill Lofi
- Deep Intense Rock
- Edge Case: Calm + Very High Energy

## Pair Comparisons

High-Energy Pop vs Chill Lofi:
The pop profile favored upbeat tracks like `Sunrise City` and `Gym Hero`, while the lofi profile moved toward softer, more acoustic songs like `Library Rain` and `Midnight Coding`. This makes sense because `Chill Lofi` asks for lower energy and includes an acoustic preference bonus.

High-Energy Pop vs Deep Intense Rock:
Both profiles liked energetic music, so some songs overlapped near the top, but `Deep Intense Rock` pushed `Storm Runner` to rank 1 because it matched both the `rock` genre and `intense` mood. The pop profile kept `Sunrise City` at the top due to exact `pop/happy` alignment.

High-Energy Pop vs Edge Case: Calm + Very High Energy:
The edge-case profile produced a mixed list where `Ocean Lantern` ranked first even with low energy, because exact `classical + calm` matches were rewarded strongly. The pop profile stayed more consistent and upbeat, showing how contradictory preferences can produce unexpected top choices.

Chill Lofi vs Deep Intense Rock:
`Chill Lofi` selected low-tempo, high-acoustic tracks, while `Deep Intense Rock` selected high-energy tracks with intense mood signals. The contrast confirms the model responds meaningfully to energy and tempo targets, not just one global popularity pattern.

Chill Lofi vs Edge Case: Calm + Very High Energy:
Both profiles shared calmer mood signals, but the edge case forced much higher target energy and tempo, so heavier tracks like `Storm Runner` and `Iron Static` appeared. This shows the numeric weights can pull recommendations away from mood when the requested energy is extreme.

Deep Intense Rock vs Edge Case: Calm + Very High Energy:
These two profiles both liked high energy, so `Storm Runner` stayed high, but only the rock profile gave it strong category bonuses. The edge profile rewarded `Ocean Lantern` because category matches (`classical`, `calm`) outweighed energy mismatch, which exposed a scoring tradeoff.
