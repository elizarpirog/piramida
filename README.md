# Contact Book

A tiny desktop-style contact manager written in Python.

Instead of keeping phone numbers on paper or scattered across different applications, this project stores contacts in one place and allows searching and exporting them.

---

## What can it do?

✔ Store contacts

✔ Search by name

✔ Search by city

✔ Export contact list

✔ Display simple statistics

---

## Example

```
Contact Book

John Miller
+1 555-1234
London

Anna Smith
+44 777-2233
Manchester

-------------------------
Contacts: 5
Cities: 3
```

---

## File Layout

| File | Responsibility |
|------|----------------|
| contact.py | Contact model |
| addressbook.py | Stores contacts |
| search.py | Search functions |
| exporter.py | Console output |
| validator.py | Input validation |
| sample_contacts.py | Demo data |

---

## Ideas for the future

- Birthday reminders
- Import from CSV
- Contact groups
- Favorite contacts
- Duplicate detection
