# this program calculates arithmetic mean, variance, standard 
# deviation, and range for data
import csv

def main():
    print("This program calculates arithmetic mean, variance, standard deviation, and range for data.\n")
    # get the data points
    fname= input("What .csv file are the numbers in? ")
    numbrs=[fields for fields in csv.reader(open(fname))]
    numblst= []
    for i in range(len(numbrs)):
        numblst.append(float(numbrs[i][0]))
    # print what you know
    print("\n")
    print("Measured Data:", numbrs)
    print("Number of Data points:", len(numbrs))
    print("\n")
    # calculate the mean
    mean = sum(numblst)/len(numbrs)
    # calculate the variance 
    ### calculate the difference between each number and the mean
    diffs = []
    for i in numblst:
        diffs.append(i-mean)
    ### square the differences
    sqddiffs = []
    for i in diffs:
        sqddiffs.append(i**2)
    ### sum the squares of the differences
    sumsqddiff = sum(sqddiffs)
    ### final variance calculation
    varnce= sum(sqddiffs)/(len(numbrs)-1)
    # calculate the standard deviation
    stdev = varnce**(1/2)
    # calculate the range
    rnge = max(numblst)-min(numblst)
    # print
    print("Mean:", mean)
    print("Variance:", varnce)
    print("Standard Deviation:", stdev)
    print("Range:", float(rnge))
if __name__ == '__main__':
    main()
    input("Press <Enter> when done.")