#!/usr/bin/python3
"""Reads standard input logs line by line and computes metrics"""
import sys
import signal
import re


total_size = 0
status_counts = {}
valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0
log_pattern = re.compile(r'''
    ^                                   # Start of line
    (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) # IP address
    \s-\s                               # " - " separator
    \[[^\]]+\]                          # [date]
    \s"GET\s/projects/260\sHTTP/1\.1"   # "GET /projects/260 HTTP/1.1"
    \s(\d{3})                           # Status code
    \s(\d+)$                            # File size
''', re.VERBOSE)


def print_stats():
    """Prints the collected metrics."""
    print(f"File size: {total_size}")
    for code in sorted(valid_status_codes):
        if code in status_counts:
            print(f"{code}: {status_counts[code]}")


def signal_handler(sig, frame):
    """Handle keyboard interrupt (CTRL+C)."""
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        match = log_pattern.match(line.strip())
        if match:
            status_code = match.group(2)
            file_size = int(match.group(3))
            total_size += file_size

            if status_code in valid_status_codes:
                status_counts[status_code] = status_counts.get(
                        status_code, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats()
except Exception:
    pass
finally:
    print_stats()
