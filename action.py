from os import path
from csv import DictWriter, DictReader

filename = "phonebook.csv"


class PhoneBook:
    phone = []
    counter = 0

    def __init__(self):
        if PhoneBook.counter == 0:
            self.read(filename)
            PhoneBook.counter = PhoneBook.counter + 1

        self.book = {"Name": "", "PhoneNumber": "", "Email Address": ""}
        self.personal_information()
        print(self.phonenumber)

        self.stat = self.duplicatecheck1(self.phonenumber)
        print(self.phone)
        self.phoneadd = PhoneBook.phone.append(self.book)

    def personal_information(self):
        print("Please provide the information to add in a phone diary")
        name = input("Enter a name:\n")
        self.book["Name"] = name

        self.phonenumber = input("Enter the phone number:\n")

        self.book["PhoneNumber"] = self.phonenumber

        self.book["Email Address"] = input("Enter an email_address:\n")

    def duplicatecheck1(self, name):
        # status = False
        print("123", name)
        print("list", self.phone)
        for check in self.phone:
            print(check)
            print("name", name)
            if check["PhoneNumber"] == name:
                # status = True
                return True
        return False

    def read(self, filename):
        with open(filename, "r") as handlerRead:
            reader = DictReader(handlerRead)
            self.phone.extend(reader)

    def witeintofile(self, filename):
        print(filename)
        a = [self.book]
        if path.exists(filename):
            with open(filename, "a", newline="") as handler:
                print("b")
                writer = DictWriter(handler, fieldnames=["Name", "PhoneNumber", "Email Address"])
                writer.writerows(a)

        else:
            print(filename)
            with open(filename, "w", newline="") as handler:
                writer = DictWriter(handler, fieldnames=["Name", "PhoneNumber", "Email Address"])
                writer.writeheader()
                writer.writerows(a)


class List:
    phone = []
    counter = 0

    def __init__(self):

        if List.counter == 0:
            self.read(filename)
            List.counter = List.counter + 1

    def read(self, filename):
        with open(filename, "r") as handlerRead:
            reader = DictReader(handlerRead)
            self.phone.extend(reader)

    def search(self, key, index):
        counters = 0
        for ser in self.phone:

            if ser[key].lower() == index.lower():
                for serkey, serindex in ser.items():
                    print(serkey, ":", serindex)
                print("-" * 60)
                counters += 1
        if counters == 0:
            print("Entered {} does not exists.".format(key))

    def delete(self, phone_number):
        counterl = 0
        print(phone_number)
        for index, value in enumerate(self.phone):
            print(index, value)
            if value["PhoneNumber"] == phone_number:
                print(index)
                self.phone.pop(index)
                counterl += 1

        if counterl == 0:
            print("Entered phone number does not exists.")
        else:
            with open(filename, "w", newline="") as handler:
                writer = DictWriter(handler, fieldnames=["Name", "PhoneNumber", "Email Address"])
                writer.writeheader()
                writer.writerows(self.phone)
            print("Phone Number deleted successfully")

    def edit(self, phone12, name12, phone_num12, email12):
        countere = 0
        for f in self.phone:
            for phone_key, phone_value in f.items():
                if f["PhoneNumber"] == phone12:
                    if name12.isspace() is False and name12 != "":
                        f["Name"] = name12
                    if phone_num12.isspace() is False and phone_num12 != "":
                        f["PhoneNumber"] = phone_num12
                    if email12.isspace() is False and email12 != "":
                        f["Email Address"] = email12
                    countere += 1

        if countere == 0:
            print("Entered phone number does not exists.")
        else:
            with open(filename, "w", newline="") as handler:
                writer = DictWriter(handler, fieldnames=["Name", "PhoneNumber", "Email Address"])
                writer.writeheader()
                writer.writerows(self.phone)

            print("Data edited successfully")
