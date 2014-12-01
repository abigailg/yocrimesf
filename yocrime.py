import requests
import urlparse
from pprint import pprint
import string

CRIME_URL = 'http://sanfrancisco.crimespotting.org/crime-data?format=json&dstart=2014-11-01&bbox='

lat_radius = 0.003621
long_radius = 0.003632

def geo_bounds_west(longitude):
	W = longitude - long_radius
	return W

def geo_bounds_south(latitude):
	S = latitude - lat_radius
	return S

def geo_bounds_east(longitude):
	E = longitude + long_radius
	return E

def geo_bounds_north(latitude):
	N = latitude + lat_radius
	return N

def geo_bounds(latitude, longitude):
	#estimated latitude and longitude based on average calculations for San Francisco
	lat_radius = 0.003621
	long_radius = 0.003632
	W = longitude - long_radius
	S = latitude - lat_radius
	E = longitude + long_radius
	N = latitude + lat_radius
	return W, S, E, N
	#latitide and longitude must be floating point

def get_crime_data(we, so, ea, no):
	bounds = "%d,%d,%d,%d" % (we, so, ea, no)
	'''I know this isn't right, but I can't quite figure out how to construct this component'''
	
	print "here are the bounds: " + bounds
	
	recent_crimes = requests.get(CRIME_URL + bounds)
	rc = recent_crimes.json()
	pprint(rc)

def crime_data_by_type(crime_type):
	'''N.B. I am having the same problem here when trying to send across the 'type' parameter'''
	rcrimes_of_type = requests.get(CRIME_URL, type=crime_type)
	rc = rcrimes_of_type.json()
	pprint(rc)
	

def main():
	lat = 37.788666
	lon = -122.411462
	
	west = geo_bounds_west(lon)
	print west
	
	south = geo_bounds_south(lat)
	print south
	
	east = geo_bounds_east(lon)
	print east
	
	north = geo_bounds_north(lat)
	print north


	get_crime_data(west, south, east, north)
	
	#ctype = 'theft'
	#crime_data_by_type(ctype)

if __name__ == '__main__':
	main()
