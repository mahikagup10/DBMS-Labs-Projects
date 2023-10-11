import streamlit as st
import pandas as pd
import plotly.express as px
from database import view_albums,view_artists,view_songs,view_users

def read_album():
    result = view_albums()
    df = pd.DataFrame(result,columns = ['AlbumID','AlbumName','AlbumYear','Genre'])

    with st.expander("View all Albums"):
        st.dataframe(df)

def read_artist():
    result = view_artists()
    df = pd.DataFrame(result,columns = ['ArtistID','ArtistName'])

    with st.expander("View all Artists"):
        st.dataframe(df)

def read_song():
    result = view_songs()
    df = pd.DataFrame(result,columns = ['SongID','ArtistID','AlbumID','Streams','SongName','SongLength','Genre'])

    with st.expander("View all Songs"):
        st.dataframe(df)

def read_user():
    result = view_users()
    df = pd.DataFrame(result,columns = ['UserID','Email','UserPassword','Dob','Gender','Subscription','DateSubscribed'])

    with st.expander("View all User Accounts"):
        st.dataframe(df)