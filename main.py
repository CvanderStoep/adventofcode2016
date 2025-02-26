import unittest


class TestProgram(unittest.TestCase):

    def test_read_input_file(self):
        # Test reading a sample input file
        with open('test_input.txt', 'w') as f:
            f.write('cpy 41 a\ninc a\ndec a\njnz a 2\ndec a\n')

        expected_output = ['cpy 41 a', 'inc a', 'dec a', 'jnz a 2', 'dec a']
        self.assertEqual(read_input_file('test_input.txt'), expected_output)

    def test_process_instruction(self):
        instructions = ['cpy 41 a', 'inc a', 'dec a', 'jnz a 2', 'dec a']
        registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
        position = 0

        position = process_instruction(position, instructions, registers)
        self.assertEqual(registers['a'], 41)
        self.assertEqual(position, 1)

        position = process_instruction(position, instructions, registers)
        self.assertEqual(registers['a'], 42)
        self.assertEqual(position, 2)

        position = process_instruction(position, instructions, registers)
        self.assertEqual(registers['a'], 41)
        self.assertEqual(position, 3)

        position = process_instruction(position, instructions, registers)
        self.assertEqual(position, 5)

        position = process_instruction(position, instructions, registers)
        self.assertEqual(registers['a'], 41)

    def test_compute_part_one(self):
        # Test compute_part_one with a sample input file
        with open('test_input.txt', 'w') as f:
            f.write('cpy 41 a\ninc a\ndec a\njnz a 2\ndec a\n')

        expected_output = "registers['a']=41"
        self.assertEqual(compute_part_one('test_input.txt'), expected_output)

    def test_compute_part_two(self):
        # Test compute_part_two with a sample input file
        with open('test_input.txt', 'w') as f:
            f.write('cpy 41 a\ninc a\ndec a\njnz a 2\ndec a\n')

        expected_output = "registers['a']=41"
        self.assertEqual(compute_part_two('test_input.txt'), expected_output)


if __name__ == '__main__':
    unittest.main()
