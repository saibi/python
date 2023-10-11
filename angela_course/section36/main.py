import requests
import os
from sample_data import stock_sample, news_sample

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_key = os.environ.get("STOCK_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")
if stock_api_key is None or news_api_key is None:
    print("You need to set your api key in your environment variable.")


# STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

# url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&outputsize=compact&apikey={stock_api_key}"
# r = requests.get(url)
# r.raise_for_status()
# data = r.json()["Time Series (Daily)"]

# use preloaded data
data = stock_sample["Time Series (Daily)"]

# or value_list = [value for (key, value) in data.items()]
# yesterday_value = value_list[0]

date_list = list(data.keys())
yesterday = date_list[0]
the_day_before_yesterday = date_list[1]
stock_price_yesterday = float(data[yesterday]["4. close"])
stock_price_before = float(data[the_day_before_yesterday]["4. close"])

print(f"yesterday {yesterday} {stock_price_yesterday}")
print(
    f"the day before yesterday {the_day_before_yesterday} {stock_price_before}")

# TODO 2. - Get the day before yesterday's closing stock price

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

diff = abs(stock_price_yesterday - stock_price_before)
print(diff)

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentage = round((diff/stock_price_yesterday)*100, 2)
print(percentage)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if percentage > 1:
    print("Get News")

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# news_url = f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&from=2023-09-10&sortBy=publishedAt&apiKey={news_api_key}"
# news_response = requests.get(news_url)
# news_response.raise_for_status()
# print(news_response.json())

# use preloaded data
first_three_articles = news_sample["articles"][:3]

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# to send a separate message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
#
# [ new_item for item in list ]
#

email_contents = [
    f"Subject: {STOCK_NAME} {percentage}\n\nHeadline: {article['title']}\n\nBrief: {article['description']}" for article in first_three_articles]
print(email_contents)

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
