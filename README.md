# Logs Analysis Project

### Aim of this project

This project analyzes the data of a newspaper database according to different criteria. 
A Python code with built-in sql statements accesses the database and returns the results of the individual queries as text.

### How to run it

The following components are required for this project:
- Virtual Box
- Vagrant
- Python 3

### Setup

1. Install Virtual Box / you can download the virtual machine [here](https://www.virtualbox.org/wiki/Downloads)
2. Install Vagrant and `vagrant up` / you can download vagrant [here](https://www.vagrantup.com/downloads.html)
3. Clone this repository

### First steps after install

1. Download the newsdata.sql [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
1. Start vagrant with `vagrant ssh`
2. Load the data with `psql -d news -f newsdata.sql` to connect a database and run the necessary SQL statements
3. Run news.py with python3

# Contents of the database

- Authors table
- Articles table
- Log table

