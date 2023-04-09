# Tackle Box Calculator
# Coded on my android phone ;)
# Copy and paste this source code and run it on an online python interpreter https://www.programiz.com/python-programming/online-compiler/

# Budget

budget = 3000 # Number of WLS
budget_dls = budget / 100 # Converted to DLS

rate = 3.33 # Price of 1 tackle box in WLS

buy_tackle = budget / rate # Number of tackle boxes you can afford with the number of WLS you have in your budget

print("I can buy " + str(round(buy_tackle, )) + " tackle boxes for " + str(round(budget, )) + "WLS or " + str(round(budget_dls, )) + "DLS at a rate of " + str(rate) + "WLS per tackle box")

# Item drop rate equation 
# Let x be the number of tackle boxes

# x = 5000 # <-- Use this if you want to calculate amount of WLS you will earn without having to calculate budget
# x = buy_tackle # <-- Use this if you want to figure out the number of tackle boxes you can afford according to your budget

fishingfly_equation = (121/600) * x
megapellet_equation = (31/600) * x
salmon_equation = (151/600) * x
shiny_equation = (211/600) * x
shrimp_equation = (47/600) * x
uranium_equation = (19/600) * x
wiggly_equation = (93/200) * x

total_drops = fishingfly_equation + megapellet_equation + salmon_equation + shiny_equation + shrimp_equation + uranium_equation +  wiggly_equation

print(str(round(x, )) + " tackle boxes drop approximately " + str(round(fishingfly_equation, )) + " Fishing Fly, " + str(round(megapellet_equation, )) + " Mega-Pellet Bait, " + str(round(salmon_equation,)) + " Salmon Eggs, " + str(round(shiny_equation, )) + " Shiny Flashy Thing, " + str(round(shrimp_equation, )) + " Shrimp Lure, " + str(round(uranium_equation, )) + " Uranium Glowing Lure and " + str(round(wiggly_equation, )) + " Wiggly Worm, " + str(round(total_drops, )) + " drops in total per harvest")

# Item price rate

fishingfly_rate = fishingfly_equation / 100
megapellet_rate = megapellet_equation / 30
salmon_rate = salmon_equation / 200
shiny_rate = shiny_equation / 200
shrimp_rate = shrimp_equation / 8
uranium_rate = uranium_equation / 30
wiggly_rate = wiggly_equation / 500

total_earned = fishingfly_rate + megapellet_rate + salmon_rate + shiny_rate + shrimp_rate + uranium_rate + wiggly_rate

print("I will earn roughly " + str(round(total_earned, )) + " WLS in total for every harvest (2 days)")

# Tackle box price rate

tackle_rate = rate * x 
tackle_rate_dls = tackle_rate / 100
earn_wls = tackle_rate / (total_earned / 2)

print("It will take me about " + str(round(earn_wls, )) + " days to earn back the amount of wls I spent on " + str(round(x, )) + " tackle boxes in which I paid " + str(round(tackle_rate, )) + "WLS or " + str(round(tackle_rate_dls, )) + "DLS at a rate of " + str(rate) + "WLS per tackle box")
