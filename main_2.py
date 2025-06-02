import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
aplhavantage_apikey = "O7UXRWFGKKMIUAME"

twilio_account_sid = "AC0d94fcf7b076c9a7e250b41dda70c5d9"
twilio_auth_key = "1977ca20c2ef9d1ec2af4fae1aa5b9ad"

newapi_key = "4bd45be643a140d78aa5f7d93f265cec"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "interval": "1min",
    "apikey": aplhavantage_apikey,
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday = data_list[0]
yesterday_closing_price = yesterday["4. close"]


day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]


difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))


diff_percentage = difference / float(yesterday_closing_price) * 100


if diff_percentage > 5:
    newapi_parameters = {
        "apikey": newapi_key,
        "qInTitle": COMPANY_NAME,
        "pageSize": "5",
    }

    news_response = requests.get(NEWS_ENDPOINT, params=newapi_parameters)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]



    formatted_articles_list = [f"Headline: {article['title']}. \n Brief: {article['description']} " for article in three_articles]

#TODO 9. - Send each article as a separate message via Twilio.

    client = Client(twilio_account_sid, twilio_auth_key)

    for article in formatted_articles_list:
        message = client.messages .create(
            body=article,
            from_="whatsapp:+14155238886",
            to="whatsapp:+918422031338",
        )

