from haversine import haversine
import geocoder
import cloudscraper

# Make a request to the ISS position API and get the current position
req = cloudscraper.create_scraper().get("http://api.open-notify.org/iss-now.json").json()["iss_position"]

# Coordinates of the first location
lat1 = float(req["latitude"])
lon1 = float(req["longitude"])

# Coordinates of the second location
g = geocoder.ip("me")
lat2 = g.latlng[0]
lon2 = g.latlng[1]

# Calculate the distance in miles
distance_in_miles = haversine((lat1, lon1), (lat2, lon2)) * 0.621371

print(f"The distance is {distance_in_miles:.2f} miles.")
