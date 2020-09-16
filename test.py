import requests
import time
import json


import altair as alt
import pandas as pd
import streamlit as st


@st.cache
def load_external_data():
    sample_iris_url = "https://raw.githubusercontent.com/aether-ai/grimoire/master/grim/sample_data/iris.csv"
    df = pd.read_csv(sample_iris_url)
    return df



def main():
    st.title("Teams Beta")
    st.header("Hello from teams")

    st.write("Here is a dataframe")
    df = load_external_data()
    st.dataframe(df)



if __name__ == "__main__":
    main()