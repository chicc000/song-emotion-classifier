import streamlit as st
import json
import collections

with open("full_songs.json", "r", encoding="utf-8") as f:
    songs = json.load(f)

st.title("檢查年代欄位")

# 印出所有年代值分布
era_values = [s.get("era") for s in songs]
era_counts = collections.Counter(era_values)

st.write("所有年代欄位值與數量：")
for era_val, count in era_counts.items():
    st.write(f"'{era_val}': {count} 筆")

# 建立選單，只取非空值
eras = sorted(set(s.get("era") for s in songs if s.get("era")))

selected_era = st.selectbox("年代", eras)
