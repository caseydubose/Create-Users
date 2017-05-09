from splinter import Browser
import time
import csv

#define variables
userscreen = str('https://tracker.serengetilaw.com/tracker/Users?FileSubmitted=&ffid=-4')

#Prompt for sign in and database
# print('What is your Username?')
# UserName = input()
# print('What is your Password?')
# Password = input()
CompanyName = str('Raytheon Company')

#import csv
exampleFile = open('C:\\Users\\U0127576\Dropbox\Programming\Python\Create Users\\UserList.csv')
reader = csv.DictReader(exampleFile)
credFile = open('C:\\Users\\U0127576\Dropbox\Programming\Python\Create Users\creds.txt')
cred_lines = credFile.readlines()

#initialize browser
browser = Browser('chrome')

#login
browser.visit('http://tracker.serengetilaw.com')
browser.find_by_id('logonUserID').first.fill(cred_lines[0])
browser.find_by_id('btnLogon').first.click()
browser.find_by_id('logonPassword').first.fill(cred_lines[1])
browser.find_by_id('btnLogon').first.click()


#pick company DB
browser.find_by_text(CompanyName).first.click()
time.sleep(1)


#Create User Loop
for row in reader:
        browser.visit(userscreen)
        try:
            alert = browser.get_alert()
            alert.accept()
        except Exception as e:
            pass
        browser.find_by_text("ACTIONS").first.click()
        browser.find_link_by_partial_text('Company User').first.click()
        browser.find_by_id('idTxtEMail').first.fill(row['EMAIL'])
        browser.find_by_id('idtxtFirstName').first.fill(row['FIRST_NAME'])
        browser.find_by_id('idtxtLastName').first.fill(row['LAST_NAME'])
        office = browser.find_by_id('idcboCoOfficeID').first
        office.select(row['OFFICEID'])
        time.sleep(1)
        #Click Save
        #browser.find_by_text("ACTIONS").first.click()
        #browser.find_link_by_partial_text('Save & Close').first.click()
        with open("C:\\Users\\U0127576\Dropbox\Programming\Python\Create User\\UserLog.txt", "a") as myfile:
            myfile.write(row['EMAIL'])
