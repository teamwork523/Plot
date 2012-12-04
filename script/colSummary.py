#!/usr/bin/env python

import sys

def Usage():
    print sys.argv[0] + " col_num header < filepath"

def main():
    # delimiter
    DEL = "\t"
    data = []
    total = 0.0

    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 3:
        Usage()
        sys.exit(1)

    col_num = int(sys.argv[1])

    # check header
    if sys.argv[2] == "y" or sys.argv[2] == "Y":
        header = sys.stdin.readline()

    line = sys.stdin.readline()
    while line != "":
        tempData = line.strip().split(DEL)
        curData = float(tempData[col_num - 1])
        total += curData
        data.append(curData)
        line = sys.stdin.readline()
    
    sortData = sorted(data)
    dataLen = len(data)
    print "Data Summary:"
    print "Mean: " + str(total/dataLen)
    print "Min: " + str(sortData[0])
    print "Q1: " + str(sortData[int(dataLen*0.25)])
    print "Median: " + str(sortData[int(dataLen*0.5)])
    print "Q3: " + str(sortData[int(dataLen*0.75)])
    print "Max: " + str(sortData[dataLen-1])

if __name__ == "__main__":
    main()
