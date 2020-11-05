# Submits a flag, or flags quickly to a given server
# Make sure to do pip3 install swpag_client before running

from swpag_client import Team

flagToken = "" # put team's flag token here (between "")
t = Team("http://actf0-thu.cse365.io/", flagToken) # sets team


print("Welcome to flag submission! \n")

def submitFlag():
	choice = 1 # don't change this 
	while (choice != 0):
		choice = input("Input flag to submit, or 0 to quit: ") # Takes input as string
		if (choice == "0"): # If user entered 0 as a string, casts to int to break while loop
			choice = int(choice)
		else:
			try:
				t.submit_flag([choice]) # Submits string of flag
				print("Flag successfully submitted, status: ")
			except:
				print("Game not running, try again later")
				choice = 0

	print("Quitting program...") # Only output when while loop breaks


submitFlag() # calls function