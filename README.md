# Item Catalog
The requirements for the project:
To develop a catalog web application that displays a list of items within a variety of categories
and integrate third party user registration and authentication. Only authenticated users are able 
to post, edit and delete their own items. The application should provide API endpoints.
No templates were included. The project was made from scratch.

Extra features:
- The app has anti forgery request implemented with a state token.
- The app has CRUD functionality for image handling.

About my project:
A web application called THE CAT LOVERS where Cat Lovers can share pictures of their cats in 
own lists.

The project runs inside a Virtual Machine with Vagrant.

**_This is the fifth project submission for Udacity Full Stack Web Developer Nanodegree Program._**

## Installation
In order to run and make changes to this project, you'll need:
- [Python](https://www.python.org/)
- [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](http://www.vagrantup.com/downloads.html) is optional

## Usage
To run this project directly from Vagrant make sure you have both Virtual Box and Vagrant 
installed. Also download this project to your local machine.

**First of all, open the terminal**

1. Start the Virtual Machine:
- `cd project/vagrant` to get inside Vagrant project machine directory
- `vagrant up` to start Vagrant
- `vagrant ssh` to start Ubuntu Machine
- `cd /vagrant/catalog` to get inside project directory

2. Run files in order:
- `python models.py` to create the database
- `python database_populate.py` to populate database with initial data
- `python views.py` to initiate the webapp server.

3. You can view the application in your browser at: http://localhost:8000

That's it! You can now sign in and create your own list!

## Files
The files of the project are all inside the **catalog folder**. 
The other files are for the vagrant and virtual machine. 

Understanding the project files:

`/catalog`: the project directory

	`/static`: directory with bootstrap files, favicon icon and the project sylesheet.

	`/templates`: directory with all HTML templates. The frontend code for the application.
		`404.html`: template for 404 error page.
		`category.html`: template for all single category pages.
		`index.html`: template for homepage.
		`item.html`: template for all single item pages.
		`item_delete.html`: template page with form to delete an item.
		`item_edit.html`: template page with form to edit an item.
		`item_new.html`: template page with form to create a new item.
		`layout.html`: main template layout for all the pages.
		`list.html`: template page for a user's list.
		`list_delete.html`: confirmation template page for deleting a user's list.
		`login.html`: template for login page.

	`/uploads`: directory for all the images uploaded.

	`client_secrets_fb.json`: the client secrets for Facebook OAuth login.
	`client_secrets_gplus.json`: the client secrets for Google OAuth login.
	`database_populate.py`: initial data to database.
	`models.py`: define and create database.
	`views.py`: the backend code of the web application. 


## Built With
- [Python](https://www.python.org/)
- [SQLAlchemy](http://www.sqlalchemy.org/)
- [Flask](http://flask.pocoo.org/)
- [Bootstrap](http://getbootstrap.com/)
- [Google Fonts](https://fonts.google.com/)
- [Google+ OAuth2 API](https://developers.google.com/identity/protocols/OAuth2)
- [Facebook OAuth API](https://developers.facebook.com/)
- [Vagrant](http://www.vagrantup.com/downloads.html)
- [Virtual Box](https://www.virtualbox.org/wiki/Downloads)