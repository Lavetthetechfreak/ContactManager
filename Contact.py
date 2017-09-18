
class Contact:
    def __init__(self):
        self.value = {}
        self.all_contacts = []
    #create new contact
    def create_contact(self):
        self.contact = ['name', 'phone', 'email']

        for request in self.contact:
            self.value[request] = input("Please input your {}:".format(request))
        self.all_contacts.append(self.value)
        print(self.all_contacts)

     #delete contacts

    def delete_contact(self, contact_name):
        delete = self.all_contacts
        for index, contacted in enumerate(delete):
            if contact_name == contacted['name']:
                delete.pop(index)
        print(delete)

    #search for contacts
    def search_contact(self):
        search = self.all_contacts
        search_input = input("Enter your name:")

        if len(search) > 0:
            for data in search:
                if search_input == data['name']:
                    print(data)

            else:
                return ValueError("sorry")
        else:
            print("Empty Contact list")

    #perform all operations
    def all_operations(self):
        value = ''

        while value is not "Q":
            print(''' 
                     A.To add contacts
                     B.To delete contacts
                     C.To View contacts''')
            value = str(input("Enter A,B or C:"))
            if value == "A":
                contact.create_contact()
            if value == "B":
                contact_name = str(input("Enter a Name: "))
                contact.delete_contact(contact_name)
            if value == 'C':
                contact.search_contact()

#call
contact = Contact()
contact.all_operations()





