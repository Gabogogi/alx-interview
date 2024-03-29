#!/usr/bin/python3

import sys
import re

def output(log: dict, total_size: int) -> None:
    """
    Helper function to display stats
    """
    print("Total file size:", total_size)
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code]:
            print("{}: {}".format(code, log["code_frequency"][code]))

if __name__ == "__main__":
    regex = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)')  # Regex modified for correct grouping

    line_count = 0
    log = {}
    log["file_size"] = 0
    log["code_frequency"] = {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.match(line)
            if match:
                line_count += 1
                file_size = int(match.group(3))

                # File size
                log["file_size"] += file_size

                # Status code
                code = match.group(2)
                if code.isdecimal() and int(code) in log["code_frequency"]:
                    log["code_frequency"][code] += 1

                if line_count % 10 == 0:
                    output(log, log["file_size"])

    except KeyboardInterrupt:
        output(log, log["file_size"])
        sys.exit(0)
