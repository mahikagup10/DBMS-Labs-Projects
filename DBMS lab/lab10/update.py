import streamlit as st
import pandas as pd
from database import view_trains,view_only_train,get_trains,edit_train

def update_f():
    result = view_trains()
    df = pd.DataFrame(result,columns = ["Train No","Train Name","Train Type","Source","Destination","Availability"])
    with st.expander("Current Trains"):
        st.dataframe(df)

    #st.write(view_only_train())
    list_of_trains = [i[0] for i in view_only_train()]

    selected_trains = st.selectbox("Train to edit",list_of_trains)
    selected_result = get_trains(selected_trains)
    if selected_result:
        train_no = selected_result[0][0]
        train_name = selected_result[0][1]
        train_type = selected_result[0][2]
        source = selected_result[0][3]
        destination = selected_result[0][4]
        availability = selected_result[0][5]

        col1, col2, col3 = st.columns(3)
        with col1:
            new_train_no = st.text_input("Train No", train_no)
            new_train_name = st.text_input("Train Name", train_name)
        with col2:
            new_source = st.text_input("Source",source)
            new_destination = st.text_input("Destination", destination)
        with col3:
            new_train_type = st.selectbox("Train Type",["Mail","Fast","Superfast"])
            new_availability = st.selectbox("Availability",["Yes","No"])

        if st.button("Update Train"):
            edit_train(new_train_no, new_train_name, new_train_type, new_source, new_destination, new_availability, train_no, train_name, train_type, source, destination, availability)
            st.success("Successfully updated values for train:: {} to ::{}".format(train_name, new_train_name))

    result2 = view_trains()
    df2 = pd.DataFrame(result2, columns=['Train no','Train Name','Train Type', 'Source', 'Destination','Availability'])
    with st.expander("Updated data"):
        st.dataframe(df2)