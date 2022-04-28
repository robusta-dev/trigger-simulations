import time
import sys


def eat_disk(num_chunks, chunk_size, delay_between_chunks):
    arr = []

    for i in range(num_chunks):
        with open("file_test.txt", "a+") as f:
            f.write('a' * chunk_size)
        
        time.sleep(delay_between_chunks)
        print(i)


if __name__ == "__main__":
    if len(sys.argv) != 2 and len(sys.argv) != 3:
        print("usage: disk_eater.py number_of_megabytes [delay_in_secs]", file=sys.stderr)
        sys.exit(1)

    # Allocate the given number of megabytes
    num_megabytes = int(sys.argv[1])
    MB = 1024 * 1024
    delay_in_secs = int(sys.argv[2]) if len(sys.argv) == 3 else 0

    eat_disk(num_megabytes, MB, delay_in_secs)

    # Sleep for an hour
    print("time to sleep...")
    MINUTE = 60
    HOUR = 60 * MINUTE
    time.sleep(HOUR)
