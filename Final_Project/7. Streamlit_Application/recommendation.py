import seaborn as sns
import streamlit as st

import pandas as pd
import numpy as np


import base64
import datetime
from urllib.parse import urlencode


import json
import re
import sys
import itertools

from scipy.spatial import distance
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

import plotly.express as px

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util

import warnings
warnings.filterwarnings("ignore")


from skimage import io
import matplotlib.pyplot as plt
import plotly.graph_objects as go


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
    "Please Select anyone",
    ("Introduction","Exploratory Data Analysis","Market Analysis","Customer Segmentation using RFM","Churn Analysis","Recommendation System")
)




if add_selectbox == 'Recommendation System':
    st.title("Recommendations System :")
    st.write("-------------------------------------------------------------------------------------------------")


    def visualize_songs(df):
        """
        Visualize cover art of the songs in the inputted dataframe

        Parameters:
            df (pandas dataframe): Playlist Dataframe
        """

        temp = df['url'].values
        plt.figure(figsize=(15, int(0.625 * len(temp))))
        columns = 5

        for i, url in enumerate(temp):
            plt.subplot(len(temp) / columns + 1, columns, i + 1)

            image = io.imread(url)
            plt.imshow(image)
            plt.xticks(color='w', fontsize=0.1)
            plt.yticks(color='w', fontsize=0.1)
            plt.xlabel(df['name'].values[i], fontsize=12)
            plt.tight_layout(h_pad=0.4, w_pad=0)
            plt.subplots_adjust(wspace=None, hspace=None)
            st.image(image, width=None)
            st.write(df['name'].values[i], fontsize=12)

        plt.show()


    def get_playlist_edm():
        return pd.read_csv('playlist_EDM.csv')


    def get_playlist_metal():
        return pd.read_csv('playlist_Metal.csv')


    def get_playlist_rock():
        return pd.read_csv('playlist_Rock.csv')


    def get_playlist_english():
        return pd.read_csv('playlist_English_songs.csv')


    def get_playlist_hindi():
        return pd.read_csv('playlist_Hindi_songs.csv')


    def get_playlist_pop():
        return pd.read_csv('playlist_Pop.csv')


    def get_playlist_hip_hop():
        return pd.read_csv('playlist_Hip_Hop.csv')


    def get_playlist_latin():
        return pd.read_csv('playlist_Latin.csv')


    def get_playlist_beatles():
        return pd.read_csv('playlist_Beatles.csv')


    def get_playlist_mix():
        return pd.read_csv('playlist_Mix.csv')


    def get_playlist_nirvana():
        return pd.read_csv('playlist_Nirvana.csv')


    def get_data():
        return pd.read_csv('data.csv')

    def get_edm():
        return pd.read_csv('edm_top20.csv')

    def get_english():
        return pd.read_csv('english_top20.csv')

    def get_hindi():
        return pd.read_csv('hindi_top20.csv')

    def get_hip_hop():
        return pd.read_csv('hip_hop_top20.csv')

    def get_pop():
        return pd.read_csv('pop_top20.csv')

    def get_latin():
        return pd.read_csv('latin_top20.csv')

    def get_metal():
        return pd.read_csv('metal_top20.csv')

    def get_rock():
        return pd.read_csv('rock_top20.csv')

    def get_beatles():
        return pd.read_csv('beatles_top20.csv')

    def get_mix():
        return pd.read_csv('mix_top20.csv')

    def get_nirvana():
        return pd.read_csv('nirvana_top20.csv')


    def load_data():
        df = pd.DataFrame({'Name': [' ','Jack', 'Heather', 'Mark',
                                    'Chris', 'Ankit', 'Maria','Vincent','Zian',
                                    'Samuel','Becky','Robert']})
        return df

    df_english = get_english()
    df_edm = get_edm()
    df_hindi = get_hindi()
    df_latin = get_latin()
    df_rock = get_rock()
    df_hip_hop = get_hip_hop()
    df_pop = get_pop()
    df_metal = get_metal()
    df_beatles = get_beatles()
    df_mix = get_mix()
    df_data = get_data()
    df = load_data()

    st.subheader("Choose a Name : ")
    name_list = st.selectbox("Select User", df["Name"].unique())

    if name_list == 'Jack' :
        st.title("Current Playlist : ")

        visualize_songs(get_playlist_english())

        st.title("Recommended Songs : ")

        visualize_songs(get_english())

    elif name_list == 'Ankit' :
        st.title("Current Playlist : ")

        visualize_songs(get_playlist_hindi())

        st.title("Recommended Songs : ")

        visualize_songs(get_hindi())

    elif name_list == 'Heather' :
        st.title("Current Playlist : ")

        visualize_songs(get_playlist_metal())

        st.title("Recommended Songs : ")

        visualize_songs(get_metal())

    elif name_list == 'Mark' :
        st.title("Current Playlist : ")

        visualize_songs(get_playlist_rock())

        st.title("Recommended Songs : ")

        visualize_songs(get_rock())

    elif name_list == 'Vincent' :
        st.title("Current Playlist : ")

        visualize_songs(get_playlist_edm())

        st.title("Recommended Songs : ")

        visualize_songs(get_edm())

    elif name_list == 'Maria' :
        st.title("Current Playlist : ")

        visualize_songs(get_playlist_latin())

        st.title("Recommended Songs : ")

        visualize_songs(get_latin())

    elif name_list == 'Chris' :
        st.title("Current Playlist : ")

        visualize_songs(get_playlist_hip_hop())

        st.title("Recommended Songs : ")

        visualize_songs(get_hip_hop())

    elif name_list == 'Zian' :
        st.title("Current Playlist : ")

        visualize_songs(get_playlist_pop())

        st.title("Recommended Songs : ")

        visualize_songs(get_pop())


    elif name_list == 'Samuel' :
        st.title("Current Playlist : ")

        visualize_songs(get_playlist_beatles())

        st.title("Recommended Songs : ")

        visualize_songs(get_beatles())

    elif name_list == 'Becky' :
        st.title("Current Playlist : ")

        visualize_songs(get_playlist_mix())

        st.title("Recommended Songs : ")

        visualize_songs(get_mix())

    elif name_list == 'Robert' :
        st.title("Current Playlist : ")

        visualize_songs(get_playlist_nirvana())

        st.title("Recommended Songs : ")

        visualize_songs(get_nirvana())


