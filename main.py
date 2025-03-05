def compute_part_one(file_name: str) -> str:
    content = read_input_file(file_name)
    total_count = content.count('.')

    for _ in range(39):
        content = ''.join(process_rules(content, pos) for pos,_ in enumerate(content))
        total_count += content.count('.')

    return f'{total_count= }'

def loop_through_string(s: str) -> None:
    for pos, char in enumerate(s):
        print(f'Position: {pos}, Character: {char}')
