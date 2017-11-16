import webbrowser

# structure data about a movie
class Movie():
	"""Class to store information about a movie"""
	
	# constructor to save information on a movie
	def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_youtube_url):
                self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = movie_poster_image
		self.trailer_youtube_url = movie_youtube_url
	
	
    # method to show trailer via url
	def show_trailer(self):
                webbrowser.open(self.trailer_youtube_url)
