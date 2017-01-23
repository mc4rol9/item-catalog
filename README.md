# Tournament Results
The goal of this project was to write a Python module using the PostgreSQL database to keep track of players and matches in a game tournament that uses the Swiss Pairings System in each round. That means that players are not eliminated and each player should be paired with another player with the same number of wins, or as close as possible.

I defined the database schema and wrote the code to use it inside the project template that was given.

The project runs inside a Virtual Machine with Vagrant.

**_This is the fourth project submission for Udacity Full Stack Web Developer Nanodegree Program._**

## Installation
In order to run and make changes to this project, you'll need:
- [Python](https://www.python.org/)
- [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](http://www.vagrantup.com/downloads.html)

## Usage
To run this project, make sure you have both Virtual Box and Vagrant installed on your machine.
Also download this project to your local machine.

**First of all, open the terminal**

1. Start the Virtual Machine:
- `cd project/vagrant` to get inside Vagrant project machine directory
- `vagrant up` to start Vagrant
- `vagrant ssh` to start Ubuntu Machine
- `cd /vagrant/tournament` to get inside project directory

2. Create the database for the project:
- `psql` to start PostgreSQL
- `create database tournament;` to create a database for the project
- `\c tournament` to connect to the project database
- `\i tournament.sql` to run the sql script that creates all the tables and views
- `\d` to see the elements creates

3. Run the python script for testing:
- `\q` to exit PostgreSQL
- `python tournament_test.py` to run the script

Use the command `psql tournament` to connect directly to the database again.

## Files
The files of the project are all inside the **tournament folder**. The other files are for the 
vagrant and virtual machine. 

Understanding the project files:

`tournament.py`
This is the database module. 

`tournament.sql`
This is the database schema with SQL commands. The script to create the database.

`tournament_test.py`
This is the test module. It contains all the functions to test the database module.


## Built With
- [Python](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Vagrant](http://www.vagrantup.com/downloads.html)
- [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
