**HOW TO RUN**

You may have a different way of running the application if you know how, 
but the way I do is to go to the application directory in terminal and then use this command: 

createdb music_shop

run psql -d music_shop -f db/music_shop.sql

python3 -m flask run

Once it's running you can then go to http://localhost:5000/ on the browser of your choice and use the app.

**WHAT I USED TO CREATE THE APP**

HTML / CSS
Python
Flask
PostgreSQL and the psycopg

**MY BRIEF**

Shop Inventory
Build an app which allows a shopkeeper to track their shop's inventory. This is not an app which the customer will see, it is an admin/management app for the shop workers.

MVP
The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.
The inventory should track manufacturers, including a name and any other appropriate details.
The shop can sell anything you like, but you should be able to create and edit manufacturers and products separately.
This might mean that it makes more sense for a car shop to track makes and models of cars. Or a bookstore might sell books by author, or by publisher, and not by manufacturer. You are free to name classes and tables as appropriate to your project.
Show an inventory page, listing all the details for all the products in stock in a single view.
As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.

Inspired by
eBay, Amazon (back end only), Magento

Possible Extensions
Calculate the markup on items in the store, and display it in the inventory
Filter the inventory list by manufacturer. For example, provide an option to view all books in stock by a certain author.
Categorise your items. Books might be categorised by genre (crime, horror, romance...) and cars might be categorised by type (SUV, coupé, hatchback...). Provide an option to filter the inventory list by these categories.
Mark manufacturers as active/deactivated. Deactivated manufacturers will not appear when creating new products.

<img width="1440" alt="app screenshot" src="https://user-images.githubusercontent.com/57117685/142244207-8305ecdd-140a-4f1e-afb1-8801f1740386.png">

I was able to achieve all of the MVP and also most of the Extensions. The only one I did not acheive was the 'genre' extension. I had decided at the beginning that this would require a 'many to many' table set up and so did not include it. I now realise that I could have just added a category/genre column to the items table and then added more options to filter by category/genre in the web pages. I decided not to attempt this at the last minute as it was a 'nice to have' anyway and I had already acheieved every other part of the brief. I also forgot to write a test for the one class method I had (markup).
