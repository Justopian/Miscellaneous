# Take input (number of cookies)
num_cookies = int(input("How many cookies are to be made?: "))

# Multiply by conversion factors to get flour, sugar, and butter
cups_flour = num_cookies / 10 * 3/2
cups_sugar = num_cookies / 10 * 2/3
cups_butter = num_cookies / 10 * 3/8

# Alternative method
conversions = [3/2, 2/3, 3/8]
ingredients = [(num_cookies / 10) * i for i in conversions]

# Output
print("You need {:.2f} cups of flour, {:.2f} cups of sugar, and {:.2f} cups of butter.".format(cups_flour, cups_sugar, cups_butter))
print("You need {0:.2f} cups of flour, {1:.2f} cups of sugar, and {2:.2f} cups of butter.".format(ingredients[0],
                                                                                                  ingredients[1],
                                                                                                  ingredients[2]))
