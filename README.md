<h1>
Nearest Neighbor
</h1>


------------------------------------------<br />
Description<br />
------------------------------------------<br />

Given a set of points in a two dimensional plane, output the distance
between the closest set of points comparing the brute force method
with the divide-and-conquer method.

The brute force method:
- takes in a set of points and starts at the first set of points and then 
  sequentially goes through every pair of points to find the minimum 
  distance between the possible pairs of points.

The divide-and-conquer method:
- Find a value x for which exactly half the points have xi < x, and half 
  have xi > x. On this basis, split the points into two groups L and R.
- Recursively find the closest pair in L and in R. Say these pairs are pL, qL 
  in L and pR. qR in R, with distances dL and dR respectively. Let d be the 
  smaller of these two distances.
- It remains to be seen whether there is a point in L and a point in R that 
  are less than distance d apart from each other. To this end, discard all 
  points with xi < x - d or xi > x + d and sort the remaining points by 
  their y-coordinate.
- Now, go through this sorted list, and for each point, compute its distance 
  to the subsequent points in the list. Let pM, qM be the closest pair found 
  in this way.
- The answer is one of the three pairs {pL, qL}, {pR, qR}, {pM, qM}, 
  whichever is closest.

------------------------------------------<br />
Command Line Arguments<br />
------------------------------------------<br />

Example:  .python nearest\_neighbor.py -dc input\_10.txt

-dc | -bf | -both <br />
  (required) Specifies the type of algorithm to be run (divide and conquer, 
  brute force, or both)

    -dc - divide and conquer algorithm 
    -bf - brute force algorithm 
    -both - both the divide and conquer algorithms
    
input\_10.txt | input\_100.txt | input\_10e5.txt | input\_10e6.txt <br />
  (required) Specifies the input file of the data that the algorithms will be
  run on
  
    input_10.txt - data file of size n=10
    input_100.txt - data file of size n=100
    input_10e5.txt - data file of size n=10,000
    input_10e6.txt - data file of size n=100,000
    
------------------------------------------<br />
Design Decisions & Issues<br />
------------------------------------------<br />

Output file: <br />
  For each .txt file that is passed in as an argument such as filename.txt, an 
  output of the name filename\_distance.txt is created that outputs the name of 
  the algorithm called by either -dc/bf/both, followed by the closest distance
  between any two points in the dataset, along with the runtime of the 
  algorithm. When both algorithms are called, it outputs both of the above
  information for each algorithm. 
  
  Example:  for calling the divide and conquer algorithm (-dc) using the input
            file name of 'input\_10.txt', the output file name would be
            
                input\_10\_distance.txt
            
   and the information contained in the file would be:
            
                Divide and Conquer: 2.86356421266
                Runtime: 8.29696655273e-05
                
  Note: it should be noted that when the files were inputted into the program,
        all the data was still in string format. Thus it had to be converted to
        float format. Then, prior to outputting the information to a file, the
        values had to be converted back into a string format.
        
  The creation of the output files was created within each branch of the if
  statements for determining which algorithms to call. An output file creation
  functin would normally have been created to avoid having separate code in 
  each branch of the if statements, however, due the fact that multiple lines
  of code were appended to the output files during several of the if branches,
  this was avoided in this case.
                
Run Time: <br />
  Calculating the runtime of each algorithm was accomplished importing the 
  'time' and utilizing it's 'time.time()' method which obtains the current time. 
  This can then be used to subtract an earlier time to determine how much time
  has passed.
  
  Example:  before an algorithm is called, a time was stored as
  
                  start_time=time.time()
            
 then after the algorithm was run, the runtime was calculated by
            
                  runtime=time.time()-start_time
                  
Sorting: <br />
  Both algorithms rely on the x-values to be sorted prior to passing them as 
  arguments to functions. This was accomplished during the reading of the input
  file by the read\_file using the built in sort() function in python.
  
  In addition, to maintain the O(n lgn) time desired by the divide and conquer
  algorithm, sorting the data by y-values inside each recursion call had to be
  avoided. Not doing so would cause the divide and conquer to run in O(n lg^2n)
  time which is less than the ideal case for divide and conquer. To accomplish 
  this, the data was sorted by the y-values in addition to the x-values. The 
  sorted x-values were stored in 'points' and the sorted y-values were stored in
  'Py'. Both were passed to the divide and conquer algorithms with each 
  recursion, thus avoiding having to sort the data by the y-values within each
  recursion step. The sorting of the y-values was accomplished inside the main
  file prior to the algorithm calls.
  
Initialized distances to Infinity: <br />
  Any time that a distance was initialized, it was set to the value 'Inf' for 
  Infinity. This was done due to the fact that the goal of the algorithms is to
  determine the minimum distance between two points. As such, setting any
  distance to default to zero could trigger the default being the smallest
  distance. Thus, each distance was initialized to zero when possible.
  
Median vs Middle Point: <br />
  Various sources describe implementing the divide and conquer algorithm for
  nearest neighbors in a slightly different way. The key difference seems to be
  whether to use the exact median of the x-values as the dividing value for
  determining the left and right subsets or to use the middle value in the 
  dataset as the dividing value. Both implementations were approached and both
  seemed to accomplish that task equally. Thus, the method of utilizing the 
  middle value was used in the algorithm due to the fact that inluding a 
  function that calculates the median involves more lines of code than simply
  calculating the middle value. 
  
      
