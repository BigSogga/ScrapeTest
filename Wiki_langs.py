from bs4 import BeautifulSoup
import requests
from ComposerScrape import get_composer_info
from API_Links import get_composers


composers = get_composers()


def get_wiki_langs_and_links():
    for composer in composers:
        composer_info = get_composer_info(composer['permlink'])

        if composer_info is None:
            continue

        composerName, names_in_languages, aliases_in_languages, wikipedia_link = composer_info
        if wikipedia_link != '':
            link = requests.get(wikipedia_link)
            soup = BeautifulSoup(link.content, 'html.parser')

            table_of_language_links = soup.find_all(class_='interlanguage-link-target')

            language_and_link = {}

            for element in table_of_language_links:
                language_of_other_wiki = element.get('lang')
                link_to_other_wiki = element.get('href')
                language_and_link[language_of_other_wiki] = link_to_other_wiki
            return language_and_link


if __name__ == '__main__':
    get_wiki_langs_and_links()
