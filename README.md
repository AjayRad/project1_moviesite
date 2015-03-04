# Project1: Movie site

### About 
This simple python script reads from a list of movies from a CSV file.This list is then served as a web page along with movie box images  and trailers.

Inputs: 
CSV file with movie title and youtube trailer; movie details from rottentomatoes.

Output:
Webpage with list of movies in CSV, box art and trailer

### Details 

RottenTomatoes API: This program gets movie related data from rottentomatoes. The API and related details at : http://developer.rottentomatoes.com/
- NOTE: The API key is stored in the config.ini file. Before running the program, one will need to update the file with their own rottentomatoes API key

Python modules required to run this program :
- simplejson : to process JSON requests (https://github.com/simplejson/simplejson)
- requests : Uses requests instead of standard urllib (http://docs.python-requests.org/en/latest/)
- ConfigObj: Uses ConfigObj for Config file reading, writing and validation


