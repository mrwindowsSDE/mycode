#!/usr/bin/env python3

animals = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for animal in farms[0]["agriculture"]:
	print(animal)

farm = input("Choose a farm(NE Farm, W Farm, or SE Farm) ")

for obj in farms:
	if farm == obj["name"]:
		for thing in obj["agriculture"]:
			print(thing)


farm = input("Choose a farm(NE Farm, W Farm, or SE Farm) ")

for obj in farms:
	if farm == obj["name"]:
		for thing in obj["agriculture"]:
			if thing in animals:
				print(thing)


