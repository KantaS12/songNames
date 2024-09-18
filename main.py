import string #imports string

#Popular Names
def findName(name, outputFile):
  inFile = open("allNames.csv", "r") #Read the file "allNames.csv"
  next(inFile) #Skipping the first header
  
  joinedFile = "".join(["tests/",outputFile]) #joining both the test folder and output to have output into folder
  outFile = open(joinedFile, "w") #making the outputfile
  outFile.write("Artist,Song,Year") #Writing the header onto the new file

  dictionary = {} #Make a dictionary
  newList = [] #Make a list

  for aline in inFile:
    stripline = aline.strip() #Strips all unwanted
    splitline = stripline.split("\t") #Split the strings into a list by '\t'
    names = splitline[5] #Defining the name that was featurned in the song
    
    if name in names:
      newstring = splitline[0] + "," + splitline[1] + "," + splitline[3]  
      #Add up all the Artists, Song, and Year with a comma in between
      dictionary[newstring] = 0 #Add it all in a dictionary to sort out duplicates
      
  for items in dictionary: #Print all the things into the new file
    outFile.write("\n")
    outFile.write(items)
  inFile.close()
  
#Repeat Names
def findRepeatedNameSongs(threshold, outputfile): #Defining Function
  inFile = open("allNames.csv", "r") #Read the file "allNames.csv"
  next(inFile) #Skipping the first header
  
  joinedFile = "".join(["tests/",outputfile]) #joining both the test folder and output to have output into folder
  outFile = open(joinedFile, "w")
  outFile.write("Names,Times,Artist,Song") #Writing the header onto the new file
  outFile.write("\n") 
  
  dictionary1 = {} #making a dictionary for names
  dictionary2 = {} 
  mixedDict = {} # name artist and song dictionary 

  for aline in inFile: #create a loop to go through each line of the file
    stripline = aline.strip("\n") # end of the line strip
    splitline = stripline.split("\t") # split by tabs inbetween values
    sentence = splitline[5] # splitting the "name" values
    
    if sentence != "name": # if loop to count the number of occurences
      dictionary1[sentence] = dictionary1.get(sentence, 0) + 1 #actual code to count repeat names

    name = splitline[5] #splitting by the actual name being counted
    artist = splitline[0] #splitting by artist of the song
    song = splitline[1] # splitting by the name of the song 
    mix = (name, artist, song) # including all values necessary to analyze
    mixedDict[mix] = mixedDict.get(mix, 0) + 1 #creating the mixed dictionary

    result = {key:value for (key, value) in mixedDict.items() if value >= threshold} #code to outline threshold in analysis 
    sortedResult = sorted(result.items(), key=lambda x:x[1], reverse=True) #sorting the amount of occurences from greatest to least
    newDict = dict(sortedResult) 
    
  for (k, v) in newDict.items(): #generating for loop to organize the output file
    outFile.write(k[0]) #pull the first column of data ie- Names
    outFile.write(",") #separate by comma to be a "CSV"
    outFile.write(str(v)) #Pull the number of times the name occurred within a song
    outFile.write(",")#separate by comma to be a "CSV"
    outFile.write(k[1]) #pull the artist of the song      
    outFile.write(",")#separate by comma to be a "CSV"
    outFile.write(k[2]) #pull the name of the song
    outFile.write("\n") # end of line
  inFile.close() #closing the for loop that generates the output file
  
