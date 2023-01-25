import requests
from bs4 import BeautifulSoup
'''
result = requests.get("https://www.google.com/")
#print(result.status_code)
#print(result.headers)
src = result.content
#print(src)
soup = BeautifulSoup(src, features="html.parser")
links = soup.find_all("a")
#print(links)
#print("\n")
for link in links:
    if "About" in link.text:
        print(link)
        print(link.attrs['href'])

'''
#Code to retrieve urls from briefing statements
'''
result = requests.get("https://www.whitehouse.gov/briefings.statements/")
src = result.content
soup = BeautifulSoup(src, features='html.parser')
urls = []
for h2_tag in soup.findall("h2"):
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])
print(urls)
'''
'''
html_doc = " "
with open('index.html', 'w') as f:
    f.write(html_doc)
'''
url_path = 'https://www.basketball-reference.com/'
reciever = requests.get(url_path)
src = reciever.content
sp = BeautifulSoup(src, features='html.parser')
with open('nba2.html', 'w') as f:
    f.write(str(sp))
with open('nba2.html', 'rb') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
tag = soup.a.attrs['href']
print(tag)
