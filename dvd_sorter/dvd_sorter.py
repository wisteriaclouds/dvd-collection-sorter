import random

# welcome user and print options
# add all elements of chosen genre list to [genre] set
# add all elements of chosen runtime list to [runtime] set
# find intersection between genre and runtime sets - WORKS
# add to new [choices] set - WORKS
# print random choice from [choices] set - WORKS

# genres
adventure = ["A Bug's Life", "Finding Nemo", "LOTR: Fellowship of the Ring", "LOTR: Two Towers", "LOTR: Return of the King",
       "Moana", "Mr Peabody and Sherman", "Muppets Wizard of Oz", "Toy Story", "Toy Story 2", "Toy Story 3"]
animated = ["Big Hero 6", "A Bug's Life", "Finding Nemo", "The Incredibles", "Incredibles 2", "Inside Out",
"Kung Fu Panda", "Kung Fu Panda 2", "The Lego Movie", "The Lego Movie 2", "The Little Mermaid", "Moana",
"Monsters Inc.", "Mr Peabody and Sherman", "Spider-Man: Into The Spider-Verse", "Tangled", "Toy Story",
"Toy Story 2", "Toy Story 3", "Zootopia"]
comedy = ["Hotel for Dogs", "Inside Out", "Kung Fu Panda", "Kung Fu Panda 2", "The Lego Movie", "Mean Girls", "Scooby-Doo",
       "Scooby-Doo 2", "Spider-Man: Homecoming", "Zootopia"]
drama = ["Contagion", "La La Land", "Little Women"]
fantasy = ["The Little Mermaid", "LOTR: Fellowship of the Ring", "LOTR: Two Towers", "LOTR: Return of the King", "Moana", "Muppets Wizard of Oz",
       "Scooby-Doo", "Scooby-Doo 2", "Tangled", "Toy Story", "Toy Story 2", "Toy Story 3"]
musical = ["La La Land", "The Little Mermaid", "Moana", "Muppets Wizard of Oz", "Tangled"]
scifi = ["The Lego Movie 2"]
superhero = ["Big Hero 6", "The Incredibles", "Incredibles 2", "Spider-Man: Homecoming", "Spider-Man: Into The Spider-Verse"]

# runtimes
under_90 = ["The Little Mermaid", "Scooby-Doo", "Toy Story"]
greater_equal_90 = ["Kung Fu Panda", "Kung Fu Panda 2", "Toy Story 2", "Monsters Inc.", "Mr Peabody and Sherman", "Scooby-Doo 2",
                    "A Bug's Life", "Inside Out", "Mean Girls", "Finding Nemo", "Muppets Wizard of Oz", "Hotel for Dogs", "Tangled", "The Lego Movie",
                    "Toy Story 3", "Big Hero 6", "Contagion", "Moana", "The Lego Movie 2", "Zootopia", "The Incredibles", "Spider-Man: Into The Spider-Verse",
                    "Incredibles 2"]
greater_equal_120 = ["La La Land", "Little Women", "LOTR: Fellowship of the Ring", "LOTR: Two Towers", "Spider-Man: Homecoming"] # greater than or equal to 120 mins
greater_equal_180 = ["LOTR: Return of the King"]

genre = set() # genre set
runtime = set() # runtime set

print("Welcome to the DVD collection sorter! \nGenres: \nadventure, animated, comedy, drama, fantasy, musical, scifi, superhero \nRuntimes: \nunder_90, greater_equal_90, greater_equal_120, greater_equal_180")

dvd1 = input("Which genre would you like to watch? ")
dvd2 = input("How long do you want your dvd to be (in minutes)? ")

# chosing genre - refactor this later 
if dvd1 == "adventure":
    genre.update(adventure)
elif dvd1 == "animated":
    genre.update(animated)
elif dvd1 == "comedy":
    genre.update(comedy)
elif dvd1 == "drama":
    genre.update(drama)
elif dvd1 == "fantasy":
    genre.update(fantasy)
elif dvd1 == "musical":
    genre.update(musical)
elif dvd1 == "scifi":
    genre.update(scifi)
elif dvd1 == "superhero":
    genre.update(superhero)

# chosing runtime - refactor this later
if dvd2 == "under_90":
    runtime.update(under_90)
elif dvd2 == "greater_equal_90":
    runtime.update(greater_equal_90)
elif dvd2 == "greater_equal_120":
    runtime.update(greater_equal_120)
elif dvd2 == "greater_equal_180":
    runtime.update(greater_equal_180)

# print random intersection between genre and runtime
res = list(filter(lambda x: x in runtime, genre))
if res == []:
    print("Sorry, there isn't a DVD in that genre that's also your chosen length.")
else:
    print(random.choice(res))

input("Press Enter to exit...")