import cloudscraper

# Create a Cloudscraper instance with a captcha service configured
scraper = cloudscraper.create_scraper(
    captcha={
        'provider': 'provider_name',
        'api_key': 'your_provider_api_key'
    }
)

# Perform a GET request to a Cloudflare-protected website
response = scraper.get('https://iproyal.com')

# Print the website's content
print(response.text)
