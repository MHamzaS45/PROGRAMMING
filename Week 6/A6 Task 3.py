#A6 Task 3
print ("Program starting.")
print ("This program can copy a file.")
SourceFileName = input("Insert source file name: ")
DestFileName = input("Insert destination file name: ")
sourceFile = open(SourceFileName, "r", encoding="utf-8")
print (f"Reading file, {SourceFileName} content")
print ("File content ready in memory")
destFile = open(DestFileName, "w", encoding="utf-8")
print ("Writing content into file", destFile)
while True:
    line = sourceFile.readline()
    if len(line) == 0:
        break
    destFile.write(line)
sourceFile.close()
destFile.close()
print ("Copying operation complete")
print ("Program ending.")
