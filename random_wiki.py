from bs4 import BeautifulSoup
import requests
import os
import analyser

url_pl = 'https://pl.wikipedia.org/wiki/Specjalna:Losowa_strona'
url_en = 'https://en.wikipedia.org/wiki/Special:Random'

# Asks the user for language (english or polish)
def choose_lang():
    pl = False
    lang = input('Please choose a language (EN/PL): ')
    
    if lang.lower() == 'en':
        return pl
    elif lang.lower() == 'pl':
        pl = True
        return pl
    return None

# Scrapes the website using BeautifulSoup (only the main header and paragraphs)
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
        
# Creates directories for files if they don't exist
def create_dir():
    lang = website[1].upper()
    
    if not os.path.isdir('websites/'):
        os.mkdir('websites/')
    if not os.path.isdir(f'websites/{lang}'):
        os.mkdir(f'websites/{lang}')
    
    os.mkdir(f'websites/{lang}/{website[0]}')

def write_files():
    # Writes the website to an .html and .txt file
        # Analyses it and writes that to .txt file
        lang = website[1].upper()

        with open(f'websites/{lang}/{website[0]}/{website[0]}.html', 'a', encoding='UTF-8') as hf:
            with open(f'websites/{lang}/{website[0]}/{website[0]}.txt', 'a', encoding='UTF-8') as tf:
                # Takes basic html template and writes it to a file
                with open(f'templates/html_{website[1]}.txt', 'r', encoding='UTF-8') as template:
                    for line in template:
                        hf.write(str(line))
                        
                    hf.write('<h1>' + website[0] + '</h1>\n')
                    tf.write(website[0] + '\n\n')
                    
                    for line in website[2]:
                        for i in range(50):
                            line = line.replace(f'[{i}]', '')
                            
                        hf.write('<p>' + line.strip('[').strip(']').strip('\n').strip() + '</p>')
                        tf.write(line.strip('[').strip(']').strip('\n').strip() + '\n')
                        
        with open(f'websites/{lang}/{website[0]}/info.txt', 'a', encoding='UTF-8') as info:
            info.write(analyser.count_words(website[0], lang))


if __name__ == "__main__":
    website = get_website()
    create_dir()

    if website != None:
        write_files()