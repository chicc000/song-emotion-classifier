import streamlit as st
import json
import random

# 載入歌曲資料
with open("songs.json", "r", encoding="utf-8") as f:
    songs = json.load(f)

# 預設情緒選項
emotions = ["愉悅", "憤怒", "煩躁", "悲傷"]

# UI 選單
st.title("音樂情緒分類器")
st.write("根據你的情緒推薦歌曲，支援中、日、英、韓語歌")

emotion = st.selectbox("請選擇目前的情緒", emotions)
language = st.selectbox("選擇歌曲語言", ["中文", "日文", "英文", "韓文"])
genre = st.selectbox("選擇曲風", ["流行", "搖滾", "嘻哈", "電子", "民謠", "爵士", "其他"])
era = st.selectbox("選擇年代", ["80年代", "90年代", "2000年代", "2010年代至今"])

# 篩選符合條件的歌曲
filtered_songs = [
    s for s in songs
    if s["emotion"] == emotion and s["language"] == language
    and s["genre"] == genre and s["era"] == era
]

# 隨機選幾首歌推薦
if filtered_songs:
    st.subheader("為你推薦的歌曲：")
    for song in random.sample(filtered_songs, min(5, len(filtered_songs))):
        st.markdown(f"**{song['title']}** - *{song['artist']}*  \n"
                    f"風格：{song['genre']} | 年代：{song['era']}  \n"
                    f"歌詞片段：{song['lyrics']}  ")
        st.video(song["youtube"])
else:
    st.warning("找不到符合條件的歌曲，請試試其他選項～")
