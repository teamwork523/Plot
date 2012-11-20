#!/usr/bin/env python

import sys

def Usage():
    print sys.argv[0] + " x_col_num y_col_num header < filepath"

def main():
    # use a dict to hold all data. {key:value} = {x:y}
    data = {}
    header = ""
    x_col_num = 0
    y_col_num = 0
    DEL = "\t"

    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 4:
        Usage()
        sys.exit(1)
    
    x_col_num = int(sys.argv[1])
    y_col_num = int(sys.argv[2])

    # check header
    if sys.argv[3] == "y" or sys.argv[3] == "Y":
        header = sys.stdin.readline()
    
    # process input
    line = sys.stdin.readline()
    while line != "":
        tempData = line.strip().split(DEL)
        x_data = tempData[x_col_num-1]
        y_data = tempData[y_col_num-1]

        if x_data not in data.keys():
            data[x_data] = [y_data]
        else:
            data[x_data].append(y_data)

        line = sys.stdin.readline()

    for eachData in sorted(data.keys()):
        cdf_data = data[eachData]
        cdf_data.sort()
        cdf_data_len = len(cdf_data)
        min_data = cdf_data[0]
        max_data = cdf_data[cdf_data_len-1]
        first_quarter = cdf_data[int(cdf_data_len*0.25)]
        third_quarter = cdf_data[int(cdf_data_len*0.75)]
        median = cdf_data[int(cdf_data_len*0.5)]
        print eachData + DEL + \
              min_data + DEL + \
              first_quarter + DEL + \
              median + DEL + \
              third_quarter + DEL + \
              max_data

if __name__ == "__main__":
    main()