elif add_selectbox == 'Introduction':
    st.title("Spotify Marketing Analytics")
    # st.image('C:/Users/jshar/OneDrive/Desktop/ADM_Final_Project/Spotify.jpeg')

    st.markdown(
        """
        
        Welcome to the web application with Sales Marketing Insights, Personalized Recommendation, RFM, and Churn Information required for the Marketing and Analysis team at Spotify, which will help them to view information of customers all in one place. Resulting in taking quick data-driven decisions for greater profits!
        
        """
    )




# elif add_selectbox == 'Artist Analysis':
#     st.title("Artist Analysis :")
#     st.write("-------------------------------------------------------------------------------------------------")
#
#
#     class SpotifyAPI(object):
#         access_token = None
#         access_token_expires = datetime.datetime.now()
#         access_token_did_expire = True
#         client_id = None
#         client_secret = None
#         token_url = "https://accounts.spotify.com/api/token"
#
#         def __init__(self, client_id, client_secret, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.client_id = client_id
#             self.client_secret = client_secret
#
#         def get_client_credentials(self):
#
#             # Returns a base64 encoded string
#
#             client_id = self.client_id
#             client_secret = self.client_secret
#             if client_secret == None or client_id == None:
#                 raise Exception("You must set client_id and client_secret")
#             client_creds = f"{client_id}:{client_secret}"
#             client_creds_b64 = base64.b64encode(client_creds.encode())
#             return client_creds_b64.decode()
#
#         def get_token_headers(self):
#             client_creds_b64 = self.get_client_credentials()
#             return {
#                 "Authorization": f"Basic {client_creds_b64}"
#             }
#
#         def get_token_data(self):
#             return {
#                 "grant_type": "client_credentials"
#             }
#
#         def perform_auth(self):
#             token_url = self.token_url
#             token_data = self.get_token_data()
#             token_headers = self.get_token_headers()
#             r = requests.post(token_url, data=token_data, headers=token_headers)
#             if r.status_code not in range(200, 299):
#                 raise Exception("Could not authenticate client")
#                 # return False
#             data = r.json()
#             now = datetime.datetime.now()
#             access_token = data['access_token']
#             expires_in = data['expires_in']  # seconds
#             expires = now + datetime.timedelta(seconds=expires_in)
#             self.access_token = access_token
#             self.access_token_expires = expires
#             self.access_token_did_expire = expires < now
#             return True
#
#         def get_access_token(self):
#             token = self.access_token
#             expires = self.access_token_expires
#             now = datetime.datetime.now()
#             if expires < now:
#                 self.perform_auth()
#                 return self.get_access_token()
#             elif token == None:
#                 self.perform_auth()
#                 return self.get_access_token()
#             return token
#
#         def get_resource_header(self):
#             access_token = self.get_access_token()
#             headers = {
#                 "Authorization": f"Bearer {access_token}"
#             }
#             return headers
#
#         def base_search(self, query_params):
#             headers = self.get_resource_header()
#             endpoint = "https://api.spotify.com/v1/search"
#             lookup_url = f"{endpoint}?{query_params}"
#             print(lookup_url)
#             r = requests.get(lookup_url, headers=headers)
#             if r.status_code not in range(200, 299):
#                 return {}
#             return r.json()
#
#         def search(self, query=None, operator=None, operator_query=None, search_type='artist'):
#             if query == None:
#                 raise Exception("A query is required")
#             if isinstance(query, dict):
#                 query = " ".join([f"{k}:{v}" for k, v in query.items()])
#             if operator != None and operator_query != None:
#                 if operator.lower() == "or" or operator == "not":
#                     operator = operator.upper()
#                     if isinstance(operator_query, str):
#                         query = f"{query} {operator} {operator_query}"
#             query_params = urlencode({"q": query, "type": search_type.lower()})
#             print(query_params)
#             return self.base_search(query_params)
#
#
#     def local_css(file_name):
#         with open(file_name) as f:
#             st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
#
#
#     local_css("style.css")
#
#     Types_of_Features = (
#         "acousticness", "danceability", "energy", "instrumentalness", "liveness", "loudness", "speechiness", "tempo",
#         "valence")
#
#     # st.title("Spotify Features App")
#     Name_of_Artist = st.text_input("Artist Name")
#     Name_of_Feat = st.selectbox("Feature", Types_of_Features)
#     button_clicked = st.button("OK")
#
#     # Spotipy
#
#     import spotipy
#     import spotify_client
#     import pandas as pd
#
#     import requests
#
#     client_id = '0db80e5faee14db69c32b08f82c9722d'
#     client_secret = 'c6978163f49541f1bcd5eb2115187104'
#
#     spotify = SpotifyAPI(client_id, client_secret)
#
#     Data = spotify.search({"artist": f"{Name_of_Artist}"}, search_type="track")
#
#     need = []
#     for i, item in enumerate(Data['tracks']['items']):
#         track = item['album']
#         track_id = item['id']
#         song_name = item['name']
#         popularity = item['popularity']
#         need.append(
#             (i, track['artists'][0]['name'], track['name'], track_id, song_name, track['release_date'], popularity))
#
#     Track_df = pd.DataFrame(need, index=None,
#                             columns=('Item', 'Artist', 'Album Name', 'Id', 'Song Name', 'Release Date', 'Popularity'))
#
#     access_token = spotify.access_token
#
#     headers = {
#         "Authorization": f"Bearer {access_token}"
#     }
#     endpoint = "https://api.spotify.com/v1/audio-features/"
#
#     Feat_df = pd.DataFrame()
#     for id in Track_df['Id'].iteritems():
#         track_id = id[1]
#         lookup_url = f"{endpoint}{track_id}"
#         ra = requests.get(lookup_url, headers=headers)
#         audio_feat = ra.json()
#         Features_df = pd.DataFrame(audio_feat, index=[0])
#         Feat_df = Feat_df.append(Features_df)
#
#     Full_Data = Track_df.merge(Feat_df, left_on="Id", right_on="id")
#
#     Sort_DF = Full_Data.sort_values(by=['Popularity'], ascending=False)
#
#     chart_df = Sort_DF[['Artist', 'Album Name', 'Song Name', 'Release Date', 'Popularity', f'{Name_of_Feat}']]
#
#     # Streamlit Chart
#
#     import altair as alt
#
#     feat_header = Name_of_Feat.capitalize()
#
#     st.header(f'{feat_header}' " vs. Popularity")
#     c = alt.Chart(chart_df).mark_circle().encode(
#         alt.X('Popularity', scale=alt.Scale(zero=False)), y=f'{Name_of_Feat}',
#         color=alt.Color('Popularity', scale=alt.Scale(zero=False)),
#         size=alt.value(200), tooltip=['Popularity', f'{Name_of_Feat}', 'Song Name', 'Album Name'])
#
#     st.altair_chart(c, use_container_width=True)
#
#     st.header("Table of Attributes")
#     st.table(chart_df)
#
#     st.write("acousticness: Confidence measure from 0.0 to 1.0 on if a track is acoustic.")
#     st.write(
#         "danceability: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.")
#     st.write(
#         "energy: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.")
#     st.write(
#         "instrumentalness: Predicts whether a track contains no vocals. “Ooh” and “aah” sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly “vocal”. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.")
#     st.write(
#         "liveness: Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.")
#     st.write(
#         "loudness: The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db.")
#     st.write(
#         "speechiness: Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.")
#     st.write(
#         "tempo: The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.")
#     st.write(
#         "valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).")
#
#     st.write(
#         "Information about features is from:  https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/")

