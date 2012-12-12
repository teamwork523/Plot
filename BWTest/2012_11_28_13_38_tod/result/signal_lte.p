
set autoscale
set xtic auto                          # set xtics automatically
set ytic auto                          # set ytics automatically
set title 'LTE RSRP vs Bandwidth'
set xlabel "LTE_RSRP(W)"
set ylabel "Bandwidth(kbps)"

plot "lte_result.txt" using 11:3 with points  lt 4 title columnheader
     
