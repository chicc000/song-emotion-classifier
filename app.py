import streamlit as st
import json

with open("full_songs.json", "r", encoding="utf-8") as f:
    songs = json.load(f)

st.title("資料欄位檢查")

# 取所有欄位可能的值
emotions = sorted(set(s.get("emotion", "") for s in songs))
languages = sorted(set(s.get("language", "") for s in songs))
genres = sorted(set(s.get("genre", "") for s in songs))
eras = sorted(set(s.get("era", "") for s in songs))

user_emotion = st.selectbox("情緒", emotions)
language = st.selectbox("語言", languages)
genre = st.selectbox("曲風", genres)
era = st.selectbox("年代", eras)

# 逐步篩選，分別印出結果數量
filtered_emotion = [s for s in songs if s.get("emotion") == user_emotion]
st.write(f"只用情緒篩選：{len(filtered_emotion)}")

filtered_language = [s for s in filtered_emotion if s.get("language") == language]
st.write(f"再加語言篩選：{len(filtered_language)}")

filtered_genre = [s for s in filtered_language if s.get("genre") == genre]
st.write(f"再加曲風篩選：{len(filtered_genre)}")

filtered_era = [s for s in filtered_genre if s.get("era") == era]
st.write(f"最後加年代篩選：{len(filtered_era)}")

if filtered_era:
    st.write("找到以下歌曲：")
    for song in filtered_era:
        st.write(f"標題：{song.get('title')}, 藝人：{song.get('artist')}")
else:
    st.warning("找不到符合條件的歌曲，請試試其他選項～")