#Unique Names
def findUniqueNameSongs(threshold, outputfile): #Defining Function
  inFile = open("allNames.csv", "r")  #Read the file "allNames.csv"
  next(inFile) #Skipping the first header
  
  joinedFile = "".join(["tests/",outputfile]) #joining both the test folder and output to have output into folder
  outFile = open(joinedFile, "w")
  outFile.write("Number,Artist,Song") #organizing what will be included in the outfile
  outFile.write("\n") # end of line 
  
  dictionary1 = {} #creating new dictionary
  prevartist = "" #looking at the previous artist to see if it aligns

  for aline in inFile: # loop to go through each line of a file
    stripline = aline.strip("\n") # splitting the original file by line
    splitline = stripline.split("\t") #splitting each line between the tabs separating the values

    name = splitline[5] #pulling the name being analyzed
    song = splitline[1] #pulling the song being analyzed
    artist = splitline[0] #pulling the artist of the song being analyzed
    
    if prevartist != artist: #for loop to recognize when the artists are not the same 
      diffnames = len(dictionary1) # counting the amount of unique names within a song
      
      if prevartist != "" and diffnames >= threshold: #nested if to only include the threshold of unique names within a song to be included
        outFile.write(str(diffnames) + "," + artist + "," + song + "\n") # produce outfile that includes the string value of the unique name itself, the artist, and the song for each line
      prevartist = artist 
      dictionary1.clear() #clears the dictionary
    dictionary1[name] = True #makes the artists with assigned to a variable with all the unique names
  diffnames = len(dictionary1) #the length of the unique names
  if diffnames >= threshold: #if the len >= threshold then
    outFile.write(str(diffnames) + "," + artist + "," + song + "\n")
    #Write the amount of unique names, the artist, then the song
  inFile.close()
#Timeless Names 
def countNameDecades(name, outputfile): #Defining Function
  inFile = open("allNames.csv", "r") #Read the file "allNames.csv"
  next(inFile) #Skipping the first header
  
  joinedFile = "".join(["tests/",outputfile]) #joining both the test folder and output to have output into folder
  outFile = open(joinedFile, "w") #making the outputfile
  outFile.write("Number,Decade") # defining the necessary headers included in the outfile
  outFile.write("\n") #separating each of the lines
  
  decades = {} #generating a new dictionary
  decades[1970] = 0 #number of songs in the 1970s
  decades[1980] = 0 #number of songs in the 1980s
  decades[1990] = 0 #number of songs in the 1990s
  decades[2000] = 0 #number of songs in the 2000s
  decades[2010] = 0 #number of songs in the 2010s

  for aline in inFile:
    stripline = aline.strip("\n") #strips all the "\n" at the end
    splitline = stripline.split("\t") #splits the lines by the spaces

    year = splitline[3] #assigning year
    names = splitline[5] #assinging names
    
    if name == names: #if name that is provided is equal to the names in the file... 
      if 1970 <= int(year) < 1980: #if the year is greater or equal to 1970 and less than 1970...
        decades[1970] += 1 #then the total number is counted up to 1 
      elif 1980 <= int(year) < 1990: #^ same but with 1980 and 1990
        decades[1980] += 1 
      elif 1990 <= int(year) < 2000: #^ same thing but with 1990 and 200
        decades[1990] += 1
      elif 2000 <= int(year) < 2010: #^ same thing but with 2000 and 2010
        decades[2000] += 1
      elif 2010 <= int(year) < 2020: #^ same thing but with 2010 and 2020
        decades[2010] += 1 
    
    sortedResult = sorted(decades.items()) #sorts into the amount of decades
    sortedDict = dict(sortedResult) #make it into a dictionary
    
  for (k, v) in sortedDict.items(): # for item and value in the dictionary
    outFile.write(str(v) + "," + str(k) + "\n") #value of the decade, and the decade
  inFile.close()      
  
