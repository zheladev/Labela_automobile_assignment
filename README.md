# Stuff 


Preface
-------

    I'm pretty new to MVC, and it doesn't help Pyramid gives the developer a lot of freedom with the way the project can be structured. 
    I'm a bit lost on that regard, so I have tried my best to keep some kind of sense as to where every part of the logic resides.
    Taking that into account:
        -ModelRepository classes deal with the connection between the database and the program logic. 
        -ModelService classes act as intermediary between the Repository andthe frontend (except CartService, which I didn't really know where to put within the project's structure).
        -ModelSchema classes deal with serialization of SQLAlchemy classes using marshmallow_sqlalchemy library.
        -ModelView classes control the actions which are done on each different view, based on the routes set up in label_automobile/routes.py
        -There's a couple of routes set up, along with very basic views with show some JSON data, which will be explained later on in this document.


Python library dependencies added:
---------------------------------

    -marshmallow_sqlalchemy: Used to serialize sqlalchemy models


Added to the project's structure
--------------------------------

    label_automobile
        ├ models
        │   ├ part.py           : model representing a car part
        │   ├ order.py          : model representing an order made by an user
        │   ├ order_line.py     : a single order line to represent a many to many relationship between order and part tables
        │
        ├ repositories
        │   ├ order.py          : contains OrderRepository, which connects with the database via sqlalchemy and returns sets of results (from what I understood)
        │   ├ part.py           : same as above, but with parts
        │
        ├ schemas           : marshmallow schemas for serialization reside here
        │   ├ part.py           : contains PartSchema, which serializes Part objects
        │   ├ user.py           : contains UserSchema, which serializes User objects
        │
        ├ services
        │   ├ cart.py           : contains CartService, which is a collection of utilites used to manage the cart (which by the way, I'm unsure whether this file should reside here or not)
        │   ├ order.py          : contains OrderService, which  manages OrderRepository, returning serialized strings ready to be processed
        │   ├ part.py           : same as above with parts
        │
        ├ views            : Added some view controllers to test some services
        │   ├ cart.py           : Contains actions related to managing the cart
        │   ├ site.py           : Contains a really simple view for the site root, so it doesn't throw a 404
        │   ├ part.py           : Contains actions related to showing parts (every part, only one part based on its vendor_id attribute)


Views
-----

    routes dispatched:
        /part           Returns every part in the database.
        /part/detail    Shows details of a single part, based on vid (*v*endor_*id*) GET param. usage: /part/detail?vid=<vendor_id_of_item_to_be_shown>
        /part/add       Adds a test item to the database to check PartService add method works
        /part/delete    Deletes test item added with /part/add to check PartService remove method works

        /cart/add       Adds part to the cart based on vid GET param. usage: /cart/add?vid=<vendor_id_of_item_to_be_added>
        cart/delete     Deletes part from the cart based on vid GET param. same usage as add, just with a different route.
        cart/order      Calls order method from CartService, which is not functional, sadly, but in theory should create an order and commit it to the database
        cart/empty      Empties the cart.


TODO
----

    Order creation currently does not work, table relationships have not been properly established in the model.
    User data serialization with UserSchema, as I've only done that with Part.
    Probably a lot of stuff that has gone over my head and I could make better.

