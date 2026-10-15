
import streamlit as st

from src.components.footer import footer_dashboard
from src.ui.base_layout import style_background_dashboard , style_base_layout

from src.components.header import header_dashboard
from src.database.db import check_teacher_exists, create_teacher , teacher_login 
from PIL import Image
import numpy as np 
def student_screen():
    
    style_background_dashboard()
    style_base_layout()
    c1,c2 = st.columns(2 , vertical_alignment="center", gap="large")
    with c1:
        header_dashboard()
        
    with c2:
        if st.button("go to home",icon="🏠" , shortcut="Ctrl+backspace"  ):
            st.session_state['login_type'] = None
            st.rerun()
        
    st.header("login using face recognition", text_alignment="center")
    st.space()
    st.space()

    photo_source=st.camera_input("Take a picture of your face for login", label_visibility="collapsed" , key="student_login_camera_input" )
    if photo_source:
        np.array(Image.open(photo_source))



    footer_dashboard()