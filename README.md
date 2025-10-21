# How to Use Cloudscraper in Python: 2025 Guide

Cloudflare protects many sites from attacks, but often blocks web scraping, hindering large-scale data collection. 
The Cloudscraper Python library was created to handle Cloudflare’s anti-bot measures and enable scraping of protected sites.

## What is Cloudscraper?

Cloudscraper is a Python library that supports web scraping projects by providing easy-to-use ways to [bypass Cloudflare protection](https://iproyal.com/blog/cloudflare-bypass/). 

Cloudscraper uses various features to detect the different challenges that the service can throw to users. It then uses automation to attempt to solve them or, if a CAPTCHA is provided, forward that to a CAPTCHA-solving service.

## How Does Cloudscraper Work? 

Cloudscraper bypasses Cloudflare using three main tactics: 
* JavaScript handling & challenge solving. Renders and solves JS challenges; engine is customizable.
* Spoofing user agents & browser headers. Replaces Request default User Agent and uses optimized browser headers (customizable, e.g., mobile Chrome).
* Limited browser fingerprint evasion. Can bypass basic checks but often fails against advanced fingerprinting (plugins, fonts, environment).

## Setup

Make sure [python3](https://www.python.org/downloads/) is installed on your system.

Then, install cloudscraper using `pip` package manager. 

```
pip install cloudscraper
```

ℹ️ To avoid installing the library system-wide (and avoid the need for root privileges) you can use [python virtual environments](https://docs.python.org/3/library/venv.html)

Let’s send a simple GET HTTP request to the IPRoyal website using Cloudscraper:


```python
import cloudscraper

# Create a Cloudscraper instance
scraper = cloudscraper.create_scraper()

# Perform a GET request to a Cloudflare-protected website
response = scraper.get('https://iproyal.com')

# Print the website's content
print(response.text)
```

A working example can be found [here](simple-example/main.py).

There’s one degree of separation when using Cloudscraper – you first need to create a scraper instance. Even that isn’t anything special as the Cloudscraper instance is simply a Requests session.

After that, we use Cloudscraper exactly how we use Requests. In fact, if you have an existing project that uses the latter library, updating it to match Cloudscraper requirements can be done in mere minutes.

## Setting Up Proxies in Cloudscraper

To use proxies with Cloudscraper, we’ll need to create a dictionary with the value key pair being the protocol and the proxy server and port

```python
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
```

A working example can be found [here](proxy-example/main.py).

## Handling CAPTCHAs Through Third Parties

While Cloudscraper will attempt to solve some CAPTCHAs on its own, you shouldn’t expect it to do all the legwork. CAPTCHAs evolve quickly and Cloudscraper is managed by a single developer – he won’t be able to keep up with all the changes, so Cloudscraper will likely fail often.

So, using third-party CAPTCHA-solving services is likely to come into play. Cloudscraper has even implemented such usage and even supports some services by default

According to the documentation, Cloudscraper supports these CAPTCHA services by default:
* 2captcha
* anticaptcha
* CapSolver
* CapMonster Cloud
* deathbycaptcha
* 9kw
* return_response

```python
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
```

A working example can be found [here](captcha-example/main.py).

## Customizing Headers and Cookies With Cloudscraper

Finally, as mentioned previously, you can customize the header and cookie logic if required. There are two ways to do so.

### First way: change the Cloudscraper default user agent logic (recommended)

Cloudscraper uses a randomization system to pick out user agents according to your settings (or their default ones).

```python
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
```

A working example can be found [here](custom-user-agent-example/internal_logic.py).

### Second way: force headers just like through Requests (not recommended)
You can force headers through `Requests`.
It’s not recommended to do that as Cloudscraper has already optimized features for headers.

```python
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
```

A working example can be found [here](custom-user-agent-example/requests_logic.py).

## Conclusion

Cloudscraper is a powerful library that’ll greatly reduce block rates from Cloudflare-protected websites. It won’t, however, be the panacea, and some of the websites will still be impassable. 

For that, you may need to use other methods or libraries:

* Selenium: A classic browser automation library that has a lot of plugins and add-ons that improve evasion techniques, including those of Cloudflare.
* Requests-HTML: An alternative library that does not bypass Cloudflare by default but does render JavaScript, so it could be useful in some applications.
* Playwright: A modern browser automation library that has a lot of customization and evasion capabilities.
* [Flaresolverr](https://iproyal.com/blog/flaresolverr-python-guide/): Another library that’s optimized to solve Cloudflare challenges, but a bit harder to set up than Cloudscraper.

Each of the alternatives can be useful in certain scenarios, although browser automation libraries will be somewhat slower than direct HTTP request libraries. On the other hand, they will be less detectable. So, it’s all about making the correct trade-offs.
