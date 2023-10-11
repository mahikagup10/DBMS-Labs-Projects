import pandas as pd
import streamlit as st
from database import execute_query

#Command bar-------------------------------------------------------------------
def command_window():
    #st.text("Enter MySQL Command")
    q = st.text_area("Command")
    if st.button("Run"):
        if 'select' in str(q).lower():
            res,desc=execute_query(q)
            st.success("Success")
            st.table(pd.DataFrame(res, columns=[col[0] for col in desc]))
        else:
            execute_query(q)
            st.success("Success")