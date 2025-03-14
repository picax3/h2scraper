from bs4 import BeautifulSoup
import requests

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
    soup: BeautifulSoup = get_soup()
    headlines: list[str] = get_headlines(soup=soup)

    #for headline in headlines:
        #print(headline)

    user_input: str = 'wombat'
    check_headlines(headlines, user_input)

if __name__ == '__main__':
    main()

# if we type ai we will get every word containing 'ai' like mountains
# we just searching combination inside strings
# make it more accurate
# add interaction with user
# search more sites