import heapq


def min_cost_cables_connection(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first_shortest_cable = heapq.heappop(cables)
        next_shortest_cable = heapq.heappop(cables)

        connected_cables = first_shortest_cable + next_shortest_cable

        heapq.heappush(cables, connected_cables)

        total_cost += connected_cables

    return total_cost


cables = [5, 12, 25, 8, 3, 2, 7]

print("Мінімальні витрати на об'єднання кабелів:", min_cost_cables_connection(cables))
