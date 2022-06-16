#!/usr/bin/python3
#Whiskey = 1.8
#IPA = 1.7
#Bud_Light = 1.6
#Jack_n_Coke = 1.5
#White_Wine = 1.4
#Whiteclaw = 1.3
#PBR = 1.2
#bottom_shelf_shots = 1.1
#A = Whiskey += 3

drinks = [{"Whiskey" : 1.1} , {"IPA" : 1.2} , {"Bud Light" : 1.3} , {"Jack n Coke" : 1.4} , {"White Wine" : 1.5} , {"Whiteclaw" : 1.6} , {"PBR" : 1.7} , {"bottom shelf shots" : 1.8}]
print("What's your favorite drink?")
def quiz():
     q2 = input("Question #2 \nHow do you take your coffee? \n A - Black \n B - Cream and Sugar \n C - Frappuccino from Starbucks \n D - I prefer Monsters \n").upper
     if q2 == 'A':
         drinks[0]["Whiskey"] += 3
         drinks[1]["IPA"] += 2
     #elif q2 == 'B':
         drinks[2] += 2
         drinks[3] += 3
     #elif q2 == 'C':
         drinks[4] += 3
         drinks[5] += 2
     #elif q2 == 'D':
         drinks[6] += 2
         drinks[7] += 3
     else:
         print("Please select answer A, B, C, or D.")
age = input("Question #1 \nHow old are you? \n")
if int(age) < 21:
         print("Your favorite drink is milk. Come back when you are old enough to play.")
else:       
         quiz()

print(drinks)
print(drinks[0] + 1)
print(drinks[0])
print(max(drinks))
