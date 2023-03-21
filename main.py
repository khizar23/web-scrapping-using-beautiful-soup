# step 0: install all the requirements 
# pip install requests
# pip install html5lib
# pip install bs4
import requests 
from bs4 import BeautifulSoup
url = "https://codewithharry.com/"
#step 1:get the html
r = requests.get(url)
htmlContent = r.content
print(htmlContent)

#step 2:parse the html
soup = BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)

#step 3: traverse the html
#commonly used bjects
#1. tag print(type(title))
#2.navigable string print(type(title.string))
#3. BeautifulSoup print(type(soup))
# 4. comment
markup = "<p><!-- this is a comment--></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))

# get the title of html page
title = soup.title

# get the paragraphs from the page
paras = soup.find_all('p')
print(paras)


# get the first element of the html page
print(soup.find('p')

# get classes of any element in html page 
print(soup.find('p')['class'])

# find all the elements with class lead
print(soup.find("p",class_="lead"))

# get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

# get the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()
print(anchors)

# get all the link on the page
for link in anchors:
    if (link.get('href')!= '#'):
        link_text = "https://codewithharry.com/" + link.get('href')
        all_links.add(link)
        print(link_text)
contents - A tags children are available as list
contents - A tags children are available as generator
imgpreview2 = soup.find(id='imgpreview2')
for elem in imgpreview2.contents:
    print(elem)

for item in imgpreview2.stripped_strings:
    print(item)

print(imgpreview2.parent)

for item in imgpreview2.parents:
    print(item.name)

print(imgpreview2.next_sibling.next_sibling)
element = soup.select('Modal~footer')
print(element)