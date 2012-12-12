
set autoscale
set xtic auto                          # set xtics automatically
set ytic auto                          # set ytics automatically
set title 'HSPA+ Signal Strength vs Bandwidth'
set xlabel "Signal Strength(dB)"
set ylabel "Bandwidth(kbps)"

plot "hsdpa_result.txt" using 10:3 with points  lt 4 title columnheader
    
