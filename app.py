import streamlit as st

st.title("🚀 나의 첫 웹앱")
st.info("파이썬만으로 제작하는 UI")

col1, col2 = st.columns(2)
with col1:
    st.success("왼쪽 영역")
with col2:
    st.write("오른쪽 영역")