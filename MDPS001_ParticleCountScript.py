    #Code written by Matthew Dunn

    #REQUIREMENTS#
    #This script must be run in a master folder where the two following subfolders exist:
    #1) Particle Count Results [this is for actual data]
    #2) Archived Data [all parsed data will be moved to this location]
    #3) The .mes files to be parsed are semi-colon delimited. If this changes, the script will no longer work

    #Appendix:
    #- A - Library Importing
    #- B - Determination of parse file count
    #- C - Set the script run date for logging purposes
    #- D - Iterate through .mes data files and collect appropriate information, split into appropriate lists
    #- E - Create parse points & particle count data variables
    #- F - Splitting result data into appropriate particle sizes & iso code python lists
    #- G - Move parsed files to archive directory so repeat parsing doesn't happen using SHUTIL
    #- H - list from section F split via additional concatenated ','
    #- I - Write parsed data to file "ParticleCountData" located in master directory

    #- Z - Log script run data after execution

    #Error List:
    #- ERR1 - No .mes files present in data directory



#-SCRIPT-#

# - A - 
# Import CSV & file handling libraries
import csv
from ntpath import join
import os
import pathlib
import shutil

from pathlib import Path
from os.path import exists
from csv import writer

mattScriptErrorCode = "NUL"

# - B - 
# Determine how many files there are to parse 

fileCount = 0
for path in pathlib.Path("./Particle Count Results").iterdir():
    if path.is_file():
        fileCount += 1

# - C - 
# Write script execution date/time to scriptExecutionDate for troubleshooting/logging purposes#

from datetime import datetime
scriptExecutionDate = datetime.now()
scriptExecutionDateTime = scriptExecutionDate.strftime("%d/%m/%Y %H:%M:%S")

# - D -
#this code iterates over all files with extension .mes and records their file name
pathlist = Path(".\Particle Count Results").glob('**/*.mes')

# - E - 
# Establish the parse points variables for data isolation:
pp4umINDEXA = 0
pp4umINDEXB = 0
pp6umINDEXA = 0
pp6umINDEXB = 0
pp10umINDEXA = 0
pp10umINDEXB = 0
pp14umINDEXA = 0
pp14umINDEXB = 0
pp21umINDEXA = 0
pp21umINDEXB = 0
pp25umINDEXA = 0
pp25umINDEXB = 0
pp38umINDEXA = 0
pp38umINDEXB = 0
pp70umINDEXA = 0
pp70umINDEXB = 0
ppISOAINDEXA = 0
ppISOAINDEXB = 0
ppISOBINDEXA = 0
ppISOBINDEXB = 0
ppISOCINDEXA = 0
ppISOCINDEXB = 0

#establish the particle count data handlers

data4um = ""
data6um = ""
data10um = ""
data14um = ""
data21um = ""
data25um = ""
data38um = ""
data70um = ""
dataISOcodeA = ""
dataISOcodeB = ""
dataISOcodeC = ""

#first parse array/list data to be stored in following globals
parsedDeterminationDate=[]
parsedSampleID=[]
parsedResults=[]

# - F -
# Splitting result data into appropriate particle sizes & iso code python lists

