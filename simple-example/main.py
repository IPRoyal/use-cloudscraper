import cloudscraper

# Create a Cloudscraper instance
scraper = cloudscraper.create_scraper()

# Perform a GET request to a Cloudflare-protected website
response = scraper.get('https://iproyal.com')

# Print the website's content
print(response.text)
