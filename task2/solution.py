import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "https://ru.wikipedia.org"
START_URL = "/wiki/Категория:Животные_по_алфавиту"

def get_animals_by_letter_counts():
    url = BASE_URL + START_URL
    counts = {}

    while url:
        print(f"Fetching: {url}")
        response = requests.get(url)
        if response.status_code != 200:
            print("Error fetching page:", url)
            break

        soup = BeautifulSoup(response.content, "html.parser")


        animals_list = soup.select("#mw-pages .mw-category-group ul li a")

        for animal in animals_list:
            title = animal.get_text()
            if title:
                first_letter = title[0].upper()
                if first_letter.isalpha():  
                    counts[first_letter] = counts.get(first_letter, 0) + 1

        next_link = soup.select_one("a:contains('Следующая страница')")
        if not next_link:
            next_link = soup.find("a", string="Следующая страница")

        if next_link and 'href' in next_link.attrs:
            url = BASE_URL + next_link['href']
            time.sleep(0.5)  
        else:
            url = None

    return counts


def save_to_csv(counts, filename="beasts.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        for letter in sorted(counts.keys()):
            writer.writerow([letter, counts[letter]])


if __name__ == "__main__":
    counts = get_animals_by_letter_counts()
    save_to_csv(counts)
    print("Succes")
