#!/usr/bin/env python3

from authentication.authTools import login_pipeline, update_passwords, hash_password
from database.db import Database
from flask import Flask, render_template, request
from core.session import Sessions

app = Flask(__name__)
HOST, PORT = 'localhost', 8080
global username, products, db, sessions
username = 'default'
db = Database('database/storeRecords.db')
products = db.get_full_inventory()
sessions = Sessions()
sessions.add_new_session(username, db)



@app.route('/')
def index_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    return render_template('index.html', username=username, products=products, sessions=sessions)


@app.route('/login')
def login_page():
    """
    Renders the login page when the user is at the `/login` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('login.html')


@app.route('/home', methods=['POST'])
def login():
    """
    Renders the home page when the user is at the `/home` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds a new session to the sessions object

    """
    username = request.form['username']
    password = request.form['password']
    if login_pipeline(username, password):
        sessions.add_new_session(username, db)
        return render_template('home.html', products=products, sessions=sessions)
    else:
        print(f"Incorrect username ({username}) or password ({password}).")
        return render_template('index.html', products=products )


@app.route('/register')
def register_page():
    """
    Renders the register page when the user is at the `/register` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('register.html')


@app.route('/checkout')
def checkout():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    
    return render_template('checkout.html')



# This only works if the text boxes inputs are long enough

@app.route('/register', methods=['POST'])
def register():
    """
    Renders the index page when the user is at the `/register` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - passwords.txt: adds a new username and password combination to the file
        - database/storeRecords.db: adds a new user to the database
    """
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    salt, key = hash_password(password)
    update_passwords(username, key, salt)
    db.insert_user(username, key, email, first_name, last_name)
    return render_template('home.html', products=products, username=username)


@app.route('/personalCart', methods=['POST'])
def personalCart():
    """
    Renders the checkout page when the user is at the `/checkout` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds items to the user's cart
    """

    #creates a dictionary called order
    order = {}

    #gets session
    user_session = sessions.get_session(username)

    #runs a for loop in the products database
    for item in products:

        #this just prints all of the items in products in the terminal
        #print(f"item ID: {item['id']}")

        #this checks if the user put a value higher than one in the number box
        if request.form[str(item['id'])] > '0':

            #this gets the amount the user wants and stores it in count
            count = request.form[str(item['id'])]

            #this adds the items to the order dictionary along with the image, price and quantity
            order[item['item_name']] = {'quantity': count, 'image_url': item['image_url'], 'price': item['price']}

            #this adds it to the cart in the session
            user_session.add_new_item(
                item['id'], item['item_name'], item['price'], count)
            
    #this sends it to their cart and is part of the process of pulling up the personal cart html
    user_session.submit_cart()


    #loads the personal cart.html with all of the info
    return render_template('personalCart.html', order=order, sessions=sessions, total_cost=round(user_session.total_cost*1.0725, 2))

@app.route('/about')
def about_page():
    

    # creates a dictionary called collection
    collection = {}

    #gets session still not sure why we need it but other methods had it so we ball
    user_session = sessions.get_session(username)

    #grabs the category parameter of the image you clicked 
    firstcat = request.args.get('category')

    #checks if firstcat has a value
    if firstcat:

        #this runs through the database(products) and checks every album's category to see if it matches with the firstcat
        wanted_products = [p for p in products if p['category'] == firstcat]

        #this goes through the wantedproducts and adds its name and image to collecton the 1 adds the product with a quantity of 1
        for music in wanted_products:
            collection[music['item_name']] = {'image_url': music['image_url']}
            user_session.add_new_item(music['id'], music['item_name'], music['price'], 1)

    #this renders eveything and passes collection        
    return render_template('about.html', collection=collection)

    

if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
