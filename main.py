def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        return [(int(b), int(e)) for b, e in (line.split('-') for line in f)]

def process_ip_ranges(lines: list) -> tuple:
    begin_interval, end_interval = lines[0]
    lowest_ip = end_interval + 1
    total_allowed_ip = 0
    max_ip = 4294967295

    for b, e in lines:
        if b <= end_interval + 1:
            end_interval = max(end_interval, e)
        else:
            total_allowed_ip += b - (end_interval + 1)
            lowest_ip = min(lowest_ip, end_interval + 1)
            end_interval = e

    total_allowed_ip += max_ip - end_interval
    return lowest_ip, total_allowed_ip

def compute_results(file_name: str) -> tuple:
    lines = sorted(read_input_file(file_name))
    lowest_ip, total_allowed_ip = process_ip_ranges(lines)
    return lowest_ip, total_allowed_ip

if __name__ == '__main__':
    lowest_ip, total_allowed_ip = compute_results('input/input20.txt')
    print(f"Part I: {lowest_ip}")
    print(f"Part II: {total_allowed_ip}")
