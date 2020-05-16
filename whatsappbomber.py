from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://web.whatsapp.com')
personName=input("Name of the person/group to send message: ")
Message=input("Enter message: ")
count=int(input("Name of times to send the message: "))
#Scan the code
print('Scan the QR code and wait for the page to load and make sure devices are connected to internet')
input("Press any key to start ")
usr=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
usr.click()
usr.send_keys(personName)
time.sleep(8)
str="document.querySelector('[title="+'"'+personName+'"'+"]')"
usr1=driver.execute_script("return "+str)
usr1.click()
usr2=driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Type a message'])[1]/following::div[1]")
usr2.click()
i=1
while i<=count:
	usr2.send_keys(Message)
	time.sleep(1)
	usr3=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button")
	usr3.click()
	time.sleep(2)
	i=i+1

print('Done')