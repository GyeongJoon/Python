from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# pip install beautifulsoup4
# pip list
# pip install --upgrade beautifulsoup4
# pip uninstall beautifulsoup4