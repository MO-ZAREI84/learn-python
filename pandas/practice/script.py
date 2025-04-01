import folium
import pandas as pd
import json

df = pd.read_csv("waterfalls.txt")  # خواندن فایل آبشارها

# ایجاد نقشه با مرکز ایران
m = folium.Map(location=[32.4279, 53.6880], zoom_start=4)

#  **لایه‌ی مرز کشورها (GeoJson)**
with open("world.json", "r", encoding="utf-8") as f:
    world_geojson = json.load(f)

geojson_layer = folium.GeoJson(
    world_geojson,
    name="مرز کشورها",  # نام لایه برای کنترل
    style_function=lambda x: {"fillColor": "gray", "color": "black", "weight": 20, "fillOpacity": 0.2}
).add_to(m)

#  **لایه‌ی مارکرهای آبشارها**
waterfall_layer = folium.FeatureGroup(name=" آبشارها")

for index, row in df.iterrows():
    try:
        height = float(row["HEIGHT"])  # تبدیل ارتفاع به عدد اعشاری
    except ValueError:
        height = 100  # مقدار پیش‌فرض در صورت خطا (مثلاً 'بالای 100')


    if height > 50:
        color = "red"  
    elif height > 20:
        color = "blue"  
    else:
        color = "green"  
    folium.Marker(
        location=[float(row["LATITUDE"]), float(row["LONGITUDE"])],
        popup=f"{row['NAME']} - {row['STATE']}  (ارتفاع: {row['HEIGHT']} متر)",
        tooltip=row["NAME"],
        icon=folium.Icon(color=color)
    ).add_to(waterfall_layer)

# اضافه کردن لایه‌ی آبشارها به نقشه
waterfall_layer.add_to(m)

# **افزودن کنترل لایه‌ها**
folium.LayerControl().add_to(m)

# ذخیره نقشه به عنوان HTML
m.save("waterfalls_map.html")
