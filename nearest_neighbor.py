import sys
from math import sqrt
import re
import time # to see how long each algorithm takes
from operator import itemgetter # used to sort by 2nd item in tuple (y-values)

################################################################################
################################################################################
###
### D&C:            'python nearest_neighbor.py -dc input_10.txt'
### Brute Force:    'python nearest_neighbor.py -bf input_10.txt'
### Both:           'python nearest_neighbor.py -both input_10.txt'
###
################################################################################
################################################################################

pointRE=re.compile("(-?\\d+.?\\d*)\\s(-?\\d+.?\\d*)")

###############################################################################

# calculate the distance between two points p1=(x1,y1) and p2=(x2,y2)
def dist(p1, p2):
    return sqrt(pow(float(p1[0])-float(p2[0]),2) + pow(float(p1[1])-float(p2[1]),2))

###############################################################################

#Run the divide-and-conquor nearest neighbor 
def nearest_neighbor(points, Py):
    if len(points) <= 3:
        return brute_force_nearest_neighbor(points)
    else:
        return nearest_neighbor_recursion(points, Py)
        
###############################################################################

def nearest_neighbor_recursion(points, Py):
    
    min_distance=float("inf")

    if len(points) <= 3:
        return brute_force_nearest_neighbor(points)
        
    else:

        # divide into two parts using n/2
        
        n = len(points)
        c = n/2
        
        left = points[:c]
        right = points[c:]
        
        Pyl=[]
        Pyr=[]
        
        midVal=points[c][0]
        
        for w in Py:
            if w[0]<midVal:
                Pyl.append(w)
            else:
                Pyr.append(w)
        
        delta = min( nearest_neighbor_recursion(left, Pyl), nearest_neighbor_recursion(right, Pyr) )
        
        # This is where Py comes in, it's already sorted so we just get the
        # values in Py that have an x-value less than delta away
        y = []
        for w in Py:
            if ( abs(w[0] - midVal ) <= delta) :
                y.append(w)

        delta2 = float("inf")
        
        if (len(y) > 0):

            for i in range(0, len(y)-1):
                j = i+1
                while ( (j < len(y)) and (y[j][1]-y[i][1] <= delta) ):
                    if dist(y[i],y[j]) < delta2:
                        delta2 = dist(y[i],y[j])
                    j = j+1
            
            return min(delta, delta2)
        else:

            return delta
        
    return min_distance
    
###############################################################################

#Brute force version of the nearest neighbor algorithm, O(n**2)
def brute_force_nearest_neighbor(points):

    min_distance=float("inf")
    
    if len(points) > 1:
        min_distance=dist(points[0],points[1])

        for i in range(0,len(points)-1):
            for j in range(i+1,len(points)):
                if dist(points[i],points[j]) < min_distance:
                    min_distance = dist(points[i],points[j])

    return min_distance

###############################################################################

# read in the text file of data and create an array of points where
# pi=(xi,yi), then return that array
def read_file(filename):
    points=[]
    # File format
    # x1 y1
    # x2 y2
    # ...
    in_file=open(filename,'r')
    for line in in_file.readlines():
        line = line.strip()
        point_match=pointRE.match(line)
        if point_match:
            x = point_match.group(1)
            x = float(x)
            y = point_match.group(2)
            y = float(y)
            points.append((x,y))
    
    # print
    # print("unsorted points: {}".format(points))
    points.sort()
    # print
    # print("sorted points: {}".format(points))
    # print

    return points

# Gather code in a main() function
# Command line args are in sys.argv[1], sys.argv[2] ..
# sys.argv[0] is the script name itself and can be ignored
def main(filename,algorithm):

    algorithm=algorithm[1:] 
    
    # points is sorted by x-values in read_file
    points=read_file(filename)
    
    # Py is the points data sorted by the y-values
    Py = sorted(points,key=itemgetter(1))
    
    if algorithm =='dc':
        
        # Begining of the clock for determining runtimes
        # slice object (constructed by 'start:stop:step' notation inside brackets)
        start_time = time.time()
        x = nearest_neighbor(points, Py)
        t2 = (time.time() - start_time)
        print
        print("Divide and Conquer: {}".format(x))
        print("--- {} seconds ---".format( t2 ))
        print
        # print("Divide and Conquer: {}".format( nearest_neighbor(points)))
        
        #################################
        # create output file
        lhs = filename.split(".txt")
        lhs = str(lhs[0])

        newfile = lhs + '_distance.txt'

        f = open(newfile, 'w')
        x = str(x)
        f.write("Divide and Conquer: " + x + "\n")
        f.write("Runtime: " + str(time.time() - start_time) )
        #################################
        
    if algorithm == 'bf':
        
        # Begining of the clock for determining runtimes
        # slice object (constructed by 'start:stop:step' notation inside brackets)
        start_time = time.time()
        x = brute_force_nearest_neighbor(points)
        t1 = (time.time() - start_time)
        print
        print("Brute Force: {}".format(x))
        print("--- {} seconds ---".format( t1 ))
        print
        
        #################################
        # create output file
        lhs = filename.split(".txt")
        lhs = str(lhs[0])

        newfile = lhs + '_distance.txt'

        f = open(newfile, 'w')
        x = str(x)
        f.write("Brute Force: " + x + "\n")
        f.write("Runtime: " + str(time.time() - start_time) )
        #################################
        
    if algorithm == 'both':
        
        # Begining of the clock for determining runtimes
        # slice object (constructed by 'start:stop:step' notation inside brackets)
        start_time = time.time()
        x = nearest_neighbor(points, Py)
        t2 = (time.time() - start_time)
        
        # Begining of the clock for determining runtimes
        # slice object (constructed by 'start:stop:step' notation inside brackets)
        start_time = time.time()
        y = brute_force_nearest_neighbor(points)
        t1 = (time.time() - start_time)
        
        print
        print("Brute Force: {}".format(y))
        print("--- {} seconds ---".format( t1 ))
        print
        print("Divide and Conquer: {}".format(x))
        print("--- {} seconds ---".format( t2 ))
        print
        
        #################################
        # create output file
        lhs = filename.split(".txt")
        lhs = str(lhs[0])

        newfile = lhs + '_distance.txt'

        f = open(newfile, 'w')
        x = str(x)
        y = str(y)
        f.write("Brute Force: " + y + "\n")
        f.write("Runtime: " + str(t1) + "\n" )
        f.write("Divide and Conquer: " + x + "\n")
        f.write("Runtime: " + str(t2) )
        #################################

###############################################################################
# the below calls the main function and passes in the third argument and the 
# second argument as parameters for the main function
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("1 python assignment1.py -<dc|bf|both> <input_file>")
        # if the number of arguments passed in is less than 3, output
        # an error message and quit
        quit(1)
    if len(sys.argv[1]) < 2:
        print("2 python assignment1.py -<dc|bf|both> <input_file>")
        # if the second argument has less than 2 characters, output 
        # the following error message and quit
        quit(1)
    main(sys.argv[2],sys.argv[1])
###############################################################################