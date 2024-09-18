import streamlit as st
import leafmap.foliumap as leafmap
import json
from shapely.geometry import shape

class Config:
    @staticmethod
    def configure(title):
        st.set_page_config(
            page_title=title,
            layout="wide",
            initial_sidebar_state="expanded",
        )

        st.markdown("""
                <style>
                .column-padding {
                    padding: 20px;
                }
                .stApp {
                    background-color: #D2E0FB;
                    padding: 10px;
                }
                .col4{
                    background: #EAE4DD;
                }
                </style>
                """, unsafe_allow_html=True)
        
    @staticmethod
    def app_sidebar():
        sidebar = st.sidebar
        sidebar.image("data/Images/bhuh_pramaan_logo.jpg", caption=None)
        return None
        
