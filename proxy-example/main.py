import cloudscraper

# Create a Cloudscraper instance with a proxy
scraper = cloudscraper.create_scraper()

# Proxy dictionary
proxies = {
    'http': 'http://proxy_user:proxy_pass@proxy_host:proxy_port',
    'https': 'http://proxy_user:proxy_pass@proxy_host:proxy_port'
}

# Send a request through the proxy
response = scraper.get('https://iproyal.com', proxies=proxies)

# Print the content of the response
print(response.text)
