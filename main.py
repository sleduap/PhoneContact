from action import PhoneBook, List

from csv import DictWriter
# from csv import DictReader
from os import path

filename = "phonebook.csv"
if path.exists(filename) is False:
    with open(filename, "w", newline="") as handler:
        writer = DictWriter(handler, fieldnames=["Name", "PhoneNumber", "Email Address"])
        writer.writeheader()


def main():
    print("""Welcome to our Phone Diary""".center(150, "*"), "\n",
          "=" * 149, """
Available action 
A : Add
B : List
C : Search
D : Delete
E : Edit
F : Exit
""")
    while True:
        action = input("Please select any one listed action to carry out ""\033[3;93;93m(Enter F or Press Enter two times to exit):\n")
        if action.upper() == "A":

            add = PhoneBook()

            # phonenumber = add.stat
            stats = add.stat
            print(stats)
            if stats is False:
                print(filename)
                add.witeintofile(filename)
            else:
                print("Phone number already exists")
                # print(add.phone)
        elif action.upper() == "B":
            lis = List()
            for list1 in lis.phone:
                for key, value in list1.items():
                    print(key, ":", value)
                print("-" * 60)

        elif action.upper() == "C":
            ser = List()
            print("""Enter N to search by Name
Enter P to search by Phone Number
Enter E to search by Email
""")
            action2 = input("Select the search method:\n")
            if action2.upper() == "N":
                name = input("Enter a name:\n ")
                ser.search("Name", name)
            elif action2.upper() == "P":
                phone_num = input("Enter the phone number:\n")
                ser.search("PhoneNumber", phone_num)
            elif action2.upper() == "E":
                email = input("Enter an Email Address:\n")
                ser.search("Email Address", email)
            else:
                print("Please Select the valid search option")

        elif action.upper() == "D":
            p = input("Enter the Phone Number to be deleted:\n")
            de = List()
            de.delete(p)
        elif action.upper() == "E":
            p = input("Enter the Phone Number of which you like to  edit basic details:\n")
            n = input("Enter a name:\n ")
            ph = input("Enter the phone number:\n")
            em = input("Enter an Email Address:\n")
            ed = List()
            ed.edit(p, n, ph, em)
        elif action.upper() == "F" or action == "" \
                                                "" \
                                                "":


            break

        else:
            print("Please select the valid action")


if __name__ == '__main__':
    main()
