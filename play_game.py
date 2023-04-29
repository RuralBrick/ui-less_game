progress = set()


def say(*values):
    print(*values, end='')
    input()


def load_prompts(name):
    with open(f'./game_files/{name}.txt') as f:
        script = f.read()

    prompts = script.split('\n\n')
    prompts = [prompt.replace('\n', ' ') for prompt in prompts]
    prompts = map(lambda prompt: prompt.strip(), prompts)
    prompts = filter(None, prompts)

    return prompts


def mazes():
    walls = {
           (1,10),(3,10),(5,10),(7,10),(9,10),
        (0,9),      (4,9),      (8,9),(10,9),
           (1,8),            (7,8),
        (0,7),            (6,7),      (10,7),
                 (3,6),
        (0,5),      (4,5),      (8,5),(10,5),
           (1,4),      (5,4),(7,4),
        (0,3),      (4,3),            (10,3),
                 (3,2),            (9,2),
        (0,1),            (6,1),      (10,1),
           (1,0),(3,0),(5,0),(7,0),(9,0),
    }
    pos = (1, 5)
    while pos != (9,5):
        print(f"You are at {chr(ord('A') + pos[0]//2)}{pos[1]//2 + 1} "
              f"(w, a, s, d) ", end='')
        match input():
            case 'w':
                pass_point = (pos[0], pos[1]+1)
                new_pos = (pos[0], pos[1]+2)
            case 'a':
                pass_point = (pos[0]-1, pos[1])
                new_pos = (pos[0]-2, pos[1])
            case 's':
                pass_point = (pos[0], pos[1]-1)
                new_pos = (pos[0], pos[1]-2)
            case 'd':
                pass_point = (pos[0]+1, pos[1])
                new_pos = (pos[0]+2, pos[1])
            case _:
                continue
        if pass_point in walls:
            print("You hit a wall")
            continue
        pos = new_pos
    say("Congratulations! You made it out of the maze!")


def main():
    global progress

    with open('./game_files/script.txt') as f:
        script = f.read()

    levels = script.splitlines()

    print("(Press [enter] to continue. Press [ctrl/cmnd]-[C] to quit.)")

    try:
        with open('./game_files/progress.txt') as f:
            progress = set(f.read().splitlines())
        levels = [level for level in levels if level not in progress]
        hello, *_ = load_prompts('hello')
        say(hello)
    except FileNotFoundError:
        progress = set()

    for level in levels:
        for prompt in load_prompts(level):
            tokens = prompt.split(' ')
            match tokens[0]:
                case 'START':
                    globals()[tokens[1]]()
                case _:
                    say(prompt)
        progress.add(level)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        goodbye, *_ = load_prompts('goodbye')
        print(f'\n{goodbye}')
    finally:
        with open(f'./game_files/progress.txt', 'w') as f:
            f.write('\n'.join(progress) + '\n')
