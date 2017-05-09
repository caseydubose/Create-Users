#import csv
#exampleFile = open('UserList.csv')
#exampleReader = csv.reader(exampleFile)
#for row in exampleReader:
 #   print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

import csv
import time

exampleFile = open('UserList.csv')
#exampleReader = csv.reader(exampleFile)
#exampleData = list(exampleReader)
#print(exampleData[0][0])
#for i in exampleData:
 #   print(i),
  #  time.sleep(1)
    

reader = csv.DictReader(exampleFile)
for row in reader:
    print(row['FIRST_NAME'], row['LAST_NAME'])
    #time.sleep(1)
