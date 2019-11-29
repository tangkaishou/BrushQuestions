class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        sum_distance = sum(distance)
        if start <= destination:
            first_distance = sum(distance[start:destination])
        else:
            first_distance = sum(distance[destination:start])
        return min(first_distance, sum_distance-first_distance)
