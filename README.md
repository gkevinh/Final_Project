# Ono Sweets

### Ono Sweets is a fullstack web application designed for helping users find desserts on the islands of Hawaii.  Integration of the Yelp API allows users to search for dessert venues by zip-code or city. The Google Maps API then dynamically displays directions from the user's location to the dessert venue. The app also allows the user to save their favorite venues in their profile so they can reference them at a later time.  While focused  on Hawaii and it's desserts, the user also has the capability to search for desserts in any location worldwide. Aloha! 

### **Technologies**

-SQL / PostgreSQL / SQLAlchemy

-Python

-Flask

-Jinja

-Javascript 

-AJAX

-Bootstrap

-HTML/CSS

-Sweet Alert

-Font Awesome

-[Yelp API](https://docs.developer.yelp.com/docs/fusion-intro)

-[Google Maps API](https://developers.google.com/maps/documentation)


![example-1](static/img/search-example.jpeg)
![example-2](static/img/results-example.jpeg)
![example-3](static/img/venue-example.jpeg)


**INSTALLATION:**

To have this app running on your local computer, please follow the below steps:

CLONE REPOSITORY:


$ git clone https://github.com/gkevinh/Final_Project


CREATE AND ACTIVATE A VIRTUAL ENVIRONMENT:


   $ pip3 install virtualenv  
   $ virtualenv env  
   $ source env/bin/activate  


INSTALL DEPENDENCIES:


(env) $ pip3 install -r requirements.txt


CREATE DATABASE:


(env) $ createdb test_db


CREATE DATABASE TABLES:


  (env) $ python3 -i model.py  
  db.create_all()  


START BACKEND SERVER:


(env) $ python3 server.py