import streamlit as st
from create import create_album,create_artist,create_song,create_user
from database import create_table_album,create_table_artist,create_table_song,create_table_user
from read import read_album,read_artist,read_song,read_user
from update import update_album,update_artist,update_song,update_user
from delete import delete_album,delete_artist,delete_song,delete_user
from query import command_window

def main():
    st.title("Music Streaming App")
    st.subheader("PES1UG20CS243")
    menu = ['Create', 'Read', 'Update', 'Delete','Query']
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Create":
        st.subheader("Add new entries:")
        menu1 = ['Album','Artist','Song','User']
        choice1 = st.selectbox("Tables",menu1)
        if choice1 == 'Album':
            create_table_album()
            st.subheader("Add Album")
            create_album()
        elif choice1 == 'Artist':
            create_table_artist
            st.subheader("Add new Artist")
            create_artist()
        elif choice1 == 'Song':
            create_table_song()
            st.subheader("Add new Song")
            create_song()
        elif choice1 == 'User':
            create_table_user()
            st.subheader("Add new User account")
            create_user()

    elif choice == "Read":
        st.subheader("View entries:")
        menu1 = ['Album','Artist','Song','User']
        choice1 = st.selectbox("Tables",menu1)
        if choice1 == 'Album':
            st.subheader("View Albums")
            read_album()
        elif choice1 == 'Artist':
            st.subheader("View Artists")
            read_artist()
        elif choice1 == 'Song':
            st.subheader("View Songs")
            read_song()
        elif choice1 == 'User':
            st.subheader("View User accounts")
            read_user()

    elif choice == "Update":
        st.subheader("Update entries:")
        menu1 = ['Album','Artist','Song','User']
        choice1 = st.selectbox("Tables",menu1)
        if choice1 == 'Album':
            st.subheader("Update Album")
            update_album()
        elif choice1 == 'Artist':
            st.subheader("Update Artist")
            update_artist()
        elif choice1 == 'Song':
            st.subheader("Update Song")
            update_song()
        elif choice1 == 'User':
            st.subheader("Update User account")
            update_user()

    elif choice == "Delete":
        st.subheader("Delete entries:")
        menu1 = ['Album','Artist','Song','User']
        choice1 = st.selectbox("Tables",menu1)
        if choice1 == 'Album':
            st.subheader("Delete Album")
            delete_album()
        elif choice1 == 'Artist':
            st.subheader("Delete Artist")
            delete_artist()
        elif choice1 == 'Song':
            st.subheader("Delete Song")
            delete_song()
        elif choice1 == 'User':
            st.subheader("Delete User account")
            delete_user()

    elif choice == "Query":
        st.subheader("Query")
        command_window()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()
