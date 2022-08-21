import pandas as pd
import plotly.express as px

df = pd.read_csv("covid-19_data.csv")

fig = px.scatter(df, x = 'Date', y = 'Cases', color = 'Country', title = 'Covid-19 Data')
fig.show()