#!/usr/bin/python3
Whiskey = 1.8
IPA = 1.7
Bud_Light = 1.6
Jack_n_Coke = 1.5
White_Wine = 1.4
Whiteclaw = 1.3
PBR = 1.2
bottom_shelf_shots = 1.1
drinks = [Whiskey , IPA , Bud_Light , Jack_n_Coke , White_Wine , Whiteclaw , PBR , bottom_shelf_shots]
ans = ["A", "B", "C", "D", "E","F"]
print("What's your favorite drink?")
def quiz():
    
        q2 = input("Question #1 \nHow do you take your coffee? \n A - Black \n B - Cream and Sugar \n C - Frappuccino from Starbucks \n D - I prefer Monsters \n").upper()
  
        if q2 == ans[0]:
            drinks[0] += 3
            drinks[1] += 2
        elif q2 == ans[1]:
            drinks[2] += 2
            drinks[3] += 3
        elif q2 == ans[2]:
            drinks[4] += 3
            drinks[5] += 2
        elif q2 == ans[3]:
            drinks[6] += 2
            drinks[7] += 3
        else:
            print("Please select answer A, B, C, or D.")

        q3 = input("Question #2 \nWhat does Fall get you excided for? \n A - FOOTBALL! \n B - Spooky Season \n C - Bonfires \n D - Fall Colors \n E - Pumpkin Spice \n").upper()
  
        if q3 == ans[0]:
            drinks[1] += 1
            drinks[2] += 3
            drinks[6] += 2
        elif q3 == ans[1]:
            drinks[7] += 3
            drinks[5] += 2
            drinks[3] += 2
        elif q3 == ans[2]:
            drinks[0] += 3
            drinks[1] += 2
            drinks[2] += 1
        elif q3 == ans[3]:
            drinks[1] += 2
            drinks[4] += 3
        elif q3 == ans[4]:
            drinks[4] += 3
            drinks[5] += 2
        else:
            print("Please select answer A, B, C, D, or E.")
          
        q4 = input("Question #3 \nEdward or Jacob? \n A - Edward \n B - Jacob \n").upper()
  
        if q4 == ans[0]:
            drinks[0] += 3
            drinks[1] += 3
            drinks[2] += 3
            drinks[3] += 3
        elif q4 == ans[1]:
            drinks[4] += 3
            drinks[5] += 3
            drinks[6] += 3
            drinks[7] += 3
        else:
            print("Please select answer A or B.")
          
        q5 = input("Question #4 \nWhat is your favorite Summertime activity? \n A - Boating \n B - Sitting by the pool \n C - Hiking \n D - Fishing \n").upper()
  
        if q5 == ans[0]:
            drinks[5] += 3
            drinks[2] += 3
            drinks[6] += 2
        elif q5 == ans[1]:
            drinks[7] += 1
            drinks[5] += 3
            drinks[3] += 2
        elif q5 == ans[2]:
            drinks[0] += 3
            drinks[1] += 2
            drinks[4] += 1
        elif q5 == ans[3]:
            drinks[3] += 2
            drinks[2] += 3
        else:
            print("Please select answer A, B, C, or D.")
          
        q6 = input("Question #5 \nWhat time do you go to sleep?\n A - 9pm or earlier\n B - Between 10pm and 11pm\n C - Between 11pm and Midnight\n D - What's sleep?\n").upper()
  
        if q6 == ans[0]:
            drinks[0] += 3
            drinks[7] += 3
        elif q6 == ans[1]:
            drinks[4] += 3
            drinks[1] += 2
            drinks[0] += 2
        elif q6 == ans[2]:
            drinks[5] += 3
            drinks[3] += 2
            drinks[2] += 3
        elif q6 == ans[3]:
            drinks[7] += 2
            drinks[6] += 3
            drinks[5] += 3
        else:
            print("Please select answer A, B, C, or D.")        

        q7 = input("Question #6 \nSith or Jedi?\n A - Sith\n B - Jedi\n").upper()

        if q7 == ans[0]:
            drinks[0] += 3
            drinks[2] += 3
            drinks[4] += 3
            drinks[6] += 3
        elif q7 == ans[1]:
            drinks[1] += 3
            drinks[3] += 3
            drinks[5] += 3
            drinks[7] += 3
        else:
            print("Please select answer A or B.")

        q8 = input("Question #7 \nWhat kind of water do you drink?\n A - Tap\n B - Aquafina \ Dasani\n C - Fiji \ Voss\n D - There's water in Monster... right?\n").upper()

        if q8 == ans[0]:
            drinks[0] += 3
            drinks[7] += 3
            drinks[6] += 2
        elif q8 == ans[1]:
            drinks[2] += 3
            drinks[3] += 2
            drinks[5] += 2
        elif q8 == ans[2]:
            drinks[1] += 3
            drinks[4] += 2
            drinks[0] += 1
        elif q8 == ans[3]:
            drinks[1] += 2
            drinks[4] += 3
            drinks[5] += 3
        else:
            print("Please select answer A, B, C, or D.")  

        q9 = input("Question #8 \nHouse plants are...\n A - MANDATORY\n B - OK.. I guess..\n C - Something I will definitely kill\n D - STUPID!\n").upper()

        if q9 == ans[0]:
            drinks[1] += 3
            drinks[4] += 3
            drinks[0] += 1
        elif q9 == ans[1]:
            drinks[4] += 3
            drinks[1] += 2
            drinks[0] += 2
        elif q9 == ans[2]:
            drinks[5] += 3
            drinks[3] += 2
            drinks[2] += 3
        elif q9 == ans[3]:
            drinks[7] += 2
            drinks[6] += 3
            drinks[5] += 3
        else:
            print("Please select answer A, B, C, or D.")  

        q0 = input("Question #9 \nCats or Dogs?\n A - Cats\n B - Dogs\n").upper()

        if q9 == ans[0]:
            drinks[0] += 3
            drinks[1] += 3
            drinks[4] += 3
            drinks[6] += 3
        elif q9 == ans[1]:
            drinks[2] += 3
            drinks[3] += 3
            drinks[5] += 3
            drinks[7] += 3
        else:
            print("Please select answer A or B.")

        q1 = input("Question #10 \nPick your favorite streaming service.\n A - Netflix\n B - Prime\n C - YouTube\n D -Disney+\n E - What is streaming?\n F - Does Tik Tok count?\n").upper()
  
        if q1 == ans[0]:
            drinks[1] += 1
            drinks[2] += 3
            drinks[6] += 2
        elif q1 == ans[1]:
            drinks[7] += 3
            drinks[5] += 2
            drinks[3] += 2
        elif q1 == ans[2]:
            drinks[0] += 3
            drinks[1] += 2
            drinks[2] += 1
        elif q1 == ans[3]:
            drinks[1] += 2
            drinks[4] += 3
        elif q1 == ans[4]:
            drinks[4] += 3
            drinks[5] += 2
        elif q1 == ans[5]:
            drinks[1] += 2
            drinks[4] += 3
        else:
            print("Please select answer A, B, C, D, E, or F")

          
        if max(drinks)  == drinks[0]:
          print("Your favorite drink is Whiskey. You enjoy torturing yourself and want the world to know it.")
        elif max(drinks) == drinks[1]:
          print("Your favorite drink is a cold IPA. Nothing says 'I'm better than you' more than drinking something gross.")
        elif max(drinks) == drinks[2]:
          print("Your favorite drink is Bud Light. You're basic, but that's ok.")
        elif max(drinks) == drinks[3]:
          print("Your favorite drink is Jack and Coke. You want the world to know how manly you are, but your sensitive taste buds prevent you from drinking real liquor.")
        elif max(drinks) == drinks[4]:
          print("Your favorite drink is chilled White Wine. You want the world to think you're classy, but that box of Sutter Homes screams the opposite.")
        elif max(drinks) == drinks[5]:
          print("Your favorite drink is Whiteclaw. You want to party, but you don't want to get fat. Luckly the only thing you had to give up was flavor.")
        elif max(drinks) == drinks[6]:
          print("Your favorite drink is PBR. Are you poor or are you a hipster? Either way, you have to ask yourself; Is something that taste this bad worth the massive hangover?")
        elif max(drinks) == drinks[7]:
          print("Your favorite drink is Shots.. The cheaper the better! When you were growing up, your parents said that you could become anything you wanted to. You decided to become a problem.. nice")

      
        
age = input("How old are you? \n")
if int(age) < 21:
    print("Your favorite drink is milk. Come back when you are old enough to play.")
else:
    quiz()
 
