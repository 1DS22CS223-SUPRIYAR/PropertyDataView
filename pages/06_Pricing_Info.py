import streamlit as st
from Components.components import Config

def create_pricing_info():

    Config.configure(title = "Pricing Info")
    Config.app_sidebar()

    st.markdown("# Pricing Information for Land Plots")
    st.markdown("## Select Your Preferred Land Option")

    
    st.markdown("""
    | Land Type   | Plot Size         | Features                                | Price in Rupees     |
    |-------------|--------------------|-----------------------------------------|-------------|
    | **Residential** | 4000 sq ft       | 🏡 Suitable for residential use | 30,00,000    |
  
    | **Industrial**  | 10,000 sq ft      | 🏭 Zoned for industrial use| 40,00,000    |
    """)


    st.markdown("## Additional Features")
    st.markdown("""
    - 🏞️ **Scenic Views**: Available for Residential plots.
    - 📈 **High Growth Area**: Commercial plots located in high-growth areas.
    - 🛠️ **Infrastructure Ready**: Industrial plots come with necessary infrastructure.
    """)


    st.markdown("## Ready to Invest?")
    st.markdown("""
    - **Contact Us**: [Inquire Now](#) to get more details about the land options.
    - **Site Visits**: Schedule a site visit by [Contacting Us](#) directly.
    """)

def main():
    create_pricing_info()

if __name__ == '__main__':
    main()
