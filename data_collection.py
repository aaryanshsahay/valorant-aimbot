# Press P to take a screenshot
# Press Q to quit program
# Creates a new directory 'images' saves screenshots on it.

from PIL import ImageGrab
import cv2
import numpy as np
import keyboard 
import time



def TakeScreenShot():
  '''
  Input : None
  
  Output : None
  
  Takes a screenshot, converts color channel and saves the image.
    
  '''
	screenshot = np.array(ImageGrab.grab(bbox=(640,220,1280,860)))
	screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2RGB)
	cv2.imwrite(f'images/{filename}', screenshot)



if __name__ == "__main__":
	
	x=0	
	print('Program started !\nPress P to take a screenshot\nPress Q to quit program')
	while True:
		try:
			if keyboard.is_pressed('p'):
				filename = str(x) + ".jpg"
				TakeScreenShot()
				x+=1
				time.sleep(1)
				print(f'Screenshot taken! Number : {x}')
			if keyboard.is_pressed('q'):
				break
		except:
			print("Couldn't take screenshot")
		
