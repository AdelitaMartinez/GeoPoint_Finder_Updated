# GeoPoint Finder

## Overview
The **GeoPoint Finder** is a desktop application that allows users to find the closest geographical point from a set of predefined locations based on their input latitude and longitude. The app uses a graphical interface built with Tkinter and retrieves points from an SQLite database, ensuring data persistence.

## Features
- **Closest Location Finder**: Input latitude and longitude to find the nearest location from a database of geographical points.
- **User-Friendly Interface**: Simple and intuitive GUI using Tkinter, with fields for latitude and longitude and a display area for results.
- **Data Persistence**: Locations are stored in an SQLite database (`geopoints.db`), allowing easy access and modification of the dataset.
- **Distance Calculation**: Uses the Haversine formula to calculate the distance between user input and each point in the database.

## Installation
### Requirements:
- Python 3.12.3 or higher.

### Dependencies:
- No additional dependencies are required beyond the standard Python libraries (`tkinter`, `sqlite3`, `math`).

## Usage
1. **Database Initialization**:
   - Run `init_db.py` to initialize the SQLite database and populate it with default geographical points.

2. **Running the Application**:
   - Run `main.py` to launch the GeoPoint Finder application.

3. **Finding the Closest Location**:
   - Enter the latitude and longitude in the respective fields.
   - Click **Find Closest Location** to display the nearest location from the database.

## Files Included
- **main.py**: The main application file that creates the GUI, handles user input, and finds the closest location.
- **GeoPoint.py**: Contains the `GeoPoint` class, which defines geographical points and provides distance calculation functionality.
- **init_db.py**: Initializes the database (`geopoints.db`) and populates it with a list of sample geographical points.

The database (`geopoints.db`) will be automatically created if it doesn’t already exist, storing data persistently.

## Credits
- **Programmer**: [Adelita Martinez](https://www.linkedin.com/in/adelitamartinez/)
- **Email**: 94martinez.adelita@gmail.com

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
