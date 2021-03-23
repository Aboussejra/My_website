from datetime import datetime

# user database model
class User:
   """
     A representation of a person 
     Attributes:
         Firstname(string)
         Lastname(String)
     """
     def __init__(self, name, last_name):
         self.firstname = first_name
         self.lastname = last_name 
     def show_full_name(self):
         return self.firstname + ' ' + self.lastname
