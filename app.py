# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 12:44:38 2026

@author: wphut
"""

import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile Page with STEM Data")

# Collect basic information
name = "Wendy Setsiba"
field = "Analytical Chemistry"
institution = "University of Pretoria"
qualification = "Masters of Science in Chemistry"
research_title = "A biohybrid platelet drug delivery device for the treatment of ischemic stroke"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")
st.write(f"**Qualification:** {qualification}")
st.write(f"**Research Title:** {research_title}")

st.image(
    "C:/Users/wphut/Downloads/Chemistry.jpg",
    caption="Chemistry"
)

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Filter by keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Visualize publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add STEM Data Section
st.header("Explore STEM Data")

# Generate dummy data
Chemistry_data = pd.DataFrame({
    "Experiment": ["TEM_EDX"] * 4,
    "Element": ["C", "O", "Fe", "Cu"],
    "Wt (percentage)": [82.34, 0.43, 2.82, 12.54],
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

# Tabbed view for STEM data
st.subheader("STEM Data Viewer")
data_option = st.selectbox(
    "Choose a dataset to explore", 
    ["Chemistry Experiments", "Astronomy Observations", "Weather Data"]
)

# Chemistry Experiments Section
if data_option == "Chemistry Experiments":
    st.write("### Chemistry Experiment Data")

    # Dropdown to select Element
    selected_element = st.selectbox(
        "Select Element",
        options=["All"] + Chemistry_data["Element"].unique().tolist()
    )


    # Slider to filter by Wt (percentage)
    Wtpercentage_filter = st.slider(
        "Filter by Wt (percentage)",
        min_value=float(Chemistry_data["Wt (percentage)"].min()),
        max_value=float(Chemistry_data["Wt (percentage)"].max()),
        value=(float(Chemistry_data["Wt (percentage)"].min()), float(Chemistry_data["Wt (percentage)"].max())),
        step=0.01
    )

    # Filter dataframe based on Element and Wt
    filtered_Chemistry = Chemistry_data[
        (Chemistry_data["Wt (percentage)"] >= Wtpercentage_filter[0]) &
        (Chemistry_data["Wt (percentage)"] <= Wtpercentage_filter[1])
    ]

    if selected_element != "All":
        filtered_Chemistry = filtered_Chemistry[filtered_Chemistry["Element"] == selected_element]

    st.write(f"Filtered Results for Element: {selected_element} and Wt Range: {Wtpercentage_filter}")
    st.dataframe(filtered_Chemistry)

# Astronomy Observations Section
elif data_option == "Astronomy Observations":
    st.write("### Astronomy Observation Data")
    
    # Slider to filter by Brightness
    brightness_filter = st.slider(
        "Filter by Brightness (Magnitude)",
        min_value=float(astronomy_data["Brightness (Magnitude)"].min()),
        max_value=float(astronomy_data["Brightness (Magnitude)"].max()),
        value=(float(astronomy_data["Brightness (Magnitude)"].min()), float(astronomy_data["Brightness (Magnitude)"].max())),
        step=0.1
    )

    filtered_astronomy = astronomy_data[
        astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
    ]

    st.write(f"Filtered Results for Brightness Range: {brightness_filter}")
    st.dataframe(filtered_astronomy)

# Weather Data Section
elif data_option == "Weather Data":
    st.write("### Weather Data")
    
    # Sliders to filter by temperature and humidity
    temp_filter = st.slider(
        "Filter by Temperature (°C)",
        min_value=float(weather_data["Temperature (°C)"].min()),
        max_value=float(weather_data["Temperature (°C)"].max()),
        value=(float(weather_data["Temperature (°C)"].min()), float(weather_data["Temperature (°C)"].max())),
        step=0.1
    )

    humidity_filter = st.slider(
        "Filter by Humidity (percentage)",
        min_value=0,
        max_value=100,
        value=(0, 100)
    )

    filtered_weather = weather_data[
        weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
        weather_data["Humidity (percentage)"].between(humidity_filter[0], humidity_filter[1])
    ]

    st.write(f"Filtered Results for Temperature: {temp_filter} and Humidity: {humidity_filter}")
    st.dataframe(filtered_weather)

# Contact Section
st.header("Contact Information")
email = "wphuti2@gmail.com"
cell_no = "+27713118450"
st.write(f"You can reach {name} at {email}, {cell_no}.")
