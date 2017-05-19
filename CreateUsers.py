from splinter import Browser
import time
import csv

# You'll need to install Splinter and Chromium's pack to be able to run Chrome
# However, this should be able to run with Splinter's IE process
# I haven't bothered with relative paths to the files yet so that'll need updates
# as well as you'll need to create a cred file and define the absolute path.

#define variables
print('What is the Company Name?')
CompanyName = input()

userscreen = str('https://tracker.serengetilaw.com/tracker/Users?FileSubmitted=&ffid=-4')

exampleFile = open('C:\\Users\\U0127576\Dropbox\Programming\Python\Create Users\\UserList.csv')
reader = csv.DictReader(exampleFile)

with open('C:\\Users\\U0127576\Dropbox\Programming\Python\Credentials\creds.txt') as credFile:
    cred_lines = list(credFile)

#initialize browser
browser = Browser('chrome')

#login
browser.visit('https://tracker.serengetilaw.com/tracker/Logon?szReturn=/')
browser.find_by_id('logonUserID').first.fill(cred_lines[0])
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
        browser.find_by_name('txtEmployeeID').first.fill(row['EMPL_ID'])
        time.sleep(1)

        #Click Save
        browser.find_by_text("ACTIONS").first.click()
        browser.find_link_by_partial_text('Save & Close').first.click()

        with open("C:\\Users\\U0127576\Dropbox\Programming\Python\Create Users\\UserLog.txt", "a") as myfile:
            myfile.write('Row #' + str(reader.line_num) + " | " + row['EMAIL'])
            myfile.write("\n")