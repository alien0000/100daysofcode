#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
import os

with open("Input/Letters/starting_letter.txt") as file:
    line=file.read()
    # print(line)
    with open("Input/Names/invited_names.txt") as nameFile:
        # for i in range(1,8):
            newNameList=nameFile.read().splitlines()
            # print(newName)
            # newName=nameFile.readline()
            for newName in newNameList:
                newLine=line.replace("[name]",newName)
                # print(newLine)
                newLetter=newLine.strip()
                # print(newLetter)
                with open(os.path.join("Output/ReadyToSend/",newName+".txt"),mode='w') as output:
                    output.write(newLetter)

