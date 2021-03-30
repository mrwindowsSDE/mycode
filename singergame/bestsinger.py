#!/usr/bin/env python3

import sys

hints = ["She's got a powerful voice.", "She's really tiny.", 
"Thanks for making me a Fighter!", "She's a Genie in a Bottle."]
correct_answers = ["aguilera", "christina aguilera", "xtina"]
close_guesses = ("chris", "christina")
laughably_wrong_answers = ["ariana grande", "cardi b", "khalid"]
acceptable_answers = ["whitney houston", "mariah carey"]
TOTAL_GUESSES = 3
won = False
output = {"guesses": TOTAL_GUESSES}

def answer_checker(guess, guesses):
	correct_guess_checker(guess, output)
	close_guess_checker(guess, output)
	acceptable_guess_checker(guess, output)
	dumb_guess_checker(guess, output)
	wrong_guess_checker(guess, output)
	output["guesses"] -= 1
	print_to_console(output)

def hint_printer(guesses):
	if guesses != TOTAL_GUESSES:
		print(f"Here's a hint: {hints[guesses]}")

def correct_guess_checker(guess, output):
	if guess in correct_answers:
		output["win"] = "You got it right. She's the best!"
		won = True

def close_guess_checker(guess, output):
	if guess in close_guesses or guess.lower().startswith(close_guesses):
		output["close"] = "You're really close!"

def dumb_guess_checker(guess, output):
	if guess in laughably_wrong_answers:
		output["dumb_guess"] = "The program is now ending due to your answer."

def wrong_guess_checker(guess, output):
	if not output.get("win"):
		output["wrong"] = "Wrong answer."

def acceptable_guess_checker(guess, output):
	if guess in acceptable_answers:
		output["acceptable"] = "This answer is acceptable. But at the same time. No. It's someone else. But you have good taste."

def print_to_console(output):
	what_to_print = ""
	if(output.get("dumb_guess")):
		sys.exit(output.get("dumb_guess"))
	elif output.get("win"):
		sys.exit(output.get("win"))
	elif output.get("close"):
		what_to_print = output.get('close')
	elif output.get("acceptable"):
		what_to_print = output.get('acceptable')
	elif output.get("wrong"): 
		what_to_print = output.get("wrong")
	print(what_to_print)


def main():
	while output["guesses"] > 0 and not won:
		current_guesses = output.get("guesses")
		output.clear()
		output["guesses"] = current_guesses
		hint_printer(output["guesses"])
		guess = input(f"Who is the best singer of all time? You have {output.get('guesses')} guesses. ")
		guess = guess.lower()
		answer_checker(guess, output["guesses"])

main()
