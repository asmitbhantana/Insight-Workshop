def perform_replacement(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod", from_rod, "to rod", to_rod)
        return
    perform_replacement(n - 1, from_rod, aux_rod, to_rod)
    print("Move ", n, "disk from", from_rod, "to", to_rod)
    perform_replacement(n - 1, aux_rod, to_rod, from_rod)


if __name__ == '__main__':
    n = 4
    perform_replacement(n, 'A', 'B', 'C')
