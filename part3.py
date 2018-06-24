'''
Hope Tambala
25677464
'''
# these should be the only imports you need

import requests
from bs4 import BeautifulSoup

# write your code here
# usage should be python3 part3.py

# http://www.pythonforbeginners.com/requests/using-requests-in-python

url = 'https://www.michigandaily.com/'
page = requests.get(url)

# print the first 500 characters of the HTML
#print(r.text[0:500]) 
#print(page.text)

'''
run the page.text document through the module to give us a BeautifulSoup object 
Create parse tree from this parsed page with html.parser over the HTML. 
The constructed object represents the index.html document as a nested data structure. 
Assigned to the variable soup.
'''
soup = BeautifulSoup(page.text, 'html.parser')

#Prints soup output
#print(soup.prettify())

#Prints all 'div' objects
#print(soup.find_all('div'))

#Prints all elements in 'view-most-read' class
#print(soup.find_all(class_='view-most-read'))

#Combination
#print(soup.find_all("div", {'class':'view-most-read'}))



most_read_content = soup.find_all("div", {'class':'view-most-read'})



for athing in most_read_content:
    print('Michigan Daily -- MOST READ ' + athing.text)
