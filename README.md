# 🎬 AI-Powered Movie Recommender System

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![TMDB API](https://img.shields.io/badge/TMDB_API-01B4E4?style=for-the-badge&logo=themoviedb&logoColor=white)

An end-to-end, content-based Movie Recommendation Application built with Python, Scikit-Learn, and Streamlit. The system analyzes movie metadata—including genres, plot overviews, keywords, cast, and crew—to compute pairwise similarity vectors and deliver instant, highly relevant film recommendations along with dynamic posters fetched via the TMDB REST API.

🚀 **Live Web App:** [Movie Recommender System](https://movie-recommender-system-truf2a7wrsymemcbcfeymd.streamlit.app/)

---

## 📌 System Architecture

```text
┌────────────────┐     ┌───────────────────────┐     ┌───────────────────────┐
│ Raw TMDB Data  │ ──> │ Feature Engineering   │ ──> │ NLP Text Vectorization│
│ (Metadata/Cast)│     │ (Merge Genre/Overview)│     │ (Bag of Words / TFIDF)│
└────────────────┘     └───────────────────────┘     └───────────────────────┘
                                                                 │
                                                                 ▼
┌────────────────┐     ┌───────────────────────┐     ┌───────────────────────┐
│ Streamlit UI   │ <── │ Top-5 Matches         │ <── │ Cosine Similarity     │
│ (Posters + Meta)│     │ (Sorted Distance)     │     │ Matrix Calculation    │
└────────────────┘     └───────────────────────┘     └───────────────────────┘

```
## 📂 Project Directory Structure

```mermaid
graph LR
    Root["📂 movie-recommender-system/"]
    
    Root --> App["📄 app.py<br/><i>Main Streamlit UI & Engine</i>"]
    Root --> Movies["📦 movies.pkl<br/><i>Processed Metadata DataFrame</i>"]
    Root --> Vectors["📦 vectors.pkl<br/><i>Similarity Matrix & Vectors</i>"]
    Root --> Req["📋 requirements.txt<br/><i>Package Dependencies</i>"]
    Root --> Git["🔒 .gitignore<br/><i>Git Exclusion Rules</i>"]
    Root --> Readme["📖 README.md<br/><i>Project Documentation</i>"]

    style Root fill:#1f2937,stroke:#3b82f6,stroke-width:2px,color:#fff
    style App fill:#1e293b,stroke:#0284c7,color:#e2e8f0
    style Movies fill:#1e293b,stroke:#0284c7,color:#e2e8f0
    style Vectors fill:#1e293b,stroke:#0284c7,color:#e2e8f0
    style Req fill:#1e293b,stroke:#0284c7,color:#e2e8f0
    style Git fill:#1e293b,stroke:#0284c7,color:#e2e8f0
    style Readme fill:#1e293b,stroke:#0284c7,color:#e2e8f0
```

git clone [https://github.com/Cosmic-Sangam/Movie-Recommender-System.git](https://github.com/Cosmic-Sangam/Movie-Recommender-System.git)
cd Movie-Recommender-System
