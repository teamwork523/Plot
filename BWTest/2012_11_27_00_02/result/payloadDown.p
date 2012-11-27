# Data columns:X Min 1stQuartile Median 3rdQuartile Max

set bars 3.0

set style fill empty

set   autoscale
unset log 
unset label
set xtic auto                          # set xtics automatically
set ytic auto                          # set ytics automatically
set title "Payload Size vs Downlink Throughput"
set xlabel "Payload Size (Bytes)"
set ylabel "Downlink Throughput (kbps)"

plot 'payloadDown.dat' using 1:3:2:6:5 with candlesticks lt 4 notitle, \
     ''                using 1:4:4:4:4 with candlesticks lt 4 notitle, \
     ''                using 1:2:2:2:2 with candlesticks lt 4 notitle, \
     ''                using 1:6:6:6:6 with candlesticks lt 4 notitle, \
     ''                using 1:4       with linespoints  lt 3 notitle
