import streamlit as st
import json
import random

# 載入歌曲資料
with open("full_songs.json", "r", encoding="utf-8") as f:
    songs = json.load(f)

st.set_page_config(page_title="音樂情緒分類器", layout="centered")
st.title("音樂情緒分類器")
st.markdown("依據你的情緒或情境，推薦合適的歌曲\n支援：中文、日文、英文、韓文")

# 定義預設情緒選項
emotions = ["愉悅", "憤怒", "煩躁", "悲傷"]

# 印出資料所有欄位的可能值，幫助檢查
all_emotions = set()
all_languages = set()
all_genres = set()
all_eras = set()

for s in songs:
    all_emotions.add(s.get("emotion", "").strip())
    all_languages.add(s.get("language", "").strip())
    all_genres.add(s.get("genre", "").strip())
    all_eras.add(s.get("era", "").strip())

st.write("資料中所有情緒：", all_emotions)
st.write("資料中所有語言：", all_languages)
st.write("資料中所有曲風：", all_genres)
st.write("資料中所有年代：", all_eras)

# 選擇輸入方式
mode = st.radio("請選擇輸入方式：", ["從選單選擇情緒", "輸入生活情境"])

user_emotion = None

if mode == "從選單選擇情緒":
    user_emotion = st.selectbox("請選擇你目前的情緒", emotions)
else:
    situation = st.text_input("請輸入你目前的情境（例如：今天功課寫不完好煩躁）")
    if situation:
        if any(word in situation for word in ["開心", "快樂", "喜歡", "幸福", "開胃", "期待"]):
            user_emotion = "愉悅"
        elif any(word in situation for word in ["生氣", "氣死", "爆炸", "火大", "罵人", "衝突"]):
            user_emotion = "憤怒"
        elif any(word in situation for word in ["煩", "煩躁", "壓力", "緊張", "焦慮", "厭世"]):
            user_emotion = "煩躁"
        elif any(word in situation for word in ["難過", "悲傷", "委屈", "哭", "崩潰", "失落", "孤單"]):
            user_emotion = "悲傷"
        else:
            user_emotion = "煩躁"  # fallback 預設為煩躁
        st.success(f"系統判斷你的情緒為：**{user_emotion}**")

if user_emotion:
    # 選擇條件時請留意和資料中值一致
    language = st.selectbox("選擇歌曲語言", sorted(all_languages))
    genre = st.selectbox("選擇曲風", sorted(all_genres))
    era = st.selectbox("選擇年代", sorted(all_eras))

    # 篩選條件分步檢查
    filtered_by_emotion = [s for s in songs if s.get("emotion", "").strip() == user_emotion]
    st.write(f"符合情緒 {user_emotion} 的歌曲數：{len(filtered_by_emotion)}")

    filtered_by_language = [s for s in filtered_by_emotion if s.get("language", "").strip() == language]
    st.write(f"符合語言 {language} 的歌曲數：{len(filtered_by_language)}")

    filtered_by_genre = [s for s in filtered_by_language if s.get("genre", "").strip() == genre]
    st.write(f"符合曲風 {genre} 的歌曲數：{len(filtered_by_genre)}")

    filtered_by_era = [s for s in filtered_by_genre if s.get("era", "").strip() == era]
    st.write(f"符合年代 {era} 的歌曲數：{len(filtered_by_era)}")

    filtered_songs = filtered_by_era

    if filtered_songs:
        st.subheader("為你推薦的歌曲：")
        for song in random.sample(filtered_songs, min(5, len(filtered_songs))):
            st.markdown(f"**{song['title']}** - *{song['artist']}*  \n"
                        f"風格：{song['genre']} | 年代：{song['era']}  \n"
                        f"歌詞片段：{song['lyrics']}")
            st.video(song.get("youtube", ""))
    else:
        st.warning("找不到符合條件的歌曲，請試試其他選項～")
