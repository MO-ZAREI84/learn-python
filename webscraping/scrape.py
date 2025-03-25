import requests
from bs4 import BeautifulSoup
import time
import csv
import send_mail

csv_file = open("scrape.csv", "w", newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Stock Title", "Current Price", "Pre. Settlement", "Settlement Date", "Open", "Bid", "Last Day", "Day's range", "Volume", "Ask"])

urls = ["https://finance.yahoo.com/quote/GC=F?p=GC=F", "https://finance.yahoo.com/quote/CL=F?p=CL=F"]

for url in urls:
    stock = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
    html_page = requests.get(url, headers=headers )
    #print(html_page.content)
    soup = BeautifulSoup(html_page.content, "lxml")
    #print(soup.title.text)

    header_info = soup.find("div", id="quote-header-info")
    #print(header_info)
    stock_title = header_info.find("h1", class_="D(ib) Fz(18px)").text
    current_price = header_info.find("div", class_="My(6px) Pos(r) smartphone_Mt(6px)").find("span").text

    stock.append(stock_title)
    stock.append(current_price)

    table_rows = soup.find("div" , id="quote-summary").find_all("tr")
    #print(len(table_rows))


    for i in range(0 , len(table_rows)):
        value = table_rows[i].find_all("td")[1].text
        stock.append(value)
    csv_writer.writerow(stock)
    time.sleep(5)

csv_file.close()

send_mail.send()




