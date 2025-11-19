"""# assigning genres
ani = animated 
adv = adventure
com = comedy
dra = drama
fan = fantasy
mus = musical
sci = sci_fi
sup = superhero
tv = TV """

import random

dvd = ["Big Hero 6", "A Bug's Life", "Finding Nemo", "Hotel for Dogs", "The Incredibles", "Incredibles 2", "Inside Out", "Kung Fu Panda", "Kung Fu Panda 2", "La La Land",
        "The Lego Movie", "The Lego Movie 2", "The Little Mermaid", "Little Women", "LOTR: Fellowship of the Ring", "LOTR: Two Towers", "LOTR: Return of the King", "Mean Girls", "Moana", "Monsters Inc.", "Mr Peabody and Sherman",
        "Muppets Wizard of Oz", "Scooby-Doo", "Scooby-Doo 2", "Spider-Man: Homecoming", "Spider-Man: Into The Spider-Verse", "Tangled", "Toy Story", "Toy Story 2", "Toy Story 3", "Zootopia"]

# genre list
ani = ["Big Hero 6", "A Bug's Life", "Finding Nemo", "The Incredibles", "Incredibles 2", "Inside Out", "Kung Fu Panda", "Kung Fu Panda 2",
       "The Lego Movie", "The Lego Movie 2", "The Little Mermaid", "Moana", "Monsters Inc.", "Mr Peabody and Sherman"
       , "Spider-Man: Into The Spider-Verse", "Tangled", "Toy Story", "Toy Story 2", "Toy Story 3", "Zootopia"] # animated 
adv = ["A Bug's Life", "Finding Nemo", "LOTR: Fellowship of the Ring", "LOTR: Two Towers", "LOTR: Return of the King",
       "Moana", "Mr Peabody and Sherman", "Muppets Wizard of Oz", "Toy Story", "Toy Story 2", "Toy Story 3"] # adventure
com = ["Hotel for Dogs", "Inside Out", "Kung Fu Panda", "Kung Fu Panda 2", "The Lego Movie", "Mean Girls", "Scooby-Doo",
       "Scooby-Doo 2", "Spider-Man: Homecoming", "Zootopia"] # comedy
dra = ["Contagion", "La La Land", "Little Women"] # drama
fan = ["The Little Mermaid", "LOTR: Fellowship of the Ring", "LOTR: Two Towers", "LOTR: Return of the King", "Moana", "Muppets Wizard of Oz",
       "Scooby-Doo", "Scooby-Doo 2", "Tangled", "Toy Story", "Toy Story 2", "Toy Story 3"] # fantasy
mus = ["La La Land", "The Little Mermaid", "Moana", "Muppets Wizard of Oz", "Tangled"] # music
sci = ["The Lego Movie 2"] # sci-fi
sup = ["Big Hero 6", "The Incredibles", "Incredibles 2", "Spider-Man: Homecoming", "Spider-Man: Into The Spider-Verse"] # superhero
tv = ["Beatrix Potter Collection", "Mr. Men and Little Miss Collection"] # TV series

# runtimes
under_90 = ["The Little Mermaid", "Scooby-Doo", "Toy Story"] # under 90 mins
greater_equal_90 = ["Kung Fu Panda", "Kung Fu Panda 2", "Toy Story 2", "Monsters Inc.", "Mr Peabody and Sherman", "Scooby-Doo 2",
                    "A Bug's Life", "Inside Out", "Mean Girls", "Finding Nemo", "Muppets Wizard of Oz", "Hotel for Dogs", "Tangled", "The Lego Movie",
                    "Toy Story 3", "Big Hero 6", "Contagion", "Moana", "The Lego Movie 2", "Zootopia", "The Incredibles", "Spider-Man: Into The Spider-Verse",
                    "Incredibles 2"] # greater than or equal to 90 mins
greater_equal_120 = ["La La Land", "Little Women", "LOTR: Fellowship of the Ring", "LOTR: Two Towers", "Spider-Man: Homecoming"] # greater than or equal to 120 mins
greater_equal_180 = ["LOTR: Return of the King"] # greater than or equal to 180 mins

sort_greater_equal_90 = sorted(greater_equal_90) # alphabetizes greater_equal_90

valid_genre_input = (ani, adv, com, dra, fan, mus, sci, sup, tv)
valid_runtime_input = (under_90, greater_equal_90, greater_equal_120, greater_equal_180)

genre = input("Which genre would you like to watch? \n 'ani' for animated \n 'adv' for adventure \n 'com' for comedy \n 'dra' for drama \n 'fan' for fantasy \n 'mus' for music \n 'sci' for sci-fi \n 'sup' for superhero \n 'tv' for TV: ")
runtime = input("How long do you want your DVD to be?: \n 'under_90', 'greater_equal_90', 'greater_equal_120', 'greater_equal_180_': ")

# choosing from genre input
def find_film():

    def genre_result():
        if genre == ani:
            result = random.choice(ani)

        elif genre == adv:
            result = random.choice(adv)

        elif genre == com:
            result = random.choice(com)

        elif genre == dra:
            result = random.choice(dra)
            
        elif genre == fan:
            result = random.choice(fan)

        elif genre == mus:
            result = random.choice(mus)

        elif genre == sci:
            result = random.choice(sci)

        elif genre == sup:
            result = random.choice(sup)

        elif genre == tv:
            result = random.choice(tv)

    # choosing from runtime input
    def runtime_result():
        if runtime == under_90:
            result = random.choice(under_90)

        elif runtime == greater_equal_90:
            result = random.choice(greater_equal_90)

        elif runtime == greater_equal_120:
            result = random.choice(greater_equal_120)

        elif runtime == greater_equal_180:
            result = random.choice(greater_equal_180)
            
    
            chosen_genre = str(genre_result) # comparing genre and runtime to create new result
            chosen_runtime = str(runtime_result)

print(genre_result, runtime_result)
                
        