# elif add_selectbox == 'Recommendation using Euclidean Distance':
#     st.title("Recommendation using Euclidean Distance :")
#     st.write("-------------------------------------------------------------------------------------------------")
#
#
#     def get_load_data():
#         return pd.read_csv('C:/Users/jshar/OneDrive/Desktop/ADM_Final_Project/data_Euclidean_Distance.csv')
#
#
#     # def make_matrix(df, best, number, artist):
#     #     st.write(best)
#     #     st.write(artist)
#     #     st.write("++" , df['artists'])
#     #
#     #
#     #     df.drop_duplicates(subset=['artists', 'name'], inplace=True)
#     #     x = df[(df['name'] == best) & (df['artists'] == artist)].drop(columns=['name', 'artists']).values
#     #     #st.write("oooo",x)
#     #     artist = artist.replace("'", "").replace("'", "").replace('[', '').replace(']', '')
#     #     st.write("ddddd" , artist)
#     #     if ',' in artist:
#     #         inm = artist.rfind(",")
#     #         st.write("####",inm)
#     #         artist = artist[:inm] + ' and' + artist[inm + 1:]
#     #         st.write("$$$$",artist)
#     #     print('The song closest to your search is :', best, ' by ', artist)
#     #     st.write("The song closest to your search is :", best, " by ", artist)
#     #
#     #     song_names = df['name'].values
#     #     st.write("++++", song_names)
#     #     # df=df.fillna(df.mean())
#     #     p = []
#     #     count = 0
#     #     for i in df.drop(columns=['artists', 'name']).values:
#     #         p.append([distance.euclidean(x, i), count])
#     #         count += 1
#     #     p.sort()
#     #     # for i in range(1, number):
#     #     #     artists = data['artists']
#     #     #     st.write(artists)
#     #     for i in range(1, number + 1):
#     #         artists = data['artists']
#     #         artist = artists[p[i][1]]
#     #         # artist = artist.replace("'", "").replace("'", "").replace('[', '').replace(']', '')
#     #         if ',' in artist:
#     #             inm = artist.rfind(",")
#     #             st.write("[[[]]]")
#     #             artist = str(artist[:inm]) + ' and' + str(artist[inm + 1:])
#     #             st.write("?????")
#     #             print("??????")
#     #         print(song_names, 'by', artist)
#     #         st.write(song_names, 'by', artist)
#
#     def make_matrix(df, best, number, artist):
#         # st.write("test2")
#         df.drop_duplicates(subset=['artists', 'name'], inplace=True)
#         # st.write("test3")
#         x = df[(df['name'] == best) & (df['artists'] == artist)].drop(columns=['name', 'artists']).values
#         #y = x.squeeze()
#         y = x.flatten()
#         # st.write(y)
#         z = pd.Series(y)
#         # st.write("FFF",type(y))
#         # #st.write("DDD", type(z))
#         # st.write("FFF", y)
#         artist = artist.replace("'", "").replace("'", "").replace('[', '').replace(']', '')
#         if ',' in artist:
#             inm = artist.rfind(",")
#             st.write(type(inm))
#             artist = artist[:inm] + ' and' + artist[inm + 1:]
#         print('The song closest to your search is :', best, ' by ', artist)
#
#         song_names = df['name'].values
#         #    df=df.fillna(df.mean())
#         p = []
#         count = 0
#         for i in df.drop(columns=['artists', 'name']).values:
#             #st.write(distance.euclidean(z, i))
#             p.append([distance.euclidean(z,i), count])
#             count += 1
#         p.sort()
#         st.write(type(number))
#         for i in range(int(number) + 1):
#             artists = data['artists'].values
#             artist = artists[p[i][1]]
#             artist = artist.replace("'", "").replace("'", "").replace('[', '').replace(']', '')
#             if ',' in artist:
#                 inm = artist.rfind(",")
#                 artist = artist[:inm] + ' and' + artist[inm + 1:]
#             print(song_names[p[i][1]], 'by', artist)
#             st.write(song_names[p[i][1]], 'by', artist)
#
#
#     def find_word(word, df, number = 10):
#         df.drop_duplicates(inplace=True)
#         words = df['name'].values
#         artists = df['artists'].values
#         t = []
#         count = 0
#         if word[-1] == ' ':
#             word = word[:-1]
#         for i in words:
#             if word.lower() in i.lower():
#                 t.append([len(word) / len(i), count])
#             else:
#                 t.append([0, count])
#             count += 1
#         t.sort(reverse=True)
#         s = [[words[t[i][1]], artists[t[i][1]].strip('][').split(', ')] for i in range(number)]
#         songs = [words[t[i][1]] for i in range(number)]
#         artist = [artists[t[i][1]] for i in range(number)]
#         x = []
#         for i in s:
#             l = ''
#             by = ''
#             for j in i[1]:
#                 by += j
#             l += i[0] + ' by ' + by
#             x.append(l)
#         tup = []
#         for i in range(number):
#             tup.append((x[i], i))
#             #tup.append(x[i])
#
#
#         return tup, songs, artist
#
#     data = get_load_data()
#
#
#     a = st.text_area("Enter Song Name : ")
#
#     if a:
#         b = st.text_area("Please enter the number of recommendations you want : ")
#
#         if b:
#             # tup, s, ar = find_word(a, data)
#             # st.write("tup" , tup)
#             # st.write("s",s)
#             # st.write("ar",ar)
#             #
#             # ans = []
#             # for i in range(10):
#             #     ans.append(tup[i][0])
#             #
#             # ans1 = st.selectbox("Closest Song : ", ans)
#             #
#             # song_name = ans1.split(" by ")[0]
#             # artist_name = ans1.split(" by ")[1]
#             #
#             # artist = "[" + str(artist_name) + "]"
#             # # artist.append(artist_name)
#
#             tup, s, ar = find_word(a, data)
#
#             ans = []
#             for i in range(10):
#                 ans.append(tup[i][0])
#
#             ans1 = st.selectbox("Closest Song : ", ans)
#
#
#             #st.write(ans)
#             if ans1:
#                 song_name = ans1.split(" by ")[0]
#                 artist_name = ans1.split(" by ")[1]
#
#                 artist = "[" + str(artist_name) + "]"
#                 # artist.append(artist_name)
#                 # st.write(ans1)
#                 make_matrix(data, song_name, b, artist_name)
#                 # make_matrix(data,song_name,b,artist_name)
#
#     # #b = st.number_input('Please enter the number of recommendations you want: ')
#     # b = st.text_area("Please enter the number of recommendations you want : ")
#     # tup, s, ar = find_word(a, data)
#     #
#     # ans = st.selectbox("Closest Songs : ", a)
#     #
#     # make_matrix(data, s[ans.value], b, ar[ans.value])

