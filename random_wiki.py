from bs4 import BeautifulSoup
import requests

url_pl = 'https://pl.wikipedia.org/wiki/Specjalna:Losowa_strona'
url_en = 'https://en.wikipedia.org/wiki/Special:Random'

def choose_lang():
    pl = False
    lang = input('Please choose a language (EN/PL): ')
    
    if lang.lower() == 'en':
        return pl
    elif lang.lower() == 'pl':
        pl = True
        return pl
    return None

def get_website():
    lang = choose_lang()
    if lang:
        url = url_pl
        lang = 'pl'
    else:
        url = url_en
        lang = 'en'
        
    response = requests.get(url)
    page_dom = BeautifulSoup(response.text, 'html.parser')
    title = page_dom.find('h1').getText()
        
    print(title, '\n----------')
    user_conf = input('Would you like to see this website? (Y/N)')
        
    if user_conf.lower() == 'y':
        try:
            page = page_dom.find_all('p')
            site = []
            
            for line in page:
                site.append(line.getText())
                  
            return title, lang, site
        except:
            return None

website = get_website()

if website != None:
    with open(f'websites/{website[0]}.html', 'a', encoding='UTF-8') as file:
        with open(f'templates/html_{website[1]}.txt', 'r', encoding='UTF-8') as template:
            for line in template:
                file.write(str(line))
                
            file.write('<h1>' + website[0] + '</h1>\n')
            for line in website[2]:
                file.write('<p>' + line.strip('[').strip(']').strip('\n') + '</p>')