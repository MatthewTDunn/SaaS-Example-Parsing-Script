# Data Handling/Parsing Script SaaS Example

An example of a SaaS python script I wrote to automate the handling of data from an analytical process in a local laboratory.

![Example GIF](https://github.com/Pyr1te/SaaS-Example-Parsing-Script/blob/main/Example.gif?raw=true)

# How it works:

In this particular example, the clients analytical instrument would process a sample and store an individual .MES result file in a specified directory. Through the software provided by the instrument manufacturer, the result output file was set to "/Particle Count Results" of the .py master file. Once the analyst had finalised their instrumental work for the day, the script would be run and a single .CSV file produced for easy importing into their Laboratory Information Management System (LIMS).

Due to inaccesibility and IT restrictions around the clients backend data storage, automatic update directly to their LIMS was prohibited.

# Reason for Implementation:

As described by the client and under typical laboratory workload conditions, this instrument could be responsible for analysing upwards of a 100 samples a day - resulting in 100 individual .MES files.

Prior to the implementation of this parsing script, the client would open each individual .MES file and paste the entirety into a formulated excel workbook. Through basic excel functionality, the result line was examined and formatted appropriately so the client could copy and paste it to a separate sheet and collate a list of results for the day. Once the list was ready, it was manually copied across to their LIMS for scrutiny and reporting.

This process is cumbersome, particularly prone to human error and required automation.

# Cost Savings:

With in-house IT software development capability lacking and no support from the instrument manufacturer, I was able to provide the client with a lean data handling solution to this previously manual process.

The automation of the manual process has alleviated (at minimum), half an hour of a laboratory technicians daily workload and <strong>saved the client upwards of $3,900 annually in addition to removing a data handling process prone to human error. </strong>