elif add_selectbox == 'Exploratory Data Analysis':
    st.title("Exploratory Data Analysis :")
    st.write("-------------------------------------------------------------------------------------------------")

    def get_year():
        return pd.read_csv('data_by_year.csv')

    def get_w_genre():
        return pd.read_csv('data_w_genres.csv')

    def get_by_genre():
        return pd.read_csv('data_by_genres.csv')

    def get_data():
        return pd.read_csv('data.csv')


    df_year = get_year()
    df_w = get_w_genre()
    df_genre = get_by_genre()
    data = get_data()

    df_year = df_year[:101]

    df_year_control = df_year.copy()
    df_year_control['acousticness'] = df_year_control['acousticness'] / df_year_control['acousticness'].max()
    df_year_control['danceability'] = df_year_control['danceability'] / df_year_control['danceability'].max()
    df_year_control['duration_ms'] = df_year_control['duration_ms'] / df_year_control['duration_ms'].max()
    df_year_control['energy'] = df_year_control['energy'] / df_year_control['energy'].max()
    df_year_control['instrumentalness'] = df_year_control['instrumentalness'] / df_year_control[
        'instrumentalness'].max()
    df_year_control['liveness'] = df_year_control['liveness'] / df_year_control['liveness'].max()
    df_year_control['speechiness'] = df_year_control['speechiness'] / df_year_control['speechiness'].max()
    df_year_control['tempo'] = df_year_control['tempo'] / df_year_control['tempo'].max()
    df_year_control['valence'] = df_year_control['valence'] / df_year_control['valence'].max()
    df_year_control['popularity'] = df_year_control['popularity'] / df_year_control['popularity'].max()
    df_year_control['loudness'] = df_year_control['loudness'] / df_year_control['loudness'].min()
    df_year_control['year'] = df_year_control['year'].astype(str)

    df_year_control.drop(["key", "mode"], axis=1, inplace=True)
    df_year_control = df_year_control.melt("year")

    fig = px.line_polar(df_year_control, r="value", theta="variable", line_close=True,
                        animation_frame="year", template="plotly_dark", range_r=(0, 1))
    fig.update_traces(fill='toself')
    fig.update_layout(font_size=15)
    st.write(fig)

