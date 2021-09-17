import math
baby_yoda = 20
beyblades = 7.2
stickyhands = 0.5
budget = float(input("Input your budget: "))
babyyodaplush = math.floor(int((budget / 20)))
budget = budget % 20
beyblades = math.floor(int((budget / 7.2)))
budget = budget % 7.2
stickyhands = math.floor(int((budget / 0.5)))
budget = budget % 0.5
print("You can afford:")
print(babyyodaplush)
print(" Yoda Plushies")
print(beyblades) 
print(" Beyblades")
print(stickyhands) 
print(" Sticky Hands")
print("You have a remaining: ")
print(budget)