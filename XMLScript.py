#authored by Ethan Gutierrez and Cayden Shaffer, but mostly Ethan

#insert file from argument in command line and search query 
from re import search
import sys
import xml.etree.ElementTree as ET
import os

rootDir = sys.argv[1]
searchQuery = []
foundEntries = False

if __name__ == "__main__":
	print("Using folder: " + rootDir)
	for arg in sys.argv: # get all search queries
		if arg == sys.argv[0] or arg == rootDir:
			continue
		searchQuery.append(arg)
		print("Searching for: " + arg)
	print("List of searches: " + ','.join(searchQuery))
#make output text file
outputFile = open('_'.join(searchQuery) + '.csv','w')
outputFile.write(','.join(searchQuery) + '\n')

#traverse folder
# print("Found: " + len(fileList) + " Files")
totalFiles = 0
for root, directory, fileList in os.walk(os.path.realpath(rootDir)):
	for fileName in fileList:
		totalFiles = totalFiles + 1
		#file parse XML
		tree = ET.parse(fileName).getroot()
		# loop through tree children #search parsed
		for child in tree: # items

			foundArray = [] 
			for index in len(searchQuery):
				foundArray.push(",")

			for grandchild in child.child: # elements of items
				index = searchQuery.index(grandchild.tag)
				if not (index == 0):
					foundEntries = True
					foundArray[index] = grandchild.tag + ","

			outputFile.write(''.join(foundArray) + '\n')
print("Searched: ", totalFiles, " Files")
if not foundEntries:
	print("Noting matched your search Queries")
else:
	print("Sucsess!")

#close file
outputFile.close()
print(os.path.realpath(outputFile.name))