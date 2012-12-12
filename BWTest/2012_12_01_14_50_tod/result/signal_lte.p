
set autoscale
set xtic auto                          # set xtics automatically
set ytic auto                          # set ytics automatically
set title 'LTE SNR vs Bandwidth'
set xlabel "LTE_SNR(dB)"
set ylabel "Bandwidth(kbps)"

plot "lte_result.txt" using 13:3 with points  lt 4 title columnheader
     
