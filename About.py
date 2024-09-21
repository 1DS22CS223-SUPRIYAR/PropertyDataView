import streamlit as st
import leafmap.foliumap as leafmap
import json
from Components.components import Config


Config.configure(title = "Property Data Visualization")

def main():
    Config.app_sidebar()
    app_body()

def app_body():
    st.markdown("""
        <style>
        .centered-heading {
            text-align: center;
            margin-bottom: 20px;
        }
        .content {
            text-align: center;
            margin-top: 10px;
        }
        </style>
        """, unsafe_allow_html=True)
    st.markdown("<h1 style = 'text-align: center;'> M/S Vinayaka Housing </h1>" , unsafe_allow_html=True)
    st.markdown("<h1 class='centered-heading'>About Us</h1>", unsafe_allow_html=True)

    st.markdown("""
        <h2 class='centered-heading'>Overview</h2>
        <div class='content'>
        Welcome to <strong>Vasuki Homes 3</strong> – an innovative project by <strong>M/S Vinayaka Housing</strong> designed to help you explore and understand our residential plots. This interactive map provides a detailed view of available and sold plots, as well as other land types such as roads and resorts.
        </div>
        <h2 class='centered-heading'>Project Purpose</h2>
        <div class='content'>
        At <strong>M/S Vinayaka Housing</strong>, our goal is to provide transparent and accessible information about our residential plots. With our interactive map, you can:
        <ul style="text-align: left; margin: 0 auto; display: inline-block;">
            <li><strong>Visualize</strong>: See the geographic layout of available and sold plots.</li>
            <li><strong>Explore</strong>: Get detailed information about each plot, including its status and area.</li>
            <li><strong>Navigate</strong>: Easily switch between different plot types and zoom into specific areas of interest.</li>
        </ul>
        </div>
        <h2 class='centered-heading'>Features</h2>
        <div class='content'>
        <ul style="text-align: left; margin: 0 auto; display: inline-block;">
            <li><strong>Interactive Map</strong>: View an interactive map with satellite imagery.</li>
            <li><strong>Plot Status</strong>: Different colors represent different statuses of plots (Sold, Available).</li>
            <li><strong>Custom Legends</strong>: Understand the map with an easy-to-read legend.</li>
            <li><strong>Detailed Information</strong>: Select a plot to view detailed information including area.</li>
        </ul>
        </div>
        <h2 class='centered-heading'>How It Works</h2>
        <div class='content'>
        <ol style="text-align: left; margin: 0 auto; display: inline-block;">
            <li><strong>Select a Plot</strong>: Use the dropdown menu to choose between an overview of all plots or individual plots.</li>
            <li><strong>View Details</strong>: Click on a plot to see detailed information such as its area and status.</li>
            <li><strong>Explore Map</strong>: Use the interactive map to explore the layout of residential plots, roads, and resorts.</li>
        </ol>
        </div>
        <h2 class='centered-heading'>Contact Us</h2>
        <div class='content'>
        For more information, please feel free to reach out to us:<br></br>
        <ul style="text-align: left; margin: 0 auto; display: inline-block;">
            <li><strong>Email</strong>: contact@vinayakahousing.com</li>
            <li><strong>Phone</strong>: +123-456-7890</li>
            <li><strong>Address</strong>: Kuduru, Magadi, Ramanagara, Karnataka</li>
        </ul>
        </div>
        <div class='content'>
        Thank you for visiting <strong>Vasuki Homes 3</strong>. We hope this tool helps you find the perfect plot for your needs!
        </div>
        <div class='content'>
        <em>This application is part of our ongoing effort to make real estate information more accessible and user-friendly. We appreciate your feedback and suggestions.</em>
        </div>
    """, unsafe_allow_html=True)
    return None

if __name__ == '__main__':
    main()
