# ManAHLTakeHome
ManAHL's Take Home Test

# Introduction
___

The problem statement is as follows:

```commandline
Implement the method nextNum() and a minimal but effective set of unit tests. Implement in the language of your choice, Python is preferred,
but Java and other languages are completely fine. Make sure your code is exemplary, as if it was going to be shipped as part of a production
system.
```
More details on the problem statement are in the PDF that has been included with this repository.

# Solutions
___

There are a couple of ways in which the function nextNum() can be implemented. This largley pivots
around Big-O complexity. However, the more time/space optimised the algorithm is, the more
complex the code comes across to a fresh pair of eyes. I've included 3 different solutions
in this repository. They are as follows:

1. <u>**Naive approach**</u>: If the probabilities are rounded numbers (such as 0.1, 0.2, 0.3 etc), we can
construct a simple array that consists of the repetition of the number of elements and then use
random.choice() (Which is extending uniform distribution to act on our custom distribution). So,
for example, if our random numbers are [0, 1, 2, 3] and our probabilities are [0.1, 0.3, 0.4, 0.2],
then, we can just create an array as [0, 1, 1, 1, 2, 2, 2, 2, 3, 3] and choose a value from this.
Again, this seems inefficient because of creation of a large array that can be 100x the values of
the numbers that are given. It can have its use-cases, which is, a piece of code that need not
be called often, and have super simple maintainability.<br>
<strong>Time Complexity: </strong> O(n)<br>
<strong>Space Complexity: </strong> O(n^2)<br>
2. <u>**Efficient Approach**</u>: The above solution takes up too much of memory, and hence, a better
approach would be to generate an array of cumulative sum of weights, generate a random number, do a linear search, and
get the value corresponding to the entry. This approach can be further optimised by using
binary search (or bisect library in python), bringing the time from O(n) to O(logn)<br>
<strong>Time Complexity: </strong> O(n)<br>
<strong>Space Complexity: </strong> O(n) or O(logn)<br>
3. <u>**Alias Method**</u>: This is a method published by A.J. Walker in 1974, and the algorithm
can be found on [Wikipedia](https://en.wikipedia.org/wiki/Alias_method) and [Keith Schwarz](http://www.keithschwarz.com/darts-dice-coins/).<br>
<strong>Time Complexity: </strong> O(n) to initialize, O(1) to choose.<br>
<strong>Space Complexity: </strong> O(n)<br>
Addendum: I've used the inbuilt unittests instead of the pytests, in order to avoid 
third-party dependencies altogether

# Installation
___

### requirements.txt method
1. Please make sure you are using Python 3.6 and above, since the "bisect" method for binary search is only
available in Python 3.6 and above
2. Change the directory to ManAHLTakeHome
3. Fire the command "pip install -r requirements.txt" (The assumption here is that python and pip)
both are on the PATH variable.
4. Please Note: Yes, the file is empty at this point, but this is in order to standardise the process, in case
in the future we add some third-party library

### Conda environment method
1. Please make sure that you have a conda environment installed (such as Anaconda/Miniconda)
2. Change the directory to ManAHLTakeHome
3. Fire the command "conda env create -f environment.yml"


# Useage
___
1. The main entry point to the script is the "main.py" file. This takes in three arguments,
all of which are mandatory
   1. Method: A string containing the methodology to use, that is, either 'naive', 'efficient', or 'alias'
   2. Numbers: A comma separated list of numbers
   3. Probabilities: A comma separated list of probabilities, resulting into a summation of 1
2. Please note: The "naive" method requires that the probabilities be whole numbers
For Example
```commandline
python3 main.py -m naive -n 1,2,3 -p 0.1,0.8,0.1
```
```commandline
python3 main.py -m efficient -n 1,2,3 -p 0.33,0.33,0.34 
```
```commandline
python3 main.py -m alias -n 1,2,3 -p 0.25,0.25,0.75
```
```commandline
python3 main.py -m alias -n " -1,0,1,2,3" -p 0.01,0.3,0.58,0.1,0.01
# PLEASE NOTE: The space and quotes in "numbers" argument is for accepting negative numbers
```

3. In order to run unittests, execute the following on the command line:
```commandline
cd tests
python3 -m unittest randompick_test
```