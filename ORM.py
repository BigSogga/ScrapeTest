from peewee import *

db = SqliteDatabase('IMSLPtest.db')


class BaseModel(Model):
    class Meta:
        database = db


class Composer(BaseModel):
    refName = TextField()
    imslpCategory = TextField(unique=True)
    wikipedia_bio = TextField()
    biography = TextField()


class Language(BaseModel):
    isoCode = TextField(unique=True)


class Alias(BaseModel):
    composer = ForeignKeyField(Composer)
    language = ForeignKeyField(Language)
    alias = TextField()


class NameInLanguage(BaseModel):
    composer = ForeignKeyField(Composer)
    language = ForeignKeyField(Language)
    name = TextField()

    class Meta:
        indexes = (
            (('composer', 'language'), True),
        )


class WikibioLanguage(BaseModel):
    composer = ForeignKeyField(Composer)
    language = ForeignKeyField(Language)
    wiki_link = TextField()


if __name__ == '__main__':
    Composer.create_table()
    Language.create_table()
    Alias.create_table()
    NameInLanguage.create_table()
    WikibioLanguage.create_table()
