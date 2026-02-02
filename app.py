import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Researcher Profile and STEM Data Explorer", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Researcher Profile", "Publications", "STEM Data Explorer", "Contact"],
)

# Dummy STEM data
Chemistry_data = pd.DataFrame({
    "Experiment": ["TEM_EDX"] * 4,
    "Element": ["C", "O", "Fe", "Cu"],
    "Wt (percentage)": [82.34, 0.43, 2.82, 12.54,],
    "Date": pd.date_range(start="2024-01-01", periods=4),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (percentage)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# Sections based on menu selection
if menu == "Researcher Profile":
    st.title("Researcher Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Wendy Setsiba"
    field = "Analytical Chemistry"
    institution = "University of Pretoria"
    qualification = "Masters of Science in Chemistry"
    research_title = "A biohbrid platelet drug delivery device for the treatment of ischemic stroke"


    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Field of Research:** {field}")
    st.write(f"**Institution:** {institution}")
    st.write(f"**Qualification:** {qualification}")
    st.write(f"**Reasearch_Title:** {research_title}")
    
    st.image(
    "C:/Users/wphut/Downloads/Chemistry.jpg",
    caption="Chemistry"
)

elif menu == "Publications":
    st.title("Publications")
    st.sidebar.header("Upload and Filter")

    # Upload publications file
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)

        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")

        # Publication trends
        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)
        else:
            st.write("The CSV does not have a 'Year' column to visualize trends.")

elif menu == "STEM Data Explorer":
    st.title("STEM Data Explorer")
    st.sidebar.header("Data Selection")
    
    # Tabbed view for STEM data
    data_option = st.sidebar.selectbox(
        "Choose a dataset to explore", 
        ["Chemistry Experiments", "Astronomy Observations", "Weather Data"]
    )

    if data_option == "Chemistry Experiments":
        st.write("### Chemistry Experiment Data")
        st.dataframe(Chemistry_data)
        
       # Add widget to filter by Wt (percentage) levels
    Wtpercentage_filter = st.slider(
    "Filter by Wt (percentage)",
    min_value=0.43,
    max_value=82.34,
    value=(12.54, 82.34),
    step=0.01
)
        
    # Add widget to filter by elements
    element_filter = st.multiselect(
    "Select Elements",
    ["C", "O", "Fe", "Cu"],
    default=["C", "O", "Fe", "Cu"])
        
    filtered_Chemistry = Chemistry_data[ Chemistry_data["Wt (percentage)"].between(Wtpercentage_filter[0], Wtpercentage_filter[1])
    & (Chemistry_data["Element"].isin(element_filter)) ]
    st.write(f"Filtered Results for Wt (percentage)Range {Wtpercentage_filter}:")
    st.dataframe(filtered_Chemistry)
     
    if data_option == ("Astronomy Observations"):
       st.write("### Astronomy Observation Data")
       st.dataframe(astronomy_data)
        
    # Add widget to filter by Brightness
    brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
    filtered_astronomy = astronomy_data[
    astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
        ]
    st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
    st.dataframe(filtered_astronomy)

    if data_option == "Weather Data":
        st.write("### Weather Data")
        st.dataframe(weather_data)
        # Add widgets to filter by temperature and humidity
        temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
        humidity_filter = st.slider("Filter by Humidity (percentage)", 0, 100, (0, 100))
        filtered_weather = weather_data[
            weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
            weather_data["Humidity (percentage)"].between(humidity_filter[0], humidity_filter[1])
        ]
        st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
        st.dataframe(filtered_weather)
        
        

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "wphuti2@gmail.com"
    Cell_no = "+27713118450"
    st.write(f"You can reach me at {email}. {Cell_no}")
