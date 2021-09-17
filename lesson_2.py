import math
test1 = int(input("Enter your first test score"))
test2 = int(input("Enter your second test score"))
test3 = int(input("Enter your third test score"))
score = (test1 + test2 + test3)/3
print(score)
if score >= 90:
    print ("A")
elif score >= 80:
    print ("B")
elif score >= 70:
    print ("C")
elif score >= 60:
    print ("D")
else:
    print ("F")


