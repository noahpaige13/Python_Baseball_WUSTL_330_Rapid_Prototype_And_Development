import re
import sys

# Dictionaries Created
atbats =  {

}
hits = {

}
avg = {

}

# Try Open File
try:
    filepath = open(sys.argv [1],'r') 

# Exception if Cant Open File
except:
    sys.exit("File Does Not Exist")



# filepath = open('cardinals-1940.txt','r')

# Read in File 
x = filepath.readline()
for x in filepath:
    if (re.match('\w', x)):

        # Retrieve batter Name
        n = re.search('(\w+\s\w+)',x)
        name = n.group()

        # Retrieve List of Hitting Stats for a Game
        b = re.findall('\d', x)
        
        if name in atbats:
            atbats[name] = atbats[name] + int(b[0])
            hits[name] = hits[name] + int(b[1])
        else:
            atbats[name] = int(b[0])
            hits[name] = int(b[1])
                
filepath.close()
print "Got Here"


# Compute Averages
for  name, bats in atbats.items():
    avg[name] = float(hits[name])/float(atbats[name])  



# Print in Descending Batting Avg. Order
while (len(avg) > 0):
    max = float(0)
    n = ""
    for name, a in avg.items():
        if (a >= max):
            max = a
            n = name
    print ("%s: %.3f" %(n, max))
    # print (n + ": " + str(max))
    del avg[n]


 
       