for path in pathlist:
    pathInString = str(f".\{path}")
    print(os.path.basename(pathInString))
    with open(f".\{pathInString}","r",newline="") as f:
        reader = csv.reader(f)
        rows = list
        #if the file to be parsed has contains NUL
        if '\0' in open(pathInString).read():
            reader = csv.reader(x.replace('\0','') for x in f)

        for row in reader:
            totalParsedData = [row for idx, row in enumerate(reader) if idx in (4,5,27)]

            #append parsed data to appropriate lists

            parsedDeterminationDate.append(totalParsedData[0])
            parsedSampleID.append(totalParsedData[1])
            parsedResults.append(totalParsedData[2])

            #convert the list objects to a string for secondary parsing & isolate each data point to individual list
            #we are utilising key markers in ' and ; to determine stripping indexes

            secondaryParsedResults = str(totalParsedData[2])
            #----
            pp4umINDEXA = secondaryParsedResults.find("'")+1
            pp4umINDEXB = secondaryParsedResults.find("'",pp4umINDEXA+1)
            data4um = data4um + secondaryParsedResults[pp4umINDEXA:pp4umINDEXB] + ','

            pp6umINDEXA = secondaryParsedResults.find("'",pp4umINDEXB)+4
            pp6umINDEXB = secondaryParsedResults.find("'",pp6umINDEXA)
            data6um = data6um + secondaryParsedResults[pp6umINDEXA+3:pp6umINDEXB] + ','

            pp10umINDEXA = secondaryParsedResults.find("'",pp6umINDEXB)+4
            pp10umINDEXB = secondaryParsedResults.find("'",pp10umINDEXA)
            data10um = data10um + secondaryParsedResults[pp10umINDEXA+3:pp10umINDEXB] + ','

            pp14umINDEXA = secondaryParsedResults.find("'",pp10umINDEXB)+4
            pp14umINDEXB = secondaryParsedResults.find("'",pp14umINDEXA)
            data14um = data14um + secondaryParsedResults[pp14umINDEXA+3:pp14umINDEXB] + ','

            pp21umINDEXA = secondaryParsedResults.find("'",pp14umINDEXB)+4
            pp21umINDEXB = secondaryParsedResults.find("'",pp21umINDEXA)
            data21um = data21um + secondaryParsedResults[pp21umINDEXA+3:pp21umINDEXB] + ','

            pp25umINDEXA = secondaryParsedResults.find("'",pp21umINDEXB)+4
            pp25umINDEXB = secondaryParsedResults.find("'",pp25umINDEXA)
            data25um = data25um + secondaryParsedResults[pp25umINDEXA+3:pp25umINDEXB] + ','

            pp38umINDEXA = secondaryParsedResults.find("'",pp25umINDEXB)+4
            pp38umINDEXB = secondaryParsedResults.find("'",pp38umINDEXA)
            data38um = data38um + secondaryParsedResults[pp38umINDEXA+3:pp38umINDEXB] + ','

            pp70umINDEXA = secondaryParsedResults.find("'",pp38umINDEXB)+4
            pp70umINDEXB = secondaryParsedResults.find("'",pp70umINDEXA)
            data70um = data70um + secondaryParsedResults[pp70umINDEXA+3:pp70umINDEXB] + ','

            ppISOAINDEXA = secondaryParsedResults.find(";",pp70umINDEXB)+1
            ppISOAINDEXB = secondaryParsedResults.find(";",ppISOAINDEXA)
            dataISOcodeA = dataISOcodeA + secondaryParsedResults[ppISOAINDEXA:ppISOAINDEXB] + ','

            ppISOBINDEXA = secondaryParsedResults.find(";",ppISOAINDEXB)+1
            ppISOBINDEXB = secondaryParsedResults.find(";",ppISOBINDEXA)
            dataISOcodeB = dataISOcodeB + secondaryParsedResults[ppISOBINDEXA:ppISOBINDEXB] + ','

            ppISOCINDEXA = secondaryParsedResults.find(";",ppISOBINDEXB)+1
            ppISOCINDEXB = secondaryParsedResults.find(";",ppISOCINDEXA)
            dataISOcodeC = dataISOcodeC + secondaryParsedResults[ppISOCINDEXA:ppISOCINDEXB] + ','

# - G -
# Move parsed files to archive so repeat parsing doesn't happen using SHUTIL

    shutil.move(pathInString,f".\Archived Results\{os.path.basename(pathInString)}")
    
# - H -
# list from section F split via additional concatenated ','

list4um = data4um.split(',')
list6um = data6um.split(',')
list10um = data10um.split(',')
list14um = data14um.split(',')
list21um = data21um.split(',')
list25um = data25um.split(',')
list38um = data38um.split(',')
list70um = data70um.split(',')
listISOA = dataISOcodeA.split(',')
listISOB = dataISOcodeB.split(',')
listISOC = dataISOcodeC.split(',')

print(len(parsedResults))

#- I -
# Write parsed data to file "ParticleCountData" located in master directory

ExportHeader=['DeterminationDate','SampleID','4um','6um','10um','14um','21um','25um','38um','70um','ISO_A','ISO_B', 'ISO_C']

outputExists = 'ParticleCountData.csv'
outputPath = Path(outputExists)
#create the file/write the header to it if it doesn't exist.
if outputPath.is_file:
    print('ParticleCountData.csv File Exists')
else:
    with open('ParticleCountData.csv','w', newline="") as f:
        w = writer(f)
        w.writerow(ExportHeader)

#append the data to the currently existing file.
for i in range(0,len(parsedDeterminationDate)):
    with open('ParticleCountData.csv','a',newline="") as f:
        appendData = writer(f)
        appendData.writerow(parsedDeterminationDate[i] + parsedSampleID[i] + list4um[i].split(",") + list6um[i].split(",") + list10um[i].split(",") + list14um[i].split(",") + list21um[i].split(",") + list25um[i].split(",") + list38um[i].split(",") + list70um[i].split(",") + listISOA[i].split(",") + listISOB[i].split(",") + listISOC[i].split(","))
    f.close    

# - Z - 

# Log script run data after execution
logFileAuthorContact=["Bureau Veritas Particle Count Parse Script Written by Matthew Dunn: Any issues, please contact me at dunn0139@gmail.com"]
logFileHeader=['Execution Time','Count of files to parse','Parsed Files','MattScript Error Code']
logFileData=[scriptExecutionDateTime,fileCount,fileCount,mattScriptErrorCode]

# check to see if the log file exists first, if so, append data to it, if not, create it and write run data
scriptLogExists = 'MattScriptLog.csv'
path = Path(scriptLogExists)
if path.is_file():
    with open('MattScriptLog.csv','a',newline="") as f:
        appendScriptLog = writer(f)
        appendScriptLog.writerow(logFileData)
        f.close()
else:
    with open('MattScriptLog.csv','w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(logFileAuthorContact)
        writer.writerow(logFileHeader)
        writer.writerow(logFileData)

