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