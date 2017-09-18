import time
import datetime
from datetime import date


class Contact:
    def __init__(self, name, phone, email, website, B_day, linkedIn, picture):
        self.name = name
        self.phone = phone
        self.Email = email
        self.website = website
        self.B_day = B_day
        self.linkedIn = linkedIn
        self.picture = picture

    def make_contact(self):
        print("hey enter your details to get our services")
        self.name = input("enter your name:")
        self.phone = int(input("Enter your phone number:"))
        if self.phone < 10:
            print("Invalid phone number")
        else:
            self.Email = input('Enter your email address:')
            self.website = input("Enter your website:")
            self.B_day = input("Enter your birthday {}: ".format(datetime.date))
            self.linkedIn = input("Enter your LinkedIn link here:")
            self.picture = input("Please place your photo here:")
            print('''Thank you {} Here are your details: 
                                                phonenumber:{}
                                                Email:{}
                                                Website:{}
                                                Birthday:{}
                                                LinkedIn:{}
                                                Photo{}'''.format(self.name, self.phone, self.Email, self.website, self.B_day, self.linkedIn, self.picture))
contact = Contact("lavet", '0710698143', 'lavet@gmail.com', 'wwww.lavet.com', '10/20/30', 'gvhbjhgvhbjn', 'no photo')
contact.make_contact()
