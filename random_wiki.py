from bs4 import BeautifulSoup
import requests

def choose_lang():
    url_pl = 'https://pl.wikipedia.org/wiki/Specjalna:Losowa_strona'
    url_en = 'https://en.wikipedia.org/wiki/Special:Random'
    
    lang = input('Please choose a language (EN/PL): ')
    
    if lang.lower() == 'en':
        return url_en
    elif lang.lower() == 'pl':
        return url_pl
    return None

def get_website():
    url = choose_lang()
        
    response = requests.get(url)
    page_dom = BeautifulSoup(response.text, 'html.parser')
    title = page = page_dom.find('h1').getText()
        
    print(title, '\n----------')
    user_conf = input('Would you like to see this website? (Y/N)')
        
    if user_conf.lower() == 'y':
        try:
            page = page_dom.find_all('p')
            return title, page
        except:
            return None

website = get_website()

if website != None:
    with open(f'websites/{website[0]}.html', 'w', encoding='UTF-8') as file:
        file.write(str(website))