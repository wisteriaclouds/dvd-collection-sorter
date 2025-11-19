import random

drama = ["Contagion", "La La Land", "Little Women"]
greater_equal_120 = ["La La Land", "Little Women", "LOTR: Fellowship of the Ring", "LOTR: Two Towers", "Spider-Man: Homecoming"]

# valid inputs
valid_genre = ["adventure", "animated", "comedy", "drama", "fantasy", "musical", "scifi", "superhero", "television"]
valid_time = ["under_90", "greater_equal_90", "greater_equal_120", "greater_equal_180"]

# random choice
print(valid_genre)
print(valid_time)

genre = input("Which genre do you want to watch? ")
time = input("How long do you want your dvd to be (in minutes)? ")

res = list(filter(lambda x: x in greater_equal_120, drama)) # need to ask user for general genre/runtime, call stored choice and replace that in lambda argument
res2 = print(random.choice(drama) + " " + random.choice(greater_equal_120))


"""while genre not in valid_genre:
    print("That is an invalid choice. Choose from the list")
    while time not in valid_time:
        print("That is not a valid choice. Choose from the list")
    if genre in valid_genre and time in valid_time:
        break
    genre = input("Which genre do you want to watch? ")
    if time in valid_genre:
        time = input("How long do you want your dvd to be (in minutes)? ")
           


if time in valid_time:
    print(random.choice(greater_equal_120))
if genre == "drama" and time == "greater_equal_120":
    print(res)
elif genre != "drama" and time == "greater_equal_120":
    print("Oopsie!")
elif genre == "drama" and time != "greater_equal_120":
    print("Error. Wrong time.")
elif genre != "drama" and time != "greater_equal_120":
    print("You haven't chosen a genre or time.")"""