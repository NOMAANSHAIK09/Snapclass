import streamlit as st

def footer_home():
    logo_url = "https://t4.ftcdn.net/jpg/11/80/21/69/240_F_1180216973_KiAbeTXpIqscXDHLBhvByGt9lef64CbZ.jpg"
    
    
    st.markdown(f"""
                <div style="display: flex; align-items: center; justify-content: center; flex-direction: column; margin-top: 2rem;">
                <p>Made by Nomaan Shaik </p>
                <img src='{logo_url}' height="30px;"/>
                </div>
                """, unsafe_allow_html=True)
    
    
def footer_dashboard():
    logo_url = "https://t4.ftcdn.net/jpg/11/80/21/69/240_F_1180216973_KiAbeTXpIqscXDHLBhvByGt9lef64CbZ.jpg"
    
    
    
    st.markdown(f"""
                <div style="display: flex; align-items: center; justify-content: center; flex-direction: column; margin-top: 2rem;">
                <p>Made  by Nomaan Shaik  </p>
                <img src='{logo_url}' height="30px;"/>
                </div>
                """, unsafe_allow_html=True)