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
    page = [title]
        
    if user_conf.lower() == 'y':
        try:
            page.append(page_dom.find_all('p'))
        except:
            url = None
    
    return page

page = get_website()

with open(f'websites/{page[0]}.html', 'w', encoding='UTF-8') as file:
    file.write(str(page))
    