#Top Artists with Popularity by Sum
    fig = plt.figure(figsize=(16, 8))
    sns.set(style="whitegrid")
    x = data.groupby("artists")["popularity"].sum().sort_values(ascending=False).head(20)
    ax = sns.barplot(x.index, x)
    ax.set_title('Top Artists with Popularity by Sum')
    ax.set_ylabel('Popularity')
    ax.set_xlabel('Artists')
    plt.xticks(rotation = 90)
    st.write(fig)

#Top Tracks with Popularity
    df1 = data.copy()
    df1['duration_ms'] = df1['duration_ms'] / 1000
    df1.rename({'duration_ms': 'duration_in_seconds'}, axis=1, inplace=True)

    fig1 = plt.figure(figsize=(16, 8))
    g_pn = df1.groupby("name")['popularity'].sum().sort_values(ascending=False)[:20]
    axis = sns.lineplot(g_pn.index, g_pn, palette='rocket')
    axis.set_title('Top Tracks with Popularity')
    axis.set_ylabel('Popularity')
    axis.set_xlabel('Tracks')
    plt.xticks(rotation=90)
    st.write(fig1)

#Top artists with tracks
    fig2 = plt.figure(figsize=(16, 8))
    g_an = df1.groupby('artists')['name'].count().sort_values(ascending=False)[:20]
    axis = sns.barplot(g_an.index, g_an, palette='winter')
    axis.set_title('Top artists with tracks')
    axis.set_ylabel('Track count')
    axis.set_xlabel('Artists')
    plt.xticks(rotation=90)
    st.write(fig2)

