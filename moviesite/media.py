import webbrowser
import requests
import simplejson
import urllib

from configobj import ConfigObj
 
class Movie():
    def __init__(self,movie_title,trailer_youtube):

        self.title = movie_title
        self.trailer_youtube_url=trailer_youtube
        

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def get_movie_details(self):
        """
        Get movie details from rottentomatoes

        """

        #get rottentomatoes API key from config file
        config = ConfigObj("config.ini")
        key = config["api_key"]

        #uri encode the query as required by RT API
        #rottentomatoes API doc at:http://developer.rottentomatoes.com/docs
        #use simple json and loop over a python dict

        base_uri= "http://api.rottentomatoes.com/api/public/v1.0/movies.json"
        url = "%s?apikey=%s&q=%s&page_limit=1"
        url = url % (base_uri, key, self.title)
        res = requests.get(url)
        js = simplejson.loads(res.content)

        for movie in js["movies"]:
            self.rating = movie["mpaa_rating"]
            self.synopsis = movie["synopsis"]
            self.poster_image_url = movie["posters"]["original"] 

        


      
        
    
    
