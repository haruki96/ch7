number = [7, 15, 8, 41]
number.append(99)

while True:
	answer = input("Guess a number or type 'q' to quit.")
	if answer == "q":
		break
	try:
		answer = int(answer)
	except ValueError:
		print("Type a number or 'q' to quit.")
	if answer in number:
		print("correct")
	else:
		print("not correct")

	