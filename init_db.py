# init_db.py
# Programmer: Adelita Martinez
# Email: amartinez1013@cnm.edu
# Purpose: Create and initialize the database with points
# Python Version: 3.12.3

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('geopoints.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS points (
               id INTEGER PRIMARY KEY,
               latitude REAL,
               longitude REAL,
               description TEXT
)
''')

# Insert points
points = [
  (32.341906, -106.758862, 'Las Cruces'),
  (36.884615, -104.439862, 'Raton'),
  (35.171950, -103.724588, 'Tucumcari'),
  (35.528541, -108.758155, 'Gallup'),
  (35.105925, -106.628423, 'Albuquerque')
]

cursor.executemany('''
INSERT INTO points (latitude, longitude, description)
VALUES (?, ?, ?)
''', points)

# Commit and close connection
conn.commit()
conn.close()