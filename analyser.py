# Counts the words in paragraphs
def count_words(title, lang):
    x = 0
    with open(f'websites/{lang}/{title}/{title}.txt', 'r', encoding='UTF-8') as website:
        for line in website:
            for letter in line:
                if letter == ' ':
                    x += 1
    return (f'Sentences: {x}')