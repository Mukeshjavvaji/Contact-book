# Contact-book
A **Simple contact book** web app using HTML, CSS, Jinja web template and Django framework of Python.

```Task``` - Create a Contact book directory using *Doubly linked list* with sorting, searching, deleting and adding contacts.

In the files, *Contactlist* is a Django project and *contacts* is Django web app.

The basic implementation is done using two doubly linked lists: one for storing the contacts and the other for storing the call logs.

You can find the implementation of doubly linked lists in **contacts/models.py**
In the same file you can find the *functions* for inserting(while sorting), deleting contacts, deleting logs.

I have used *linear search* assuming that there are less contacts however you can use binary search depending on the number of contacts.
The search algorithm is in **contacts/views.py**. It can search both names as well as numbers.
In *views.py* you can find functions for displaying the contacts, logs and for adding a log.

All the url patterns are added in **contacts/urls.py**.

Coming to the HTML, The main template(Home page) is **templates/phonelog.html**
Every other HTML pages will be extended after the home page.

**templates/addcontact.html** has the form to take the input for adding a new contact.
**templates/message.html** is used for displaying the messages(like no contacts found, no logs etc..)
**templates/contacts.html** is used for displaying the contacts and logs.

For designing the website, I have used *CSS* which you can find in **static/css/phonelog.css**

I have downloaded icofont for the icons. 
Link: https://icofont.com
Read the *'How to use'* section in the above link to know how to embed icons in the website.

I have used *jinja web template* for using loops, condition statements etc. in HTML.

Note: This project is done as a part of **Case study** for *Data Structures in Python*, 2nd year, CSE, B.tech.

Credits:
Mukesh Kumar Javvaji 
