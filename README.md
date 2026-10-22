# MoodFlix — Manual Movie Catalog

This version has a manually included catalog of Bollywood and Hollywood movies. It does **not** use a database or any API.

## Run
Open a terminal in this folder and run:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

If Streamlit is already installed, you only need:

```powershell
python -m streamlit run app.py
```

Open the local URL shown in the terminal, usually http://localhost:8501.

## Features
- 50 manually entered movies across Bollywood, Hollywood, and international cinema
- Mood, genre, industry, rating, and keyword filters
- Cinematic dark UI with movie cards
- Session-only watchlist
- No database, API key, or internet connection required for movie data

## Mini-project note
Recommendations are generated using manually assigned mood and genre tags and a simple scoring rule. This is a rule-based recommendation demo, not a trained machine-learning model. To add ML later, you can use TF-IDF and cosine similarity over movie descriptions.
