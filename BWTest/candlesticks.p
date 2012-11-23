# Data columns:X Min 1stQuartile Median 3rdQuartile Max

# set bars 4.0

set style fill empty

set   autoscale
unset log 
unset label
set xtic auto                          # set xtics automatically
set ytic auto                          # set ytics automatically
set title "Sample Candlestick plot"
set xlabel "Gap Size (ms)"
set ylabel "Link Capacity (Mbps)"

plot 'result.txt' using 1:3:2:6:5 with candlesticks lt 4 notitle, \
     ''           using 1:4:4:4:4 with candlesticks lt 3 notitle, \
     ''           using 1:4       with linespoints  notitle
