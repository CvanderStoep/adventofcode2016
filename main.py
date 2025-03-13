from typing import List, Dict


def read_input_file(file_name: str) -> List[str]:
    """Reads input file and returns content as a list of strings."""
    with open(file_name) as f:
        return f.read().splitlines()


def inc(registers: Dict[str, int], x: str) -> None:
    registers[x] += 1


def dec(registers: Dict[str, int], x: str) -> None:
    registers[x] -= 1


def cpy(registers: Dict[str, int], src: str, dest: str) -> None:
    registers[dest] = registers[src] if src in 'abcd' else int(src)


def jnz(registers: Dict[str, int], src: str, offset: str) -> int:
    x = int(src) if src.isdigit() else registers[src]
    return int(offset) if offset.isdigit() else registers[offset] if x != 0 else 1


def tgl(registers: Dict[str, int], position: int, instructions: List[str], x: str) -> int:
    tgl_position = position + registers[x]
    if 0 <= tgl_position < len(instructions):
        tgl_instruction = instructions[tgl_position].split(' ')
        if len(tgl_instruction) == 2:
            instructions[tgl_position] = 'dec' if tgl_instruction[0] == 'inc' else 'inc ' + tgl_instruction[1]
        elif len(tgl_instruction) == 3:
            instructions[tgl_position] = 'cpy' if tgl_instruction[0] == 'jnz' else 'jnz ' + tgl_instruction[1] + ' ' + \
                                                                                   tgl_instruction[2]
    return position + 1


def mul(registers: Dict[str, int], x: str, y: str, z: str) -> None:
    registers[z] = registers[x] * registers[y]


def process_instruction(position: int, instructions: List[str], registers: Dict[str, int]) -> int:
    """Processes a single instruction and updates the registers."""
    instruction = instructions[position].split(' ')
    cmd = instruction[0]
    args = instruction[1:]

    commands = {
        'inc': inc,
        'dec': dec,
        'cpy': cpy,
        'jnz': jnz,
        'tgl': tgl,
        'mul': mul
    }

    if cmd == 'jnz':
        return position + commands[cmd](registers, *args)
    elif cmd == 'tgl':
        return commands[cmd](registers, position, instructions, *args)
    else:
        commands[cmd](registers, *args)
        return position + 1


def compute(file_name: str, initial_a: int) -> str:
    """Computes the value of register 'a' after processing all instructions."""
    instructions = read_input_file(file_name)
    registers = {'a': initial_a, 'b': 0, 'c': 0, 'd': 0}
    position = 0
    while position < len(instructions):
        position = process_instruction(position, instructions, registers)
        print(registers)
        input()
    return f'{registers["a"]= }'


if __name__ == '__main__':
    print(f"Part I: {compute('input/input23.txt', initial_a=7)}")
    print(f"Part II: {compute('input/input23.txt', initial_a=12)}")
