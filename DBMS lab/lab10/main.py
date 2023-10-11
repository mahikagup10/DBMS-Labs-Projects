import streamlit as st
from create import create_f
from database import create_table
from read import read_f
from update import update_f
from delete import delete_f
from query import command_window

def main():
    st.title("Railways APP")
    st.subheader("PES1UG20CS243")
    menu = ['Create', 'Read', 'Update', 'Delete','Query']
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()
    if choice == "Create":
        st.subheader("Add Train")
        create_f()

    elif choice == "Read":
        st.subheader("View Train")
        read_f()

    elif choice == "Update":
        st.subheader("Edit Train")
        update_f()

    elif choice == "Delete":
        st.subheader("Remove Train")
        delete_f()

    elif choice == "Query":
        st.subheader("Query")
        command_window()

    else:
        st.subheader("About tasks")


if __name__ == '__main__':
    main()
