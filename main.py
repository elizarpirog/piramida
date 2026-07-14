from addressbook import AddressBook

from sample_contacts import CONTACTS

from exporter import show

from search import by_city

book = AddressBook()

for contact in CONTACTS:

    book.add(contact)

show(book.list())

print()

print("People from London")

print("-" * 20)

for person in by_city(

        book.list(),

        "London"

):

    print(person.name)
