import bisect

N, K = map(int, input().split())
Ps = [int(v) for v in input().split()]

deleted_turn_list = [-1] * N
cards = []
cards_min = []

for turn, P in enumerate(Ps, 1):
    index = bisect.bisect_left(cards_min, P)

    if index < len(cards_min):
        cards_min[index] = P
        cards[index].append(P)
    else:
        cards_min.insert(index, P)
        cards.append([P])

    if len(cards[index]) == K:
        for number in cards[index]:
            deleted_turn_list[number - 1] = turn
        del cards[index]
        del cards_min[index]

for turn in deleted_turn_list:
    print(turn)

