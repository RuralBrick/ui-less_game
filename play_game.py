def mazes():
    walls = {
           (1,10),(3,10),(5,10),(7,10),(9,10),
        (0,9),      (4,9),      (8,9),(10,9),
           (1,8),            (7,8),
        (0,7),            (6,7),      (10,7),
                 (3,6),
        (0,5),      (4,5),      (8,5),
           (1,4),      (5,4),(7,4),
        (0,3),      (4,3),            (10,3),
                 (3,2),            (9,2),
        (0,1),            (6,1),      (10,1),
           (1,0),(3,0),(5,0),(7,0),(9,0),
    }
    pos = (1, 5)
    while pos != (11,5):
        print(f"You are at {chr(ord('A') + pos[0]//2)}{pos[1]//2 + 1} (w, a, s, d) ", end='')
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
    print("Congratulations! You made it out of the maze!", end='')
    input()


def main():
    with open('./game_files/script.txt') as f:
        script = f.read()

    prompts = script.split('\n\n')
    prompts = [prompt.replace('\n', ' ') for prompt in prompts]
    prompts = map(lambda prompt: prompt.strip(), prompts)
    prompts = filter(None, prompts)

    print("(Press [enter] to continue)")
    for prompt in prompts:
        tokens = prompt.split(' ')
        match tokens[0]:
            case 'START':
                globals()[tokens[1]]()
            case _:
                print(prompt, end='')
                input()


if __name__ == '__main__':
    main()
