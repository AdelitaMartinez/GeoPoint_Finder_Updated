# init_db.py
# Programmer: Adelita Martinez
# Email: amartinez1013@cnm.edu
# Purpose: Create and initialize the database with points
# Python Version: 3.12.3

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('geopoints.db')
cursor = conn.cursor()