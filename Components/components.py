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
                </style>
                """, unsafe_allow_html=True)
        
    @staticmethod
    def app_sidebar():
        sidebar = st.sidebar
        sidebar.markdown(" <br></br> ", unsafe_allow_html=True)
        col1 = st.sidebar.columns([1, 3, 1])[1]  
        col1.image("data/Images/bhuh_pramaan_logo.jpg", use_column_width=True)
        col1.markdown("[bhuhpramaan.com](https://www.bhuhpramaan.com/)")
        return None
        
