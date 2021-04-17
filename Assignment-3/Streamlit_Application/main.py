
import streamlit as st

import numpy as np
import pandas as pd

from PIL import Image

import imageio




html = """
  <style>
    .reportview-container {
      flex-direction: row;
    }

    header > .toolbar {
      flex-direction: row;
      left: 2rem;
      right: auto;
    }

    body {
    color: #fff;
    background-color: #ff0000;
    }

    .sidebar .sidebar-collapse-control,
    .sidebar.--collapsed .sidebar-collapse-control {
      left: auto;
      right: 0.5rem;
      background-color: #ff6347
    }

    .sidebar .sidebar-content {
      transition: margin-right .6s, box-shadow .6s;
      color: #fff;
      background-color: #ff6347;
    }

    .sidebar.--collapsed .sidebar-content {
      margin-left: auto;
      margin-right: -18rem;
      background-color: #ff6347;
    }

    @media (max-width: 991.98px) {
      .sidebar .sidebar-content {
        margin-left: auto;
        background-color: #ff6347
      }
    }
  </style>
"""

st.markdown(html, unsafe_allow_html=True)

add_selectbox = st.sidebar.radio(
    "Please Select a search method",
    ("Artistic Similarity Search", "Facebook AI")
)

if add_selectbox == 'Artistic Similarity Search':
    st.title("**_Recommendations using Artistic Similarity Search_** :camera:")
    st.write("-------------------------------------------------------------------------------------------------")


    def get_data():
        return pd.read_csv('CosineSimilarityOutput.csv')

    n = 1
    df = get_data()
    count = 0

    # images1 = df['second']
    st.subheader("Choose an image :camera:")
    uploaded_file = st.file_uploader("Images:", type="jpg")
    if uploaded_file is not None:
        count = 1
        pic = uploaded_file.name
        st.image(pic, width=None)
        st.write("Classifying...")

    if count == 0:
        st.write("**OR**")
        images = df['0'].unique()
        st.subheader("Select an image below :point_down:")
        pic = st.selectbox('Images:', images)
        st.write("**Image you selected:**")
        st.image(pic, width=None)
        st.write("Classifying...")


    z = st.slider('How many similar products would you like to see?', 1, 10, 5)
    st.write("-------------------------------------------------------------------------------------------------")
    st.subheader("YOU MAY ALSO LIKE:")
    # st.write('**Images similar to the image selected by you:**')
    for index, row in df.iterrows():
        if row['0'] == pic:
            while n < z + 1:
                st.image(row[n], use_column_width=None, caption=row[n])
                n += 1




elif add_selectbox == 'Facebook AI':
    st.title("**_Recommendations using facebook AI_** :computer:")
    st.write("-------------------------------------------------------------------------------------------------")


    def get_data():
        return pd.read_csv('FaissOutput.csv')

    n = 1
    df = get_data()
    count1 = 0


    st.subheader("Choose an image :camera:")
    uploaded_file = st.file_uploader("Images:", type="jpg")
    if uploaded_file is not None:
        count1 = 1
        pic = uploaded_file.name
        st.image(pic, width=None)
        st.write("Classifying...")

    if count1 == 0:
        st.write("**OR**")
        images = df['0'].unique()
        st.subheader("Select an image below :point_down:")
        pic = st.selectbox('Images:', images)
        st.write("**Image you selected:**")
        st.image(pic, width=None)
        st.write("Classifying...")

    z = st.slider('How many similar products would you like to see?', 1, 10, 5)
    st.write("-------------------------------------------------------------------------------------------------")
    st.subheader("YOU MAY ALSO LIKE:")
    # st.write('**Images similar to the image selected by you:**')
    for index, row in df.iterrows():
        if row['0'] == pic:
            while n < z + 1:
                st.image(row[n], use_column_width=None, caption=row[n])
                n += 1

