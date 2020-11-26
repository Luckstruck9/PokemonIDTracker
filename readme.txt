Welcome to the Pokemon ID Tracker in Python!
by Lucky "Luckstruck9" Lai

http://www.Luckstruck9.com
Luckstruck9@gmail.com

The purpose of this program is to keep track of the Pokemon IDs in your storage.

I consider this program to be helpful because it will help you arrange a subset of your Pokemon that give you the best odds at the Loto-ID. The Loto-ID reads ID numbers in reverse and begins matching consecutive digits to a randomly generated 5 digit number. Optimally, you want to have your entire storage with unique permutations starting at the last digit. All the permutations of a length should be obtained before incrementing the permutation size. You do not simply care about random permutations. You care about creating different paths from the end of the ID to the beginning of the ID.

Example (In Order):
1. Obtain all   10 Pokemon with unique last 1 digit
2. Obtain all  100 Pokemon with unique last 2 digits (Overlaps with #1)
3. Obtain all 1000 Pokemon with unique last 3 digits (Overlaps with #2)
	- 3 cannot actually be obtained because the maximum box storage in Pokemon Sword/Shield is 960 (32 Boxes * 30 Pokemon Each)

How-to-use:
- To open the program, double-click 'RunPokemonIDTracker.bat'
- If you are starting your list of IDs from a txt file, make sure to load it. Otherwise, you will start with a blank list.
- When you are adding entries, the program will attempt to get confirmation if you enter an ID that shares the last X digits as another ID already entered.
		(Program will also indicate what digits matched to other IDs entered. Matches only appear if the shared digits/placings start from the end and continue consecutively)
- When you are finished, you should export your IDs into a file. You can use the export function to save your ID list as a txt file that can be imported/loaded by the program

Notes:
- With 100 Pokemon that all have a unique permutation of the last 2 ID digits will give you a 100% chance of getting a Tier 2 prize (PP-Up) or greater
- The 'Remove Duplicates' function was intended in the event that a user accidentally loaded their txt file more than once

Known Issues:
- No ID remover. If someone wants to remove an ID from the list, they must export it as a txt file, manually delete the ID, and then load it into the program.


References:
- Loto-ID by Bulbapedia
				https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Lottery_Corner

---------------------------------------------------------------------------------------------------------------------------------------------------

Changelog:
- 11/26/2020
				V1 Released