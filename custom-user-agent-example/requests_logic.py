import cloudscraper

# Create a Cloudscraper instance
scraper = cloudscraper.create_scraper()

# Define custom headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept-Language': 'en-US,en;q=0.9',
}

# Define cookies
cookies = {
    'sessionid': '1234567890abcdef'
}

# Make a request with custom headers and cookies
response_headers = scraper.get('https://httpbin.org/headers', headers=headers, cookies=cookies)
response_cookies = scraper.get('https://httpbin.org/cookies', headers=headers, cookies=cookies)

# Print the headers received by the server
print("Headers perceived by the server:")
print(response_headers.json())

# Print the cookies received by the server
print("\nCookies perceived by the server:")
print(response_cookies.json())
