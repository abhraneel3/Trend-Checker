import json
import requests
from telegram import Bot
from datetime import datetime

# Function to format the approx_traffic value
def format_traffic(traffic):
    if traffic.endswith('+'):
        traffic = traffic[:-1]  # Remove the '+' sign
    if traffic.endswith('M'):
        return traffic.replace('M', 'M+')
    elif traffic.endswith('K'):
        return traffic.replace('K', 'K+')
    return traffic

# Function to parse and format the date
def parse_and_format_date(date_str):
    date_obj = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %z')
    return date_obj.strftime('%Y-%m-%d')

# Fetch data from the JSON URL
response = requests.get('https://raw.githubusercontent.com/abhraneel3/Trend-Checker/main/trend.json')
data = response.json()

# Initialize Telegram bot
bot = Bot(token='7187447274:AAEuQ7e-It7e8YFzAOFu2D17o7p3iIdaLWc')

# Define an asynchronous function to send messages
async def send_messages():
    # Iterate over each item in the data
    for item in data:
        # Format the approx_traffic value
        item['approx_traffic'] = format_traffic(item['approx_traffic'])

        # Parse and format the date
        item['pubDate'] = parse_and_format_date(item['pubDate'])

        # Define the message
        caption = f"""
🌍 Trending News From: {item['country']}\n
📰 {item['title']}\n\n
📝 {item['news_item_snippet']}\n
🔗 Read here: {item['news_item_url']}\n
📷 Source: {item['picture_source']}
🚀 Today's Traffic: {item['approx_traffic']}\n\n
#️⃣ #trendingnews #news #trending #latestnews #todaynews #telegramnews #latesttrendingnews
"""

        # Send the message to Telegram channel with photo
        await bot.send_photo(chat_id='@today_trending_news', photo=item['picture'], caption=caption, parse_mode='Markdown')

# Run the asynchronous function
import asyncio
asyncio.run(send_messages())
