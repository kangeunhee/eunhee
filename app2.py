import json
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Firebase 중복 초기화 방지
if not firebase_admin._apps:
    key_string = st.secrets["firebase_key"]
    cred_dict = json.loads(key_string)
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()

st.title("은희의 메모장")  

# 1. 할 일 추가
with st.form("input_form", clear_on_submit=True):  
    task = st.text_input("할일을 적으세요")
    if st.form_submit_button("추가") and task:
        db.collection("todos").add({"content": task, "at": firestore.SERVER_TIMESTAMP})
        st.success("추가되었습니다!")
        st.rerun()

st.divider()
st.subheader("📝 할 일 목록")

# 2. 목록 불러오기 (최신순)
docs = db.collection("todos").order_by("at", direction=firestore.Query.DESCENDING).stream()

# 3. 목록 출력 및 수정/삭제
for doc in docs:
    doc_id = doc.id
    content = doc.to_dict().get("content", "")

    # 항목별 Expander(접이식 상자)를 사용해 화면을 깔끔하게 분리
    with st.expander(content):
        # 수정 입력창
        new_content = st.text_input("내용 수정", value=content, key=f"txt_{doc_id}")
        
        # 버튼들을 나란히 배치
        col_save, col_del = st.columns(2)
        
        with col_save:
            if st.button("수정 저장", key=f"save_{doc_id}"):
                db.collection("todos").document(doc_id).update({"content": new_content})
                st.success("수정 완료!")
                st.rerun()
                
        with col_del:
            if st.button("삭제하기", key=f"del_{doc_id}"):
                db.collection("todos").document(doc_id).delete()
                st.success("삭제 완료!")
                st.rerun()
