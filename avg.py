ride1 = float(input("Speed of rider 1: "))
ride2 = float(input("Speed of rider 2: "))
ride3 = float(input("Speed of rider 3: "))
avg = (ride1 + ride2 + ride3)/3

if avg > ride1:
    print("Rider one is too slow by", avg - ride1)
else:
    print("Good job")
if avg > ride2:
    print("Rider one is too slow by", avg - ride2)
else:
    print("Good job")
if avg > ride3:
    print("Rider one is too slow by", avg - ride3)
else:
    print("Good job")