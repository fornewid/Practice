def max_cost_effect(origin_cost, origin_p, available_cost, available_ps):
    basic_cost_effect = origin_p / origin_cost
    min_ps = basic_cost_effect * available_cost
    over_min_ps = [ p for p in available_ps if p > min_ps ]
    return int((origin_p + sum(over_min_ps))
               / (origin_cost + available_cost * len(over_min_ps)))

# print(max_cost_effect(10, 150, 3, [30, 70, 15, 40, 65]))