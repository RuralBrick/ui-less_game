import sys
import random


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


def graphs():
    class Node:
        def __init__(self, name) -> None:
            self.name = name
            self.neighbors = []

    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')
    e = Node('E')
    f = Node('F')
    g = Node('G')
    h = Node('H')
    i = Node('I')
    j = Node('J')
    k = Node('K')
    l = Node('L')
    m = Node('M')
    n = Node('N')
    o = Node('O')

    a.neighbors.extend([b, c])
    b.neighbors.extend([a, c, e, g])
    c.neighbors.extend([a, b, d])
    d.neighbors.extend([c, f, i])
    e.neighbors.extend([b, f, h, i, l])
    f.neighbors.extend([d, e, h, k])
    g.neighbors.extend([b, j])
    h.neighbors.extend([e, f, j])
    i.neighbors.extend([d, e, n])
    j.neighbors.extend([g, h, m])
    k.neighbors.extend([f, l])
    l.neighbors.extend([e, k, o])
    m.neighbors.extend([j])
    n.neighbors.extend([i])
    o.neighbors.extend([l])

    pos = a

    while pos is not o:
        print(f"You are at {pos.name} "
              f"({', '.join(str(i+1) for i in range(len(pos.neighbors)))}) ",
              end='')
        try:
            pos = pos.neighbors[int(input())-1]
        except (ValueError, IndexError):
            pass
    say("Congratulations! You made it out of the graph!")


def connect4(breadth=None, depth=None, start_with_computer=False):
    NUM_ROW = 6
    NUM_COL = 7
    NUM_WIN = 4
    MCTS_BREADTH = breadth or 20
    MCTS_DEPTH = depth or 4

    class Player:
        USER = -1
        COMPUTER = 1

        def other(player):
            return Player.USER if player is not Player.USER else Player.COMPUTER

    class Piece:
        def __init__(self, row, col, player) -> None:
            self.row = row
            self.col = col
            self.player = player

        def __hash__(self) -> int:
            return self.row + self.col*NUM_ROW

        def __eq__(self, __value: object) -> bool:
            return (self.row == __value.row
                    and self.col == __value.col
                    and self.player == __value.player)

    class State:
        def __init__(self) -> None:
            self.pieces = set()

        def copy(self) -> object:
            __other = State()
            __other.pieces = self.pieces.copy()
            return __other

        def add_piece(self, column, player) -> bool:
            try:
                row = 1 + max([piece.row for piece in self.pieces
                               if piece.col == column])
            except ValueError:
                row = 0
            if 0 > row or row >= NUM_ROW or 0 > column or column >= NUM_COL:
                return False
            piece = Piece(row, column, player)
            if piece in self.pieces:
                return False
            self.pieces.add(Piece(row, column, player))
            return True

    def check_win(state) -> int | None:
        for piece in state.pieces:
            vert = all(Piece(piece.row, piece.col+i, piece.player)
                       in state.pieces for i in range(NUM_WIN))
            hori = all(Piece(piece.row+i, piece.col, piece.player)
                       in state.pieces for i in range(NUM_WIN))
            slant_up = all(Piece(piece.row+i, piece.col+i, piece.player)
                           in state.pieces for i in range(NUM_WIN))
            slant_down = all(Piece(piece.row+i, piece.col-i, piece.player)
                             in state.pieces for i in range(NUM_WIN))
            if vert or hori or slant_up or slant_down:
                return piece.player
        return None

    def board_full(state) -> bool:
        return len(state.pieces) == NUM_ROW * NUM_COL

    def game_over(state) -> tuple[bool, int | None]:
        if player := check_win(state):
            return True, player
        if board_full(state):
            return True, 0
        return False, None

    def play_from_state(state, current_player) -> int:
        for _ in range(MCTS_DEPTH):
            stop, player = game_over(state)
            if stop:
                return player
            while not state.add_piece(random.randrange(NUM_COL),
                                      current_player):
                pass
            current_player = Player.other(current_player)
        return 0

    def pure_monte_carlo_search(state) -> int:
        move_states = ((move, state.copy()) for move in range(NUM_COL))
        move_states = filter(lambda ms: ms[1].add_piece(ms[0], Player.COMPUTER),
                             move_states)
        results = [(move, sum(play_from_state(next.copy(), Player.USER)
                              for _ in range(MCTS_BREADTH)))
                   for move, next in move_states]
        random.shuffle(results)
        move, value = max(results, key=lambda mv: mv[1])
        return move

    while True:
        state = State()
        player = Player.USER if not start_with_computer else Player.COMPUTER
        finished, winner = game_over(state)
        while not finished:
            match player:
                case Player.USER:
                    while True:
                        print(f"({', '.join(str(i+1) for i in range(NUM_COL))}"
                              f") ", end='')
                        try:
                            move = int(input()) - 1
                            if (0 <= move < NUM_COL
                                and state.add_piece(move, Player.USER)):
                                break
                        except ValueError:
                            pass
                        print("Invalid move")
                case Player.COMPUTER:
                    move = pure_monte_carlo_search(state)
                    print(f"Computer plays {move+1}")
                    state.add_piece(move, Player.COMPUTER)
            finished, winner = game_over(state)
            player = Player.other(player)
        match winner:
            case Player.USER:
                break
            case Player.COMPUTER:
                say("The computer beat you. Try again.")
            case _:
                say("The board filled up. Try again.")
    say("Congratulations! You beat the computer!")


def main():
    global progress

    if sys.version[:4] != '3.10':
        print("Please rerun this script using Python 3.10")
        return

    with open('./game_files/script.txt') as f:
        script = f.read()

    levels = script.splitlines()

    print("(Press [enter] to continue. Press [ctrl/cmnd]-[C] to quit.)")

    try:
        with open('./game_files/progress.txt') as f:
            progress = set(filter(None, f.read().splitlines()))
        levels = filter(lambda level: level not in progress, levels)
    except FileNotFoundError:
        progress = set()

    if progress:
        hello, *_ = load_prompts('00-hello')
        say(hello)

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
        goodbye, *_ = load_prompts('00-goodbye')
        print(f'\n{goodbye}')
    finally:
        with open(f'./game_files/progress.txt', 'w') as f:
            f.write('\n'.join(progress) + '\n')
