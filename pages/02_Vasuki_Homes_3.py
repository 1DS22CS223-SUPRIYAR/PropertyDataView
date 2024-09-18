#-----Contains Scripts Of Vasuki Homes Page-----'''
#------Default Styles Are Imported From "components.py" File-----
import streamlit as st
import leafmap.foliumap as leafmap
import json
from shapely.geometry import shape
from components import Config

class PlotsLayout:

    @staticmethod
    def getColor(status, type):
            if status == "Sold":
                return "red"
            elif status == "Available":
                return "green"
            elif type == "Road":
                return "grey"
            elif type == "Resort":
                return "purple"
            else:
                return "yellow"
            
    @staticmethod
    def styleFunction(feature):
        status = feature['properties'].get('Status', 'unknown')
        type = feature['properties'].get('Type', 'unknown')
        return {
            'fillColor': PlotsLayout.getColor(status, type),
            'color': 'black',
            'weight': 1.5,
            'fillOpacity': 0.6,
        }
    
    @staticmethod
    def createLayout(title , file):

        #Default Configuration
        Config.configure(title = title) 
        Config.app_sidebar()    

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
        
        #Data
        with open(file, 'r') as f:
            geojson_data = json.load(f)
        legend_dict = {
            "Sold": "red",
            "Available": "green",
            "Road": "grey",
            "Resort": "purple",
            "Other": "yellow"
        }

        #Start Of Page Content
        st.markdown("<h1 style = 'text-align: center;'> M/S Vinayaka Housing </h1>" , unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>Vasuki Homes 3</h3>", unsafe_allow_html=True)
    
        col1, col2 = st.columns([1, 1])

        # Extract plot names or IDs
        plot_names = ["Overview"] 
        plot_data = {}
        for feature in geojson_data['features']:
            if feature['properties'].get('Type') == "Residential":
                plot_id = feature['properties'].get('id', 'Unknown')
                plot_names.append("Plot"+" "+str(plot_id))
                plot_data["Plot"+" "+str(plot_id)] = feature 

        # Dropdown to select a plot
        selected_plot = st.selectbox("Select a plot:", plot_names)
        zoom_to_layer = True
        if selected_plot == "Overview":
            target_geojson = geojson_data
        else:
            target_geojson = {"type": "FeatureCollection", "features": [plot_data[selected_plot]]}
            zoom_to_layer = False 
        col3, col4 = st.columns([3, 1])

        with col3:        
            with col3:        
                m = leafmap.Map(zoom =20)
                m.add_basemap("SATELLITE")
                m.add_legend(title="Plot Status And Type", legend_dict=legend_dict)
                m.add_geojson(geojson_data, style_function= PlotsLayout.styleFunction, zoom_to_layer=zoom_to_layer)
                if selected_plot != "Overview":
                    plot_geometry = plot_data[selected_plot]["geometry"]
                    m.zoom_to_bounds(shape(plot_geometry).bounds)
                m.to_streamlit(height=500)

        with col4:
            cont1 = st.container(border = True)
            with cont1:
                st.markdown("### Report")
                if selected_plot != "Overview":
                    plot_id = plot_data[selected_plot]["properties"]["id"]
                    e_area = plot_data[selected_plot]["properties"]["E.Area(sqft)"]
                    p_area = plot_data[selected_plot]['properties']['P.Area(sqft)']
                    type = plot_data[selected_plot]["properties"]["Type"]
                    status = plot_data[selected_plot]["properties"]["Status"]
                    st.markdown(f"Plot: ***{plot_id}***")
                    st.markdown(f"P.Area (sq feet): ***{p_area}***")
                    st.markdown(f"E.Area (sq feet): ***{e_area}***")
                    st.markdown(f"Type: ***{type}***")
                    st.markdown(f"Status: ***{status}***")
              
def main():
    PlotsLayout.createLayout(title = "Vasuki Homes", file = "data/Kudur_Plots_Data.geojson")

if __name__ == '__main__':
    main()

