import re,json
#VALIDATORS
def Name(a):#NAME VALIDATION
    if len(a)>2 and len(a)<13:
        if re.match("[A-Z]{3,}",a):
            return True
    else:
        return False

def Mobile(n):#MOBILE NUMBER VALIDATION
    if len(n)==10:
        if re.match('[6-9][0-9]{9}',n):
            return True
    else:
        return False

def Email(e):#EMAIL VALIDATION
    if re.match("[\w\.-]+@[\w\.-]+\.\w+$",e):
        return True
    else:
        return False

#FILE HANDLING
def save_contact(contact):#CREATION OF JSON FILE
    with open("contacts.json", "w") as file:
        json.dump(contact, file, indent=4)

def get_contacts():#READING FROM JSON FILE
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    return contacts

#MANAGING CONTACTS
def create():#CONTACT CREATION
    contacts=get_contacts()
    name=input("Enter name:-").upper()
    for contact in contacts:
        if name not in contact["name"]:#CHECKING NAME IS ALREADY PRESENT OR NOT
            if Name(name):#VALIDATING NAME
                mobile = input('Enter Phone number:-')
                email = input ('Enter Email ID :-')
                if Mobile(mobile):#VALIDATING MOBILE NUMBER
                    if Email(email):#VALIDATING EMAIL ID
                        contact={"name":name,"mobile":mobile,"email":email}
                        contacts.append(contact)
                        save_contact(contacts)#STORING CONTACT IN JSON FILE
                        print("contact created")
                        break
                    else:
                        print("INVALID EMAIL")
                else:
                    print("INVALID MOBILE NUMBER!!")
            else:
                print("invalid name! please provide valid name!")
        else:
            print (f"{name} already exists.")
   

def update():#UPDATION
    
    contacts=get_contacts()#GETTING CONTACTS FROM JSON FILE
    name=input("Choose the contact to update:-").upper()
    for contact in contacts:
        if name in contact["name"]:#CHECKING THE CONTACT IS PRESENT IN FILE OR NOT
            print("""SELECT FIELD TO UPDATE
                1.NAME
                2.MOBILE
                3.EMAIL """)#OPTIONS TO UPDATE
            
            choice=int(input("number:-"))
            if choice==1:#UPDATING NAME
                new_value=input("enter new name:-").upper()
                if Name(new_value):
                    contact['name']=new_value
                    save_contact(contacts)
                    print("contact updated")
                    
                else:
                    print("INVALID NAME!")
            elif choice==2:#UPDATING MOBILE
                mobile=input('enter a 10 digit number:-')
                if Mobile(mobile):
                    contact["mobile"]=mobile
                    save_contact(contacts)
                    print("contact updated")
                  
                else:
                    print("invalid mobilenumber!! ")
            elif choice==3:#UPDATING EMAIL
                email=input("enter email:-")
                if Email(email):
                    contact["email"]=email
                    save_contact(contacts)
                    print("contact updated")
                    
                else:
                    print("invalid mail id!")
            else:
                print("""SELECT THE FIELD TO UPADTE
                    1.NAME
                    2.MOBILE
                    3.EMAIL""")
        else:
            print(f"{name} NOT FOUND!")
                    
        
def search():#SEARCHING
    contacts=get_contacts()#GETTING CONTACTS FROM JSON FILE
    name=input("Enter contact name to search:-").upper()
    for contact in contacts:#SEARCHING FOR CONTACT
        if name in contact["name"]:
            print("NAME="+contact["name"],"MOBILE="+contact["mobile"],"EMAIL="+contact["email"],sep="\n")
            break
    else:
        print("NO CONTACT FOUND!")
    
def delete():#DELETION
    contacts=get_contacts()#GETTING CONTACTS FROM JSON FILE
    name=input("Enter Contact name for deletion ").upper()
    for contact in contacts:#SEARCHING FOR CONTACT
        if name == contact['name']:
            contacts.remove(contact)#DELETING CONTACT
            save_contact(contacts)
            print("CONTACT"+f"{name}"+"deleted successfully")
            break
        else:
            print("NO CONTACT FOUND TO DELETE")

def all_contacts():#VIEW ALL CONTACTS
    contacts=get_contacts()
    print()
    print("NAME","MOBILE","EMAIL",sep="     ")

    for contact in contacts:
        print(contact["name"],contact["mobile"],contact["email"],sep=" ")
    print()


flag=True
while flag:
    print("""CONTACTS MANAGEMENT SYSTEM
    PLEASE CHOOSE THE OPERATION
    1. CREATE
    2. UPDATE
    3. SEARCH
    4. DELETE
    5. ALL CONTACTS
    0. EXIT
    """)
    choice = int(input("Enter your option (number): "))
    if choice == 1: #CREATE operation
        create()
    elif choice == 2:#UPDATE Operation
        update()
    elif choice==3:#Search Operation
        search()
    elif choice==4:#DELETE Operation
        delete()
    elif choice==5:
        all_contacts()#All Contacts Functionality
    elif choice==0:#EXIT OPERATION
        flag=False
    else:
        print("PLEASE CHOOSE VALID OPTION")


