import streamlit as st
from database import add_data

def create_f():
    col1,col2,col3 = st.columns(3)
    with col1:
        train_no = st.text_input("Train Number")
        train_name = st.text_input("Train Name")

    with col2:
        source = st.text_input("Source")
        destination = st.text_input("Destination")
    
    with col3:
        train_type = st.selectbox("Train Type",["Mail","Fast","Superfast"])
        availabilty = st.selectbox("Availabilty: ",["Yes","No"])

    if st.button("Add Train"):
        add_data(train_no,train_name,train_type,source,destination,availabilty)
        st.success("Added Train to Train Table:{}".format(train_name))
