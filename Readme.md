This python script will upload the image of any object which is connected to the circuit named 'Makey-Makey'. In this case, it uploads the nutritional content of fruit which have been designed as .jpg files.

The program can execute in win32 or linux platform.However, for windows, cygwin must be installed.

For win32, the serial port has to be configured  by using the serial instance 'COM%', for linux2, the '/dev/ttyACM0/' is the serial instance, and for cygwin, 
it is 'COM%+1'.

Here, the package opencv is used to display the image. This package comes with a method cv2.waitKey() which waits for the key press. 
Use 0 so that the program waits for the inifnite amount of time for the key to be pressed.

The file is kept in the directory, which is read using cv2.imread() function, if file is not found at that location, then it raises an error. The opencv uses the ASCII character of the key which has been pressed, so, even if 'w' is pressed, the ascii value of 'w' which is 119,will be used to process further.

In order to run the script, download the program and the files in a folder, and make sure that 'Python' is installed. This program would currently execute on Python-2.7. Use python <program name> to run the script after moving into the directory.

