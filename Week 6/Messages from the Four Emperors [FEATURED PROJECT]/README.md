# A6_T7 Messages from the Four Emperors


Each of the Four Emperors—Galba, Otho, Vitellius and Vespasian—has left a message in their own palaces. Your task is to travel programmatically to each location and gather all their messages.

You may travel only once per program run. Travel should begin by displaying the current location, followed by the process of traveling to the next location. The first location is the “start” or “Home” location on the map below.



Place names listed:

home
Galba's palace
Otho's palace
Vitellius' palace
Vespasian's palace
Create a file “player_progress.txt” and initialize it with the following details.

file 1
current_location;next_location;passphrase
0;1;qvfpvcyvar

Player progress file explained:

First row is the header row with the column names.
Data row 1
Current location id 0 refers to the starting point (Home).
Next location id 1 refers to the next objective (Galba's palace).
Passphrase ciphered (ROT13)
Next data row
Should be added after progress is made on it’s own new line in the same file.
Once you have traveled to the destination, walk into the palace and shout the passphrase(print the plain version) to the guard as you enter. After entering, locate the message (open file "{NextLocationId}_{PassPhrase}.gkg") and read the content.

The “.gkg” file extension in this context means that the text file content is in ciphered form. It can be deciphered back to plain text using the Ceasar Cipher (ROT13).

Read the first line as ciphered text and append it to the player_progress.txt. After the first line, save the plain version of the message into "{NextLocationId}-{PlainPassPhrase}.txt".

Examples of message formats:

file1: Ciphered message "{NextLocationId}_{PassPhrase}.gkg"
file2: Plain version to save "{NextLocationId}-{PlainPassPhrase}.txt"
file 1 file 2
0;1;qvfpvcyvar
Cneg 0 - Lrne bs gur Sbhe Rzcrebef:

Va NQ 68, nsgre Areb'f qrngu, Ebzr cyhatrq vagb punbf.
Jvgu ab pyrne urve, gur rzcver fnj encvq cbjre fgehttyrf.
Tnyon gbbx gur guebar svefg, sbyybjrq ol Bgub, Ivgryyvhf, naq svanyyl Irfcnfvna,
rnpu onggyvat sbe pbageby va jung orpnzr gur Lrne bs gur Sbhe Rzcrebef.

After the progress and the Emperor’s message have been saved, the program closes with the final phrases. The next time the program runs, it should be able to read the previous progress from player_progress.txt and continue the next turn.

Example program runs:

run 1 run 2 run 3 run 4

Travel starting.
Currently at home.
Travelling to Galba's palace...
...Arriving to the Galba's palace.
Passing the guard at the entrance.
"Discipline!"
Looking for the message in the palace...
Ah, there it is! Seems cryptic.
[Game] Progress autosaved!
Deciphering Emperor's message...
Looks like I've got now the plain version copy of the Emperor's message.
Time to leave...
Travel ending.


