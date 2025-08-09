from datetime import datetime

with open('hblog.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    content = content.strip().splitlines()
# print(content)
# print(type(content))

newlog = []

for line in content:
    if "Key TSTFEED0300|7E3E|0400" in line:
        newlog.append(line)
        # print(newlog)

with open('hb_test.log', 'w', encoding='utf-8') as logfile:
    for record in range(len(newlog) - 1):
        time_str1 = newlog[record][newlog[record].find("Timestamp ") + 10:newlog[record].find("Timestamp ") + 18]
        time_str2 = newlog[record + 1][newlog[record + 1].find("Timestamp ") + 10:newlog[record + 1].find("Timestamp ") + 18]

        time1 = datetime.strptime(time_str1, "%H:%M:%S")
        time2 = datetime.strptime(time_str2, "%H:%M:%S")

        delta = abs((time2 - time1).total_seconds())

        if 31 < delta < 33:
            logfile.write(f"{time_str2} WARNING: heartbeat = {delta} sec\n")
        elif delta >= 33:
            logfile.write(f"{time_str2} ERROR: heartbeat = {delta} sec\n")
    print("Records are added to created 'hb_test.log'")