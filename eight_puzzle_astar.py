"""Solve the 8-puzzle optimally with A* and Manhattan distance."""

from heapq import heappop, heappush
from itertools import count
from sys import argv

SIZE = 3
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)
GOAL_POS = {tile: divmod(i, SIZE) for i, tile in enumerate(GOAL)}

# For every blank position: (new blank position, direction of blank movement).
NEIGHBORS = tuple(
    tuple(
        (nr * SIZE + nc, move)
        for dr, dc, move in ((-1, 0, "Up"), (1, 0, "Down"),
                             (0, -1, "Left"), (0, 1, "Right"))
        if 0 <= (nr := i // SIZE + dr) < SIZE
        and 0 <= (nc := i % SIZE + dc) < SIZE
    )
    for i in range(SIZE * SIZE)
)


def manhattan(state):
    """Return the sum of each tile's distance from its goal position."""
    return sum(
        abs(i // SIZE - GOAL_POS[tile][0])
        + abs(i % SIZE - GOAL_POS[tile][1])
        for i, tile in enumerate(state) if tile
    )


def is_solvable(state):
    """A 3x3 puzzle is solvable exactly when its inversion count is even."""
    tiles = [tile for tile in state if tile]
    inversions = sum(
        tiles[i] > tiles[j]
        for i in range(len(tiles))
        for j in range(i + 1, len(tiles))
    )
    return inversions % 2 == 0


def solve(start):
    """Return (states, moves, expanded) for an optimal solution, or None."""
    start = tuple(start)
    if len(start) != 9 or set(start) != set(range(9)):
        raise ValueError("state must contain each number from 0 to 8 exactly once")
    if not is_solvable(start):
        return None

    serial = count()
    start_h = manhattan(start)
    frontier = [(start_h, start_h, next(serial), start)]
    best_g = {start: 0}
    parent = {start: (None, None)}
    expanded = 0

    while frontier:
        f, h, _, state = heappop(frontier)
        g = f - h
        if g != best_g.get(state):       # Ignore stale heap entries.
            continue
        if state == GOAL:
            states, moves = [], []
            while state is not None:
                states.append(state)
                state, move = parent[state]
                if move:
                    moves.append(move)
            return states[::-1], moves[::-1], expanded

        expanded += 1
        blank = state.index(0)
        br, bc = divmod(blank, SIZE)
        for swap, move in NEIGHBORS[blank]:
            next_state = list(state)
            tile = next_state[swap]
            next_state[blank], next_state[swap] = tile, 0
            next_state = tuple(next_state)
            next_g = g + 1

            if next_g >= best_g.get(next_state, float("inf")):
                continue

            # Only the swapped tile changes its Manhattan contribution.
            tr, tc = GOAL_POS[tile]
            old_distance = abs(swap // SIZE - tr) + abs(swap % SIZE - tc)
            new_distance = abs(br - tr) + abs(bc - tc)
            next_h = h - old_distance + new_distance
            best_g[next_state] = next_g
            parent[next_state] = (state, move)
            heappush(frontier, (next_g + next_h, next_h,
                                next(serial), next_state))

    return None


def show(state):
    """Format one puzzle state."""
    cells = [str(tile) if tile else "_" for tile in state]
    return "\n".join(" ".join(cells[i:i + SIZE]) for i in range(0, 9, SIZE))


def main():
    try:
        start = tuple(map(int, argv[1:])) if len(argv) > 1 else (
            1, 2, 3,
            4, 0, 6,
            7, 5, 8,
        )
        result = solve(start)
    except ValueError as error:
        raise SystemExit(f"Error: {error}") from error

    if result is None:
        print("This puzzle is not solvable.")
        return

    states, moves, expanded = result
    print(f"Solved optimally in {len(moves)} moves: "
          f"{' -> '.join(moves) or 'Already solved'}")
    print(f"Expanded nodes: {expanded}\n")
    for step, state in enumerate(states):
        label = "Start" if step == 0 else f"{step}. {moves[step - 1]}"
        print(f"{label}\n{show(state)}\n")


if __name__ == "__main__":
    main()
