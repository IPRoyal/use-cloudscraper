
import cloudscraper

# Mobile Chrome User-Agents on Android
scraper_android_chrome = cloudscraper.create_scraper(
    browser={
        'browser': 'chrome',  # Specify the browser as Chrome
        'platform': 'android',  # Specify the platform as Android
        'desktop': False  # Set desktop to False to target mobile User-Agents
    }
)

# Check the User-Agent perceived by the website
response_android_chrome = scraper_android_chrome.get('https://httpbin.org/user-agent')
print("Android Chrome User-Agent:", response_android_chrome.json()['user-agent'])


# Desktop Firefox User-Agents on Windows
scraper_windows_firefox = cloudscraper.create_scraper(
    browser={
        'browser': 'firefox',  # Specify the browser as Firefox
        'platform': 'windows',  # Specify the platform as Windows
        'mobile': False  # Set mobile to False to target desktop User-Agents
    }
)

# Check the User-Agent perceived by the website
response_windows_firefox = scraper_windows_firefox.get('https://httpbin.org/user-agent')
print("Windows Firefox User-Agent:", response_windows_firefox.json()['user-agent'])


# Custom User-Agent
scraper_custom = cloudscraper.create_scraper(
    browser={
        'custom': 'ScraperBot/1.0',  # Define a custom User-Agent string
    }
)

# Check the User-Agent perceived by the website
response_custom = scraper_custom.get('https://httpbin.org/user-agent')
print("Custom User-Agent:", response_custom.json()['user-agent'])
