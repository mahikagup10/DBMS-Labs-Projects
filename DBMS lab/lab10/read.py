import streamlit as st
import pandas as pd
import plotly.express as px
from database import view_trains

def read_f():
    result = view_trains()
    df = pd.DataFrame(result,columns = ["Train No","Train Name","Train Type","Source","Destination","Availability"])

    with st.expander("View all Trains"):
        st.dataframe(df)