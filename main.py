import functions
import calculate_entropy
import calculate_information
import calculate_gain_ratio

def getGainRatiosForNode(Node):
    countOccurValuesFromColumns = functions.getCountOccurValuesFromColumns(Node.attributes)

    information = calculate_information.calculate(Node.decisions, Node.attributes, countOccurValuesFromColumns)
    gainRatio = calculate_gain_ratio.calculate(Node.attributes, countOccurValuesFromColumns, information)

    return gainRatio

def isContinueToBuildingTree(gainRatios):
    return max(gainRatios) > 0