class ContactList(list):
    def search(self, name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(name)
        return matching_contacts


class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)


class Friend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone


class MailSender:
    def send_mail(self, message):
        print("Sending email to {email}".format(email=self.email))
        print(message)


class EmailableContact(Contact, MailSender):
    pass


if __name__ == "__main__":
    e = EmailableContact("Yung Feezy", "yung@feezy.com")
    print(Contact.all_contacts)
    e.send_mail("Carry one")