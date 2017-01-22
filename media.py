########################################################################################
# Description: 
# Define a class for displaying movie details and launching trailers embedded in the webpage
# 
# Steps:
# 1. Create a constructor for the data associated with movies
# 2. Create a method for  
#
#
#
#
########################################################################################
import webbrowser

# structure data about a movie
class Movie():
	#1
	
	def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_youtube_url):
                self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = movie_poster_image
		self.trailer_youtube_url = movie_youtube_url
	
	#2
        # method to show trailer via url
	def show_trailer(self):
                webbrowser.open(self.trailer_youtube_url)
