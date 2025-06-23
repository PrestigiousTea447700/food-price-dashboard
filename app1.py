# %%
# Import necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# %%
df = pd.read_csv('D:\\datasets\\food_price_indices_data_jun25_modified.csv')

# %%
# sidebar filer-options
st.sidebar.header('Filter Options')
st.set_page_config(page_title='Food Price Indices', layout='wide')
st.title('Food Price Indices')
st.markdown("Visualize trends in global food prices from the FAO database.")


# %%
# Sidebar filters
available_indices = df.columns.tolist()
Selected_index = st.sidebar.selectbox("Select a food category",available_indices)



# %%
# Date filter
start_date = st.sidebar.date_input("Start Date", pd.to_datetime(df['Date'].min()))
end_date = st.sidebar.date_input("End Date", pd.to_datetime(df['Date'].max()))

# Ensure 'Date' column is datetime
df['Date'] = pd.to_datetime(df['Date'])

# Filter the DataFrame using a boolean mask
filtered_df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]

# %%
# Line chart
st.subheader(f"{Selected_index} Price Index Over Time")
fig = px.line(
    filtered_df,
    x=filtered_df['Date'],
    y=Selected_index,
    title=f"{Selected_index} Index from {start_date} to {end_date}",
    labels={"x": "Date", Selected_index: "Index Value"}
)
st.plotly_chart(fig, use_container_width=True)


# %%
# Summary statistics
st.subheader("Summary Statistics")
column1, column2, column3, column4 = st.columns(4)

if pd.api.types.is_numeric_dtype(filtered_df[Selected_index]):
	avg = filtered_df[Selected_index].mean()
	max_val = filtered_df[Selected_index].max()
	min_val = filtered_df[Selected_index].min()
	std_val = filtered_df[Selected_index].std()
else:
	# For non-numeric columns (like 'Date'), convert to string for display
	avg = str(filtered_df[Selected_index].mean())
	max_val = str(filtered_df[Selected_index].max())
	min_val = str(filtered_df[Selected_index].min())
	std_val = "N/A"

column1.metric("Average", avg)
column2.metric("Maximum", max_val)
column3.metric("Minimum", min_val)
column4.metric("Standard Deviation", std_val)


# %%

st.markdown("---")
st.markdown("Data Source: FAO Food Price Index Database")
st.markdown("Created by: Your Name")
# Run the app with: streamlit run app.py
# To run the app, save this code in a file named `app.py` and execute the command:
# streamlit run app.py in your terminal.
# Note: Make sure to have the required libraries installed in your Python environment.
# This code creates a Streamlit app that visualizes food price indices over time.
# The app allows users to filter by date and food category, and displays a line chart along with summary statistics

# %%



