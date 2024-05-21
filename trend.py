import feedparser
import json

# List of countries and their corresponding geo codes
countries = {
    'United States': 'US',
    'India': 'IN',
    'Argentina': 'AR',
    'Australia': 'AU',
    'Brazil': 'BR',
    'Canada': 'CA',
    'France': 'FR',
    'Germany': 'DE',
    'Italy': 'IT',
    'Mexico': 'MX',
    'Spain': 'ES',
    'United Kingdom': 'GB',
    # Add more countries as needed
}

# Create a list to store items from all countries
all_items = []

# Iterate through each country
for country, geo_code in countries.items():
    # URL of the RSS feed for the country
    url = f'https://trends.google.co.in/trends/trendingsearches/daily/rss?geo={geo_code}'
    
    # Parse the RSS feed
    feed = feedparser.parse(url)

    # Create a list to store items for the current country
    country_items = []

    # Iterate through entries in the feed for the current country
    for entry in feed.entries:
        # Check if 'ht:approx_traffic' is above 100,000
        if int(entry.ht_approx_traffic.replace(',', '').replace('+', '')) > 100000:
            item = {}
            item['country'] = country
            item['title'] = entry.title
            item['pubDate'] = entry.published
            item['picture'] = entry.ht_picture
            item['news_item_snippet'] = entry.ht_news_item_snippet
            item['news_item_url'] = entry.ht_news_item_url
            item['picture_source'] = entry.ht_picture_source
            item['approx_traffic'] = entry.ht_approx_traffic

            country_items.append(item)

    # Add items for the current country to the list of all items
    all_items.extend(country_items)

# Convert to JSON format
output_json = json.dumps(all_items, indent=2)

# Save the JSON output to a file
with open('trend.json', 'w') as json_file:
    json_file.write(output_json)

print("JSON data for all countries has been saved to trend.json file.")
