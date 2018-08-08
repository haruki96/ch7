name = "Ted"
for character in name:
    print(character)

#
shows = ["GOT", "Narcos", "Vince"]
print("------")
for show in shows:	
    print(show)
	
#
coms = ("A. Development", "Friends", "Always Sunny")
print("------")
for com in coms:
    print(com)
	
#p106
people = {"G. Bluth IT":"A. Development",
          "Barney":"HIMYM",
		  "Dennis":"Always Sunny",
		  }
print("------")
print(people["Barney"])
for human in people:
    print(human)
	
	
#p106 ERROR
print("-----")

tv = ["GOT",
     "Narcos",
     "Vice"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1
	
print(tv)


#p107
print("-----")

tv = ["GOT", "Narcos", "Vice"]
for i, new in enumerate(tv):
	new = tv[i]
	new = new.upper()
	tv[i] = new
print(tv)


#
print("-----")

tv = ["GOT", "Narcos", "Vice"]
coms = ["Arrested Development", "friends", "Always Sunny"]
all_shows = []

for show in tv:
	show = show.upper()
	all_shows.append(show)

for show in coms:
	show = show.upper()
	all_shows.append(show)

print(all_shows)


#
print("----------")
for i in range(1,11):
	print(i)

###while###
print("----------")
x = 10
while x > 0:
	print('{}'.format(x))
	x -= 1
print("Happy New Year!")


###break###
print("----------")
for i in range(0, 100):
	print(i)
	break

####p111###
print("----------")
#qs = ["What is your name?",
#      "What is your fav.color?",
#      "What is your quest?"]
#n = 0
#while True:
#	print("Type q to quit")
#	a = input(qs[n])
#	if a == "q":
#		break
#	n = (n + 1) % 3


###continue###
print("----------")
for i in range(1,6):
	if i == 3:
		continue
	print(i)

#
print("----------")
i = 1
while i <= 5:
    if i == 3:
    	i += 1
    	continue
    print(i)
    i += 1


###p113###
print("----------")
for i in range(1, 3):
	print(i)
	for letter in ["a", "b", "c"]:
		print(letter)

#p114
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
added = []
for i in list1:
	for j in list2:
		added.append(i + j)

print(added)


##p114##
#print("----------")
#while input('y or n?') != 'n':
#	for i in range(1, 6):
#		print(i)