#popularity by years group

    bins = [1920, 1960, 2000, 2020]
    df1['year_bins'] = pd.cut(df1['year'], bins, labels=['20s-60s', '60s-2000', '2000-2020'])
    df1['year_bins'].head(10)

    fig3 = plt.figure(figsize=(10, 5))
    g_yp = df1.groupby('year_bins')['popularity'].mean().sort_values(ascending=False)[:20]
    axis = sns.barplot(g_yp.index, g_yp, palette='autumn_r')
    axis.set_title('popularity categories')
    axis.set_xlabel('Categories')
    axis.set_ylabel('popularity')
    plt.xticks(rotation=90)
    st.write(fig3)







elif add_selectbox == 'Customer Segmentation using RFM':
    st.title("Customer Segmentation using RFM :")
    st.write("-------------------------------------------------------------------------------------------------")

    def get_rfm():
        return pd.read_csv('rfm_level_ag - Copy.csv')

    rfm = get_rfm()

    # rfm_new = pd.DataFrame()

    # arr = []
    #
    #
    # rfm_new['MonetaryValue'] = rfm['MonetaryValue']
    # rfm_new['MonetaryValue1'] = rfm['MonetaryValue1']
    def get_customers():
        return pd.read_csv('customers.csv')




    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#FF00FF', '#C0C0C0']
    # st.write("Value", rfm['MonetaryValue(Mean)'])
    # st.write("Count", rfm['MonetaryValue(Count)'])
    values = rfm['MonetaryValue1']
    # st.write("RRR" , values)
    labels = rfm['Customer Segment']
    # st.write("Label ", labels)
    # st.write()

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    st.write(fig)

    customers = get_customers()

    from sklearn.preprocessing import StandardScaler
    from sklearn.cluster import KMeans

    # Initialize the Object
    scaler = StandardScaler()
    # Fit and Transform The Data
    scaler.fit(customers)
    customers_normalized = scaler.transform(customers)


    sse = {}
    for k in range(1, 8):
        kmeans = KMeans(n_clusters=k, random_state=1)
        kmeans.fit(customers_normalized)
        sse[k] = kmeans.inertia_

    x = list(sse.keys())
    y = list(sse.values())

    plt.bar(x, y, align='center')  # A bar chart
    plt.xlabel('Bins')
    plt.ylabel('Frequency')
    plt.plot(x, y)
    plt.show()



