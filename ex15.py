people = 10
cars = 10
trucks = 10 

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("We can't decide.")
elif trucks < cars:
    print("That's too many trucks.")
else:
    print("We still cna't decide.")

if people > trucks:
    print("ALright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
  