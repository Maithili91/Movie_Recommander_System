# Movie_Recommander_System
📖 **Overview**

The Movie Recommendation System is a machine learning-based web app built with Streamlit.
It recommends movies similar to the one entered by the user. The system uses content-based filtering to analyze movie features and find the most relevant matches.

This project helps users explore new movies based on their favorite ones through a fast and interactive interface.

🧠 **Features**
🎥 Recommends movies based on content similarity
🔍 Search any movie by name
🧾 Displays top recommended movies instantly
⚡ Built with Streamlit for a smooth web experience
💾 Uses pre-trained machine learning models for quick response

🧰 **Tech Stack**

| Category                 | Tools/Libraries Used              |
| ------------------------ | --------------------------------- |
| **Programming Language** | Python                            |
| **Framework**            | Streamlit                         |
| **Machine Learning**     | scikit-learn                      |
| **Data Handling**        | pandas, numpy                     |
| **Vectorization**        | CountVectorizer / TfidfVectorizer |
| **Similarity Measure**   | Cosine Similarity                 |
| **Dataset**              | TMDB/IMDB Movie Dataset           |

⚙️ **How It Works**
The movie dataset is preprocessed to combine key features such as genres, keywords, cast, and overview.
These textual features are vectorized using CountVectorizer to convert text into numerical format.
Cosine Similarity is calculated to measure how close or similar two movies are.
When a user inputs a movie name, the app displays the top 5–10 most similar movies as recommendations.

📊 **Example Output**
Input: Inception
Recommended Movies:
  Interstellar
  The Prestige
  Tenet
  Shutter Island
  The Matrix

