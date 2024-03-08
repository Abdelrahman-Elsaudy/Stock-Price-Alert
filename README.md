# Stock Price Alert

---

- This tool emails you when the change in the price of a stock you are interested in exceeds a magnitude you set, 
so you can make a decision of whether to buy or sell or do nothing.
- It also sends you the latest related news about it in the same email to get an idea of the cause of that change.

---
## Prerequisites:

---
1. Getting a free stock API key from [Alphavantage](https://www.alphavantage.co/documentation/).
2. Getting a free news API key from [NewsAPI](https://newsapi.org/).
3. Determining a specific stock, for this project I chose Tesla (TSLA).
4. Determining the magnitude of change in its price that will make this tool email you.

---
## Applied Skills:

---
**1. API Requests**

- Preparing API parameters according to [Alphavantage Documentation](https://www.alphavantage.co/documentation/) (the TIME_SERIES_DAILY section)
required to get the stock price data of the latest day of trading and the one before it to calculate
the difference between them.
- I use [Online JSON Viewer](https://jsonviewer.stack.hu/) to navigate through JSON data easier.
- Preparing API parameters according to [News API Documentation](https://newsapi.org/docs) to get the latest news about
the stock we are interested in.


**2. Emailing with SMTP Module**

- Setting a condition for the email to be sent, for example: when the price difference exceeds 5$.
```
price_difference = ((last_price - price_day_before)/price_day_before)*100
if abs(price_difference) > 5:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="Replace this with the receiving email",
                            msg=encoded_msg)
```

**3. Environment Variables**

- Saving email password as environment variable on Windows and retrieving it safely using os.
```
password = os.getenv("EMAIL_PASS")
```

---

## User Guide:

---

- You can follow any other stock by changing `STOCK` and `COMPANY_NAME` to the one you are interested in.
- You can automate this code to be run daily at a specific time by uploading it to a website like [Python Anywhere](https://www.pythonanywhere.com/)
, so you can follow the stock more efficiently. 
- To test the code I recommend changing the condition of sending email (the price difference) to be 0, so that any slight
change will be sent to you, then changing it back to whatever criteria you find suitable.

---
_Credits to: 100-Days of Code Course on Udemy._