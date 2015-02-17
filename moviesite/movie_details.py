import media
import fresh_tomatoes
import csv


movie_list=[]

#open csv file with movie title and youtube url
#build movie list to be passed to fresh tomatoes open_movie_pge func

try:
    with open('my_movie_list.csv', 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            movie = media.Movie(row[0], row[1])
            movie.get_movie_details()
            movie_list.append(movie)

except Exception, e:
    print "Encountered error " + str(e) + " while attempting to process input csv file. check inputs, please. Exiting...."

else:
    fresh_tomatoes.open_movies_page(movie_list)