#Lettering 
def countStartLetter(outputfile):
  inFile = open("allNames.csv", "r") #opening allnames
  inFile2 = open("onlyNames.csv", "r") #open onlynames
  next(inFile) #skip header
  next(inFile2) #skip header

  joinedFile = "".join(["tests/",outputfile]) #joining both the test folder and output to have output into folder
  outFile = open(joinedFile, "w") #making the outputfile
  outFile.write("letter,proportion") #write file letter, proportion
  outFile.write("\n") # spacing inbetween 
  
  namesdict = dict.fromkeys(string.ascii_uppercase, 0) #assign a dictionary with uppercase keys and assign it to 0 
  namesongdict = dict.fromkeys(string.ascii_uppercase, 0) #assign another dictionary with uppercase keys and assign it to 0 
  count1 = 0 #first count = 0 
  count2 = 0 #second count = 0 
  newList = [] #assign a new list called newList
  percentList = [] #assign a new list called percentList
  
  for aline in inFile2: #ONLY NAMES
    stripline = aline.strip("\n") #strip the lines with the "\n" at the ends
    splitline = stripline.split("\t") #split the lines with the spaces inbetween 

    count1 += 1 #counting the total amount of lines 
    
    number = splitline[1] #assigning a variable with the different count of the names in the social security 
    intnumber = int(number) #making the string into an integer 
    
    names = splitline[0] #assigning the different names in the names
    character = names[0] #assigning another variable with the first character of the name
 
    if intnumber >= 5000: #if the number is greater or equal to 5000...
      if character in namesdict.keys(): #if the character is already in the alphabet 
        namesdict[character] += 1 #count up
      else: 
        namesdict[character] = 1 #if it's not already in the dictionary then make it to 1 
      #anything else is equal to 0 
  
  sorted1 = sorted(namesdict.items()) #sort by the alphabet 
  sortedDict1 = dict(sorted1) #make it into the dictionary
  
  for akey in sortedDict1.keys(): #for the different numbers in the dictionary... 
    n = sortedDict1[akey] #assign the numbers to n 
    percent = (n / count1) * 100 #divide n by the count and multiplied to 100 and that's how you calc the percentage
    sortedDict1[akey] = percent #assign the different alphabets with their new percentage
  namesValueList = list(sortedDict1.values()) #make the dictionary into the list

  for aline in inFile: #ALL NAMES
    stripline = aline.strip("\n") #strips the line "\n" at the end
    splitline = stripline.split("\t") #splits the lines with the spaces

    count2 += 1 #counts all the lines in the file 

    names = splitline[5] #assign names with the names in the song
    character = names[0] #assign character as the first character in the name
    
    if character in namesongdict.keys(): #for the characters in the dictionary
      namesongdict[character] += 1 #count 1 if it's already located in the dictionary
    else:
      namesongdict[character] = 1  #anything else assign it to 1 
      
  sorted2 = sorted(namesongdict.items()) #sort it by alphabet
  sortedDict2 = dict(sorted2) #make it into a dicionary
  
  for akey in sortedDict2.keys(): #for different variables in the dictionary
    n = sortedDict2[akey] #assign the varaible n to the numbers
    percent = (n / count2) * 100 #get the percentage with n divided by the total number of lines times 100
    sortedDict2[akey] = percent #assign the alphabet with the new percentage
  namesValueList2 = list(sortedDict2.values()) #make it into a list

  alphabet = list(string.ascii_uppercase) #assign a new list with all the alphabet uppercase
  for i in range(26): #throughtout the alphabet
    roundedN = round((namesValueList2[i] - namesValueList[i]),2) #round the numbers of percentage of the songs with the social security by 2 decimal places
    newList.append(str(roundedN)) #Append a newlist with the string of the difference of percentages
    
  for i in range(26): #throughout the alphabet
    percentList.append(alphabet[i] + "," + newList[i] + "%") #assign a new list with the alphabet, percentage difference%
    
  for i in percentList: #For the different things in the percentage list...
    outFile.write(i) #write the different lines
    outFile.write("\n") #with the spaces in between the lines
  inFile.close()
  inFile2.close()
  
