import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from pynput.keyboard import Key
from pynput.mouse import Button, Controller
from pynput.keyboard import Controller as kbController
import mouse as mouse_get


keyboard 	= kbController()
mouse 		= Controller()
driver = webdriver.Chrome(ChromeDriverManager().install())



username = ""
password = ""

# User, where we are going to follow followers of him.
user_followers = ""


# TRUE if i want to follow
# FALSE if a want to remove followins
follow_bool = False




ammount_accounts = 2000
long_sleep_time = 500

ammount_follow 	= 0
ammount_unf 	= 0
each_unf 		= 10


def login(driver, username, password):
	enter_username = WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
	enter_username.send_keys(username)
	enter_password = WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
	enter_password.send_keys(password)

	time.sleep(0.5)

	#Click LogIn
	driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]').click()
	time.sleep(3)

	#Remove Notigications
	driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
	driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
	time.sleep(2)

def click_sys(coor, button, times):
	mouse.position = coor
	mouse.press(button)
	mouse.release(button)
	time.sleep(times)


# LogIn
driver.get('https://www.instagram.com')
login(driver, username, password)

# Prepare FOLLOW tab
driver.get('https://www.instagram.com/' + user_followers)
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()

#Create New Tab
mouse.position = (805, 32)
mouse.press(Button.left)
mouse.release(Button.left)
time.sleep(1)

keyboard.press(Key.ctrl)
keyboard.press('t')
keyboard.release('t')
keyboard.release(Key.ctrl)
time.sleep(1)

driver.switch_to.window(driver.window_handles[1])

#Preapare Unfollow tab
driver.get('https://www.instagram.com/'+str(username))
time.sleep(0.5)
driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()

print('Waiting to Scroll Down');	time.sleep(15)
print('READY!?');					time.sleep(5)

if True:
	for x in range( 1, ammount_accounts ):

		# Get follow Button
		if follow_bool:
			try:		cFollowButton = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li['+str(ammount_follow)+']/div/div[3]/button')
			except:
				try:	cFollowButton = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li['+str(ammount_follow)+']/div/div[2]/button')
				except:	print('Failed!')
		else: 		#											  /html/body/div[4]/div/div/div[2]/ul/div/li[174						 ]/div/div[2]/button
			try:		cFollowButton = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li['+ str(ammount_unf) +']/div/div[3]/button')
			except:	
				try: 	cFollowButton = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li['+ str(ammount_unf) +']/div/div[2]/button')			
				except:	print('/html/body/div[4]/div/div/div[2]/ul/div/li['+ str(ammount_unf) +']/div/div[2]/button')

		# Prove if is not already followed
		try:
			if cFollowButton.get_attribute('innerHTML') == 'Follow' or not follow_bool:	
				cFollowButton.click()

				if not follow_bool:
					time.sleep(1)
					try:	driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
					except:	print('failed')

			if x % each_unf == 0:		print('Long Sleep', x); time.sleep(long_sleep_time); follow_bool = not follow_bool
			else:						print('Sleep', 	x);		time.sleep(10)

			if follow_bool:	driver.switch_to.window(driver.window_handles[0]);	ammount_follow	+= 1; each_unf = 10
			else:			driver.switch_to.window(driver.window_handles[1]);	ammount_unf		+= 1; each_unf = 15
		except:	print('Failed.2')


		# xC , yC = mouse_get.get_position()
		# if xC >= 3300:
		# 	print(x, (int(round(time.time() * 1000)) - start_time) )
		# 	break

#/html/body/div[4]/div/div/div[2]/ul/div/li[85]/div/div[1]/div[2]/div[1]/span/a
# /html/body/div[4]/div/div/div[2]/ul/div/li[1]/div/div[2]/div[1]/div/div/span/a
# /html/body/div[4]/div/div/div[2]/ul/div/li[2]/div/div[2]/div[1]/div/div/span/a
# /html/body/div[4]/div/div/div[2]/ul/div/li[1]/div/div[2]/div[1]/div/div/span/a
# /html/body/div[4]/div/div/div[2]/ul/div/li[12]/div/div[2]/div[1]/div/div/span/a

# Follow
# /html/body/div[4]/div/div/div[2]/ul/div/li[1]/div/div[3]/button
# /html/body/div[4]/div/div/div[2]/ul/div/li[2]/div/div[3]/button