def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def process_instruction(position: int, instructions: list, registers: dict) -> int:
    instruction = instructions[position].split(' ')

    if instruction[0] == 'inc':
        registers[instruction[1]] += 1
        position += 1

    elif instruction[0] == 'dec':
        registers[instruction[1]] -= 1
        position += 1

    elif instruction[0] == 'cpy':
        src, dest = instruction[1], instruction[2]
        registers[dest] = int(src) if src.isdigit() else registers[src]
        position += 1

    elif instruction[0] == 'jnz':
        src, offset = instruction[1], int(instruction[2])
        x = int(src) if src.isdigit() else registers[src]
        position += offset if x != 0 else 1

    else:
        print('Invalid instruction:', ' '.join(instruction))
        position += 1

    return position


def compute_part_one(file_name: str) -> str:
    instructions = read_input_file(file_name)
    print(instructions)
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    position = 0
    while position < len(instructions):
        position = process_instruction(position, instructions, registers)

    print(registers)

    return f'{registers["a"]= }'


def compute_part_two(file_name: str) -> str:
    instructions = read_input_file(file_name)
    registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    position = 0
    while position < len(instructions):
        position = process_instruction(position, instructions, registers)

    print(registers)

    return f'{registers["a"]= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input12.txt')}")
    print(f"Part II: {compute_part_two('input/input12.txt')}")
