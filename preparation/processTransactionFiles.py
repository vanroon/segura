#!/bin/python

import os
import csv
from decimal import Decimal

directory = '/home/evroon/stack/SEGURA/Rabobank/csv_processed/'
masterCsvFileName = '/home/evroon/stack/SEGURA/Rabobank/masterCsv/masterCsv.csv'
noDuplicatesMasterFile = '/home/evroon/stack/SEGURA/Rabobank/noDuplicatesMasterCsv.csv'

# TODO:

def createFile(fileName):
    f = open(fileName, 'w')
    f.close()

# get all files in a variable
def listFiles(directory):
	tempArray = os.listdir(directory)
	fileArray = []
	for fileName in tempArray:
		fullPathToFile = '%s%s' % (directory, fileName)
		fileArray.append(fullPathToFile)
	return fileArray

def writeLinesFromSingleFile(fullPathToFile, outputFile):
	with open(fullPathToFile) as f:
		csvMaster = open(outputFile, 'a')
		for line in f:
			csvMaster.write(line)
		csvMaster.close()

def removeDuplicatesFromMasterFile(masterFile):
    line_set = set()
    for line in open(masterFile, 'r'):
        if line not in line_set:
            line_set.add(line.rstrip())
    return line_set

def writeNoDuplicatesSetToFile(noDuplicatesSet, noDuplicatesFile):
    createFile(noDuplicatesFile)
    f = open(noDuplicatesFile, 'a')
    for line in noDuplicatesSet:

        f.write(line+'\n')
    f.close()

# def removeQuotesFromField(file, fieldNum):
#     with open(file, 'rb') as f:
#         reader = csv.reader(f, delimiter = ',')
#         for row in reader:
#             print Decimal(row[fieldNum])

def main():
    #Create file to hold all lines
    createFile(masterCsvFileName)


    listWithFiles = listFiles(directory)
    for fileName in listWithFiles:
        writeLinesFromSingleFile(fileName, masterCsvFileName)

    noDuplicatesSet = removeDuplicatesFromMasterFile(masterCsvFileName)
    writeNoDuplicatesSetToFile(noDuplicatesSet, noDuplicatesMasterFile)

    #





main()
