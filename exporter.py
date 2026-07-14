def show(contacts):

    print()

    print("Contact Book")

    print("-" * 30)

    for contact in contacts:

        print(contact.name)

        print(contact.phone)

        print(contact.city)

        print()

    cities = {

        c.city

        for c in contacts

    }

    print("-" * 30)

    print(
        f"Contacts: {len(contacts)}"
    )

    print(
        f"Cities: {len(cities)}"
    )
