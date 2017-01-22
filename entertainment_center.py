import media
import movie_shoovie

# create an instance for movie - sherlock holmes
sherlock_holmes = media.Movie("Sherlock Holmes",
                              "Based on Sir Arthur Conan Doyle's work this is about a fictional private detective",
                              "https://en.wikipedia.org/wiki/Sherlock_Holmes_(2009_film)#/media/File:Sherlock_holmes_ver5.jpg",
                              "https://www.youtube.com/watch?v=iKUzhzustok")
								
#print(sherlock_holmes.storyline)

# create an instance for movie - iron man
iron_man = media.Movie("Iron Man",
                       "Superhero movie in which a genius billionaire creates an exoskeleton and becomes a technologically advanced superhero",
                       "https://en.wikipedia.org/wiki/Iron_Man_(2008_film)#/media/File:Ironmanposter.JPG",
                       "https://www.youtube.com/watch?v=tbMG2yTDXSY")

# create an instance for movie - the martian
the_martian = media.Movie("The Martian",
                       "Movie about an astronaut who is left behind on Mars by his crew while on a mission",
                       "https://en.wikipedia.org/wiki/The_Martian_(film)#/media/File:The_Martian_film_poster.jpg",
                       "https://www.youtube.com/watch?v=2p7bgMxewxA")

# create an instance for movie - catch me if you can
catch_me_if_you_can = media.Movie("Catch Me If You Can",
                       "A true story about a conman who swindles millions of dollars before turning 19 faking as a pilot, doctor and prosecutor",
                       "https://en.wikipedia.org/wiki/Catch_Me_If_You_Can#/media/File:Catch_Me_If_You_Can_2002_movie.jpg",
                       "https://www.youtube.com/watch?v=71rDQ7z4eFg")

					   
#print(iron_man.storyline)
#iron_man.show_trailer()

# create a list of movies to pass it to the open_movies_page function
list_of_movies = [sherlock_holmes,iron_man,the_martian,catch_me_if_you_can]

# open the webpage
movie_shoovie.open_movies_page(list_of_movies)