def countEndLetter(outputfile):
  inFile = open("allNames.csv", "r") #open all names
  inFile2 = open("onlyNames.csv", "r") #open only names
  next(inFile) #skip header
  next(inFile2) #skip header

  joinedFile = "".join(["tests/",outputfile]) #joining both the test folder and output to have output into folder
  outFile = open(joinedFile, "w") #making the outputfile
  outFile.write("letter,proportion") #write letter and proportion 
  outFile.write("\n") #seperate with a space 

  namesdict = dict.fromkeys(string.ascii_lowercase, 0) #assign a dictionary with uppercase keys and assign it to 0 
  namesongdict = dict.fromkeys(string.ascii_lowercase, 0) #assign another dictionary with uppercase keys and assign it to 0 
  count1 = 0 #first count = 0 
  count2 = 0 #second count = 0 
  newList = [] #assign a new list called newList
  percentList = [] #assign a new list called percentList
  
  for aline in inFile2: #ONLY NAMES
    stripline = aline.strip("\n") #strips the line "\n" at the end
    splitline = stripline.split("\t") #splits the lines with the spaces

    count1 += 1 #counts all the lines in the file 
    
    number = splitline[1] #assigning the different names in the names
    intnumber = int(number) #making the string into an integer 
    
    names = splitline[0] #assigning the different names in the names
    character = names[-1] #assigning another variable with the last character of the name
 
    if intnumber >= 5000: #if the number is greater or equal to 5000...
      if character in namesdict.keys(): #if the character is already in the alphabet 
        namesdict[character] += 1 #count up
      else: 
        namesdict[character] = 1 #if it's not already in the dictionary then make it to 1 
      #anything else is equal to 0 
        
  sorted1 = sorted(namesdict.items()) #sort it by alphabet
  sortedDict1 = dict(sorted1) #make it into a dictionary
  
  for akey in sortedDict1.keys(): #for different variables in the dictionary
    n = sortedDict1[akey] #assign the varaible n to the numbers
    percent = (n / count1) * 100 #get the percentage with n divided by the total number of lines times 100
    sortedDict1[akey] = percent #assign the alphabet with the new percentage
  namesValueList = list(sortedDict1.values()) #make it into a list

  
  for aline in inFile: #ALL NAMES
    stripline = aline.strip("\n") #strips the line "\n" at the end
    splitline = stripline.split("\t") #splits the lines with the spaces

    count2 += 1 #counts all the lines in the file 

    names = splitline[5] #assign names with the names in the song
    character = names[-1] #assign character as the last character in the name
    
    if character in namesongdict.keys(): #for the characters in the dictionary
      namesongdict[character] += 1 #count 1 if it's already located in the dictionary
    else:
      namesongdict[character] = 1 #anything else assign it to 1
  sorted2 = sorted(namesongdict.items()) #sort it by alphabet
  sortedDict2 = dict(sorted2) #make it into a dictionary
  
  for akey in sortedDict2.keys(): #for different variables in the dictionary
    n = sortedDict2[akey] #assign the variables n of the numbers
    percent = (n / count2) * 100 #get the percentage with n divided by the total number of lines times 100
    sortedDict2[akey] = percent #assign the alphabet with the new percentage
  namesValueList2 = list(sortedDict2.values()) #make it into a list
  
  alphabet = list(string.ascii_lowercase) #assign a new list with all the alphabet uppercase
  
  for i in range(26): #throughtout the alphabet
    roundedN = round((namesValueList2[i] - namesValueList[i]),2) #round the numbers of percentage of the songs with the social security by 2 decimal places
    newList.append(str(roundedN)) #Append a newlist with the string of the difference of percentages
    
  for i in range(26): #throughtout the alphabets
    percentList.append(alphabet[i] + "," + newList[i] + "%") #assign a new list with the alphabet, percentage difference%
    
  for i in percentList: #For the different things in the percentage list...
    outFile.write(i) #write the different lines
    outFile.write("\n") #with the spaces in between the lines
  inFile.close()
  inFile2.close()
                         
def main():
  findName("Mary", "mary.csv")
  findName("Jack", "jack.csv")
  findName("Peter", "peter.csv")

  findRepeatedNameSongs(40, "repeat.40.csv")
  findRepeatedNameSongs(30, "repeat.30.csv")
  findRepeatedNameSongs(20, "repeat.20.csv")

  findUniqueNameSongs(15, "unique.15.csv")
  findUniqueNameSongs(20, "unique.20.csv")

  countNameDecades("Mary", "Mary.decades.csv")
  countNameDecades("Joe", "Joe.decades.csv")
  countNameDecades("Mark", "name_of_choice.decades.csv")

  countStartLetter("names.start.csv")
  countEndLetter("names.end.csv")


if __name__ == "__main__":
  main()
