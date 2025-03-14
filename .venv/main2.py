from bs4 import BeautifulSoup
import requests


def get_soup() -> BeautifulSoup:
    headers: dict = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0"}
    try:
        response = requests.get('https://www.theaustralian.com.au/', headers=headers)
        response.raise_for_status()  # Check if request was successful
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None

    html: bytes = response.content
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def get_headlines(soup: BeautifulSoup) -> list[str]:
    headlines: set = set()

    # Inspect the page to confirm correct tag and class
    for h in soup.find_all('h4', class_='storyblock_title'):
        if h.contents:  # Check if contents are not empty
            headline: str = h.contents[0].lower()
            headlines.add(headline)

    return sorted(headlines)

def main():
    soup: BeautifulSoup = get_soup()
    if soup is None:
        return  # Exit if soup could not be fetched

    headlines: list[str] = get_headlines(soup=soup)

    if headlines:
        for headline in headlines:
            print(headline)
    else:
        print("No headlines found.")


if __name__ == '__main__':
    main()
