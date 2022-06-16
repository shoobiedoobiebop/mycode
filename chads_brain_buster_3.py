#!/usr/bin/python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
#for x in farms[0]["agriculture"]:
#    print(x)
plants = ['carrots', 'celery',]
animals = ['sheep', 'cows', 'pigs', 'chickens', 'llamas', 'cats',]
for farm in farms:
    print("-", farm["name"])
choice= input("Pick a farm!\n")
for farm in farms:
    if farm ["name"].lower() == choice.lower():
        for x in farm["agriculture"]:
#            if x == animals:
#                print(x)
