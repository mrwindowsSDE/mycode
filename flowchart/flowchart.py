#!/usr/bin/env python3
import sys

EDGES = {"0": ["1", "2", "3"], "2": ["4"], "3": ["4"], "4": ["5", "6"], 
"6": ["7"], "7": ["8", "9"], "8": ["10"], "9": ["10"], "10": ["11", "12"], 
"12": ["13"], "13": ["14"]}
RESPONSE_TO_ANSWER = {"0": "0", "2": "4", "3": "4", "6": "7", "8": "10", "9": "10", "12": "13"}
QUESTIONS = {"0": "Are you a horse?", "4": "How many legs do you walk on?",
"7": "Really?", "10": "Can you read and write?", "13": "Liar; You're reading this"}
OPTIONS = {"1": "No", "2": "Yes", "3": "Maybe", "5": "Two", "6": "Four", "8": "No", 
"9": "Yes", "11": "Yes", "12": "No", "14": "Yes"}
END_COMMAND = "q"

def start(node):
	if node == END_COMMAND:
		sys.exit("Bye!")
	elif not EDGES.get(node):
		sys.exit("You're not a horse")

	node = RESPONSE_TO_ANSWER.get(node)

	what_to_print = QUESTIONS.get(node)
	print(what_to_print)

	while True:
		current = EDGES.get(node)
		options_to_show = ""
		for option_number in current:
			options_to_show += f" [{option_number}]: {OPTIONS.get(option_number)}"

		print(options_to_show)
		user_choice = ""
		while user_choice not in current and user_choice != END_COMMAND:
			user_choice = input("Choose an option(enter q to quit) ")
		start(user_choice)	


def main():
	start("0")

if __name__ == "__main__":
	main()
