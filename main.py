import requests
import twilio
import datetime

newapi_key = "4bd45be643a140d78aa5f7d93f265cec"

today_date = datetime.date.today()
yesterday_date = today_date - datetime.timedelta(days=1)



STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


aplhavantage = "https://www.alphavantage.co/query"
aplhavantage_apikey = "O7UXRWFGKKMIUAME"
aplhavantage_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "1min",
    "apikey": aplhavantage_apikey,
}

newapi_parameters = {
    "q": COMPANY_NAME,
    "apikey": newapi_key,
    "pageSize": "5",
}

newapi_response = requests.get(url="https://newsapi.org/v2/everything", params=newapi_parameters)
newapi_response.raise_for_status()

news_data = newapi_response.json()


