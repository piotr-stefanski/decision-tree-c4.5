import main
import functions

class Node:
    children = None

    def __init__(self, attributes, decisions):
        self.decisions = decisions
        self.attributes = attributes

        self.findChildren()

    def __str__(self):
        return "attributes: {} ; decisions: {}".format(self.attributes, self.decisions)

    def findChildren(self):
        gainRatios = main.getGainRatiosForNode(self)
        if main.isContinueToBuildingTree(gainRatios):
            nodes = functions.findNodeChildren(gainRatios, self)
            self.children = nodes