from bokeh.plotting import figure, output_file, show
import yfinance as yf
import datetime
import numpy as np

# تعیین تاریخ شروع و پایان
start_date = datetime.datetime(2021, 1, 1)
end_date = datetime.datetime(2021, 1, 31)

#  دریافت داده‌های سهام از Yahoo Finance
df = yf.download("AAPL", start=start_date, end=end_date)

# اگر داده دریافت نشد، خروجی بده و کد رو متوقف کن
if df.empty:
    print("داده‌ای دریافت نشد! تاریخ یا نماد را بررسی کن.")
    exit()

#  تعیین وضعیت (Increase / Decrease / Equal)
df["Status"] = np.where(df["Close"] > df["Open"], "Increase", 
                        np.where(df["Close"] < df["Open"], "Decrease", "Equal"))

df["Middle"] = (df.Open + df.Close) / 2
df["Height"] = abs(df.Open - df.Close)

# ایجاد چارت کندل‌استیک
plot = figure(x_axis_type="datetime", width=800, height=400, title="Candlestick Chart")

# 🔹 اضافه کردن خطوط بالا و پایین کندل‌ها
plot.segment(df.index, df.High, df.index, df.Low, color="black")

# کندل‌های سبز (افزایش قیمت)
plot.rect(df.index[df["Status"] == "Increase"], df.Middle[df["Status"] == "Increase"], 
          12 * 60 * 60 * 1000, df.Height[df["Status"] == "Increase"], fill_color="green", line_color="black")

# کندل‌های قرمز (کاهش قیمت)
plot.rect(df.index[df["Status"] == "Decrease"], df.Middle[df["Status"] == "Decrease"], 
          12 * 60 * 60 * 1000, df.Height[df["Status"] == "Decrease"], fill_color="red", line_color="black")

# خروجی فایل HTML و نمایش
output_file("candle.html")
show(plot)
