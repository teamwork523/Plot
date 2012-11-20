set   autoscale
unset log
unset label
set xtic auto                          # set xtics automatically
set ytic auto                          # set ytics automatically
set title "Train Length VS. Link Capacity"
set xlabel "Train Length"
set ylabel "Link Capacity (Mbps)"
plot "trainLength.txt" using 6:2 title columnheader with linespoints, \
      "trainLength.txt" using 6:3 title columnheader with linespoints

