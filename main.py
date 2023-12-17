from State import State


def main():
    state = State()
    print(state)
    print()

    print("empty tile search")
    empty_tile_index = state.linear_search(0)
    print(empty_tile_index)

    print("empty tile state")
    print(state.empty_tile)
    print()

    state.swap_tiles([0, 1], [1, 1])
    print(state)
    print()
    print(state.empty_tile)


if __name__ == "__main__":
    main()
