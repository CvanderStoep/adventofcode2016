from typing import List, Dict


def read_input_file(file_name: str) -> List[str]:
    """Reads input file and returns content as a list of strings."""
    with open(file_name) as f:
        content = f.read().splitlines()
    return content


def process_instruction(position: int, instructions: List[str], registers: Dict[str, int]) -> int:
    """Processes a single instruction and updates the registers."""
    instruction = instructions[position].split(' ')

    if instruction[0] == 'inc':
        registers[instruction[1]] += 1
        position += 1

    elif instruction[0] == 'dec':
        registers[instruction[1]] -= 1
        position += 1

    elif instruction[0] == 'cpy':
        src, dest = instruction[1], instruction[2]
        registers[dest] = registers[src] if src in 'abcd' else int(src)
        position += 1

    elif instruction[0] == 'jnz':
        src = instruction[1]
        x = int(src) if src.isdigit() else registers[src]
        offset = registers[instruction[2]] if instruction[2] in 'abcd' else int(instruction[2])
        position += offset if x != 0 else 1

    elif instruction[0] == 'tgl':
        x = instruction[1]
        tgl_position = position + registers[x]
        if tgl_position >= len(instructions):
            pass
        else:
            tgl_instruction = instructions[tgl_position].split(' ')
            if tgl_instruction[0] == 'inc':
                instructions[tgl_position] = 'dec ' + tgl_instruction[1]
            if tgl_instruction[0] == 'dec':
                instructions[tgl_position] = 'inc ' + tgl_instruction[1]
            if tgl_instruction[0] == 'tgl':
                instructions[tgl_position] = 'inc ' + tgl_instruction[1]
            if tgl_instruction[0] == 'jnz':
                instructions[tgl_position] = 'cpy ' + tgl_instruction[1] + ' ' + tgl_instruction[2]
            if tgl_instruction[0] == 'cpy':
                instructions[tgl_position] = 'jnz ' + tgl_instruction[1] + ' ' + tgl_instruction[2]

        position += 1

    elif instruction[0] == 'mul':
        # www.reddit.com/r/adventofcode/comments/5jvbzt/2016_day_23_solutions/
        # replace below loop that increments a with d*b:
        # cpy b c
        # inc a
        # dec c
        # jnz c -2
        # dec d
        # jnz d -5

        # with:
        # mul b d a
        # cpy 0 c
        # cpy 0 c
        # cpy 0 c
        # cpy 0 c
        # cpy 0 d
        # could also just use 5x jnz 0 0

        registers[instruction[3]] = registers[instruction[2]] * registers[instruction[1]]
        position += 1

    else:
        print('Invalid instruction:', ' '.join(instruction))
        position += 1

    return position


def compute(file_name: str, initial_a: int) -> str:
    """Computes the value of register 'a' after processing all instructions."""
    instructions = read_input_file(file_name)
    registers = {'a': initial_a, 'b': 0, 'c': 0, 'd': 0}
    position = 0
    while position < len(instructions):
        position = process_instruction(position, instructions, registers)

    return f'{registers["a"]= }'


if __name__ == '__main__':
    print(f"Part I: {compute('input/input23.txt', initial_a=7)}")
    print(f"Part II: {compute('input/input23.txt', initial_a=12)}")

    # output = a! + 8100
