#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
	r = requests.get('https://cat-fact.herokuapp.com/facts')
	print(r.headers)

main()
