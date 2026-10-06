import streamlit as st
from src.components.header import header_home
def home_screen():
    st.title("Welcome to SnapClass!")
    st.write("Please select your login type:")
    
    
    
    header_home()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Teacher"):
            st.session_state['login_type'] = 'teacher'
            st.rerun()
        
    with col2:
        if st.button("Student"):
            st.session_state['login_type'] = 'student'
            st.rerun()