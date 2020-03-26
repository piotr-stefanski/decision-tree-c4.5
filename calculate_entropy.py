import math

def calculatePs(occursOfDecisions):
    T = sum(list(occursOfDecisions.values()))

    return [occurInDecisions/T for occurInDecisions in list(occursOfDecisions.values())]

def calculate(ps):
    if 0 in ps:
        return 0

    return -sum([p * math.log2(p) for p in ps])




