names = ['alan', 'mike', 'john', 'adam', 'frank']
count = 0

for item in names:
    message = f"Hi, {names[count].title()}, What's going on recently? "
    print(message)
    count +=1

for name in names:
    print(f"Hi, {name.title()}, What's going on recently?")