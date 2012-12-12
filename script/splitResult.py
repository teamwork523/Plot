#!/usr/bin/env python

import sys

def Usage():
    print sys.argv[0] + " col_num header < filepath"

def main():
    # delimiter
    DEL = "\t"
    LTE_col_num = 13
    HSDPA_col_num = 10

    LTE_filename = "lte_result.txt"
    HSDPA_filename = "hsdpa_result.txt"

    fp_lte = open(LTE_filename, 'w')
    fp_hsdpa = open(HSDPA_filename, 'w')

    header = sys.stdin.readline()
    fp_lte.write(header)
    hsdpa_header = header.strip().split(DEL)[:HSDPA_col_num]
    hsdpa_header[HSDPA_col_num-1] = "GSM_SS"
    hsdpa_header.append("\n")
    fp_hsdpa.write(DEL.join(hsdpa_header))
    
    line = sys.stdin.readline()
    while line != "":
        lineData = line.strip().split(DEL)
        if float(lineData[1]) == 0.0 or \
           float(lineData[2]) == 0.0 or \
           float(lineData[6]) == 0.0 or \
           float(lineData[7]) == 0.0:
            line = sys.stdin.readline()
            continue
        else:
            # convert millisecond to second
            lineData[0] = str(int(lineData[0])/1000)
            if len(lineData) == LTE_col_num:
                lineData.append("\n")
                fp_lte.write(DEL.join(lineData))
            else:
                lineData.append("\n")
                fp_hsdpa.write(DEL.join(lineData))
            line = sys.stdin.readline()
    
    fp_lte.close()
    fp_hsdpa.close()

if __name__ == "__main__":
    main()
