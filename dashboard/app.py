import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Movie Ratings Analysis",
    page_icon="🎬",
    layout="wide"
)

# Load dataset
DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "IMDB-Movie-Data.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH)

    numeric_columns = [
        "Rating",
        "Year",
        "Revenue (Millions)",
        "Runtime (Minutes)",
        "Votes",
        "Metascore"
    ]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


df = load_data()

# Dashboard title
st.title("🎬 Movie Ratings Analysis Dashboard")
st.markdown("Explore movie ratings, genres, revenue and audience engagement.")

# Sidebar filters
st.sidebar.header("Dashboard Filters")

if "Year" in df.columns:
    years = sorted(df["Year"].dropna().unique())
    selected_years = st.sidebar.multiselect(
        "Select Year",
        years,
        default=years
    )
    filtered_df = df[df["Year"].isin(selected_years)]
else:
    filtered_df = df.copy()

if "Genre" in filtered_df.columns:
    genres = sorted(
        set(
            genre.strip()
            for values in filtered_df["Genre"].dropna()
            for genre in values.split(",")
        )
    )

    selected_genres = st.sidebar.multiselect(
        "Select Genre",
        genres
    )

    if selected_genres:
        filtered_df = filtered_df[
            filtered_df["Genre"].apply(
                lambda x: any(
                    genre in str(x).split(",")
                    for genre in selected_genres
                )
            )
        ]

# Key metrics
st.subheader("📊 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Movies", f"{len(filtered_df):,}")

with col2:
    avg_rating = filtered_df["Rating"].mean()
    st.metric(
        "Average Rating",
        f"{avg_rating:.2f}/10" if pd.notna(avg_rating) else "N/A"
    )

with col3:
    avg_revenue = filtered_df["Revenue (Millions)"].mean()
    st.metric(
        "Average Revenue",
        f"${avg_revenue:.2f}M" if pd.notna(avg_revenue) else "N/A"
    )

with col4:
    avg_runtime = filtered_df["Runtime (Minutes)"].mean()
    st.metric(
        "Average Runtime",
        f"{avg_runtime:.0f} min" if pd.notna(avg_runtime) else "N/A"
    )

st.divider()

# Top 10 movies
st.subheader("🏆 Top 10 Highest-Rated Movies")

top_movies = filtered_df.dropna(subset=["Rating"]).nlargest(10, "Rating")

st.markdown(
    top_movies[
        [col for col in ["Title", "Year", "Genre", "Rating"]
         if col in top_movies.columns]
    ].to_html(index=False, escape=True),
    unsafe_allow_html=True
)

# Rating distribution
st.subheader("⭐ Movie Rating Distribution")

rating_data = filtered_df["Rating"].dropna()

fig, ax = plt.subplots()
ax.hist(rating_data, bins=15, edgecolor="black")
ax.set_xlabel("IMDb Rating")
ax.set_ylabel("Number of Movies")
ax.set_title("Distribution of Movie Ratings")
st.pyplot(fig)
plt.close(fig)

# Genre analysis
st.subheader("🎭 Genre-wise Average Rating")

genre_data = filtered_df[["Genre", "Rating"]].dropna().copy()
genre_data["Genre"] = genre_data["Genre"].str.split(",")
genre_data = genre_data.explode("Genre")
genre_data["Genre"] = genre_data["Genre"].str.strip()

genre_ratings = (
    genre_data.groupby("Genre")["Rating"]
    .mean()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(10, 5))
genre_ratings.plot(kind="bar", ax=ax)
ax.set_ylabel("Average IMDb Rating")
ax.set_xlabel("Genre")
ax.set_title("Average Rating by Genre")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)
plt.close(fig)
# Year-wise rating
st.subheader("📅 Year-wise Average Rating")

year_rating = (
    filtered_df.groupby("Year")["Rating"]
    .mean()
    .dropna()
    .sort_index()
)

fig, ax = plt.subplots(figsize=(10, 5))
year_rating.plot(kind="line", marker="o", ax=ax)
ax.set_ylabel("Average IMDb Rating")
ax.set_xlabel("Year")
ax.set_title("Year-wise Average Rating")
ax.grid(True)
plt.tight_layout()
st.pyplot(fig)
plt.close(fig)
# Revenue analysis
st.subheader("💰 Revenue vs IMDb Rating")

revenue_data = filtered_df[
    ["Revenue (Millions)", "Rating"]
].dropna()

fig, ax = plt.subplots()
ax.scatter(revenue_data["Rating"], revenue_data["Revenue (Millions)"])
ax.set_xlabel("IMDb Rating")
ax.set_ylabel("Revenue (Millions)")
ax.set_title("Revenue vs IMDb Rating")
st.pyplot(fig)
plt.close(fig)

# Runtime analysis
st.subheader("⏱️ Runtime vs IMDb Rating")

runtime_data = filtered_df[
    ["Runtime (Minutes)", "Rating"]
].dropna()

st.scatter_chart(
    runtime_data,
    x="Runtime (Minutes)",
    y="Rating"
)

# Dataset preview
with st.expander("View Complete Dataset"):
    st.markdown(
    filtered_df.to_html(index=False, escape=True),
    unsafe_allow_html=True
)

st.caption("Movie Ratings Analysis | Data Analytics Portfolio Project")