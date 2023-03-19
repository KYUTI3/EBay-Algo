import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

input = input("What are you looking for? ")
url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2499334.m570.l1313&_nkw=" + input + "&_sacat=80053"
response = requests.get(url)
content = response.content

'''
def get_data(url):
  r = requests.get(url);
  soup = BeautifulSoup(r.text, 'html.parser')
  return soup
def parse(soup):
  results = soup.find_all('div', {'class':'s-item__info clearfix'})
  productslist = []
  for item in results:
    products = {
      'title':item.find('span', {'role':'heading'}).text, 
      'price':item.find('span', {'class':'s-item__price'}).text.replace('$','').replace(',','').strip(),
      'condition':item.find('span',{'class':'SECONDARY_INFO'}).text,
      'link':item.find('a', {'class':'s-item__link'})['href'],
    }
    productslist.append(products)
    return productslist


def output(productslist):
  productsdf = pd.DataFrame(productslist)
  productsdf.to_csv('')
   
  
soup = get_data(url)
parse(soup)
'''

soup = BeautifulSoup(content, 'html.parser')
prices = []
x = [1, 2, 3, 4, 5]
for price in soup.find_all('span', {'class': 'notranslate'}):
    prices.append(float(price.text.replace('$', '').replace(',', '')))

print(prices)
plt.plot(prices)
plt.title('Price History')
plt.xlabel('Time')
plt.ylabel('Price')
plt.show()
