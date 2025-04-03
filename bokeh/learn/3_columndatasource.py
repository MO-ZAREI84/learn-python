from bokeh.plotting import figure, output_file , show, ColumnDataSource
import pandas as pd

df = pd.read_csv("all_stocks_5yr.csv")

#filter stock data for a specific symbol
df_apple = df[ df["Name"]=='AAL' ]

df_apple['Date'] = pd.to_datetime(df_apple['Date'])

#ColumnDataSource object
data = ColumnDataSource(df_apple)

plot = figure(x_axis_type="datetime")
plot.line(x='Date', y='Close', source=data)
plot.circle(x='Date', y='Close', source=data)

output_file("3_cds.html")

show(plot)