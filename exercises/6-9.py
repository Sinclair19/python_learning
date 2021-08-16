favorite_places = {'Jam':['Canada','Japan','Beijing'],
    'sam':['Newyork','losangles','torento'],
    'john':["xi'an",'hangzhou','kunming'],
    }

for name,cities in favorite_places.items():
    message = f"{name.title()}'s favorite city is {cities[0].title()}, {cities[1].title()}, {cities[2].title()}."
    print(message)

