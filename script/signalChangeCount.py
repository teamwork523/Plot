#!/usr/bin/env python

import sys

def Usage():
    print sys.argv[0] + " var_col(i.e. signal) cor_col(i.e. bandwidth) header < filepath"

def main():
    # delimiter
    DEL = "\t"
    totalChange = 0.0
    # consistant increase/decrease
    monoChange = 0.0
    ResetReq = 100
    monoList = []
    total = 0.0
    
    if (len(sys.argv) == 2 and sys.argv[1] == "-h") or len(sys.argv) != 4:
        Usage()
        sys.exit(1)
    
    var_col = int(sys.argv[1]) - 1
    cor_col = int(sys.argv[2]) - 1
    
    # check header
    if sys.argv[3] == "y" or sys.argv[3] == "Y":
        header = sys.stdin.readline()
    
    line = sys.stdin.readline().strip().split(DEL)
    lineCount = 0
    prev = "r"
    while line != "":
        prev = line
        line = sys.stdin.readline().strip().split(DEL)
        if line == [""]:
            break
        prev_var = float(prev[var_col])
        prev_cor = float(prev[cor_col])
        cur_cor  = float(line[cor_col])
        cur_var  = float(line[var_col])
        if (prev_var > cur_var and cur_cor > prev_cor) or \
           (prev_var < cur_var and cur_cor < prev_cor):
            monoChange += 1
        if prev_var != cur_var:
            totalChange += 1
        """if totalChange >= ResetReq:
            monoList.append(monoChange/totalChange)
            totalChange = 0
            monoChange = 0"""
    print monoChange/totalChange
    # print monoList
    # print sum(monoList)/len(monoList)
    
if __name__ == "__main__":
    main()

    
    
