import streamlit as st

def header_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
               <div style="display: flex; align-items: center; justify-content: center; flex-direction: column; margin-bottom: 2rem;"> 
                <img src='{logo_url}' height="100px;"/>
                <h1 style=" text-align: center; color: #E0E3FF; font-family: 'Climate Crisis', sans-serif;">Snap <br/> Class</h1>
                </div>
                """, unsafe_allow_html=True)
    
    
def header_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
               <div style="display: flex; align-items: center; justify-content: center ; gap:10px; margin-top;30px "> 
                <img src='{logo_url}' height="100px;"/>
                <h2 style=" text-align: left; color: #5865F2;">Snap <br/> Class</h2    >
                </div>
                """, unsafe_allow_html=True)