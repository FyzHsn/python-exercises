"""
Interesting lessons
-------------------

1. You can have a class variable that is global to all instances.
For example, using a class variable, one can track all the instances
of the class.

2. You can self reference within the class using *self*
"""


class ContactList(list):
    def search(self, name):
        matching_contacts = []

        # The next line of code is a little strange because it mostly make sense
        # due to the ContactList inheriting from list.
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print("Ok I'll send {} to {}".format(order, self.name))


if __name__ == "__main__":
    A = Contact("Faiyaz", "Faiyaz@G")
    B = Contact("Hasan", "Hasan@G")

    print(A.all_contacts)

    C = Supplier("Yung", "Yung@g.com")
    C.order("mangoes")
    print(C.all_contacts)
    print(B.all_contacts)

    print(Contact.all_contacts.search("Yung"))