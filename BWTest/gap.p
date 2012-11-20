set   autoscale
unset log
unset label
set xtic auto                          # set xtics automatically
set ytic auto                          # set ytics automatically
set title "Gap VS. Link Capacity"
set xlabel "Gap Size (ms)"
set ylabel "Link Capacity (Mbps)"
plot "gapSizeResult.txt" using 4:2 title columnheader with linespoints, \
      "gapSizeResult.txt" using 4:3 title columnheader with linespoints

