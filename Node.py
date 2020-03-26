class Node:
    def __init__(self, attributes, decisions):
        self.decisions = decisions
        self.attributes = attributes

    def __str__(self):
        return "attributes: {} ; decisiions: {}".format(self.attributes, self.decisions)