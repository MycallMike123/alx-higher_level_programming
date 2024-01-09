#!/usr/bin/python3
"""Reads from standard input and computes metrics"""

import sys
import signal


def print_metrics(stats):
    """Prints the computed metrics"""

    total_size = stats.get('total_size', 0)
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if code in stats['status_codes']:
            print(f"{code}: {stats['status_codes'][code]}")


def compute_metrics(line, stats):
    """Computes metrics based on the input line"""

    try:
        portion = line.split()
        size = int(portion[-1])
        status_code = int(portion[-2])

        stats['total_size'] += size

        if status_code in stats['status_codes']:
            stats['status_codes'][status_code] += 1
        else:
            stats['status_codes'][status_code] = 1

    except (ValueError, IndexError):
        pass

    return stats


def main():
    stats = {'total_size': 0, 'status_codes': {}}
    lc = 0

    try:
        for line in sys.stdin:
            lc += 1
            stats = compute_metrics(line, stats)

            if lc % 10 == 0:
                print_metrics(stats)

    except KeyboardInterrupt:
        # Handle CTRL+C interruption
        print_metrics(stats)
        sys.exit(0)


if __name__ == "__main__":
    main()