if add_selectbox == 'Churn Analysis':
    st.title("Churn Analysis : ")
    st.write("-------------------------------------------------------------------------------------------------")

    st.markdown(
        """
        # Purchase Frequency : 93.053
        
        
        # Repeat Rate : 0.333
        
        
        
        # Churn Rate : 0.666
        """
                )

    def get_sales():
        return pd.read_csv('sale.csv')

    def get_rfm_segment():
        return pd.read_csv('RFM_Segment.csv')

    sales = get_sales()
    rfm2 = get_rfm_segment()

    id = st.selectbox("Select CustomerID : ",sales['CustomerID'])


    if id:
        count = -1
        for i in sales['CustomerID']:
            count = count + 1
            if id == i:
                st.title("Customer Lifetime Value: ")
                st.subheader(sales['CLV'][count])
                st.title(rfm2['Customer Segment'][count])




if add_selectbox == 'Market Analysis':
    st.title("Market Analysis")
    st.write("-------------------------------------------------------------------------------------------------")

    st.markdown("""
        <iframe width="900" height="1000" src="https://app.powerbi.com/view?r=eyJrIjoiODAwMmNlMWEtNGFlNS00Zjg2LWE3YzAtZGFkNDE0NTg1YTU0IiwidCI6ImE4ZWVjMjgxLWFhYTMtNGRhZS1hYzliLTlhMzk4YjkyMTVlNyIsImMiOjN9" frameborder="0" style="border:0" allowfullscreen></iframe>
        """, unsafe_allow_html=True)



