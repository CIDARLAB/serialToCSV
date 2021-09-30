# serialToCSV
Pass data from serial port into a Python data structure and .csv file for further analysis.  The script expects to read one value (voltage) from the serial port at a time and outputs a .csv file with two columns headed 'Time (s)' and 'Voltage (V)'.

## Table of Contents
1. [Features Summary](#features-summary)
   - 1.1 [Parameters](#parameters)
   - 1.2 [Functions](#functions)
   - 1.3 [Running Methods](#running-methods)
2. [Requirements](#requirements)
   - 2.1 [Computational Requirements](#computational-requirements)
   - 2.2 [Connections and Adapters](#connections-and-adapters)
3. [Installation Instructions](#installation-instructions)
4. [Finding Your Serial Port Number](#finding-your-serial-port-number)
5. [Setting the Serial Port Number and Baudrate](#setting-the-serial-port-number-and-baudrate)
6. [Running the Program](#running-the-program)
7. [Known Issues and Temporary Fixes](#known-issues-and-temporary-fixes)
8. [Acknowledgements](#acknowledgements)


## Features Summary
### Parameters
- set serial port (change inside serialToCSV.py)
- set baudrate (change inside serialToCSV.py)
### Functions
- open serial port
- read serial data
- export serial data to .csv file at end of data recording
- start data recording by pressing 's' key
- stop data recording by pressing 'Enter'
- option to record new data without reinitializing program
### Running Methods
- external python script

## Requirements
### Computational Requirements
- Windows 10 OS
- Python 3.9.6
- PySerial 3.5
- msvcrt (Windows-specific package)
- tkinter 8.6.10
- matplotlib  3.4.2
- numpy 1.20.3
- pandas 1.3.2
### Connections and Adapters
- USB-serial adapter

## Installation Instructions
1. Install conda
2. Download stc_env.yml and serialToCSV.py
3. Create the environment from stc_env.yml using
```
conda env create -f stc_env.yml
```
4. Make sure serialToCSV.py is in your current directory, where you'll run your script from

## Finding Your Serial Port Number
1. Open Device Manager on Windows 10 by searching for "Device Manager" on the search field in the taskbar.
2. Click on "Ports (COM & LPT)" to expand the list of ports on your computer.
3. Find "Arduino Uno" (or a name containing the name of the Arduino model you are using if not an Uno).
4. The name of the port is in parenthesis next to "Arduino Uno."

## Setting the Serial Port Number and Baudrate
The serial port number and baudrate are currently variables within serialToCSV.py with defines values.  Locate the below code block near the top of the file and change the port number and baudrate to suit your applications.  Save the script when finished with the changes.
```
# ***CHANGE VALUES FOR OWN APPLICATION***
portID = 'COM9'
baudRate = 9600
```

## Running the program
1. Open conda prompt.
2. Activate environment using
```
conda activate stc_env
```
3. Run program using
```
python -m serialToCSV.py
```
4. The following instructions will appear.  Press 's' to begin the recording.
```
Press 's' to begin recording.  
```
5. The following output will appear after the key press.  This indicates that the program is currently collecting data froom the serial port for conversion to .csv later.
```
Beginning collection from serial port...
Press Enter to end and save:
```
6. To terminate data recording at any time, press the Enter key.  A plot of the data recorded will be displayed, and the following output will be displayed:
```
Data collection has terminated. Please select the filepath:
```
7. After closing out of the plot, a pop-up window will appear.  Select the desired file name and location for the data set and press Enter.
8. The data saved is in .csv format in the location designated in the previous step with the headers 'Time (s)' and 'Voltage (V)'.

## Known Issues and Temporary Fixes
1. Erroneous initial reading

When developing the program, it was found that some values read by the Arduino at the beginning of initializing the script would at times cause the script to throw a value error and abort the program.  To prevent these erroneous values from interfering from ending the program prematurely, a piece of code shown below was designed to catch these values and reassign a dummy value of -5 to them.  It is unknown at this time what causes these erroneous values.
```
 if not string:
    string = '-5'  # dummy value in case of erroneous value
```
When post-processing the `vltg` DataFrame within Python or the .csv file, take care to remove the -5 values.

2. Error message when running script after compiling Arduino script

conda may throw a value error (shown below) if the Python script is run in quick succession to an Arduino code compile.
![alt text](https://github.com/CIDARLAB/serialToCSV/blob/main/errormsg.png?raw=true)
Please wait for at least one minute after compiling to run the code in order to avoid this error.


## Acknowledgements
This code contains content from the following tutorials and forums:
- 'Choosing a file in Python with simple Dialog', Stack Overflow
- 'Python - Infinite while loop, break on user input', Stack Overflow
- 'Plotting Serial Data from Arduino in Real Time with Python', The Poor Engineer
