# Project1: Movie site


The program reads from a list of your movies which includes the title and themovie trailer URL. This list is then served as a web page along with movie box images from rottentomatoes.com. The page also allows to watch the trailers.

Inputs: 
CSV file with movie title and youtube trailer

Output:
Webpage with list of movies in CSV, box art and trailer

RottenTomatoes API: This program gets movie related data from rottentomatoes. The API and related details at : http://developer.rottentomatoes.com/
- NOTE: The API key is stored in the config.ini file. Before running the program, one will need to update the file with their own rottentomatoes API key

Python modules required:
- simplejson : to process JSON requests (https://github.com/simplejson/simplejson)
- requests : Uses requests instead of standard urllib (http://docs.python-requests.org/en/latest/)
- ConfigObj: Uses ConfigObj for Config file reading, writing and validation


