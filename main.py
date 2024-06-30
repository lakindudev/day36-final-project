import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
new_api_key = "734f34f22a484b7c9ec8e9e54e84b482"

account_sid = "account sid"
auth_token = "auth token"

stock_price_api = "DCV6VN4LFOLJT046"
stock_price_url = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_price_api,
}

price_response = requests.get(url=stock_price_url, params=stock_params)
price_response.raise_for_status()
price_data = price_response.json()["Time Series (Daily)"]
price_data_list = [value for (key, value) in price_data.items()]
yesterday_data = price_data_list[0]
yesterday_closing_data = yesterday_data["4. close"]


day_before_yesterday_data = price_data_list[1]
day_before_yesterday_closing_data = day_before_yesterday_data["4. close"]

price_difference = abs(float(yesterday_closing_data) - float(day_before_yesterday_closing_data))
price_percentage = (price_difference/float(yesterday_closing_data)) * 100
print(price_percentage)

if price_percentage > 0.1:
    print("Get News")

    new_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": new_api_key,
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=new_params)
    news_data = news_response.json()
    print(news_data)
    article_data = news_data["articles"]
    print(article_data)

    three_articles = article_data[:3]
    print(three_articles)

    article_list = [{"title": article["title"], "description": article["description"]} for article in three_articles]
    print(article_list)

    client = Client(account_sid, auth_token)
    for article in article_list:
        message = client.messages \
            .create(
            body=article,
            from_="+19789517779",
            to="+94721763352"
        )
        print(message.status)


