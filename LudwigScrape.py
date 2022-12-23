from bs4 import BeautifulSoup, NavigableString, Tag
import requests

link = requests.get("https://imslp.org/wiki/Category:Beethoven,_Ludwig_van")
soup = BeautifulSoup(link.content, "html.parser")

names_class = soup.find(class_="cp_firsth")
table = soup.find(class_='plainlinks cp_mainlinks')

# Name of composer
name_select = names_class.find("h2")
name = name_select.get_text().strip()
print(name)

def ffff(span):
    if 'class' in span.attrs and 'expandline' in span.attrs['class']:
        return False
    else:
        return True


# Translated names of composer finder
for element in table:
    if isinstance(element, Tag) and len(element.contents) > 0:
        if isinstance(element.contents[0], NavigableString) and element.contents[0] == 'Name in Other Languages: ':
            title_strings = element.find_all("span", title=True)
            title_strings = list(filter(ffff, title_strings))
            small_table = title_strings
        if isinstance(element.contents[0], NavigableString) and element.contents[0] == 'Aliases: ':
            title_strings2 = element.find_all("span", title=True)
            title_strings2 = list(filter(ffff, title_strings2))
            next_small_table = title_strings2



# Get language of translated name
language_and_name = {}
for tag in small_table:
    languages_as_stringlist = tag.attrs['title']
    languages = languages_as_stringlist.split(', ')
    name_in_languages = tag.get_text()
    for language in languages:
        language_and_name[language] = name_in_languages
    # print(language_and_name)


# Get aliases of composer
language_and_alias = {}
for tag2 in next_small_table:
    languages_as_stringlist2 = tag2.attrs['title']
    languages2 = languages_as_stringlist2.split(', ')
    name_in_languages2 = tag2.get_text()
    for language in languages2:
        language_and_alias[language] = name_in_languages2
    print(language_and_alias)
