cities = {'NewYork':{'country':'USA', 'population':30000000, 'fact':"The USA's biggest city"},
        'Beijing':{'country':'CHINA','population':30000000, 'fact':'The capatal of CHINA'},
        'Tokyo':{'country':'JAPAN', 'population':2000000, 'fact':'New 3rd tokyo'},
}

for city,information in cities.items():
    print(f"city:{city}")
    print(f"country:{information['country']}")
    print(f"population:{information['population']}")
    print(f"fact:{information['fact']}\n")

