#-----Contains Scripts Of My Project Location Page-----'''
#------Default Styles Are Imported From "components.py" File-----

import streamlit as st
import leafmap.foliumap as leafmap
import json
from shapely.geometry import shape
from Components.components import Config

class NearByAmenities:
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
            'fillColor': NearByAmenities.getColor(status, type),
            'color': 'black',
            'weight': 1.5,
            'fillOpacity': 0.6,
        }
    
    @staticmethod
    def amenity():
        print("Clicked")

    @staticmethod
    def createLayout(file, general_info_file, raster_file):
        #Default Configuration
        Config.configure(title = "Project Location")
        Config.app_sidebar()

        #Data
        no_of_sites = 0
        no_of_sites_sold = 0
        with open(file, 'r') as f:
            geojson_data = json.load(f)
        for feature in geojson_data['features']:
            if feature['properties'].get('Type') == "Residential":
                no_of_sites += 1
                if feature['properties'].get('Status') == "Sold":
                    no_of_sites_sold += 1

        no_of_sites_available = no_of_sites - no_of_sites_sold  
        legend_dict = {
            "Sold": "red",
            "Available": "green",
            "Road": "grey",
            "Resort": "purple",
            "Other": "yellow"
        }  

        amenities = {"School": "data/Schools.geojson", "Banks": "data/Schools.geojson","Bus Stop": "data/Schools.geojson", "Railway": "data/Schools.geojson", "Highway": "data/Schools.geojson", "Airport": "data/Schools.geojson"}    

        #Start Of Page Content
        st.markdown("<h1 style = 'text-align: center;'> M/S Vinayaka Housing </h1>" , unsafe_allow_html=True)
        st.markdown(f"""
            <h6 style = 'text-align: justify;'>
                Explore the essential amenities around your future home with ease! Our interactive map highlights nearby schools, shopping centers, hospitals, parks, and other key locations to help you make an informed decision. Whether it's ensuring your family has access to top-notch education or finding the perfect spot for a weekend outing, our property listings come with all the convenience of modern living right at your doorstep. Discover what makes each neighborhood special!
            </h6>
            """, unsafe_allow_html=True)
        

        selected_amenity = "Property"

        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

        if col1.button("Schools", use_container_width=True):
            selected_amenity = "School"   
            
        if col1.button("Railway",use_container_width=True):
            selected_amenity = "Railway"
        if col2.button("Banks",use_container_width=True):
            selected_amenity = "Banks"
        if col2.button("Bus Stop",use_container_width=True):
            selected_amenity = "Bus Stop"
        if col3.button("Highway",use_container_width=True):
            selected_amenity = "Highway"
        if col3.button("Airport",use_container_width=True):
            selected_amenity = "Airport"
        if col4.button("Back To Property", use_container_width=True):
            selected_amenity = "Property"

        #MAP and REPORT
        col5, col6 = st.columns([3, 1])
        
        with col5:        
            m = leafmap.Map(zoom = 10)
            m.add_basemap("SATELLITE")
            if selected_amenity != "Property":
                amenity_data_file = amenities[selected_amenity]
                with open(amenity_data_file, 'r') as file:
                    amenity_data = json.load(file)
                m.add_raster(raster_file, opacity = 0.8, layer_name="Project Overview")
                m.add_geojson(amenity_data, layer_name=selected_amenity, zoom_to_layer=True)
            else:
                m.add_legend(title="Plot Status And Type", legend_dict=legend_dict)
                m.add_raster(raster_file, opacity = 0.8, layer_name="Project Overview")
                m.add_geojson(file, style_function = NearByAmenities.styleFunction, layer_name="Plots", show_layer=False, zoom_to_layer=True)
            
            m.to_streamlit(height=500)
        with col6:
            cont1 = st.container(border = True)
        

def main():
    NearByAmenities.createLayout(file = "data/Kudur_Plots_Data.geojson", general_info_file = 'data/general_data.csv', raster_file = "data/ProjectLocation.tif")

if __name__ == '__main__':
    main()

