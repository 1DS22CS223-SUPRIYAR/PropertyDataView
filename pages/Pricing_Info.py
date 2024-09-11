import streamlit as st
from components import Config

def create_pricing_info():

    Config.configure()

    st.markdown("# Pricing Information for Land Plots")
    st.markdown("## Select Your Preferred Land Option")

    
    st.markdown("""
    | Land Type   | Plot Size         | Features                                | Price in Rupees     |
    |-------------|--------------------|-----------------------------------------|-------------|
    | **Residential** | 2000 sq ft       | 🏡 Suitable for residential use | 50,000      |
    | **Commercial**  | 5000 sq ft       | 🏢 Ideal for commercial developments| 120,000     |
    | **Industrial**  | 10,000 sq ft      | 🏭 Zoned for industrial use| 250,000     |
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
