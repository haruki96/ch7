###1###
drama = ["Walking dead", "Antrage", "The soplanos", "Vanpire diaries"]
for i in drama:
	print(i)


###2###
print("-----2-----")
for i in range(25, 51):
	print(i)


###3###
print("-----3-----")

drama = ["Walking dead", "Antrage", "The soplanos", "Vanpire diaries"]
for index, show in enumerate(drama):
	print(index)
	print(show)


###4###
print("-----4-----")

numbers = [11, 32, 33, 15, 1]
numbers.append(14)

while True:
	answer = input("Guess a number or type q to quit.")
	if answer == "q":
		break
	try:
		answer = int(answer)
	except ValueError:
		print("Please type a number or q to quit.")
	if answer in numbers:
		print("You guessed correctly!")
	else:
		print("You guessed incorrectly!")