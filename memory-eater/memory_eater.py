import time
import sys


MEM_SUFFIXES = ["Ki", "Mi", "Gi"]
MEM_SUFFIX_SIZE = 1024


def get_bytes_from_memory_spec(mem_spec: str):
    factor = 1024
    i = 0
    for suffix in MEM_SUFFIXES:
        if mem_spec.endswith(suffix):
            break
        factor = factor * MEM_SUFFIX_SIZE
        i = i + 1

    if i == len(MEM_SUFFIXES):
        raise Exception("cannot parse the following memory spec as it has an unrecognized suffix:", mem_spec)

    suffix = MEM_SUFFIXES[i]
    num = int(mem_spec[:-len(suffix)])
    return num * factor


def allocate_memory(initial_memory: int, sleep_after_initial_alloc: int, rest_of_memory: int, number_of_allocations: int, delay_in_seconds: float):
    # Allocate initial memory
    initial_mem = '_' * initial_memory
    time.sleep(sleep_after_initial_alloc)

    # Aloocate the rest of the memory in multiple bulks
    chunk_size = rest_of_memory // number_of_allocations
    arr = []
    for i in range(number_of_allocations):
        ch = chr(ord('A') + i)
        arr.append(ch * chunk_size)
        time.sleep(delay_in_seconds)


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: memory_eater.py [initial_allocation] [sleep_after_initial_alloc] [rest_of_memory] [number_of_allocations] [delay_in_seconds]", file=sys.stderr)
        sys.exit(1)

    initial_memory = get_bytes_from_memory_spec(sys.argv[1])
    sleep_after_initial_alloc = int(sys.argv[2])
    rest_of_memory = get_bytes_from_memory_spec(sys.argv[3])
    number_of_allocations = int(sys.argv[4])
    delay_in_seconds = float(sys.argv[5])

    allocate_memory(initial_memory, sleep_after_initial_alloc, rest_of_memory, number_of_allocations, delay_in_seconds)

