#authored by Ethan Gutierrez and Cayden Shaffer, but mostly Ethan, by mostly I mean all

#insert file from argument in command line and search query
import sys
import xml.etree.ElementTree as ET
import os

#check to make sure that program has requrired args
#if(len(sys.argv) < 3):
#	print("It looks like you forgot to input something")
#	print("Usage: python XMLScript.py FOLDER_OF_XML TAGS [...]")
#	exit()
searchQuery = [] #things to pull out of the xmls
foundEntries = False

print("Input path to the XML Folder: ", end='')
rootDir = input().replace("\"", "") #folder for xmls
print("Input nothing and press enter to continue")
while True:
	print("Input search tag[" + str(len(searchQuery)) + "]: ", end='')
	search = input()
	if(search == ""):
		break
	searchQuery.append(search)


#make output text file
outputFile = open('_'.join(searchQuery) + '.csv','w')
outputFile.write(','.join(searchQuery) + '\n')

#traverse folder files 
totalFiles = 0
for root, directory, fileList in os.walk(os.path.realpath(rootDir)):
	for fileName in fileList: #for each file in folder
		totalFiles = totalFiles + 1
		#file parse XML
		tree = ET.parse(os.path.realpath(os.path.join(rootDir, fileName))).getroot()
		nsIndex = tree.tag.index('}') + 1 #gets XML namespace
		nameSpace = tree.tag[0:nsIndex]
		for child in tree.findall(nameSpace + 'item'): # items
			foundArray = [] #holds the elements found in the element
			for index in searchQuery:
				foundArray.extend(",")
			#checks element for each of the search queries 
			for search in searchQuery:
				if(child.find(nameSpace + (search)) is not None):
					foundEntries = True
					foundArray[searchQuery.index(search)] = (child.find(nameSpace + (search)).text).strip()
			#writes to the file
			outputFile.write(','.join(foundArray) + '\n') 

print("Searched: ", totalFiles, " Files")
if not foundEntries:
	print("Noting matched your search Queries")
else:
	print("Success!")

#close file
outputFile.close()
print("Output file located at: " + os.path.realpath(outputFile.name))
print("Press enter to exit program")
done = input()