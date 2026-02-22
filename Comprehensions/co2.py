# set comprehension
chai = {
    "masala chai",
    "ginger chai",
    "iced tea",
    "iced latte",
}

fav = {tea for tea in chai if "chai" in tea}
print(fav)


# lets take how to take the expressions for the particular problem
recipes = {
    "Masala Chai" : ["ginger","cardomom","clove"],
    "Elaichi chai" : ["cardmom","milk"],
    "Spicy Chai" : ["ginger","black pepper","clove"],
}

favourites = {spice for indgredients in recipes.values()  for spice in indgredients}

print(favourites)