import streamlit as st
from recommend import recommend_by_song, recommend_by_artist, get_all_songs, get_all_artists

# Streamlit page configuration
st.set_page_config(
    page_title="Music Recommender 🎵",
    page_icon="🎧",
    layout="centered"
)

st.title("🎶 Instant Music Recommender")

# Tabs for choosing recommendation mode
tab1, tab2 = st.tabs(["🔁 Recommend by Song", "🎤 Recommend by Artist"])

with tab1:
    song_list = get_all_songs()
    selected_song = st.selectbox("🎵 Select a song:", song_list)

    if st.button("🚀 Recommend Similar Songs", key="by_song"):
        with st.spinner("Finding similar songs..."):
            recommendations = recommend_by_song(selected_song)
            if recommendations is None:
                st.warning("❌ Sorry, song not found.")
            else:
                st.success("✅ Top similar songs:")
                st.table(recommendations)

with tab2:
    artist_list = get_all_artists()
    selected_artist = st.selectbox("🎤 Select an artist:", artist_list)

    if st.button("🎧 Recommend Songs by Artist", key="by_artist"):
        with st.spinner("Finding songs..."):
            recommendations = recommend_by_artist(selected_artist)
            if recommendations.empty:
                st.warning("❌ Sorry, artist not found or has no songs.")
            else:
                st.success(f"✅ Songs by {selected_artist}:")
                st.table(recommendations)



