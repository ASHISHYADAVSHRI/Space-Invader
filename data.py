import streamlit as sl 
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error , r2_score

sl.markdown(
	"""
	<style>
	.main {
	background-color: #0775ff;
	}
	</style>
	""",
	unsafe_allow_html=True
)
@sl.cache
def get_data(filename):
	data = pd.read_csv(filename)


	return data

head = sl.beta_container()
d_set = sl.beta_container()
feature = sl.beta_container()
m_training = sl.beta_container()


with head:
	sl.title("data science")
	sl.text("my first project on india\'s stock market.... ")


with d_set:
	sl.header('NSE dataset ')
	sl.text('This is the dataset i download it from NSE.com')
 
	data = get_data("E:/streamlit/nsedata.csv")
	sl.write(data)	
	open_data = pd.DataFrame(data["Open"].value_counts()).head(50)
	sl.bar_chart(open_data)


	
with feature:
	sl.header('Adding feature')

	sl.markdown("* **First feature: ** we can visualize the data......")
	sl.markdown("* **Second feature: ** we can choose the row columns......")
	sl.text("We are gonna modify it!")





with m_training:
	sl.header("Training the data")
	sl.text("We train our data")
	dis_col, sal_col = sl.beta_columns(2)


	max_depth = dis_col.slider("What should be the depth of the model?",min_value=10, max_value=100, value=20, step=10)
	n_estimators = dis_col.selectbox("How many trees should there be?", options=[100, 200, 300, 400, "limitless"], index=0)
	sl.write("Here is name of the feature of my data!")
	sl.table(data.columns)

	input_feature = dis_col.text_input("What feature we need to use as input?", "Open")
	if n_estimators == "limitless":
		reg = RandomForestRegressor(max_depth=max_depth)
	else:
		reg = RandomForestRegressor(max_depth=max_depth, n_estimators=n_estimators)
	x = data[[input_feature]]
	y = data[['Open']]

	reg.fit(x,y)
	prediction = reg.predict(y)

	sal_col.subheader("Mean absolute error of the model is:")
	sal_col.write(mean_absolute_error(y, prediction))

	sal_col.subheader("Mean squared error of the model is:")
	sal_col.write(mean_squared_error(y, prediction))

	sal_col.subheader("r2 score of the model:")
	sal_col.write(r2_score(y, prediction))
