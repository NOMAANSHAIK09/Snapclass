import streamlit as st

def footer_home():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    
    st.markdown(f"""
                <div style="display: flex; align-items: center; justify-content: center; flex-direction: column; margin-top: 2rem;">
                <p>Made with ❤️ by </p>
                <img src='{logo_url}' height="20px;"/>
                </div>
                """, unsafe_allow_html=True)
    
    
def footer_dashboard():
    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    
    st.markdown(f"""
                <div style="display: flex; align-items: center; justify-content: center; flex-direction: column; margin-top: 2rem;">
                <p>Made with ❤️ by </p>
                <img src='{logo_url}' height="20px;"/>
                </div>
                """, unsafe_allow_html=True)