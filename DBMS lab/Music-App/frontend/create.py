import streamlit as st
from database import add_data_album,add_data_artist,add_data_song,add_data_user
import pandas as pd

def create_album():
    col1,col2 = st.columns(2)
    with col1:
        AlbumID = st.text_input("Album ID")
        AlbumName = st.text_input("Album Name")

    with col2:
        AlbumYear = st.text_input("Album Year of Release")
        Genre = st.selectbox("Genre",["Pop","Hip hop","Rock","Jazz Rap"])

    if st.button("Add Album"):
        add_data_album(AlbumID,AlbumName,AlbumYear,Genre)
        st.success("Added Album {} to Database".format(AlbumName))

def create_artist():
    col1,col2 = st.columns(2)
    with col1:
        ArtistID = st.text_input("Artist ID")

    with col2:
        ArtistName = st.text_input("Artist Name")

    if st.button("Add Artist"):
        add_data_artist(ArtistID, ArtistName)
        st.success("Added Artist {} to Database".format(ArtistName))

def create_song():
    col1,col2,col3 = st.columns(3)
    with col1:
        SongID = st.text_input("Song ID")
        Streams = st.text_input("Number of streams")

    with col2:
        ArtistID = st.text_input("Artist ID")
        SongName = st.text_input("Song Name")

    with col3:
        AlbumID = st.text_input("Album ID")
        SongLength = st.text_input("Song Length")
        Genre = st.selectbox("Genre",["Pop","Hip hop","Rock","Jazz Rap"])

    if st.button("Add Song"):
        add_data_song(SongID,ArtistID,AlbumID,Streams,SongName,SongLength,Genre)
        st.success("Added Song {} to Database".format(SongName))

def create_user():
    col1,col2,col3 = st.columns(3)
    with col1:
        UserID = st.text_input("User ID")
        Dob = st.date_input("Date of Birth", value=None, min_value=pd.to_datetime("1945-01-01"), max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

    with col2:
        Email = st.text_input("Email ID")
        Gender = st.selectbox("Gender",["M","F"])

    with col3:
        UserPassword = st.text_input("Password")
        Subscription = st.selectbox("Subscription",["1","2"])
        DateSubscribed = st.date_input("Date Subscribed", value=None, min_value=pd.to_datetime("1945-01-01"), max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

    if st.button("Add User"):
        add_data_user(UserID,Email,UserPassword,Dob,Gender,Subscription,DateSubscribed)
        st.success("Added User {} to Database".format(UserID))
