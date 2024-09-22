#-----Contains Scripts Of My Project Location Page-----'''
#------Default Styles Are Imported From "components.py" File-----

import streamlit as st
import leafmap.foliumap as leafmap
import json
import csv
from Components.components import Config

class MyPropertyLocation:
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
            'fillColor': MyPropertyLocation.getColor(status, type),
            'color': 'black',
            'weight': 1.5,
            'fillOpacity': 0.6,
        }
    
    @staticmethod
    def create_my_property_location_content(file, general_info_file, raster_file):
        #Default Configuration
        Config.configure(title = "Project Location")
        Config.app_sidebar()

        #Data
        with open(general_info_file, mode='r') as gf:
            general_info = csv.DictReader(gf)
            for row in general_info:
                village = row["VILLAGE"]
                taluk = row["TALUK"]
                district = row["DISTRICT"]
                survey_no = row["SURVEY #"]
                owner = row["OWNER"]
                contact = row["CONTACT #"]
                developer = row["DEVELOPER"]
                whatsapp = row["WHATSAPP"]
                total_area = row["TOTAL AREA"]
                site_area = row["SITE AREA"]

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

        #Start Of Page Content
        st.markdown("<h1 style = 'text-align: center;'> M/S Vinayaka Housing </h1>" , unsafe_allow_html=True)
        st.markdown(f"""
            <h3 style = 'text-align: center;'>
                <span>VILLAGE: {village}</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>TALUK: {taluk}</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>DISTRICT: {district}</span>
            </h3>
            """, unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center;'>SURVEY NO: {survey_no}</h3>", unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1])
        col1.markdown(f"Owner Name: ***{owner}***")
        col1.markdown(f"Contact #: ***{contact}***")
        col2.markdown(f"Developer Name: ***{developer}***")
        col2.markdown(f"Whatsapp: ***{whatsapp}***")

        #MAP and REPORT
        col3, col4 = st.columns([3, 1])
        with col3:        
            m = leafmap.Map(zoom = 10)
            m.add_basemap("SATELLITE")
            m.add_legend(title="Plot Status And Type", legend_dict=legend_dict)
            m.add_raster(raster_file, opacity = 0.8, layer_name = "Project Overview")
            m.add_geojson(file, style_function = MyPropertyLocation.styleFunction, layer_name="Plots", show_layer=False)
            m.to_streamlit(height=500)
        with col4:
            cont1 = st.container(border = True)
            with cont1:
                st.markdown("### Report")
                st.markdown(f"Total Area(acres): {total_area}")
                st.markdown(f"Site Area(acres): {site_area}")
                st.markdown(f"No Of Sites: ***{no_of_sites}***")
                st.markdown(f"Sites Sold: ***{no_of_sites_sold}***")

def main():
    MyPropertyLocation.create_my_property_location_content(file = "data/Kudur_Plots_Data.geojson", general_info_file = 'data/general_data.csv', raster_file = "data/ProjectLocation.tif")

if __name__ == '__main__':
    main()

