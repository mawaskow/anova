# this program runs anova on imported files

import csv
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename

def infoinstruct():
    # define info about what the program does
    # and instructions on how to use the program
    print("{0:^5}".format("\nThis program conducts analysis of variance, ANOVA, for 2 or more groups.\n"))
    print("{0:^5}".format("Two Windows Dialog boxes for 2 input files appear requsting the names of 2 files: the measurements *.csv and the F05File.csv\n"))
    print("{0:^5}".format("The User will select the measurements *.csv file and the F05File.csv respectively.\n"))
    print("{0:^5}".format("After conducting the analysis, a third Windows Dialog box will open showing the output file whose name was provided by the user.\n"))
    print("\n")
    print("{0:^5}".format("The input datafile *.csv file should contain the input data with each group in its own column with a heading for group title.\n"))
    print("{0:^5}".format("The number of groups, samples, or populations can be any number.\n"))
    print("{0:^5}".format("*** This program can only handle groups with the same number of measurements, i.e. n for each group is the same***\n"))
    print("{0:^5}".format("++++++++++ Happy ANOVA Analysis! ++++++++++\n"))
    input("********** Please press < ENTER > to continue **********\n")

def readfile():
    # import the data file that will be analyzed
    input("*** Please press < ENTER > when ready to select input file with measured data***")
    infile= open(askopenfilename(), "r")
    results = [row for row in csv.reader((infile))]
    # print the data that was imported
    # print("\nResults:")
    # print(results)
    # copy results, make header list, remove headers from input data
    inputdata= results
    headlst = inputdata[0]
    del(inputdata[0])
    # print("\nData without headings:")
    # print(inputdata)
    # create new list called groups and make inputdata's data into floats
    groups = []
    # n is number of columns, t is number of rows
    n = len(inputdata) 
    t = len(inputdata[0])
    for j in range(t):
        for i in range(n):
            groups.append(float(inputdata[i][j]))
    # print("\nAll data in one list, floated:")
    # print(groups)
    # make new list, sorting each column into a sublist
    allgroups= []
    grouplst= []
    for i in range(0, n*t, n):
        grouplst= groups[i:i+n]
        allgroups.append(grouplst)
    # print("\nEach treatment is in a sub list:")
    return allgroups

def alphainpt():
    # imports the alpha=0.05 values
    input("\n@@@ Please press <ENTER> when ready to select input file F05File.csv that contains the F values for alfa = 0.05. @@@\n")
    alphafile= open(askopenfilename(), "r")
    alphavals = [row for row in csv.reader((alphafile))]
    return alphavals

#######################
# C A L C U L A T I O N S

# make average function
def mean(lst):
    return sum(lst)/len(lst)

# make function that makes a list of each group's average
def calcavg(lst):
    avglst = []
    for i in range(len(lst)):
        meanlst = mean(lst[i])
        avglst.append(meanlst)
    return avglst

# make variance function
def var(lst, avg):
    diffs = []
    for i in range(len(lst)):
        difr = lst[i]-mean(lst)
        diffs.append(difr)
    ### square the differences
    sqddiffs = []
    for i in diffs:
        sqdifr = i**2
        sqddiffs.append(sqdifr)
    ### sum the squares of the differences
    sumsqddiff = sum(sqddiffs)
    ### final variance calculation
    varnce= sum(sqddiffs)/(len(lst)-1)
    return varnce

# make function that makes a list of each group's variance
def calcvars(lst, avg):
    varlst = []
    for i in range(len(lst)):
        varcalc = var(lst[i], avg[i])
        varlst.append(varcalc)
    return varlst

#########

def grandavg(lst):
    wholelst = []
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            wholelst.append(lst[i][j])
    gndavg = mean(wholelst)
    return gndavg

def sumsqbtw(num, avg, grand):
    sumsqbet = []
    for i in range(len(num)):
        ssb = len(num[i])*((avg[i]-grand)**2)
        sumsqbet.append(ssb)
        ssb = sum(sumsqbet)
    return ssb

def sumsqin(num, var):
    sumsqwin = []
    for i in range(len(num)):
        ssw = var[i]*(len(num[i])-1)
        sumsqwin.append(ssw)
        ssw = sum(sumsqwin)
    return ssw

###############

def anovadisp(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
    print("After conducting the analysis, a 3rd windows dialog box opens for output file name which is provided by the user. \n")
    input("Please press <ENTER> when ready to select output file.")
    outfile= open(asksaveasfilename(), "w")
    print("=" * 85, file = outfile)
    print(a.center(15), b.center(15), c.center(20), d.center(15), e.center(15), file = outfile)
    print("-" * 85, file = outfile)
    print(str(f).center(15), str(g).center(15), str(h).center(20), str(i).center(15), str(j).center(15), file = outfile)
    print(str(k).center(15), str(l).center(15), str(m).center(20), str(round(n, 1)).center(15), file = outfile)
    print("-" * 85, file = outfile)
    print(str(o).center(15), str(p).center(15), str(q).center(20), file = outfile)
    print("The value for F at alpha = 0.05 is:", r, file= outfile)
    if (float(j) > float(r)):
        print("There IS a significant statistical difference between the datasets.", file = outfile)
    else:
        print("There is NOT a significant statistical difference between the datasets.", file= outfile)
    outfile.close()
    print("=" * 85)
    print(a.center(15), b.center(15), c.center(20), d.center(15), e.center(15))
    print("-" * 85)
    print(str(f).center(15), str(g).center(15), str(h).center(20), str(i).center(15), str(j).center(15))
    print(str(k).center(15), str(l).center(15), str(m).center(20), str(round(n, 1)).center(15))
    print("-" * 85)
    print(str(o).center(15), str(p).center(15), str(q).center(20))
    print("The value for F at alpha = 0.05 is:", r)
    if (float(j) > float(r)):
        print("There IS a significant statistical difference between the datasets.")
    else:
        print("There is NOT a significant statistical difference between the datasets.")

def outselect(rests):
    print("After conducting the analysis, a 3rd windows dialog box opens for output file name which is provided by the user. \n")
    input("Please press <ENTER> when ready to select output file.")
    outfile= open(asksaveasfilename(), "w")
    print(rests, file=outfile)

def main():
    infoinstruct()
    allgroups = readfile()
    alphavals = alphainpt()
    avglst = calcavg(allgroups)
    varlst = calcvars(allgroups, avglst)
    gndavg = grandavg(allgroups)
    ssb = sumsqbtw(allgroups, avglst, gndavg)
    ssw = sumsqin(allgroups, varlst)
    tss = ssb+ssw
    degfb = len(allgroups)-1
    degft = len(allgroups)*len(allgroups[0])-1
    degfw = degft-degfb
    meansqb = ssb/degfb
    meansqw = ssw/degfw
    ftst = meansqb/meansqw
    alpha = alphavals[degfw-1][degfb-1]
    # watch out but youre gonna round here for ease of reading results
    alpha = round(float(alpha), 2)
    anovadisp("Source","Sum of Squares","Degrees of Freedom","Mean Square","F Test","Between Samples", ssb, degfb, meansqb, ftst, "Within Samples", ssw, degfw, meansqw, "Total", tss, degft, alpha)

if __name__ == '__main__':
    main()
    input("Press <Enter> when done.")