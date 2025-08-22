# fetcher.py

import requests

def fetch_html(url):
    """
    Fetches raw HTML content from a specified URL.
    """
    headers = {
        "User-Agent": "Mozilla/5.0"  # Mimic browser to avoid bot detection
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise error if bad response
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None
