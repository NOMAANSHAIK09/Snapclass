import streamlit as st

from src.components.footer import footer_dashboard
from src.ui.base_layout import style_background_dashboard , style_base_layout

from src.components.header import header_dashboard
def teacher_screen():
    
    style_background_dashboard()
    style_base_layout()
    
    
    teacher_screen_login()    
    
    if 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == 'login':
        teacher_screen_login()
    elif st.session_state.teacher_login_type == 'register':
        teacher_screen_register()


def teacher_screen_login():
    c1,c2 = st.columns(2 , vertical_alignment="center", gap="large")
    with c1:
        header_dashboard()
        
    with c2:
        if st.button("go to home",icon="🏠" , shortcut="Ctrl+backspace"  ):
            st.session_state['login_type'] = 'home'
            st.rerun()
        
    st.header("login using password", text_alignment="center")
    st.space()
    teacher_username = st.text_input("username" , placeholder="Enter your username")
    teacher_password = st.text_input("password" , placeholder="Enter your password" , type="password")
    st.divider()
    btn1,btn2=st.columns(2)
    with btn1:
        st.button("login" , icon="🔑" ,  shortcut="Ctrl+Enter" , width="stretch" )
    with btn2:
        if st.button("register", type="primary" , icon="✍️" , shortcut="Ctrl+Shift+Enter" , width="stretch" ):
            st.session_state.teacher_login_type = 'register'
            st.rerun()
        
    
    
    
    footer_dashboard()
    
    
    

def teacher_screen_register():
    c1,c2 = st.columns(2 , vertical_alignment="center", gap="large")
    with c1:
        header_dashboard()
        
    with c2:
        if st.button("go to home",icon="🏠" , shortcut="Ctrl+backspace"  ):
            st.session_state['login_type'] = 'home'
            st.rerun()
        
    st.header("Register your teacher profile", text_alignment="center")
    
    
    st.space()
    teacher_username = st.text_input("username" , placeholder="Enter your username")
    teacher_name= st.text_input("name" , placeholder="Enter your name")
    teacher_password = st.text_input("password" , placeholder="Enter your password" , type="password")
    teacher_conform_password = st.text_input("confirm password" , placeholder="Confirm your password" , type="password")
    st.divider()
    btn1,btn2=st.columns(2)
    with btn1:
        st.button("register now" , icon="🔑" , shortcut="Ctrl+Enter" , width="stretch" )
    with btn2:
        if st.button("login instead", type="primary" , icon="✍️" , shortcut="Ctrl+Shift+Enter" , width="stretch" ):
            st.session_state.teacher_login_type = 'login'
            st.rerun()

    footer_dashboard()
    pass