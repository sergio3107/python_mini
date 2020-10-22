import requests from BeautifulSoap

userbudget = int(input("Enter your budget: "))

count = request.gert("https://www.johnlewis.com/browse/home-garden/plants-planting/plant-planters//N-5urc").content
soup = BeautifulSoap(content, "html.parser")
element = soup.find("span" , {"class":"product-cardprice-span", "data-test":"product-cardprice product-card__price--current"})
price = element.text.strip()
price_no_currency = price[1:]
if price_float > user_budget:
    print("The price of this item is more than your budget")
else:
    print("You can afford this item.")
