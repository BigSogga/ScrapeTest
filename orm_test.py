from peewee import *

db = SqliteDatabase('test.db')


class BaseModel(Model):
    class Meta:
        database = db  # This model uses the "people.db" database.


class Person(BaseModel):
    name = CharField()
    other_names = CharField()
    aliases = CharField()


if __name__ == "__main__":
    Person.create_table()
    composer = Person(name='wawa', other_names='baba', aliases='dada')
    composer.save()
