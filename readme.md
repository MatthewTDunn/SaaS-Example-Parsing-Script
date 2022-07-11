[GitHub] (https://github.com/Pyr1te/MDPS001 "Github MDPS001 Home")

Particle Count Parsing Script & File Handler
----------------------------
Code written by Matthew Dunn

REQUIREMENTS#
This script must be run in a master folder where the two following subfolders exist:
1) Particle Count Results [this is for actual data]
2) Archived Data [all parsed data will be moved to this location]
3) The .mes files to be parsed are semi-colon delimited. If this changes, the script will no longer work

Appendix:
- A - Library Importing
- B - Determination of parse file count
- C - Set the script run date for logging purposes
- D - Iterate through .mes data files and collect appropriate information, split into appropriate lists
- E - Create parse points & particle count data variables
- F - Splitting result data into appropriate particle sizes & iso code python lists
- G - Move parsed files to archive directory so repeat parsing doesn't happen using SHUTIL
- H - list from section F split via additional concatenated ','
- I - Write parsed data to file "ParticleCountData" located in master directory

- Z - Log script run data after execution

Error List:
- ERR1 - No .mes files present in data directory
