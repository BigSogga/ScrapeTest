from bs4 import BeautifulSoup, NavigableString, Tag
import requests


def get_composer_info(url):
    link = requests.get(url)
    soup = BeautifulSoup(link.content, "html.parser")

    names_class = soup.find(class_="cp_firsth")
    table = soup.find(class_='plainlinks cp_mainlinks')

    if names_class == None:
        return None

    # Name of composer
    name_select = names_class.find("h2")
    official_name = name_select.get_text().strip()

    def ffff(span):
        if 'class' in span.attrs and 'expandline' in span.attrs['class']:
            return False
        else:
            return True

    # Translated names of composer finder
    names_in_languages = []
    aliases = []
    for element in table:
        if isinstance(element, Tag) and len(element.contents) > 0:
            if isinstance(element.contents[0], NavigableString) and element.contents[0] == 'Name in Other Languages: ':
                title_strings = element.find_all("span", title=True)
                names_in_languages = list(filter(ffff, title_strings))
            if isinstance(element.contents[0], NavigableString) and element.contents[0] == 'Aliases: ':
                title_strings2 = element.find_all("span", title=True)
                aliases = list(filter(ffff, title_strings2))

    # Get language of translated name
    language_and_name = {}
    for name_in_languages in names_in_languages:
        languages_as_stringlist = name_in_languages.attrs['title']
        languages = languages_as_stringlist.split(', ')
        name = name_in_languages.get_text()
        for language in languages:
            language_and_name[language] = name

    # Get aliases of composer
    language_and_alias = {}
    for alias in aliases:
        if len(alias) > 0:
            languages_as_stringlist2 = alias.attrs['title']
            languages2 = languages_as_stringlist2.split(', ')
            name_in_languages2 = alias.get_text()
            for language in languages2:
                language_and_alias[language] = name_in_languages2

    # Get Wikipedia biography
    external_links_table = soup.find(class_='cp_links')
    wikipedia_link = ''
    wikipedia_link_tag = external_links_table.find('a')
    if wikipedia_link_tag is not None:
        wikipedia_link = wikipedia_link_tag.get('href')

    return official_name, language_and_name, language_and_alias, wikipedia_link


if __name__ == '__main__':
    get_composer_info()
