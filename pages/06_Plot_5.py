import streamlit as st
import leafmap.foliumap as leafmap
import json
from shapely.geometry import shape
from components import Plot

def main():
    Plot.create_plot(title = "Plot 1", file = "D:\StreamlitApp\data\Kudur_Layout_Sites.geojson", plot_number = 4)

if __name__ == '__main__':
    main()

