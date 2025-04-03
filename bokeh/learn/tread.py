from bokeh.plotting import show,output_file,figure
import pandas as pd

df = pd.read_csv("all_stocks_5yr.csv")

df_apple = df[ df["Name"] == 'AAL' ]

df_apple['Date'] = pd.to_datetime(df_apple['Date'])
p = figure(x_axis_type="datetime")
p.line(x=df_apple['Date'], y=df_apple['Close'])

output_file("pandas.html")

show(p)