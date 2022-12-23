from API_Links import get_composers
from ComposerScrape import get_composer_info
from ORM import *
from Wiki_langs import get_wiki_langs_and_links

composers = get_composers()
for composer in composers:
    composer_info = get_composer_info(composer['permlink'])

    if composer_info is None:
        continue

    composerName, names_in_languages, aliases_in_languages, wikipedia_link = composer_info

    try:
        composer_record = Composer.get(imslpCategory=composer['id'])
        composer_record.refName = composerName
        composer_record.biography = wikipedia_link
    except DoesNotExist as a:
        composer_record = Composer(refName=composerName, biography=wikipedia_link, imslpCategory=composer['id'])
    composer_record_query = composer_record.save()

    for isoCode, name in names_in_languages.items():
        try:
            language = Language.get(isoCode=isoCode)
        except DoesNotExist as e:
            language = Language(isoCode=isoCode)
            language.save()

        try:
            nil = NameInLanguage.get(composer=composer_record, language=language)
            nil.name = name
        except DoesNotExist as b:
            nil = NameInLanguage(composer=composer_record, language=language, name=name)
        nil.save()

    for language, alias in aliases_in_languages.items():
        try:
            composer_alias = Alias.get(alias=alias, language=language, composer=composer_record)
        except DoesNotExist as c:
            composer_alias = Alias(alias=alias, language=language, composer=composer_record)
            composer_alias.save()

    if wikipedia_link:
        language_and_link = get_wiki_langs_and_links()
        for lang, wiki_link in language_and_link.items():
            try:
                wiki_bio = WikibioLanguage.get(composer=composer_record, language=lang, wiki_link=wiki_link)
            except DoesNotExist as w:
                wiki_bio = WikibioLanguage(composer=composer_record,  language=lang, wiki_link=wiki_link)
                wiki_bio.save()
                print(wiki_bio)
