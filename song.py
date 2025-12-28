import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

# 1. Load and Prepare Data
df = pd.read_csv('SpotifySongs.csv')

# Numerical features used for similarity
features = ['Popularity', 'Danceability', 'Energy', 'Key', 'Loudness', 
            'Speechiness', 'Acousticness', 'Instrumentalness', 'Valence', 'Tempo']

scaler = MinMaxScaler()
normalized_features = scaler.fit_transform(df[features])

# Calculate the 'Average Song' as a baseline
mean_profile = normalized_features.mean(axis=0)

# 2. LLM-Style 'Reasoning' Generator (Prompt Engineering Logic)
def generate_vibe_reason(row):
    if row['Danceability'] > 0.8:
        return "Perfect for a high-energy dance floor."
    elif row['Danceability'] > 0.6:
        return "Great for a rhythmic workout or upbeat commute."
    else:
        return "A chill, steady track for focused listening."

# 3. Interactive Customer Loop
def run_dance_recommender():
    print("\n" + "="*50)
    print("Welcome to the Dance-Based Music Discovery System")
    print("="*50)
    
    while True:
        try:
            print("\nHow much do you want to dance today?")
            print("[0.0 = Very Chill | 0.5 = Balanced | 1.0 = Non-stop Dancing]")
            user_input = input("Enter a value (0.0 to 1.0) or 'quit': ").strip()
            
            if user_input.lower() == 'quit':
                break
            
            target_dance = float(user_input)
            if not (0 <= target_dance <= 1):
                print("Please enter a value between 0 and 1.")
                continue
                
            # --- The Cosine Similarity Engine ---
            # Create a target vector: Start with average traits, but swap in user's danceability
            dance_idx = features.index('Danceability')
            target_profile = mean_profile.copy()
            target_profile[dance_idx] = target_dance # Set the 'Dance' dimension
            
            # Find similarity between the 'ideal song' and the database
            similarities = cosine_similarity([target_profile], normalized_features)[0]
            
            df['match_score'] = similarities
            top_recs = df.sort_values(by='match_score', ascending=False).head(5)
            
            # Display Results
            print(f"\nFinding songs with ~{target_dance*100}% danceability profile...")
            print("-" * 65)
            for i, (idx, row) in enumerate(top_recs.iterrows()):
                print(f"{i+1}. {row['SongName']} by {row['ArtistName']}")
                print(f"   Danceability: {row['Danceability']} | Vibe: {generate_vibe_reason(row)}")
                print(f"   Match Confidence: {round(row['match_score']*100, 1)}%\n")
                
        except ValueError:
            print("Invalid input. Please enter a number between 0.0 and 1.0.")

if __name__ == "__main__":
    run_dance_recommender()