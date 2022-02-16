import csv
import sys
from pythonping import ping
import sys, time, datetime

delay = sys.argv[1]

while True:
    with open('./results.csv', 'a', newline='') as f: #opened for appending with a fix for Windows newlines
        writer = csv.writer(f)
        now = datetime.datetime.now()
        timeoutput = now.strftime('%Y-%m-%d %H:%M:%S')
        response_list = ping('8.8.8.8', size=40, count=10)
        row = [timeoutput, response_list.rtt_avg_ms]
        writer.writerow(row)
        #print (row) useful for debug but no need normally
    time.sleep(int(delay))

