import streamlit as st

def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
               <div style="display: flex; align-items: center; justify-content: center; flex-direction: column; margin-bottom: 2rem;"> 
                <img src='{logo_url}' height="100px;"/>
                <h1 style=" text-align: center; color: #E0E3FF; font-family: 'Climate Crisis', sans-serif;">Snap <br/> Class</h1>
                </div>
                """, unsafe_allow_html=True)