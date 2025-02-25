from collections import deque


def sort_string(string: str) -> str:
    return ''.join(sorted(string))


def is_valid(left, right) -> bool:
    if 'B' in left:
        state = right
    else:
        state = left

    if 'K' in state and 'G' in state:
        return False
    if 'G' in state and 'W' in state:
        return False

    return True


left = 'BGKW'
right = ''
visited = set()
queue = deque([(0, left, right, [])])


def add_queue(steps, left, right, path):
    if (left, right) not in visited and is_valid(left, right):
        queue.append((steps + 1, left, right, path))
        visited.add((left, right))


while queue:
    steps, left, right, path = queue.popleft()
    # print(steps, left, right)
    if left == '' and right == 'BGKW':
        print(f'Solution found in {steps} steps')
        print('Steps taken:')
        print('BGKW:')
        for step in path:
            print(step)
        break
    if (left, right) not in visited:
        visited.add((left, right))
    if 'B' in left:
        left = left.replace('B', '')
        for el in left:
            new_left = sort_string(left.replace(el, ''))
            new_right = sort_string(right + 'B' + el)
            add_queue(steps, new_left, new_right, path + [(new_left + f' |B{el}-> ' + new_right)])

        # move boat only
        new_left = sort_string(left.replace('B', ''))
        new_right = sort_string(right + 'B')
        add_queue(steps, new_left, new_right, path + [(new_left + f' |B-> ' + new_right)])
    else:
        right = right.replace('B', '')
        for el in right:
            new_left = sort_string(left + 'B' + el)
            new_right = sort_string(right.replace(el, ''))
            add_queue(steps, new_left, new_right, path + [(new_left + f' <-B{el}| ' + new_right)])

        # move boat only
        new_left = sort_string(left + 'B')
        new_right = sort_string(right.replace('B', ''))
        add_queue(steps, new_left, new_right, path + [(new_left + f' <-B| ' + new_right)])
