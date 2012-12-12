set xdata time
set timefmt "%s"
set format x "%H:%M"     # or anything else
set autoscale
set xtic auto                          # set xtics automatically
set ytic auto                          # set ytics automatically
set title 'Time of Day Effect (HSDPA)'
set xlabel "Time"
set ylabel "Throughput (Kbps)"

plot "hsdpa_result.txt" using 1:2 with points  lt 4 title columnheader, \
     "hsdpa_result.txt" using 1:3 with points  lt 3 title columnheader
