import streamlit as sl 
import pandas as pd


head = sl.beta_container()
d_set = sl.beta_container()
feature = sl.beta_container()
m_training = sl.beta_container()

with head:
	sl.title("data science")
	sl.text("my first project on india stock exchange NSE index ")



with d_set:
	sl.header('NSE dataset ')
	sl.text('This is the dataset i download it from NSE.com')
	nsdata = pd.read_csv("streamlit/mydata/nsedata.csv")
	sl.write(nsdata.head())

with feature:
	sl.header('Adding feature')
	sl.text("We are gonna modify it!")




with m_training:
	sl.header("Training the data")
	sl.text("We train our data")

