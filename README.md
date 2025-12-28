# -SONG-_RECOMDATION-SYSTEM
This project implements an interactive Content-Based Recommendation Engine that allows users to discover music based on their preferred "danceability" profile. By leveraging vector mathematics, the system finds songs that align with a specific musical "vibe".

🚀 Core Features
Vector-Based Search: Uses Cosine Similarity to measure the mathematical distance between a user's target profile and the song database.

Feature Scaling: Implements MinMaxScaler to normalize diverse musical features like Tempo, Energy, and Loudness into a uniform scale for accurate comparison.

Dynamic Vibe Analysis: Includes a custom reasoning generator that provides a "vibe" description (e.g., "Perfect for a high-energy dance floor") based on the song's data attributes.

Interactive Interface: A command-line loop where users can input their desired intensity (0.0 to 1.0) and receive real-time ranked recommendations with match confidence percentages.

🛠️ Technical Implementation
The system processes data through several key stages:

Normalization: Numerical columns such as Acousticness, Instrumentalness, and Valence are scaled between 0 and 1.

Baseline Generation: It calculates a mean_profile (average song traits) to serve as the foundation for the search.

Target Injection: When a user provides a danceability score, the system swaps that specific dimension into the average profile to create an "ideal" target vector.

Similarity Ranking: The engine calculates the cosine similarity score for every song in the SpotifySongs.csv file and returns the top 5 matches.

📊 Data Attributes Used
The engine analyzes the following features to determine a match:

Energy & Tempo: For rhythmic intensity.

Speechiness & Acousticness: To distinguish between electronic and organic sounds.

Valence: To measure the musical positiveness of a track.

Popularity & Key: To ensure a well-rounded match profile.
