import streamlit as st
import json
import random

# 載入資料
with open("full_songs.json", "r", encoding="utf-8") as f:
    songs = json.load(f)

st.title("音樂情緒分類器 - Debug 版")

# 選擇條件
user_emotion = st.selectbox("情緒", sorted(set(s.get("emotion", "") for s in songs)))
language = st.selectbox("語言", sorted(set(s.get("language", "") for s in songs)))
genre = st.selectbox("曲風", sorted(set(s.get("genre", "") for s in songs)))
era = st.selectbox("年代", sorted(set(s.get("era", "") for s in songs)))

st.markdown("---")
st.write(f"篩選條件：情緒={user_emotion}, 語言={language}, 曲風={genre}, 年代={era}")

# 篩選條件，用嚴格相等
filtered_songs = [
    s for s in songs
    if s.get("emotion") == user_emotion
    and s.get("language") == language
    and s.get("genre") == genre
    and s.get("era") == era
]

st.write(f"找到 {len(filtered_songs)} 首符合條件的歌")

if filtered_songs:
    for idx, song in enumerate(filtered_songs):
        st.write(f"---\n第 {idx+1} 首歌資料：")
        st.json(song)  # 印出整筆歌的資料，包含所有欄位與內容
else:
    st.warning("找不到符合條件的歌曲")
