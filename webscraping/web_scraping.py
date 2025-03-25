import requests
from bs4 import BeautifulSoup

url = "https://finance.yahoo.com/quote/AMZN/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# پیدا کردن قیمت سهام
price_tag = soup.find("fin-streamer", {"data-field": "regularMarketPrice"})
if price_tag:
    price = price_tag.text
    print(f"قیمت فعلی سهام آمازون: {price}")
else:
    print("قیمت سهام پیدا نشد!")
