
# add contact
# show contact
# edit contact
# remove contact
# exit


# [
#     ["meisam, ", "ilka", "09369230358"]
#     ["shaghayegh, ", "saboori", ""]

# ]


from os import system

contact_list = list()

while True:
    menu = input("\n\n1/ add contact\n2/ show contacts\n3/ edit contact\n4/ remove contact\n5/exit")
    system("cls")
    
    if menu=="1":
        contact = list()
        contact.append(input("first name"))
        contact.append(input("last name"))
        contact .append(input("number"))
        
        contact_list.append(contact)

        phone_number=input("phone number : ")

        check_exists_phone_number = False

        for contact in [2]==phone_number:
            print(phone_number, "exists")
        check_exists_phone_number = True
        break
        
        

        system("cls")
    elif menu=="2":
        pass
    elif menu=="3":
        pass
    elif menu=="4":
        pass
    elif menu=="5":
        pass
    else:
        print("error!")



        