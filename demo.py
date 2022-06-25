from urllib.request import urlopen
# install beautifulsoup - html parser
from bs4 import BeautifulSoup

# Display the html content of webpage or website source code
html = urlopen('https://www.youtube.com/')
bsobject = BeautifulSoup(html.read(), 'html.parser')
print(bsobject.title)
