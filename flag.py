# Submits a flag, or flags quickly to a given server
# Make sure to do pip3 install swpag_client before running

from swpag_client import Team
import time

teamInterface = "http://actf1-thu.rev.fish/" # Input team interface here (between ""). Invalid example given
flagToken = "XXXXXXXXXXXX" # put team's flag token here (between ""). Invalid example given.
t = Team(teamInterface, flagToken) # sets team


print("Welcome to flag submission! \n")

def submitFlag():
	choice = "1" # don't change this 
	while (choice != "0"):
		choice = input("Input flag to submit, or 0 to quit: ") # Takes input as string
		if (choice != "0"):
			try:
				status = t.submit_flag([choice]) # Submits string of flag
				print("Flag successfully submitted, status: " + str(status))
			except Exception as e:
				print("Game not running, try again later")
				print("Error : " + str(e))
				choice = "0"

	print("Quitting program...") # Only output when while loop breaks


submitFlag() # calls function