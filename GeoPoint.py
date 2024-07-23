# GeoPoint.py
# Programmer: Adelita Martinez
# Email: amartinez1013@cnm.edu
# Purpose: Define the GeoPoint class for geographic point representation and distance calculation
# Python Version: 3.12.3

import math

class GeoPoint:
    def __init__(self, lat=0, lon=0, description='TBD'):
        self.__lat = lat
        self.__lon = lon
        self.__description = description

    # Set method to set the point coordinates (Latitude and Longitude)
    def SetPoint(self, coords):
        self.__lat = coords[0]
        self.__lon = coords[1]

    # Get method to get the point coordinates (lat and lon)
    def GetPoint(self):
        return (self.__lat, self.__lon)

    # Set method to set description
    def SetDescription(self, description):
        self.__description = description

    # Get method to get description
    def GetDescription(self):
        return self.__description

    # Calculate the distance between two points
    def Distance(self, toPoint):
        # Radius of the earth in KM
        R = 6371.0 

        # Convert lat and lon from degrees to radians
        lat1 = math.radians(self.__lat)
        lon1 = math.radians(self.__lon)
        lat2 = math.radians(toPoint[0])
        lon2 = math.radians(toPoint[1])

        # Calculate differences between lat and lon
        dlon = lon2 - lon1
        dlat = lat2 - lat1

        # Haversine formula
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        # Calculate distance
        distance = R * c
        return distance 

    # Properties to access private attributes using get and set methods
    Point = property(GetPoint, SetPoint)
    Description = property(GetDescription, SetDescription)
