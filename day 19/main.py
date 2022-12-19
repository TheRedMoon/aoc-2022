import re
#random choices, don't want to implement dfs again.
from random import random


def extract_resources(s):
    resource_pattern = r'(\d+) ([a-z]+)'
    resources = re.findall(resource_pattern, s)
    return resources

def parse_input(content):
    lines = content.splitlines()
    blueprints = {}
    for line in lines:
        blueprint = line.split(':')
        #blueprint_id = int(blueprint[0][-1])
        #the lovely line above parsed 11 as 1, so dict 1 would get overwritten by 11. Very nice. I love bugs man
        blueprint_id = re.findall(r'\d+', blueprint[0])[0]
        robots_str = blueprint[1].split(".")
        del robots_str[-1]
        robots = {}
        tuple = extract_resources(robots_str[0])
        tuple = [(t[1], int(t[0])) for t in tuple]
        robots["ore"] = tuple

        tuple = extract_resources(robots_str[1])
        tuple = [(t[1], int(t[0])) for t in tuple]
        robots["clay"] = tuple

        tuple = extract_resources(robots_str[2])
        tuple = [(t[1], int(t[0])) for t in tuple]
        robots["obsidian"] = tuple

        tuple = extract_resources(robots_str[3])
        tuple = [(t[1], int(t[0])) for t in tuple]
        robots["geode"] = tuple
        blueprints[blueprint_id] = robots
    return blueprints


def can_construct(resources, costs):
    #print(f"Resources available : {resources}")
    #print(f"Costs of Robot : {costs}")
    old_resources = resources.copy()
    for cost in costs:
        resource, amount = cost
        available = resources[resource]
        #print(f"Available {available} vs cost {amount}")
        if available < amount:
            return False, old_resources
        resources[resource] -= amount
    return True, resources


def costs_satisfied(resources, costs):
    for cost in costs:
        resource, amount = cost
        available = resources[resource]
        if available < amount:
            return False
    return True

def construct_robot(resources, blueprint):
    rnd = random()
    resource = "geode"
    costs = blueprint[resource]
    #always make geode bot if we can
    if costs_satisfied(resources,costs):
        for item in costs:
            r,num = item
            resources[r] -= num
        return resource, resources
    elif rnd <= 0.3 and costs_satisfied(resources, blueprint["ore"]):
        for item in blueprint["ore"]:
            r,num = item
            resources[r] -= num
        return "ore", resources
    elif rnd <= 0.7 and costs_satisfied(resources, blueprint["obsidian"]):
        for item in blueprint["obsidian"]:
            r,num = item
            resources[r] -= num
        return"obsidian", resources
    elif rnd <= 0.9 and costs_satisfied(resources, blueprint["clay"]):
        for item in blueprint["clay"]:
            r,num = item
            resources[r] -= num
        return "clay", resources
    else:
        return None, resources



def simulate_blueprint(blueprint, minutes):
    robots_made =  {"ore": 1, "clay": 0, "obsidian": 0, "geode":0}
    resources = {"ore": 0, "clay": 0, "obsidian": 0, "geode":0}
    for min in range(1, minutes+1):
        # print(f"Minute : {min}")
 #        non_zero_robots = {k: v for k, v in robots_made.items() if v != 0}
        robot_to_build,resources = construct_robot(resources, blueprint)
        for resource, value in robots_made.items():
            resources[resource] += value
        if robot_to_build:
            robots_made[robot_to_build] += 1
        # print(f"Resources at the end {resources}")

#    print(f"Resources at the end {resources}")
#    print(f"Robots at the end {robots_made}")
    return resources["geode"]


def r1(blueprints):
    end_results = []
    minutes = 24
    for blueprint in blueprints.items():
        print(blueprint)
        results = []
        blueprint_id = int(blueprint[0])
        blueprint = blueprint[1]
        for i in range(500000): #100000 gave 841 which was too low
            results.append(simulate_blueprint(blueprint, minutes))
        max_geodes = max(results)
        print(max_geodes)
        end_results.append(max_geodes*blueprint_id)
    print(f"f1 {sum(end_results)}")

def r2(blueprints):
    end_results = []
    minutes = 32
    for blueprint in blueprints.items():
        print(blueprint)
        results = []
        blueprint_id = int(blueprint[0])
        if blueprint_id > 3:
            break
        blueprint = blueprint[1]
        for i in range(5000000): #100000 gave 841 which was too low
            results.append(simulate_blueprint(blueprint, minutes))
        max_geodes = max(results)
        print(max_geodes)
        end_results.append(max_geodes)
    print(end_results)
    print(f"f2 {end_results[0] * end_results[1] * end_results[2]}")


if __name__ == '__main__':
    with open("input.txt") as file:
        content = file.read() #can use str as char list
    blueprints = parse_input(content)
    #r1(blueprints)
    r2(blueprints)

