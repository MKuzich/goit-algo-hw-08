import heapq

def min_cost_to_connect_ropes(ropes):
    heapq.heapify(ropes)
    total_cost = 0
    while len(ropes) > 1:
        cost = heapq.heappop(ropes) + heapq.heappop(ropes)
        total_cost += cost
        heapq.heappush(ropes, cost)
    return total_cost

arr = [5, 25, 15, 10 , 30, 20]
print('Min spendings for cables connecting: ', min_cost_to_connect_ropes(arr))