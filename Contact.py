# -*- coding: utf-8 -*-

import atexit

class Contact(object):

    _first_name = None
    _last_name = None
    _phone_number = None
    _birth_year = None
    _email = None
    contactList = list()

    def __init__(self, first_name, last_name, phone_number, birth_year, email):
        self.fName = first_name
        self.lName = last_name
        self.phone = phone_number
        self.birth = birth_year
        self.mail = email

    def get_full_name(self):
        return self._first_name + " " + self._last_name

    @staticmethod
    def add_contact(cnt):
        if isinstance(cnt, Contact):
            Contact.contactList.append(cnt)

    @staticmethod
    def print_contact_list():
        print str(Contact.contactList)

    def set_first_name(self, first_name):
        if isinstance(first_name, str):
            self._first_name = first_name
        else:
            print "First name must be of type string."

    def get_first_name(self):
        return self._first_name

    fName = property(fget = get_first_name, fset = set_first_name)

    def set_last_name(self, last_name):
        if isinstance(last_name, str):
            self._last_name = last_name
        else:
            print "Last name must be of type string."

    def get_last_name(self):
        return self._last_name

    lName = property(fget=get_last_name, fset=set_last_name)

    def set_phone_number(self, phone_number):
        if isinstance(phone_number, str):
            if not any(character.isalpha() for character in phone_number):
                self._phone_number = phone_number
            else:
                "Phone number must contain numeric characters."
        else:
            print "Phone number must be of type string."

    def get_phone_number(self):
        return self._phone_number

    phone = property(fget=get_phone_number, fset=set_phone_number)

    def set_birth_year(self, birth_year):
        if isinstance(birth_year, int):
            self._birth_year = birth_year
        else:
            print "Birth year must be of type integer."

    def get_birth_year(self):
        return self._birth_year

    birth = property(fget=get_birth_year, fset=set_birth_year)

    def set_email(self, email):
        if isinstance(email, str):
            if "@" in email:
                self._email = email
            else:
                print "Email must contain the character \'@\'."
        else:
            print "Email must be of type string."

    def get_email(self):
        return self._email

    mail = property(fget=get_email, fset=set_email)

    def __eq__(self, contact):
        return self.fName == contact.fName and self.lName == contact.lName and self.phone == contact.phone and self.birth == contact.birth and self.mail == contact.mail

    def __del__(self):
        if Contact.contactList != None:
            if self in Contact.contactList:
                Contact.contactList.remove(self)

    @staticmethod
    def write_in_file(filePath = "dat.txt"):
        with open(filePath, "w+") as file:
            file.write(str(Contact.contactList))

    def __str__(self):
        return "Contact(\"" + str(self.fName) + "\", \"" + str(self.lName) + "\", \"" + str(self.phone) + "\", " + str(self.birth) + ", \"" + str(self.mail) + "\")"

    def __repr__(self):
        return str(self)

    @staticmethod
    def read_from_file(filePath = "dat.txt"):
        try:
            with open(filePath, "r") as file:
                Contact.contactList = eval(file.read())
        except:
            "File " + str(filePath) + " does not exists."

@atexit.register
def closeProgram():
    Contact.write_in_file()

def main():
    Contact.read_from_file()
    for person in Contact.contactList:
        print person.fName
        print person.lName
        print person.phone
        print person.birth
        print person.mail
        print ""  # empty line

if __name__ == "__main__":
    main()