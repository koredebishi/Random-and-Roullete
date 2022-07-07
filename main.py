# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

rand_name = len(names)
print (rand_name)
payment = random.randint(0 , rand_name - 1)

print (payment)
who_pays = names[payment]
print (who_pays)




