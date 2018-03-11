# Aim of this project

This project analyzes the data of a newspaper database according to different criteria. 
A Python code with built-in sql statements accesses the database and returns the results of the individual queries as text.

# How to run it

The following components are required for this project:
- Virtual Box
- Vagrant
- Python 3

### Setup

1. Install Virtual Box
2. Install Vagrant and `vagrant up`
3. Clone this repository

### First steps after install

1. Start vagrant with `vagrant ssh`
2. Load the data with `psql -d news -f newsdata.sql` to connect a database and run the necessary SQL statements
3. Run news.py with python3

# Contents of the database

- Authors table
- Articles table
- Log table

