import tkinter
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import csv
from graphics import *

def getScsz(text):
    scsz=[]
    root = tkinter.Tk()
    scsz.append(root.winfo_screenwidth())
    scsz.append(root.winfo_screenheight())
    root.destroy() ### generates error
    w = GraphWin(text, scsz[0], scsz[1])
    return w, scsz[0], scsz[1]

def beLogo(w, x, y):
    # "C:\\Users\\MAWaskow\\Documents\\School\\S20\\BE205\\GraphicsProjs\\BE.gif"
    beLogo = Image(Point(x/2, 60), "BE.gif")
    beLogo.draw(w)
    return

def instructions(w,x,y):
    line1 =Text(Point(x/2,200), "This program conducts analysis of variance, ANOVA, for 2 or more groups.").draw(w)
    line2 =Text(Point(x/2, 200+30), "Three Windows Dialog boxes for 2 input files and 1 output file appear requsting the names of 3 files:").draw(w)
    line3 = Text(Point(x/2, 200+60), "The Measurements *.csv, the F05File.csv, and the output.txt files as prompted").draw(w)
    line4 = Text(Point(x/2, 200+90), "The Measurements *.csv file should contain the input data with each group in its own column").draw(w)
    line5 = Text(Point(x/2, 200+120), "\n").draw(w)
    line6 = Text(Point(x/2, 200+150), "The first row will hold the headings for group name or title.").draw(w)
    line7 = Text(Point(x/2, 200+180), "The number of groups, samples, populations, treatments, or measurements can be any number.").draw(w)
    line8 = Text(Point(x/2, 200+210), "*** This program can only handle groups with the same number of measurements, i.e. n for each group is the same***").draw(w)
    line9 = Text(Point(x/2, 200+240), "++++++++++ Happy ANOVA Analysis! ++++++++++").draw(w)
    sizeT = 12
    line1.setSize(sizeT), line2.setSize(sizeT), line3.setSize(sizeT), line4.setSize(sizeT), line5.setSize(sizeT), line6.setSize(sizeT), line7.setSize(sizeT), line8.setSize(sizeT), line9.setSize(15)
    line8.setTextColor("Brown"), line9.setTextColor("Green")
    return line1, line2, line3, line4, line5, line6, line7, line8, line9

def okBox(w,x,y, msg, txtcolor, boxcolor):
    rw, rh = x/2, 60
    x1 = x/2 - rw/2
    y1 = y/1.2 - rh/2
    x2, y2 = x/2 + rw/2, y/1.2 + rh/2
    btmR = Rectangle(Point(x1, y1), Point(x2,y2)).draw(w)
    btmR.setFill(boxcolor)
    clickMouse = Text(Point(x/2, y/1.2), msg).draw(w)
    clickMouse.setFace("arial"), clickMouse.setSize(14), clickMouse.setStyle("bold")
    clickMouse.setTextColor(txtcolor)
    while True:
        p = w.getMouse()
        if p.getX() >= x1 and p.getX() <= x2:
            if p.getY() >= y1 and p.getY() <= y2:
                break
    clickMouse.undraw()
    btmR.undraw()
    return
#####
def readfile(w,x,y):
    okBox(w,x,y,"Click Here to Select Input Data File with Measurements", "yellow", "black")
    infile= open(askopenfilename(), "r")
    results = [row for row in csv.reader((infile))]
    inputdata= results
    headlst = inputdata[0]
    del(inputdata[0])
    groups = []
    n = len(inputdata) 
    t = len(inputdata[0])
    for j in range(t):
        for i in range(n):
            groups.append(float(inputdata[i][j]))
    allgroups= []
    grouplst= []
    for i in range(0, n*t, n):
        grouplst= groups[i:i+n]
        allgroups.append(grouplst)
    return allgroups

def alphainpt(w,x,y):
    okBox(w,x,y,"Click Here to Select File That Contains the F Values for alfa = 0.05", "yellow", "black")
    alphafile= open(askopenfilename(), "r")
    alphavals = [row for row in csv.reader((alphafile))]
    return alphavals

def mean(lst):
    return sum(lst)/len(lst)

def calcavg(lst):
    avglst = []
    for i in range(len(lst)):
        meanlst = mean(lst[i])
        avglst.append(meanlst)
    return avglst

def var(lst, avg):
    diffs = []
    for i in range(len(lst)):
        difr = lst[i]-mean(lst)
        diffs.append(difr)
    sqddiffs = []
    for i in diffs:
        sqdifr = i**2
        sqddiffs.append(sqdifr)
    sumsqddiff = sum(sqddiffs)
    varnce= sum(sqddiffs)/(len(lst)-1)
    return varnce

def calcvars(lst, avg):
    varlst = []
    for i in range(len(lst)):
        varcalc = var(lst[i], avg[i])
        varlst.append(varcalc)
    return varlst

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

def anovadisp(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,w,x,y):
    line1=Text(Point(x/2,300), "After conducting the analysis, a 3rd windows dialog box opens for output file name which is provided by the user.").draw(w)
    okBox(w,x,y,"Click Here to Select Output Data File", "yellow", "black")
    line1.undraw()
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
    line3=Text(Point(x/2,200),"ANOVA Program Output").draw(w)
    line3.setSize(16), line3.setTextColor('Dark Blue')
    line4=Text(Point(x/2,200+30),(a + (" "*5) + b + (" "*5) + c + (" "*5) + d + (" "*5) + e + (" "*5))).draw(w)
    line5=Text(Point(x/2,200+60),("-" * 110)).draw(w)
    line6=Text(Point(x/2,200+90),(str(f) + (" "*10) + str(g) + (" "*30) + str(h) + (" "*30) + str(i) + (" "*13) + str(j) + (" "*22))).draw(w)
    line7=Text(Point(x/2,200+120),(str(k) + (" "*10) + str(l) + (" "*30) + str(m) + (" "*30) + str(round(n, 1)) + (" "*45))).draw(w)
    line8=Text(Point(x/2,200+150),("-" * 110)).draw(w)
    line9=Text(Point(x/2,200+180),(str(o) + (" "*13) + str(p) + (" "*28) + str(q)+ (" "*64))).draw(w)
    line10=Text(Point(x/2,200+210),("The value for F at alpha = 0.05 is: " + str(r) + (" "*70))).draw(w)
    if (float(j) > float(r)):
        line11 = Text(Point(x/2,200+240),("There IS a significant statistical difference between the datasets." + (" "*25))).draw(w)
    else:
        line11 =Text(Point(x/2,200+240),("There is NOT a significant statistical difference between the datasets." + (" "*25))).draw(w)
    okBox(w,x,y, "Click here to exit", "Dark Blue", "Pink")

def main():
    w, x, y = getScsz("ANOVA Program Using Graphics Window")
    beLogo(w,x,y)
    line1, line2, line3, line4, line5, line6, line7, line8, line9 = instructions(w,x,y)
    okBox(w,x,y, "Please Click Here to Continue", "dark blue", "pink")
    line1.undraw(), line2.undraw(), line3.undraw(), line4.undraw(), line5.undraw(), line6.undraw(), line7.undraw(), line8.undraw(), line9.undraw()
###
    allgroups = readfile(w,x,y)
    alphavals = alphainpt(w,x,y)
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
    alpha = round(float(alpha), 2)
    anovadisp("Source","Sum of Squares","Degrees of Freedom","Mean Square","F Test","Between Samples", ssb, degfb, meansqb, ftst, "Within Samples", ssw, degfw, meansqw, "Total", tss, degft, alpha, w, x, y)
###
    #w.getMouse()
    w.close()

if __name__ == '__main__':
    main()
