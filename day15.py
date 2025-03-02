import re
from dataclasses import dataclass


def read_input_file(file_name: str) -> list:
    discs = []
    with open(file_name) as f:
        content = f.read().splitlines()
    for line in content:
        d = re.findall(r'(\d+)', line)
        disc = Disc(int(d[0]), int(d[1]), int(d[3]))
        discs.append(disc)

    return discs


@dataclass
class Disc:
    number: int
    positions: int
    start: int

    def calculate_position_t(self, t):
        return (self.start + t) % self.positions


def compute_part(file_name: str, part) -> str:
    if part == 1:
        discs = read_input_file(file_name)[:-1]
    else:
        discs = read_input_file(file_name)
    print(discs)

    for t in range(0, 10_000_000):
        fits = True
        disc_number = 1
        while disc_number <= len(discs):
            disc = discs[disc_number - 1]
            t_disc_n = t + disc_number
            position_disc_n = disc.calculate_position_t(t_disc_n)
            if position_disc_n != 0:
                fits = False
                break
            disc_number += 1
        if fits:
            break

    return f'fit at {t= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part('input/input15.txt', part=1)}")
    print(f"Part II: {compute_part('input/input15.txt', part=2)}")
