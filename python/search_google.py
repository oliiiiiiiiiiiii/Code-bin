from webbrowser import open #we only need the open() function so we will just import the open function from the std python lib

query = input("Enter Your Query: ") #here enter what your query is

open(f"https://www.google.com/search?q={query}") #lets now search our query on google

'''You will need python version 3.6 or above because f strings were introduced in python 3.6'''
