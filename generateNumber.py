import random
import time
import csv


numberOfWords = 5

currentTime = int(time.time())
randomInt = random.randint(1,1000000)

myHash = currentTime * randomInt

random.seed(myHash)

finalCode = ''
finalCode = str(finalCode)

for x in range(5):
    
    anInt = random.randint(1,6)
    anInt = str(anInt)
    finalCode = finalCode + anInt

print "Number: " + finalCode


with open('dicewareList.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         idNumber = int(row["idNumber"])
         associatedWord = str(row["associatedWord"])

         print "ID Number: " + idNumber
         print "Word:" + associatedWord


#print(row['idNumber'], row['associatedWord'])




#with open('dicewareList.csv') as csvfile:
#     fileReader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     for row in fileReader:
#        print row
         
        # print(', '.join(row))


