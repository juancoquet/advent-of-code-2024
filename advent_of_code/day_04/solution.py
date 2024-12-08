from rich import print

XMAS = "XMAS"
MAS = "MAS"


DIRECTIONS = {
    "LEFT": (0, -1),
    "RIGHT": (0, 1),
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "UL": (-1, -1),
    "UR": (-1, 1),
    "DL": (1, -1),
    "DR": (1, 1),
}


def part_1(inputs: list[list[str]]) -> int:
    hits = 0
    for r in range(len(inputs)):
        for c in range(len(inputs[r])):
            hits += _search_xmas(r, c, inputs)
    return hits


def part_2(inputs: list[list[str]]) -> int:
    hits = 0
    for r in range(len(inputs)):
        for c in range(len(inputs[r])):
            hits += _search_x_mas(r, c, inputs)
    return hits


def _search_xmas(r: int, c: int, inputs: list[list[str]]) -> int:
    if not inputs[r][c] == XMAS[0]:
        return 0
    hits = 0
    curr_r, curr_c = r, c
    for x, y in DIRECTIONS.values():
        direction_hit = False
        for i, char in enumerate(XMAS):
            if _is_out_of_bounds(curr_r, curr_c, inputs) or not inputs[curr_r][curr_c] == char:
                break
            direction_hit = i == len(XMAS) - 1
            curr_r += x
            curr_c += y
        hits += int(direction_hit)
        curr_r, curr_c = r, c
    return hits


def _search_x_mas(r: int, c: int, inputs: list[list[str]]) -> int:
    if not inputs[r][c] == MAS[1]:
        return 0

    dir_complements = [
        (DIRECTIONS["UL"], DIRECTIONS["DR"]),
        (DIRECTIONS["UR"], DIRECTIONS["DL"]),
        (DIRECTIONS["DL"], DIRECTIONS["UR"]),
        (DIRECTIONS["DR"], DIRECTIONS["UL"]),
    ]

    curr_r, curr_c = r, c
    hits = 0
    for start_dir, (x, y) in dir_complements:
        curr_r += start_dir[0]
        curr_c += start_dir[1]
        direction_hit = False
        for i, char in enumerate(MAS):
            if _is_out_of_bounds(curr_r, curr_c, inputs) or not inputs[curr_r][curr_c] == char:
                break
            direction_hit = i == len(MAS) - 1
            curr_r += x
            curr_c += y
        hits += int(direction_hit)
        curr_r, curr_c = r, c
    return int(hits == 2)  # 2 hits in an X shape


def _is_out_of_bounds(r: int, c: int, inputs: list[list[str]]) -> bool:
    max_r, max_c = len(inputs) - 1, len(inputs[0]) - 1
    return r < 0 or c < 0 or r > max_r or c > max_c


def parse_data(raw_data: str) -> list[list[str]]:
    return [[c for c in line.strip()] for line in raw_data.split("\n")]


def _read_inputs() -> list[list[str]]:
    with open("advent_of_code/day_04/inputs.txt", "r") as f:
        raw_data = f.read().strip()
    return parse_data(raw_data)


if __name__ == "__main__":
    inputs = _read_inputs()
    print(part_1(inputs))
    print(part_2(inputs))
