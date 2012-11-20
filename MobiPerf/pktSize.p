set   autoscale
unset log
unset label
set xtic auto                          # set xtics automatically
set ytic auto                          # set ytics automatically
set title "Packet Size VS. Link Capacity"
set xlabel "Packet Size (B)"
set ylabel "Link Capacity (Mbps)"
plot "pktSizeResult.txt" using 5:2 title columnheader with linespoints, \
      "pktSizeResult.txt" using 5:3 title columnheader with linespoints
