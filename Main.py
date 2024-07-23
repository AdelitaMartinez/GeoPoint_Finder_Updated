# main.py
# Programmer: Adelita Martinez
# Email: amartinez1013@cnm.edu
# Purpose: Demonstrate how to use a GUI and read points from a database
# Python Version: 3.12.3

import tkinter as tk
from tkinter import messagebox
from GeoPoint import GeoPoint
import sqlite3

class GeoPointApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GeoPoint Finder")

        # Labels and Entry boxes for latitude and longitude
        tk.Label(self.root, text="Enter Latitude:").grid(row=0, column=0, padx=10, pady=5)
        self.lat_entry = tk.Entry(self.root)
        self.lat_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Enter Longitude:").grid(row=1, column=0, padx=10, pady=5)
        self.lon_entry = tk.Entry(self.root)
        self.lon_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Closest Location:").grid(row=2, column=0, padx=10, pady=5)
        self.closest_location_text = tk.Text(self.root, height=5, width=50)
        self.closest_location_text.grid(row=2, column=1, padx=10, pady=5)

        # Button
        self.find_button = tk.Button(self.root, text="Find Closest Location", command=self.find_closest_location)
        self.find_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def find_closest_location(self):
        try:
            # Get user input
            lat = float(self.lat_entry.get().strip())
            lon = float(self.lon_entry.get().strip())

            # Read points from the database
            points = self.read_points_from_db()

            # Create user GeoPoint
            user_point = GeoPoint(lat, lon, "User Location")

            # Find closest point
            closest_point = self.find_closest_point(user_point, points)

            # Display closest location in text box
            if closest_point:
                self.closest_location_text.delete('1.0', tk.END)
                self.closest_location_text.insert(tk.END, f"You are closest to {closest_point.Description} which is located at {closest_point.Point}")
            else:
                messagebox.showinfo("No Points Found", "No points found in the database.")

        except ValueError:
            messagebox.showerror("Error", "Invalid coordinates input. Please enter valid coordinates.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def read_points_from_db(self):
        # Read points from the database and return a list of GeoPoint objects
        point_list = []
        conn = sqlite3.connect('geopoints.db')
        cursor = conn.cursor()
        cursor.execute("SELECT latitude, longitude, description FROM points")
        rows = cursor.fetchall()
        for row in rows:
            lat, lon, description = row
            point = GeoPoint(lat, lon, description)
            point_list.append(point)
        conn.close()
        return point_list

    def find_closest_point(self, user_point, point_list):
        # Find the closest GeoPoint to the user's input location
        closest_point = None
        min_distance = float('inf')
        for point in point_list:
            distance = user_point.Distance(point.GetPoint())
            if distance < min_distance:
                min_distance = distance
                closest_point = point
        return closest_point

if __name__ == "__main__":
    root = tk.Tk()
    app = GeoPointApp(root)
    root.mainloop()
