# pip install beautifulsoup4

from bs4 import BeautifulSoup
import requests

def get_soup() -> BeautifulSoup:
    """Get the soup back from the website, mmm..."""

    # Make a request
        #Google My user agent for the following
    headers: dict = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}
    request = requests.get('https://www.bbc.com/news', headers=headers)
    html: bytes= request.content

    #Create soup
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def get_headlines(soup: BeautifulSoup) -> list[str]:
    """Scrape the headlines from the soup we provide"""

    headlines: set = set()

    # Finds all the headers in BBC Home
    for h in soup.findAll('h2', {'data-testid': 'card-headline'}):#old:'h3', class_='gs-c-promo-heading__title'
        headline: str = h.contents[0].lower()
        headlines.add(headline)

    return sorted(headlines)

def check_headlines(headlines: list[str], term: str):
    """Check if a term is found in a headline"""

    term_list: list[str] = []
    terms_found: int = 0

    # Loop through the headlines to find the keyword
    for i, headline in enumerate(headlines, start=1):
        if term.lower() in headline:
            terms_found += 1
            term_list.append(headline)
            print(f'{i}: {headline.capitalize()} <--------------------"{term}"')
        else:
            print(f'{i}: {headline.capitalize()}')
    
    # Show the new list that contains the headlines if a term was found in them
    print('-------------------------------------')
    if terms_found:
        print(f'"{term}" was mentioned {terms_found} times.')
        print('-------------------------------------')

        for i, headline in enumerate(term_list, start=1):
            print(f'{i}: {headline.capitalize()}')
    else:
        print(f'No matches found for: "{term}"')
        print('-------------------------------------')

def main_headlineScraper():
    soup: BeautifulSoup = get_soup()
    headlines: list[str] = get_headlines(soup=soup)

    #for headline in headlines:
    #    print(headline)

    # Get the user input and check for headlines
    #user_input: str = 'musk'
    user_input: str = input('What term would you like to check for? >>')
    check_headlines(headlines, user_input)


if __name__ == '__main__':
        main()

#Improvement: 
#   - The script does not check if its a word just if the letters are used somewhere 
