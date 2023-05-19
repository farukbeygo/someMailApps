STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


## STEP 1
import requests
from datetime import date, timedelta
import os
from twilio.rest import Client

url_stock_exh = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
exh = requests.get(url_stock_exh)
data_se = exh.json()

url_news = ('https://newsapi.org/v2/everything?'
            'q=IBM+'
            'from=2023-05-18&'
            'sortBy=popularity&'
            'apiKey=c865898c64e04db9bf6547eb478c6549')
nw = requests.get(url_news)
data_news = nw.json()

data_date = "2023-04-20"  # date.today() - timedelta(days=1)

open_level = float(data_se["Time Series (Daily)"][f'{data_date}']["1. open"])
close_level = float(data_se["Time Series (Daily)"][f'{data_date}']["4. close"])

daily_change = close_level - open_level
daily_change_per = (daily_change/close_level) * 100


if abs(daily_change_per) >= 0.5:
    if daily_change > 0:
        print(f"IBM:🔺{daily_change_per:.2}%")
    else:
        print(f"IBM:🔻{daily_change_per:.2}%")

    os.environ['your_account_sid_value'] = 'your_account_sid_value'
    os.environ['your_auth_token_value'] = 'your_auth_token_value'

    account_sid = os.environ['your_account_sid_value']
    auth_token = os.environ['your_auth_token_value']

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=data_news['articles'][0]['title'],
        from_='+15855231918',
        to='+905530131464'
    )

    print(message.sid)


