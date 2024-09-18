#-----Contains Scripts Of Utsav Club Page-----'''
#------Default Styles Are Imported From "components.py" File-----

import streamlit as st
import leafmap.foliumap as leafmap
import json
from shapely.geometry import shape
from components import Config


class ResortLayout:

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
            'fillColor': ResortLayout.getColor(status, type),
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
        st.markdown("<h3 style='text-align: center;'>Utsav Club 3</h3>", unsafe_allow_html=True)
      
        col1, col2 = st.columns([1, 1])

        # Extract resort names or IDs
        resort_names = ["Overview"] 
        resort_data = {}
        i = 0
        for feature in geojson_data['features']:
            if feature['properties'].get('Type') == "Resort":
                i += 1
                resort_id = feature['properties'].get('id', 'Unknown')
                resort_names.append("Utsav Club 3 - "+" "+str(i))
                resort_data["Utsav Club 3 - "+" "+str(i)] = feature  

        # Dropdown to select a resort
        selected_resort = st.selectbox("Select:", resort_names)
        zoom_to_layer = True
        if selected_resort == "Overview":
            target_geojson = geojson_data
        else:
            target_geojson = {"type": "FeatureCollection", "features": [resort_data[selected_resort]]}
            zoom_to_layer = False 
        col3, col4 = st.columns([3, 1])

        with col3:        
            with col3:        
                m = leafmap.Map(zoom =20)
                m.add_basemap("SATELLITE")
                m.add_legend(title="Plot Status And Type", legend_dict=legend_dict)
                m.add_geojson(geojson_data, style_function= ResortLayout.styleFunction, zoom_to_layer=zoom_to_layer)
                if selected_resort != "Overview":
                    plot_geometry = resort_data[selected_resort]["geometry"]
                    m.zoom_to_bounds(shape(plot_geometry).bounds)
                m.to_streamlit(height=500)

        with col4:
            cont1 = st.container(border = True)
            with cont1:
                st.markdown("### Report")
                if selected_resort != "Overview":
                    e_area = resort_data[selected_resort]["properties"]["E.Area(sqft)"]
                    p_area = resort_data[selected_resort]['properties']['P.Area(sqft)']
                    type = resort_data[selected_resort]["properties"]["Type"]
                    st.markdown(f"P.Area (sq feet): ***{p_area}***")
                    st.markdown(f"E.Area (sq feet): ***{e_area}***")
                    st.markdown(f"Type: ***{type}***")
        
              

def main():
    ResortLayout.createLayout(title = "Utsav Club 3", file = "data/Kudur_Plots_Data.geojson")

if __name__ == '__main__':
    main()

