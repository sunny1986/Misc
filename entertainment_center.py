import media

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

print(iron_man.storyline)
iron_man.show_trailer()
