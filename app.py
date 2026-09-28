import streamlit as st

st.title("🚀 나의 첫 웹앱")
st.info("파이썬만으로 제작하는 UI")

col1, col2, col3 = st.columns(3)
with col1:
    st.success("왼쪽 영역")
with col2:
    st.write("중간 영역")
with col3:
    st.write("오른쪽 영역")