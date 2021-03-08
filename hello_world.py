# 1. TASK: print "Hello World"
print("Hello World!")
# 2. print "Hello Noelle!" with the name in a variable
name = "Christie"
print("Hello", name)	# with a comma
print("Hello " + name + "!")	# with a +
# 3. print "Hello 42!" with the number in a variable
num = 13
print("Hello", num)	# with a comma
print(f"Hello {num}!")	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "spaghetti"
fave_food2 = "sandwiches"
print("I love to eat {} and {}." .format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}") # with an f str

print("My name is %s , my fav number is %d, and my favorite foods are: %s and %s." % (name, num, fave_food1, fave_food2))