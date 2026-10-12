import json  # 1. json 모듈 임포트 추가
import streamlit as st  # streamlit run web.py
import firebase_admin
from firebase_admin import credentials, firestore

# 2. Firebase 앱이 이미 초기화되었는지 확인하여 중복 초기화 방지
if not firebase_admin._apps:
    key_string = st.secrets["firebase_key"]
    cred_dict = json.loads(key_string)
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()

# 제목은 폼 바깥에 두는 것이 UI 구조상 더 깔끔합니다.
st.title("은희의 메모장")  

with st.form("input_form", clear_submit_on_submit=True):  # 제출 시 입력창이 비워지도록 설정
    task = st.text_input("할일을 적으세요")
    sub = st.form_submit_button("추가")  

# sub와 task가 모두 존재할 때 처리
if sub and task:
    db.collection("todos").add({"content": task, "at": firestore.SERVER_TIMESTAMP})
    st.success(f"'{task}' 추가됨!")
