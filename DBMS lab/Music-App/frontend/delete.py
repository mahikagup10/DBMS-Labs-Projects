import pandas as pd
import streamlit as st
from database import view_albums,view_artists,view_songs,view_users,view_only_album,view_only_artist,view_only_song,view_only_user,delete_data_album,delete_data_artist,delete_data_song,delete_data_user

def delete_album():
    result = view_albums()
    df = pd.DataFrame(result, columns=['AlbumID','AlbumName','AlbumYear','Genre'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_albums = [i[0] for i in view_only_album()]
    selected_album = st.selectbox("Album to Delete", list_of_albums)
    st.warning("Do you want to delete ::{}".format(selected_album))
    if st.button("Delete album"):
        delete_data_album(selected_album)
        st.success("Album has been deleted successfully")
    new_result = view_albums()
    df2 = pd.DataFrame(new_result, columns=['AlbumID','AlbumName','AlbumYea','Genre'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_artist():
    result = view_artists()
    df = pd.DataFrame(result, columns=['ArtistID','ArtistName'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_artists = [i[0] for i in view_only_artist()]
    selected_artist = st.selectbox("Artist to Delete", list_of_artists)
    st.warning("Do you want to delete ::{}".format(selected_artist))
    if st.button("Delete artist"):
        delete_data_artist(selected_artist)
        st.success("Artist has been deleted successfully")
    new_result = view_artists()
    df2 = pd.DataFrame(new_result, columns=['ArtistID','ArtistName'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_song():
    result = view_songs()
    df = pd.DataFrame(result, columns=['SongID','ArtistID','AlbumID','Streams','SongName','SongLength','Genre'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_songs = [i[0] for i in view_only_song()]
    selected_song = st.selectbox("Song to Delete", list_of_songs)
    st.warning("Do you want to delete ::{}".format(selected_song))
    if st.button("Delete Song"):
        delete_data_song(selected_song)
        st.success("Song has been deleted successfully")
    new_result = view_songs()
    df2 = pd.DataFrame(new_result, columns=['SongID','ArtistID','AlbumID','Streams','SongName','SongLength','Genre'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_user():
    result = view_users()
    df = pd.DataFrame(result, columns=['UserID','Email','UserPassword','Dob','Gender','Subscription','DateSubscribed'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_users = [i[0] for i in view_only_user()]
    selected_user = st.selectbox("User Entry to Delete", list_of_users)
    st.warning("Do you want to delete ::{}".format(selected_user))
    if st.button("Delete User entry"):
        delete_data_user(selected_user)
        st.success("User account has been deleted successfully")
    new_result = view_users()
    df2 = pd.DataFrame(new_result, columns=['UserID','Email','UserPassword','Dob','Gender','Subscription','DateSubscribed'])
    with st.expander("Updated data"):
        st.dataframe(df2)


