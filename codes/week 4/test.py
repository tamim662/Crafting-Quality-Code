class Contact:

    """ A contact with a first name, a last name, and an email address. """

    def __init__(self, first_name, last_name, email_address):

        """ (Contact, str, str, str) -> NoneType

       Initialize this Contact with first name first_name, last name
       last_name, and email address email_address.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
    def check(self):

        print(self.first_name)

    def add_phone_number(self, telephone_num):
        """ (Contact, str) -> NoneType

        Add phone number telephone_num for this contact.
        """

        self.phone_number = telephone_num
        print(self.phone_number)



# paul = Contact('Paul', 'Gries', 'paul@example.com')

# paul.check()

c=Contact('Paul', 'Gries', 'paul@example.com')
# c.add_phone_number('555-1111')


Contact.add_phone_number(c, '555-1111')