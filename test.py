import requests
import time
import json


import altair as alt
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import folium


def mark_map(row, m, map_lat, map_long, cols):

    curr_lat = row[map_lat]
    curr_long = row[map_long]

    tooltip_string = ""

    for col in cols:
        tooltip_string += "<b>" + str(col) + ": </b>" + str(row[col]) + "<br>"

    folium.Marker(
        [curr_lat, curr_long], popup=tooltip_string, tooltip=tooltip_string
    ).add_to(m)




def show_map():
    map_lat = "Lat"
    map_long = "Long_"

 
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/05-18-2020.csv"
    df = load_external_data(url).dropna()
    
    # st.dataframe(df)
    st.write("")
    st.write("")

    first_lat = df[map_lat].mean()
    first_long = df[map_long].mean()

    m = folium.Map(location=[first_lat, first_long], zoom_start=5)

    # now place a marker for each row in df
    df.apply(
        lambda row: mark_map(row, m, map_lat, map_long, df.columns), axis=1
        )


    folium_static(m)


@st.cache
def load_external_data(url):
    df = pd.read_csv(url)
    return df



def main():
    st.title("Teams Beta")
    st.header("Hello from teams")

    st.write("Here is a dataframe")
    url = "https://raw.githubusercontent.com/aether-ai/grimoire/master/grim/sample_data/iris.csv"
    df = load_external_data(url)
    st.dataframe(df)

    st.write("Here is a map")
    show_map()



if __name__ == "__main__":
    main()