import sys
import serial
import cv2
import os

#List of file in .jpg format, extensions can be change

def main():

	File_Lst =[] 


	#Host Operating system name, as file extension and serial port differs 

	plat = sys.platform
	print plat

	if plat == 'win32': #for windows operating system

		import serial.tools.list_ports

		print list(serial.tools.list_ports.comports())
			
		com_port = 'COM2'
		baud_rate = 9600
		File_dir = "C:\\Users\\user\\Desktop\\fruit\\"
		
		
	elif plat == 'cygwin': # for cygwin

		import serial.tools.list_ports_linux

		print list(serial.tools.list_ports_linux.comports())
		com_port = '/dev/com2'
		baud_rate = 9600
		
		
	elif plat == 'linux2': # for linux/ubuntu

		import serial.tools.list_ports

		print list(serial.tools.list_ports.comports())
		com_port = '/dev/ttyACM0'
		baud_rate = 9600
		File_dir = "/host/Users/user/Desktop/fruit/"
		
		
	print "Attempting to open your com port..."

	try:

		# Store files in list

		for file in os.listdir(File_dir):
				
			File_Lst.append(file)
					
		print File_Lst
		
		
		welcome_index = File_Lst.index('welcome.jpg')			
		welcome_str = File_Lst[welcome_index]
		
		print welcome_str
		
		orange_index = File_Lst.index('orange.jpg')			
		orange_str = File_Lst[orange_index]
		print orange_str.split('.')[0]
		
		print orange_str
		
		apple_index = File_Lst.index('apple.jpg')			
		apple_str = File_Lst[apple_index]
		
		print apple_str
		
		banana_index = File_Lst.index('banana.jpg')			
		banana_str = File_Lst[banana_index]
		
		print banana_str
		
		doughnuts_index = File_Lst.index('doughnuts.jpg')			
		doughnuts_str = File_Lst[doughnuts_index]

		# check the device com number
		
		
		ser = serial.Serial(com_port, baud_rate)	
		print ser
		print "Successfully opened the com port."
		print "Your com port returned the following information:", com_port, baud_rate
			
		
		print "Listening for key presses..."
		
		#Welcome Screen
		
		img = cv2.imread(File_dir + welcome_str )
		cv2.destroyAllWindows()			
		cv2.imshow("Press KEYS to know which food is good or bad", img)
		
		while True:
		
			try:
		
				k = cv2.waitKey(0)
							
				if k == ord('w'): # wait for 'w' key to upload orange nutrition information
						
					img = cv2.imread(File_dir + orange_str)	
					newx,newy = img.shape[1]/2,img.shape[0]/2 #new size (w,h)
					img = cv2.resize(img,(newx,newy))
					cv2.destroyAllWindows()		
					cv2.imshow("Orange Nutritional Information", img)
				
				elif k == ord('a'): # wait for 'w' key to upload apple nutrition information
							
					img = cv2.imread(File_dir + apple_str)	
					newx,newy = img.shape[1]/2,img.shape[0]/2 #new size (w,h)
					img = cv2.resize(img,(newx,newy))
					cv2.destroyAllWindows()		
					cv2.imshow("Apple Nutritional Information", img)
							
				elif k == ord('s'): # wait for 'w' key to upload apple nutrition information
						
					img = cv2.imread(File_dir + banana_str)	
					newx,newy = img.shape[1]/2,img.shape[0]/2 #new size (w,h)
					img = cv2.resize(img,(newx,newy))
					cv2.destroyAllWindows()		
					cv2.imshow("Banana Nutritional Information", img)
									
				elif k == 32:
								
					break
					cv2.destroyAllWindows()
													
				else:
										
					img = cv2.imread(File_dir + doughnuts_str)
					cv2.destroyAllWindows()
					cv2.imshow("Bad, Have good eating habits CHUMP", img)
						
					
			except cv2.error:	
				print "Image file not found"
				sys.exit(-1)

		ser.close()
			
	except serial.serialutil.SerialException:

		print("Kindly connect an USB device")
		sys.exit(-1)	
		
main()