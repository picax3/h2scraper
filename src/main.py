from __future__ import annotations
from bs4 import BeautifulSoup
import requests
import argparse
import sys
import json

class WebSource:
    url: str
    id_name: str
    element_name : str
    class_element : str
    def __init__(self, url: str, id_name: str, element_name: str, class_element: str):
        self.url: str = url
        self.id_name: str = id_name
        self.element_name: str = element_name
        self.class_element: str = class_element

   

    @staticmethod
    def load_from_file(file_name: str)->list[WebSource]:
        # load the file into the string

        with open(file_name, 'r')as file:
            try:
                json_str: str = file.read()
            except NameError:
                print("bs")
            except:
                print("error reading a file...")
        
            json_obj: dict = json.loads(json_str)

            webSource: list[WebSource] = []
            for site in json_obj:
                try:
                    webSource.append(WebSource(site['url'], site['id_name'], site['element_name'], site['class_element']))
                except:
                    print('something wrong')
        
        return webSource

        

def get_soup(url: str) -> BeautifulSoup:
    headers: dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0'}
    #request = requests.get('https://www.theaustralian.com.au/news/latest-news', headers=headers)
    request = requests.get(url, headers=headers)
    html: bytes = request.content

    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_headlines(soup: BeautifulSoup, element_id: str) -> list[str]:
    headlines: set = set()
    print(f'its here', {element_id})
#soup.find_all('a', {'class': 'link', 'id': 'special'})
    for h in soup.find_all('a', class_='storyblock_title_link'):
    #for h in soup.find_all('a', class_='element_id'):
    #for h in soup.find_all('a', {'class_':'element_id', 'class__':'class_element'}):
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
    parser.add_argument('-f', '--file')
    #parser.add_argument('-u', '--url')
    #parser.add_argument('-e', '--el')
    #parser.add_argument('-c', '--class')
    #parser.add_argument('-t', '--target')
    
    h2s_commands = parser.parse_args(sys.argv[1:])
    print(h2s_commands.scan)
    print(h2s_commands.file)
    #print(h2s_commands.url)
    #print(h2s_commands.el)
    #print(h2s_commands.__class__)
    #print(h2s_commands.target)

    print(WebSource.load_from_file(h2s_commands.file))
    web_sources: list[WebSource] = WebSource.load_from_file(h2s_commands.file)

    for ws in web_sources:
        try:
            soup: BeautifulSoup = get_soup(ws.url)
            print(f'HERE',{ws.element_name, ws.class_element})
            headlines: list[str] = get_headlines(soup=soup, element_id=ws.element_name)
            check_headlines(headlines, h2s_commands.scan)
            print('=========')
            print('=========')
            print(f'{ws.url}')
            print('=========')
        except:
            print('something')

    sites = [
        {'url': 'https://www.theaustralian.com.au/news/latest-news', 'class_': 'storyblock_title_link'},
        {'url': 'https://www.fedcourt.gov.au/news-and-events', 'class_': ''},
        {'url': 'https://www.austlii.edu.au/', 'class_': ''},
        {'url': 'https://asic.gov.au/newsroom', 'class_': ''}
    ]

if __name__ == '__main__':
    main()
    #logging.error('errors in code')
    #logging.warning('errors in code')
# if we type ai we will get every word containing 'ai' like mountains
# we just searching combination inside strings
# make it more accurate
# add interaction with user
# search more sites

#soup.find_all(name, attrs, recursive, string, limit, **kwargs)

 #   name: Tag name to search for (e.g., 'a', 'div').
 #   attrs: Dictionary of attributes to filter by (e.g., {'class': 'my-class'}).
  #  string: Filters elements that contain specific text.
  #  limit: Limits the number of results.
  #  **kwargs: Shortcut for attributes (like class_='my-class').