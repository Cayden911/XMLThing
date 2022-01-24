#authored by Ethan Gutierrez and Cayden Shaffer, but mostly Ethan

#insert file from argument in command line and search query
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
		tree = ET.parse(os.path.realpath(os.path.join(rootDir, fileName))).getroot()
		# loop through tree children #search parsed
		for child in tree.findall('{http://infor.com/daf}item'): # items
			foundArray = [] 
			for index in searchQuery:
				foundArray.extend(",")

			for search in searchQuery:
				if(child.find('{http://infor.com/daf}' + (search)) is not None):
					foundEntries = True
					foundArray.append(child.find('{http://infor.com/daf}' + (search)).text)
			outputFile.write(''.join(foundArray) + '\n')

print("Searched: ", totalFiles, " Files")
if not foundEntries:
	print("Noting matched your search Queries")
else:
	print("Sucsess!")

#close file
outputFile.close()
print(os.path.realpath(outputFile.name))