def read_input_file(file_name: str) -> str:
    with open(file_name) as f:
        return f.read().strip()


def is_safe(row: str, position: int) -> bool:
    if position < 0 or position >= len(row):
        return True
    if row[position] == '.':
        return True
    return False


def process_rules(row: str, position: int) -> str:
    l = is_safe(row, position - 1)
    c = is_safe(row, position)
    r = is_safe(row, position + 1)

    if not l and not c and r:
        return '^'
    if not c and not r and l:
        return '^'
    if not l and r and c:
        return '^'
    if not r and l and c:
        return '^'
    return '.'


def compute_part(file_name: str, rows: int) -> str:
    content = read_input_file(file_name)
    print(content)
    total_count = content.count('.')
    for i in range(rows-1):
        next_line = ''
        for pos, _ in enumerate(content):
            next_line += process_rules(content, pos)
        content = next_line
        total_count += content.count('.')

    return f'{total_count= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part('input/input18.txt', rows=40)}")
    print(f"Part I: {compute_part('input/input18.txt', rows=400000)}")
