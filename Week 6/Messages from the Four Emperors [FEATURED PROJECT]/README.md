# A6_T7 Messages from the Four Emperors
A Python Project in VS Code

Each of the Four Emperors—Galba, Otho, Vitellius and Vespasian—has left a message in their own palaces. Your task is to travel programmatically to each location and gather all their messages.


You may travel only once per program run. Travel should begin by displaying the current location, followed by the process of traveling to the next location. The first location is the “start” or “Home” location on the map below.

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/eb028690-58f7-4173-9db5-8b067a3ad86b" />



Place names listed:

0. home
1. Galba's palace
2. Otho's palace
3. Vitellius' palace
4. Vespasian's palace


Create a file “player_progress.txt” and initialize it with the following details
-
<img width="497" height="129" alt="image" src="https://github.com/user-attachments/assets/1755c5d8-5f51-4a4b-8737-dca025a2d5ba" />



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

File 1
---
<img width="837" height="340" alt="image" src="https://github.com/user-attachments/assets/c13810de-d693-43c4-9a4e-567cd3e92c61" />

File 2
----

<img width="828" height="345" alt="image" src="https://github.com/user-attachments/assets/8295ffe9-e98f-4dbb-91d1-7e2f88b2c3c1" />




After the progress and the Emperor’s message have been saved, the program closes with the final phrases. The next time the program runs, it should be able to read the previous progress from player_progress.txt and continue the next turn.

Example program runs:

<img width="706" height="389" alt="image" src="https://github.com/user-attachments/assets/64fa53f9-c3d6-45e8-890a-dda60f7eb953" />


