

#Testing the about method

#this tests the function used in the about method using a mock database and the same for loop used when it is implemented in the about method
test_products = [
        {'id': 1, 'item_name': 'Album 1', 'category': 'Rock', 'image_url': 'http://example.com/image1.jpg', 'price': 10},
        {'id': 2, 'item_name': 'Album 2', 'category': 'Pop', 'image_url': 'http://example.com/image2.jpg', 'price': 12},
        {'id': 1, 'item_name': 'Album 4', 'category': 'Rock', 'image_url': 'http://example.com/image4.jpg', 'price': 10},
        {'id': 1, 'item_name': 'Album 5', 'category': 'Rock', 'image_url': 'http://example.com/image5.jpg', 'price': 10},
        {'id': 1, 'item_name': 'Album 6', 'category': 'Rock', 'image_url': 'http://example.com/image6.jpg', 'price': 10},
        {'id': 3, 'item_name': 'Album 3', 'category': 'Jazz', 'image_url': 'http://example.com/image3.jpg', 'price': 15},
    ]

wanted_products = [p for p in test_products if p['category'] == 'Rock'] 
rock_products = []
rock_url = []


for p in wanted_products:
    rock_url.append(p['image_url'])

for p in wanted_products: 
    rock_products.append(p['item_name'])

print(rock_products, rock_url)


#Testing the personal cart method 

#this tests the function used in the personalCart method using a mock database and the for loop used to add items in the cart 

wanted_music = input("What genre do you want to add to the cart? ")

test_products2 = [
        {'id': 1, 'item_name': 'Album 1', 'category': 'Rock', 'image_url': 'http://example.com/image1.jpg', 'price': 10},
        {'id': 2, 'item_name': 'Album 2', 'category': 'Pop', 'image_url': 'http://example.com/image2.jpg', 'price': 12},
        {'id': 1, 'item_name': 'Album 3', 'category': 'Rock', 'image_url': 'http://example.com/image3.jpg', 'price': 10},
        {'id': 1, 'item_name': 'Album 4', 'category': 'Rock', 'image_url': 'http://example.com/image4.jpg', 'price': 10},
        {'id': 1, 'item_name': 'Album 5', 'category': 'Rock', 'image_url': 'http://example.com/image5.jpg', 'price': 10},
        {'id': 3, 'item_name': 'Album 6', 'category': 'Jazz', 'image_url': 'http://example.com/image6.jpg', 'price': 15},
    ]

userCartName = []
price = 0
userCartUrl = []

personal_cart = [p for p in test_products2 if p['category'] == wanted_music ]

for p in personal_cart:
    userCartName.append(p['item_name'])

for p in personal_cart:
    price += p['price']

for p in personal_cart:
    userCartUrl.append(p['image_url'])


print("")
print("")
print("Here is your mock cart")
print("Here are all the names of the album you purchased under the rock category ")
print( userCartName)
print("Here is the total price calculated for the purchase" )
print(price)
print ("And here we would display the image but instead here are some mock urls ")
print(userCartUrl)