# serialToCSV
Pass data from serial port into a Python data structure for further analysis

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
5. [Running the Program](#running-the-program)
6. [Acknowledgements](#acknowledgements)


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
- Windows OS
- Python
- PySerial
- msvcrt (Windows-specific package)
- time
- tkinter
- matplotlib
- numpy
- pandas
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
Press 's' to begin recording.  Press Enter to end and save:
```
5. The following output will appear after the key press.  This indicates that the program is currently collecting data froom the serial port for conversion to .csv later.
```
Beginning collection from serial port...
```
6. To terminate data recording at any time, press the Enter key.  A plot of the data recorded will be displayed, and the following output will be displayed:
```
Data collection has terminated. Please select the filepath:
```
7. After closing out of the plot, a pop-up window will appear.  Select the desired file name and location for the data set and press Enter.
8. The data saved is in .csv format in the location designated in the previous step with the headers 'Time (s)' and 'Voltage (V)'.

## Acknowledgements
This code contains content from the following tutorials and forums:
- 'Choosing a file in Python with simple Dialog', Stack Overflow
- 'Python - Infinite while loop, break on user input', Stack Overflow
- 'Plotting Serial Data from Arduino in Real Time with Python', The Poor Engineer
