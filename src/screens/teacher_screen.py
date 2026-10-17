import streamlit as st

from src.components.footer import footer_dashboard
from src.ui.base_layout import style_background_dashboard , style_base_layout

from src.components.header import header_dashboard
from src.database.db import check_teacher_exists, create_teacher , teacher_login 

def register_teacher(teacher_username,  teacher_name, teacher_password, teacher_conform_password):
    if not teacher_username or not teacher_name or not teacher_password or not teacher_conform_password:
        return False, "All fields are required."
    
    if check_teacher_exists(teacher_username):
        return False, "Username already exists. Please choose a different username."
    
    if teacher_password != teacher_conform_password:
        return False, "Passwords do not match."
    try:
        create_teacher(teacher_username, teacher_password, teacher_name)
        return True, "Teacher registered successfully."
    except Exception as e:
        return False, f"An error occurred during registration: {str(e)}"

def teacher_screen():
    
    style_background_dashboard()
    style_base_layout()
    
    
    # teacher_screen_login()    
    if "teacher_data" in st.session_state:
        teacher_dashboard()
    elif 'teacher_login_type' not in st.session_state or st.session_state.teacher_login_type == 'login':
        teacher_screen_login()
    elif st.session_state.teacher_login_type == 'register':
        teacher_screen_register()


def teacher_dashboard():
    teacher_data=st.session_state.teacher_data
    c1,c2 = st.columns(2 , vertical_alignment="center", gap="large")
    with c1:
        header_dashboard()
        
    with c2:
        st.subheader(f"Welcome, {teacher_data['name']}!", text_alignment="center")

        if st.button("logout ",icon="🏠" , shortcut="Ctrl+backspace"  ):
            st.session_state['is_login_in'] = False
            del st.session_state.teacher_data
            st.rerun()
    
    st.space()
    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = 'take_attendance'
        
        
    
    tab1,tab2,tab3 = st.columns(3)
    
    with tab1:
        type1="primary" if st.session_state.current_teacher_tab == 'take_attendance' else "tertiary"
        if st.button('Take Attendance',type=type1, width='stretch', icon=':material/ar_On_you:'):
            st.session_state.current_teacher_tab = 'take_attendance'
            st.rerun()
            
    with tab2:
        type2="primary" if st.session_state.current_teacher_tab == 'manage_subjects' else "tertiary"
        if st.button('Manage_subjects', type=type2,width='stretch', icon=':material/book_ribbon:'):
            st.session_state.current_teacher_tab = 'manage_subjects'
            st.rerun()
    with tab3:
        type3="primary" if st.session_state.current_teacher_tab == 'attendance_records' else "tertiary"
        if st.button('Attendance Records', type=type3,width='stretch', icon=':material/cards_state:'):
            st.session_state.current_teacher_tab = 'attendance_records'
            st.rerun()
            
            
            
    st.divider()
    
    if st.session_state.current_teacher_tab=="take_attendance":
        teacher_tab_take_attendance()
    if st.session_state.current_teacher_tab=="manage_subject":
        teacher_tab_manage_subject()
    if st.session_state.current_teacher_tab=="attendance_records":
        teacher_tab_attendance_records()
        
    
    
    footer_dashboard()
    
    
def teacher_tab_take_attendance():
    st.header("Teke Attendance")
    

def teacher_tab_manage_subject():
    st.header("Manage_subjects")

def teacher_tab_attendance_records():
    st.header("Attendance Records")
 
def login_teacher(teacher_username, teacher_password):
    if not teacher_username or not teacher_password:
        return False, "Both username and password are required."
    
    teacher = teacher_login(teacher_username, teacher_password)
    if teacher:
        st.session_state.user_role = 'teacher'
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True
    return False, "Invalid username or password."
    
def teacher_screen_login():
    c1,c2 = st.columns(2 , vertical_alignment="center", gap="large")
    with c1:
        header_dashboard()
        
    with c2:
        if st.button("go to home",icon="🏠" , shortcut="Ctrl+backspace"  ):
            st.session_state['login_type'] = None
            st.rerun()
        
    st.header("login using password", text_alignment="center")
    st.space()
    teacher_username = st.text_input("username" , placeholder="Enter your username")
    teacher_password = st.text_input("password" , placeholder="Enter your password" , type="password")
    st.divider()
    btn1,btn2=st.columns(2)
    with btn1:
        if st.button("login" , icon="🔑" ,  shortcut="Ctrl+Enter" , width="stretch" ):
            if login_teacher(teacher_username, teacher_password):
                st.toast("Login successful!", icon="✅")
                import time
                time.sleep(2)
                
                st.rerun()
            else:
                st.error("Invalid username or password.", icon="❌")
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
            check=st.session_state['login_type'] = 'home'
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
        if st.button("register now" , icon="🔑" , shortcut="Ctrl+Enter" , width="stretch" ):
            success, message = register_teacher(teacher_username,  teacher_name, teacher_password, teacher_conform_password)
            if success:
                st.success(message)
                import time
                time.sleep(2)
                st.session_state.teacher_login_type = 'login'
                st.rerun()
            else:
                st.error(message)
    with btn2:
        if st.button("login instead", type="primary" , icon="✍️" , shortcut="Ctrl+Shift+Enter" , width="stretch" ):
            st.session_state.teacher_login_type = 'login'
            st.rerun()

    footer_dashboard()