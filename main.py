import requests
from bs4 import BeautifulSoup
import pandas as pd

# Target URL
URL = "https://en.wikipedia.org/wiki/Main_Page"

# Send HTTP GET request
response = requests.get(URL)
if response.status_code != 200:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
    exit()

# Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract featured article section
featured = soup.find("div", id="mp-tfa")  # Today's featured article

# Extract text and links
title = featured.find("b").text if featured else "N/A"
links = featured.find_all("a") if featured else []

# Store data
data = []
for link in links:
    href = link.get("href")
    text = link.text.strip()
    if href and href.startswith("/wiki/"):
        data.append({
            "Title": title,
            "Link Text": text,
            "URL": f"https://en.wikipedia.org{href}"
        })

# Convert to DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv("wikipedia_scrape.csv", index=False)
print("Scraping complete. Data saved to wikipedia_scrape.csv.")
