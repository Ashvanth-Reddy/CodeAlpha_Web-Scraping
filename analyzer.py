# analyzer.py (update)

import csv
from collections import Counter
import re

def clean_text(text):
    return re.sub(r'[^\w\s]', '', text).lower()

def analyze_csv(file_path):
    all_titles = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            all_titles.append(row[0])  # adjust index if titles are in a different column

    combined = " ".join(all_titles)
    words = clean_text(combined).split()
    freq = Counter(words)

    print("🔍 Top Keywords:")
    for word, count in freq.most_common(10):
        print(f"{word}: {count}")

if __name__ == "__main__":
    analyze_csv("wikipedia_scrape.csv")
