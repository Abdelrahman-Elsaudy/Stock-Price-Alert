import requests
import smtplib
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

with open("api_keys.txt") as file:
    contents = file.readlines()
    STOCK_API = contents[0]        # Replace this with your stock API.
    NEWS_API = contents[1]         # Replace this with your news API.

STOCK_PAGE = "https://www.alphavantage.co/query"


# --------------------------- STEP 1: STOCK DATA FILTERING --------------------------- #


stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API
}

stock_response = requests.get(url=STOCK_PAGE, params=stock_parameters)
stock_response.raise_for_status()
full_stock_data = stock_response.json()
required_data = full_stock_data["Time Series (Daily)"]

trading_days = [date for date in required_data]
last_price = float(required_data[trading_days[0]]["4. close"])
price_day_before = float(required_data[trading_days[1]]["4. close"])
price_difference = ((last_price - price_day_before)/price_day_before)*100


# --------------------------- STEP 2: GETTING RELATED NEWS --------------------------- #


NEWS_PAGE = "https://newsapi.org/v2/everything"
LANGUAGE = "en"
ARTICLES_NUMBER = 3

news_params = {
    "qInTitle": COMPANY_NAME,
    "language": LANGUAGE,
    "apiKey": NEWS_API,
    "pageSize": ARTICLES_NUMBER,
}

news_response = requests.get(url=NEWS_PAGE, params=news_params)
news_response.raise_for_status()
news_data = news_response.json()

news_title = news_data["articles"][0]["title"]
news_desc = news_data["articles"][0]["description"]


# --------------------------- STEP 3: SENDING E-MAIL --------------------------- #


my_email = "abdelrahman.elsaudyyy@gmail.com"   # Replace this with your email.
password = os.getenv("EMAIL_PASS")   # Replace this with your password.

arrow = None
if price_difference > 0:
    arrow = "🔺"
else:
    arrow = "🔻"

full_msg = f"Subject:{STOCK}{arrow}:{str(abs(round(price_difference, 2)))}\n\nBrief: {news_title}\n{news_desc}"
encoded_msg = full_msg.encode("utf-8")

if abs(price_difference) > 5:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="abdelrahman.elsaudy@gmail.com",   # Replace this with your receiving email.
                            msg=encoded_msg)
