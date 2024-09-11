import streamlit as st
import leafmap.foliumap as leafmap
import json
from components import Config


class MyPropertyLocation:
    @staticmethod
    def create_my_property_location_content():
        
        project_geojson_file = "D:/StreamlitApp/data/KUDURUPROJBOUNDARY.geojson"
        plots_geojson_file = "D:\StreamlitApp\data\Kudur_Layout_Sites.geojson"
        
        Config.configure()
        
        st.markdown("# Vinayaka Housing Banner")
        st.markdown("## Project1: Kuduru Project Phase 1")

        col1, col2 = st.columns([1, 1])
        col1.markdown("**Owner Name:** XXX")
        col1.markdown("**Contact Number:** 99876 54332")
        col2.markdown("**Developer Name:** YYY")
        col2.markdown("**Whatsapp: 99999 99999**")

        col3, col4 = st.columns([3, 1])

        with col3:        
            m = leafmap.Map(minimap_control=True, zoom = 10)
            m.add_basemap("GoogleSatellite")
            m.add_geojson(project_geojson_file)
            m.add_geojson(plots_geojson_file, zoom_to_layer=False)
            m.to_streamlit(height=500)
        with col4:
            cont1 = st.container(border = True)
            with cont1:
                st.markdown("### Report")
                st.markdown("**Total Area:** XXX Acres")
                st.markdown("**Built Up Area:** YYY Acres")
                st.markdown("**Common Area:** ZZZ Acres")
                st.markdown("**No Of Sites:** 70")
                st.markdown("**Sites Sold:** 45")

def main():
    MyPropertyLocation.create_my_property_location_content()

if __name__ == '__main__':
    main()

