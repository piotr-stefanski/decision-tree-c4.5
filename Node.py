import main
import functions

class Node:
    children = None
    finalDecision = None
    attributeIndex = None

    def __init__(self, attributes, decisions, question=None):
        self.question = question
        self.decisions = decisions
        self.attributes = attributes

        self.findChildren()

    def __str__(self):
        return "attributes: {}; decisions: {}; attribute index: {}; question: {}".format(self.attributes, self.decisions, self.attributeIndex, self.question)

    def findChildren(self):
        gainRatios = main.getGainRatiosForNode(self)
        if main.isContinueToBuildingTree(gainRatios):
            self.children = functions.findNodeChildren(gainRatios, self)
        else:
            self.finalDecision = self.decisions[0]
