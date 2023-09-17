import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
df = pd.read_csv("./Fish.csv")
data = df["Species"].value_counts()
plt_data = data.plot(kind="bar")
plt_data.set_title("Fish count by species")
plt_data.set_xlabel("Species name")
plt_data.set_ylabel("Count")
plt_data.set_xticklabels(plt_data.get_xticklabels(), rotation=45, horizontalalignment='right')
st.pyplot(plt_data.figure)