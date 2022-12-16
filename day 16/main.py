import re
from collections import deque, defaultdict
from dataclasses import dataclass
from typing import List
from math import inf

@dataclass
class Valve:
        name: str
        flow_rate : int
        neighbors : List


def parse_input(content):
    valves = {words[1]: Valve(words[1], int(re.findall(r"-?\d+", words[4])[0]), [id.replace(",","") for id in words[9:]])
              for words in (line.split() for line in content.splitlines())}
    return valves

def floyd_warshall(valves, dist):
    for k in valves.keys():
        for i in valves.keys():
            for j in valves.keys():
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

def find_max_flow_rate_without_elephant(current_node: str, time: int, remaining_nodes: set, distance: dict, valves: dict) -> int:
    max_flow_rate = 0
    for next_node in remaining_nodes:
        # calculate the time we have at the next node by subtracting the distance
        # between the current node and the next node, as well as the time it takes
        # to switch valves, which is always 1
        time_at_next_node = time - distance[current_node][next_node] - 1

        if time_at_next_node >= 0:
            flow_rate_at_next_node = valves[next_node].flow_rate * time_at_next_node
            #remove node visited
            remaining_nodes_without_next_node = remaining_nodes - {next_node}

            # recursively call the function to find the maximum flow rate from the next node
            flow_rate_from_next_node = find_max_flow_rate_without_elephant(next_node, time_at_next_node,
                                                          remaining_nodes_without_next_node, distance, valves)

            total_flow_rate = flow_rate_at_next_node + flow_rate_from_next_node

            max_flow_rate = max(max_flow_rate, total_flow_rate)

    return max_flow_rate

def find_max_flow_rate_with_elephant(current_node: str, time: int, remaining_nodes: set, distance: dict, valves: dict) -> int:
    max_flow_rate = find_max_flow_rate_without_elephant("AA",26,remaining_nodes,distance,valves)
    for next_node in remaining_nodes:
        # calculate the time we have at the next node by subtracting the distance
        # between the current node and the next node, as well as the time it takes
        # to switch valves, which is always 1
        time_at_next_node = time - distance[current_node][next_node] - 1

        if time_at_next_node >= 0:
            flow_rate_at_next_node = valves[next_node].flow_rate * time_at_next_node
            #remove node visited
            remaining_nodes_without_next_node = remaining_nodes - {next_node}

            # recursively call the function to find the maximum flow rate from the next node
            flow_rate_from_next_node = find_max_flow_rate_with_elephant(next_node, time_at_next_node,
                                                          remaining_nodes_without_next_node, distance, valves)

            total_flow_rate = flow_rate_at_next_node + flow_rate_from_next_node

            max_flow_rate = max(max_flow_rate, total_flow_rate)

    return max_flow_rate


if __name__ == '__main__':
    with open("input.txt") as file:
        content = file.read()

    valves = parse_input(content)

    dist = defaultdict(lambda: defaultdict(lambda: float("inf")))

    # Set the distance between each valve and itself to 0
    for i in valves.values():
        dist[i.name][i.name] = 0

    # Set the edges between the connected valves with 1
    for v in valves.values():
        for nb in v.neighbors:
            i = v.name
            j = valves[nb].name
            dist[i][j] = 1

    shortest_dist = floyd_warshall(valves, dist)

    #do not visit anything with flow rate 0
    not_visited = set(x for x in valves if valves[x].flow_rate > 0)

    f1 = find_max_flow_rate_without_elephant("AA", 30, not_visited, dist, valves)
    print(f1)
    f2 = find_max_flow_rate_with_elephant("AA", 26, not_visited, dist, valves)
    print(f2)