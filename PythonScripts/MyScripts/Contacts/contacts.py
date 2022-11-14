contacts = []


class ContactNotFound(Exception):
    pass


def sort(by: str) -> list:
    contacts.sort(key=lambda k: k[by])


def add(name: str, surname: str, cell: str):
    contact = {
        "name": name,
        "surname": surname,
        "cell": cell
    }
    contacts.append(contact)


def remove(name: str) -> list[dict]:
    for i, e in enumerate(contacts):
        if e["name"] == name:
            print("Deleted the contact: ", contacts.pop(i))
            return 0
    raise ContactNotFound("Error the contact specified could not be found.")


def find(name: str):
    for e in contacts:
        if e["name"] == name:
            print("Found the contact: ", e)
            return 0
    raise ContactNotFound("Error the contact specified could not be found.")


add("Mattia", "Meligeni", "3515413664")
add("Alberto", "Provati", "3728798653")
sort("name")
print(contacts)
find("Mattia")
remove("Alberto")
print(contacts)
