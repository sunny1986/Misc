import webbrowser

# structure data about a movie
class Movie():
	def __init__(self, movie_title, movie_storyline, movie_poster_image, movie_youtube_url):
                self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image = movie_poster_image
		self.trailer = movie_youtube_url

        # method to show trailer via url
	def show_trailer(self):
                webbrowser.open(self.trailer)
