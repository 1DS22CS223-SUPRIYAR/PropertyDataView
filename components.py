import streamlit as st
import leafmap.foliumap as leafmap
import json
from shapely.geometry import shape

class Config:
    @staticmethod
    def configure():
        st.set_page_config(
            page_title='Property Data Visualization',
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
        

class Plot:
    @staticmethod
    def create_plot(title , file, plot_number):
        st.set_page_config(
            page_title=title,
            layout="wide",
            initial_sidebar_state="expanded",
        )
        plots_geojson_file = file
        status = "NA"
        with open(plots_geojson_file, 'r') as f:
            properties = json.load(f)
            status = properties["features"][plot_number]["properties"]["status"]
            geometry = properties["features"][plot_number]["geometry"]
            geom = shape(geometry)

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
        st.markdown("# Vinayaka Housing Banner")
        st.markdown("## Project1: Kuduru Project Phase 1")
        st.markdown("### Plot 1")

        col1, col2 = st.columns([1, 1])
        col1.markdown("**Owner Name:** XXX")
        col1.markdown("**Contact Number:** 99876 54332")
        col1.markdown(f"**Status:** {status} ")
        col2.markdown("**Developer Name:** YYY")
        col2.markdown("**Whatsapp: 99999 99999**")

        col3, col4 = st.columns([3, 1])

        with col3:        
            m = leafmap.Map(minimap_control=True, zoom=10)
            m.add_basemap("GoogleSatellite")
            m.add_geojson(plots_geojson_file)
            m.zoom_to_bounds(geom.bounds)
            m.to_streamlit(height=500)

        with col4:
            cont1 = st.container(border = True)
            with cont1:
                st.markdown("### Report")
                st.markdown("**Total Area:** XXX Acres")
                st.markdown("**Built Up Area:** YYY Acres")
                st.markdown("**Common Area:** ZZZ Acres")
