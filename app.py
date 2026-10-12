import streamlit as st  #streamlit run web.py
import firebase_admin
from firebase_admin import credentials, firestore





key_string = st.secrets["firebase_key"]
cred_dict = json.loads(key_string)

cred = credentials.Certificate(cred_dict)


    firebase_admin.initialize_app(cred)

db = firestore.client()


with st.form("input_form"):
    title = st.title("은희의 메모장")  
    task =st.text_input("할일을 적으세요")
    sub = st.form_submit_button("추가")  
if sub :
    st.write(f"{task}추가됨")

  
if sub and task:
    db.collection("todos").add({"content":task, "at":firestore.SERVER_TIMESTAMP})
    st.rerun()
