# This program has the following aims:
# 1. Starting and stopping recording process by pressing 's' and 'Enter',
# # respectively
# 2. Transfer data read by Arduino into a Python DataFrame via the serial port
# 3. Visualized the collected data (currently plotting after recording ends to avoid
# sampling rate issues)
# 4. Write the DataFrame to a CSV file with appropriate headers
# 5. Allows user to repeat above process without restarting the program.
#
# Acknowledgements:
# This code contains content from the following tutorials and forums:
# - 'Choosing a file in Python with simple Dialog', Stack Overflow
# - 'Python - Infinite while loop, break on user input', Stack Overflow
# - 'Plotting Serial Data from Arduino in Real Time with Python', The Poor Engineer


import msvcrt
import time
import tkinter as tk
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import serial

# initiate program variables
contLoop = True
newRead = True
run = 1

# ***CHANGE VALUES FOR OWN APPLICATION***
portID = 'COM9'
baudRate = 9600

# prompt user to begin measurement
strt = input("Press 's'+Enter to begin recording.")

if strt == 's':
    while newRead:
        i = 0
        # open serial port
        ser = serial.Serial(portID, baudRate, timeout=1)
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        print('Beginning collection from serial port...')
        print('Press Enter to end and save.')
        while True:
            line = ser.readline()  # reads a single byte string
            string = line.decode()  # convert line to string
            string = string.strip()  # strip string of \b\n
            if not string:
                string = '-5'  # dummy value in case of erroneous value
            string = float(string)
            t = time.perf_counter()
            if i == 0:
                i += 1
                init = t
                elpstm = t - init
                dat = np.array([(elpstm, string)], dtype=[("Time (s)", "float64"), ("Voltage (V)", "float64")])
                vltg = pd.DataFrame(data=dat)
            else:
                elpstm = t - init
                newData = np.array([(elpstm, string)], dtype=[("Time (s)", "float64"), ("Voltage (V)", "float64")])
                newDataFrame = pd.DataFrame(data=newData)
                vltg = vltg.append(newDataFrame, ignore_index=True)  # store elapsed time and voltage into DataFrame
            # detect Enter key input.  End data recording if hit.
            if msvcrt.kbhit():
                if msvcrt.getwche() == '\r':
                    ser.reset_input_buffer()
                    ser.reset_output_buffer()
                    ser.close()  # ***DO NOT REMOVE THIS LINE.*** Closes serial port.
                    break
            time.sleep(0)
        # plot figure after collecting data
        vltg.plot(x='Time (s)', y='Voltage (V)', xlabel='Time (s)', ylabel='Voltage (V)')
        plt.show()
        # write DataFrame to CSV file
        print('Data collection has terminated. Please select the filepath:')
        filetypes = (
            ('CSV files', '*.csv'),
            ('All files', '*.*'),
        )
        root = tk.Tk()
        filename = tk.filedialog.asksaveasfilename(
            title='Save as...',
            filetypes=filetypes,
            defaultextension='.csv'
        )
        root.destroy()
        vltg.to_csv(filename, index=False, header=True)
        # check if user wants to take another recording
        cntn = input("Start a new recording? Press 'y'+Enter to record a new file or 'n'+Enter to terminate program: ")
        while contLoop:
            if cntn == 'y':
                print("Taking a new recording...")
                break
            elif cntn == 'n':
                newRead = False
                contLoop = False
                print("Program ended by user.")
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
plt.close('all')


