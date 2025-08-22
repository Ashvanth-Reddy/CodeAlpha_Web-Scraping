from bs4 import BeautifulSoup

def extract_titles(html):
    soup = BeautifulSoup(html, "html.parser")
    titles = [title.get_text(strip=True) for title in soup.find_all("title")]
    return titles
