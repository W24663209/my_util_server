# encoding: utf-8
import sys
import time

# logfile = '%s.log' % sys.argv[1]
logfile = '/private/tmp/parkinglock/admin/logs/sys-info.log'
keyword = 'JVM running for'
timeout = 120  # 2分钟


def tail_log(logfile):
    logfile.seek(0, 2)
    start_time = time.time()
    while True:
        if time.time() - start_time >= timeout:
            break
        where = logfile.tell()
        lines = logfile.readline()
        if not lines:
            logfile.seek(where)
        else:
            yield lines


if __name__ == '__main__':
    logfile = open(logfile, 'r')
    for line in tail_log(logfile):
        line = line.replace('\n', '')
        if line.__contains__(keyword):
            print(line)
            break
        else:
            print(line)
    logfile.close()
