import random

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
television = ["Beatrix Potter Collection", "Mr. Men and Little Miss Collection"]

# runtimes in minutes
under_90 = ["The Little Mermaid", "Scooby-Doo", "Toy Story"]

greater_equal_90 = ["Kung Fu Panda", "Kung Fu Panda 2", "Toy Story 2", "Monsters Inc.", "Mr Peabody and Sherman", "Scooby-Doo 2",
                    "A Bug's Life", "Inside Out", "Mean Girls", "Finding Nemo", "Muppets Wizard of Oz", "Hotel for Dogs", "Tangled", "The Lego Movie",
                    "Toy Story 3", "Big Hero 6", "Contagion", "Moana", "The Lego Movie 2", "Zootopia", "The Incredibles", "Spider-Man: Into The Spider-Verse",
                    "Incredibles 2"]

greater_equal_120 = ["La La Land", "Little Women", "LOTR: Fellowship of the Ring", "LOTR: Two Towers", "Spider-Man: Homecoming"] # greater than or equal to 120 mins

greater_equal_180 = ["LOTR: Return of the King"]

choice = input("Which genre do you want to watch? \nanimated, adventure, comedy, drama, fantasy, musical, scifi, superhero or television \nPlease write full word: ")
if choice == "animated":
    print(random.choice(animated))
if choice == "adventure":
    print(random.choice(adventure))
if choice == "comedy":
    print(random.choice(comedy))
if choice == "drama":
    print(random.choice(drama))
if choice == "fantasy":
    print(random.choice(fantasy))
if choice == "musical":
    print(random.choice(musical))
if choice == "scifi":
    print(random.choice(scifi))
if choice == "superhero":
    print(random.choice(superhero))
if choice =="television":
    print(random.choice(television))

runtime = input("How long do you want the dvd to be (in minutes)? \nunder_90, greater_equal_90, greater_equal_120, greater_equal_180 \nPlease write using exact format: ")
if runtime == "under_90":
    print(random.choice(under_90))
if runtime == "greater_equal_90":
    print(random.choice(greater_equal_90))
if runtime == "greater_equal_120":
    print(random.choice(greater_equal_120))
if runtime == "greater_equal_180":
    print(random.choice(greater_equal_180))
    
# maybe come back to this tomorrow......