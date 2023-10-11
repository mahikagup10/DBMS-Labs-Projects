import pandas as pd
import streamlit as st
from database import view_trains,view_only_train,delete_data

def delete_f():
    result = view_trains()
    df = pd.DataFrame(result, columns=['Train no','Train Name','Train Type', 'Source', 'Destination','Availability'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_trains = [i[0] for i in view_only_train()]
    selected_train = st.selectbox("Task to Delete", list_of_trains)
    st.warning("Do you want to delete ::{}".format(selected_train))
    if st.button("Delete Train"):
        delete_data(selected_train)
        st.success("Train has been deleted successfully")
    new_result = view_trains()
    df2 = pd.DataFrame(new_result, columns=['Train no','Train Name','Train Type', 'Source', 'Destination','Availability'])
    with st.expander("Updated data"):
        st.dataframe(df2)