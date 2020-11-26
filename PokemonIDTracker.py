# Pokemon ID Tracker
# by Lucky "Luckstruck9" Lai

# Version 1.0

import os

IDList = []
IDdict = {}
IDpatterntotals = []

def main():
	global IDList
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

	options = [
	"0: View Current List",
	"1: Load List",
	"2: Export List",
	"3: Add IDs to List",
	"4: Clear List",
	"5: Remove Duplicates",
	"Exit/Quit: Close Application"]
	print("Welcome to the Pokemon ID Tracker")
	print("---------------------------------")
	print("You can use this Python Program to keep track of all the unique IDs in your Pokemon Box.")
	print("ID numbers can be viewed in reverse order because that is the direction the game reads it.")

	loop = True
	while(loop):
		print("Options")
		print("\n".join(options)+"\n")
		optionselect = input("Please enter your option: ")

		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')

		if optionselect=="0":
			IDCurrentList()
		elif optionselect=="1":
			IDLoad()
		elif optionselect=="2":
			IDExport()
		elif optionselect=="3":
			IDEntry()
		elif optionselect=="4":
			IDList.clear()
			print("Current ID List has been cleared!!!")
			input("Press <enter> to continue\n")
		elif optionselect=="5":
			newIDList = set(IDList)
			IDList = list(newIDList)
			print("Current duplicates in the IDList have been removed")
			input("Press <enter> to continue\n")
		elif optionselect.lower()=="exit" or optionselect.lower()=="quit" or optionselect=="":
			print("Now exiting...")
			return
		else:
			print("Invalid Option")

def printmatchingpermutations(breakdownIDs):
	IDdictUpdate()
	permutationmatches = []
	for perm in IDpatterntotals:
		for subID in breakdownIDs:
			if str(perm[0])==str(subID):
				permutationmatches.append(str("'"+str(perm[0])+"' : "+str(perm[1])))
	return permutationmatches

def IDdictUpdate():
	IDdict.clear()
	for preID in IDList:
		revID = preID[::-1]
		for i in range(1,6):
			shortID = revID[:i]
			if shortID in IDdict:
				IDdict[shortID]+=1
			else:
				IDdict[shortID]=1
	IDpatterntotals.clear()
	for IDpattern in IDdict.keys():
		if (len(IDpattern)>1):
			IDpatterntotals.append([IDpattern, IDdict[IDpattern]])
	IDpatterntotals.sort(reverse=True, key=lambda IDpattern: len(IDpattern[0]))
	IDpatterntotals.sort(reverse=True, key=lambda IDpattern: IDpattern[1])

def IDCurrentList():
	IDdictUpdate()
	strIDpatterntotals = ""
	toppicks = 5
	if len(IDpatterntotals)<10:
		toppicks = len(IDpatterntotals)//2
	for i in range (toppicks):
		strIDpatterntotals+=("\n"+str("'"+str(IDpatterntotals[i][0])+"' : #"+str(IDpatterntotals[i][1])+"\t\t'"+str(IDpatterntotals[i+5][0])+"' : #"+str(IDpatterntotals[i+5][1])))
	#print(IDpatterntotals)
	print("Unique ID Permutations:\t", len(IDList))
	print("10 Most Common Sequences (Excluding Starting Digits):"+strIDpatterntotals)
	print("----------------------------------------\n")
	print("Reversed ID\t||\tNormal ID")
	print("-----------\t\t---------")

	IDList.sort(key=lambda func: func[::-1])
	for ID in IDList:
		print(ID[::-1]+"\t\t\t"+ID)

	input("Press <enter> to continue\n")
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def IDLoad():
	while (True):
		filename = input("Please enter the txt filename you'd like to load from (Press <enter> to quit):\n")
		if filename=="":
			print("Now closing ID Load...")
			return
		elif ".txt" not in filename:
			print("This is not a txt document!!!")
		elif not os.path.isfile(filename):
			print("This file does not exist!!!")
		elif os.path.isfile(filename):
			break
	filecontent = open(filename, 'r')
	filecontentlines = filecontent.readlines()
	for line in filecontentlines:
		IDList.append(line.strip("\n"))
	print("IDs from "+filename+" have been inserted into your current ID List")

	input("Press <enter> to continue\n")
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
	return

def IDExport():
	while (True):
		filename = input("Please enter the txt filename you'd like to export to (Press <enter> to quit):\n")
		if filename=="":
			print("Now closing ID Export...")
			return
		elif ".txt" not in filename:
			print("This is not a txt document!!!")
		elif not os.path.isfile(filename):
			break
		elif os.path.isfile(filename):
			overwriteBool = False
			while (True):
				print("A file with this name already exists!!!")
				overwrite = input("Overwrite anyway? (Yes/No):\n")
				if (overwrite.lower()=="n" or overwrite.lower()=="no"):
					print("Not ovewriting...")
					break
				elif (overwrite.lower()=="y" or overwrite.lower()=="yes"):
					overwriteBool = True
					print("Overwriting!")
					break
			if overwriteBool:
				break

		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')

	filecontent = open(filename, 'w')
	filecontent.writelines("\n".join(IDList))
	print("IDs from your current list have been exported to "+filename)

	input("Press <enter> to continue\n")
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
	return

def IDEntry():
	loop = True
	lastID="N/A"
	while (loop):
		print("Current Number of Unique IDs:\t", len(IDList))
		print("Last Entered ID:\t\t", lastID)
		print("---------------------------------------------------------------")
		newID = input("Please enter an ID:\n")
		if (newID==""):
			loop = False
		elif len(newID)!=6 and len(newID)!=5:
			input("The ID must be 5 or 6 digits!!! (Press <enter> to continue)\n")
		elif not newID.isdigit():
			input("You can only use digits!!! (Press <enter> to continue)\n")
		else:
			if newID not in IDList:
				breakdownID = []
				RnewID = newID[::-1]
				for i in range(2, 5):
					breakdownID.append(RnewID[:i])
				totalmatches = printmatchingpermutations(breakdownID)
				if (len(totalmatches)>=1):
					print("Similar Reverse Prefixes Found:")
					print("\n".join(totalmatches))
					while (True):
						confirmadd = input("Do you still want to add "+newID+"? (Yes or No):\n")
						if confirmadd.lower()=="y" or confirmadd.lower()=="yes":
							IDList.append(newID)
							lastID=newID
							break
						elif confirmadd.lower()=="n" or confirmadd.lower()=="no":
							break
						else:
							print("Invalid option!")
				else:
					IDList.append(newID)
					lastID=newID
			else:
				input("ID ALREADY EXISTS IN THE LIST!!! (Press <enter> to continue)\n")

		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')
	input("Now closing ID Entry...\nPress <enter> to continue\n")
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
	return

main()