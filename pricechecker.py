from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq
import requests

# Print ASCII Art
print("""
__________________________________________________________________
    ____       _           ________              __            
   / __ \_____(_)_______  / ____/ /_  ___  _____/ /_____  _____
  / /_/ / ___/ / ___/ _ \/ /   / __ \/ _ \/ ___/ //_/ _ \/ ___/
 / ____/ /  / / /__/  __/ /___/ / / /  __/ /__/ ,< /  __/ /    
/_/   /_/  /_/\___/\___/\____/_/ /_/\___/\___/_/|_|\___/_/     
__________________________________________________________________                                                               
""")

# Take user input and insert into pricerunners searchbar + extract the url
search_term = input("Search for the item that you want to find the cheapest price for: ")
new_search_term = search_term.replace(" ", "%20")

search_url = "https://www.pricerunner.dk/results?q=" + new_search_term + "&suggestionsActive=true&suggestionClicked=false&suggestionReverted=false"

# Find all the elements with the given class - might not be working (doesnt print out the right amount of elements on the given url)
# - TODO delete function printing out the amount of elements - print(len(containers))
uClient = uReq(search_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div", {"class": "_2I-CVwPXYh"})
print(len(containers))

container = containers[3]

price = containers.find("div", {"class": "_2xRnN6t_3F"})
print(price[3].text)


