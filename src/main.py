from bs4 import BeautifulSoup
import requests
import argparse
import sys


def get_soup() -> BeautifulSoup:
    headers: dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0'}
    request = requests.get('https://www.theaustralian.com.au/news/latest-news', headers=headers)
    html: bytes = request.content

    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_headlines(soup: BeautifulSoup) -> list[str]:
    headlines: set = set()

    for h in soup.find_all('a', class_='storyblock_title_link'):
        headline: str = h.contents[0].lower()
        headlines.add(headline)

    return sorted(headlines)

def check_headlines(headlines: list[str], term: str):
    term_list: list[str] = []
    terms_found: int = 0

    for i, headline in enumerate( headlines, start=1):
        if term.lower() in headline:
            terms_found += 1
            term_list.append(headline)
            print(f'{i}: {headline.capitalize()} <------------------------------ "{term}"')
        else:
            print(f'{i}: {headline.capitalize()}')

        print('--------------------------------------------------------------------------------------')
        if terms_found:
            print(f'"{term}" was mentioned {terms_found} times.')
            print('======================================================================================')

            for i, headline in enumerate(term_list, start=1):
                print(f'{i}: {headline.capitalize()}')

        else:
            print(f'No matches found for: "{term}"')
            print('--------------------------------------------------------------------------------------')
            #print('======================================================================================')

def main():
   
    parser = argparse.ArgumentParser(prog='h2scraper', description='Scrape the news headlines from the Australian news sites')
    parser.add_argument('-s', '--scan')
    h2s_commands = parser.parse_args(sys.argv[1:])
    print(h2s_commands.scan)

    
    soup: BeautifulSoup = get_soup()
    headlines: list[str] = get_headlines(soup=soup)

    sites = [
        {'url': 'https://www.theaustralian.com.au/news/latest-news', 'class': 'storyblock_title_link'},
        {'url': 'https://www.fedcourt.gov.au/news-and-events', 'class': ''},
        {'url': 'https://www.austlii.edu.au/', 'class': ''},
        {'url': 'https://asic.gov.au/newsroom', 'class': ''}
    ]


    check_headlines(headlines, h2s_commands.scan)

if __name__ == '__main__':
    main()

# if we type ai we will get every word containing 'ai' like mountains
# we just searching combination inside strings
# make it more accurate
# add interaction with user
# search more sites

