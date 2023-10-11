import streamlit as st
import pandas as pd
from database import view_albums,view_artists,view_songs,view_users,view_only_album,view_only_artist,view_only_song,view_only_user,get_albums,get_artists,get_songs,get_users,edit_album,edit_artist,edit_song,edit_user

def update_album():
    result = view_albums()
    df = pd.DataFrame(result,columns = ['AlbumID','AlbumName','AlbumYear','Genre'])
    with st.expander("Current Albums"):
        st.dataframe(df)

    #st.write(view_only_album())
    list_of_albums = [i[0] for i in view_only_album()]

    selected_albums = st.selectbox("Album to edit",list_of_albums)
    selected_result = get_albums(selected_albums)
    if selected_result:
        AlbumID = selected_result[0][0]
        AlbumName = selected_result[0][1]
        AlbumYear = selected_result[0][2]
        Genre = selected_result[0][3]

        col1, col2 = st.columns(2)
        with col1:
            newAlbumID = st.text_input("Album No", AlbumID)
            newAlbumName = st.text_input("Album Name", AlbumName)
        with col2:
            newAlbumYear = st.text_input("Year of release",AlbumYear)
            newGenre = st.selectbox("Genre",["Pop","Hip hop","Rock","Jazz Rap"])

        if st.button("Update Album"):
            edit_album(newAlbumID,newAlbumName,newAlbumYear,newGenre,AlbumID,AlbumName,AlbumYear,Genre)
            st.success("Successfully updated values for album:: {} to ::{}".format(AlbumName, newAlbumName))

    result2 = view_albums()
    df2 = pd.DataFrame(result2, columns=['AlbumID','AlbumName','AlbumYear','Genre'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_artist():
    result = view_artists()
    df = pd.DataFrame(result,columns = ['ArtistID','ArtistName'])
    with st.expander("Current Artists"):
        st.dataframe(df)

    #st.write(view_only_album())
    list_of_artists = [i[0] for i in view_only_artist()]

    selected_artists = st.selectbox("Artist to edit",list_of_artists)
    selected_result = get_artists(selected_artists)
    if selected_result:
        ArtistID = selected_result[0][0]
        ArtistName = selected_result[0][1]

        col1, col2 = st.columns(2)
        with col1:
            newArtistID = st.text_input("Artist ID", ArtistID)
        with col2:
            newArtistName = st.text_input("Artist Name",ArtistName)

        if st.button("Update Artist"):
            edit_album(newArtistID,newArtistName,ArtistID,ArtistName)
            st.success("Successfully updated values for artist:: {} to ::{}".format(ArtistName, newArtistName))

    result2 = view_artists()
    df2 = pd.DataFrame(result2, columns=['ArtistID','ArtistName'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_song():
    result = view_songs()
    df = pd.DataFrame(result,columns = ['SongID','ArtistID','AlbumID','Streams','SongName','SongLength','Genre'])
    with st.expander("Current Songs"):
        st.dataframe(df)

    #st.write(view_only_album())
    list_of_songs = [i[0] for i in view_only_song()]

    selected_songs = st.selectbox("Songs to edit",list_of_songs)
    selected_result = get_songs(selected_songs)
    if selected_result:
        SongID = selected_result[0][0]
        ArtistID = selected_result[0][1]
        AlbumID = selected_result[0][2]
        Streams = selected_result[0][3]
        SongName = selected_result[0][4]
        SongLength = selected_result[0][5]
        Genre = selected_result[0][6]

        col1,col2,col3 = st.columns(3)
        with col1:
            newSongID = st.text_input("Song ID",SongID)
            newStreams = st.text_input("Number of streams",Streams)

        with col2:
            newArtistID = st.text_input("Artist ID",ArtistID)
            newSongName = st.text_input("Song Name",SongName)

        with col3:
            newAlbumID = st.text_input("Album ID",AlbumID)
            newSongLength = st.text_input("Song Length",SongLength)
            newGenre = st.selectbox("Genre",["Pop","Hip hop","Rock","Jazz Rap"])

        if st.button("Update Song"):
            edit_song(SongID,ArtistID,AlbumID,Streams,SongName,SongLength,Genre)
            st.success("Successfully updated values for song:: {} to ::{}".format(SongName, newSongName))

    result2 = view_songs()
    df2 = pd.DataFrame(result2, columns=['SongID','ArtistID','AlbumID','Streams','SongName','SongLength','Genre'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_user():
    result = view_users()
    df = pd.DataFrame(result,columns = ['UserID','Email','UserPassword','Dob','Gender','Subscription','DateSubscribed'])
    with st.expander("Current User accounts"):
        st.dataframe(df)

    #st.write(view_only_album())
    list_of_users = [i[0] for i in view_only_user()]

    selected_users = st.selectbox("User Accounts to edit",list_of_users)
    selected_result = get_users(selected_users)
    if selected_result:
        UserID = selected_result[0][0]
        Email = selected_result[0][1]
        UserPassword = selected_result[0][2]
        Dob = selected_result[0][3]
        Gender = selected_result[0][4]
        Subscription = selected_result[0][5]
        DateSubscribed = selected_result[0][6]

        col1,col2,col3 = st.columns(3)
        with col1:
            newUserID = st.text_input("User ID",UserID)
            newDob = st.date_input("Date of Birth", value=None, min_value=pd.to_datetime("1945-01-01"), max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

        with col2:
            newEmail = st.text_input("Email ID",Email)
            newGender = st.selectbox("Gender",["M","F"])

        with col3:
            newUserPassword = st.text_input("Password",UserPassword)
            newSubscription = st.selectbox("Subscription",["1","2"])
            newDateSubscribed = st.date_input("Date Subscribed", value=None, min_value=pd.to_datetime("1945-01-01"), max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, disabled=False, label_visibility="visible")

        if st.button("Update User Account"):
            edit_user(UserID,Email,UserPassword,Dob,Gender,Subscription,DateSubscribed)
            st.success("Successfully updated values for User:: {} to ::{}".format(UserID, newUserID))

    result2 = view_users()
    df2 = pd.DataFrame(result2, columns=['UserID','Email','UserPassword','Dob','Gender','Subscription','DateSubscribed'])
    with st.expander("Updated data"):
        st.dataframe(df2)

