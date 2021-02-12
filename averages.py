import sys
from statistics import mean
from statistics import mode
from statistics import median

#------- Array Initialisation -------#

number_of_args = len(sys.argv)
array = []
first_int = 0

for i in range(0, len(sys.argv)):
    if sys.argv[i].isdigit():
        first_int = i
        break

if first_int != 0:
    for n in range(first_int, len(sys.argv)):
        array.append(int(sys.argv[n]))

if len(array) > 8:
    print("Error: expected max 8 integer data points")
    sys.exit()

#------- Array Initialisation -------#

#------- Flags -------#

# [ Mean , Mode , Median, File, .txt, Data


flags = [False, False, False] #Set to default

if '--mean' in str(sys.argv):
    flags[0] = True
if '--mode' in str(sys.argv):
    flags[1] = True
if '--median' in str(sys.argv):
    flags[2] = True

file_flag = False #Set to default

if '--file' in str(sys.argv):
    file_flag = True
    data = open('array.txt', 'r')
    text_array = data.read().split(' ')
    array = [int(x) for x in text_array]


#------- Flags -------#

def mean_calc(array):
    calc = (mean(array))
    print("mean is " + str(calc))

def mode_calc(array):
    calc = (mode(array))
    print("mode is " + str(calc))

def median_calc(array):
    calc = (median(array))
    print("median is " + str(calc))

def printer(flags):
    if flags[0] == True:
        mean_calc(array)
    if flags[1] == True:
        mode_calc(array)
    if flags[2] == True:
        median_calc(array)

if flags == [False, False, False]:
    mean_calc(array)
    mode_calc(array)
    median_calc(array)
else:
    printer(flags)
