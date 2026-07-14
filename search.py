def by_name(contacts, keyword):

    return [

        contact

        for contact in contacts

        if keyword.lower()

        in contact.name.lower()

    ]


def by_city(contacts, city):

    return [

        contact

        for contact in contacts

        if contact.city.lower()

        == city.lower()

    ]
