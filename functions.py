from operator import itemgetter
import Node

def read_file(src):
    f = open(src, "r")
    data = f.read()
    f.close()

    return data

def getCountOccurValuesFromColumns(attributes):
    tmpObj = {}
    for row in attributes:
        for columnKey, el in enumerate(row):
            if columnKey not in tmpObj:
                tmpObj[columnKey] = {}
            if el in tmpObj[columnKey]:
                tmpObj[columnKey][el] += 1
            else:
                tmpObj[columnKey][el] = 1

    return tmpObj

def getDecisionsAndAttributesFromRows(rows):
    tmpArr = []
    for rowKey, row in enumerate(rows):
        row = row.split(',')
        tmpArr.append(row.pop())
        rows[rowKey] = row

    return rows, tmpArr

def calculateT(countOccurValuesFromColumns):
    return sum(list(countOccurValuesFromColumns[0].values()))

def findNodeChildren(gainRatios, ParentNode):
    splitAttributeIndex = gainRatios.index(max(gainRatios))
    ParentNode.attributeIndex = splitAttributeIndex

    attrValues = [attribute[splitAttributeIndex] for attribute in ParentNode.attributes] if type(ParentNode.attributes[0]) is list else [ParentNode.attributes[splitAttributeIndex]]
    availableAttrValues = list(set(attrValues))

    nodes = []
    for availableAttrValue in availableAttrValues:
        attrIndexes = [i for i in range(len(attrValues)) if attrValues[i] == availableAttrValue]
        childNodeAttributes = list(itemgetter(*attrIndexes)(ParentNode.attributes))

        node = Node.Node(
            childNodeAttributes if type(childNodeAttributes[0]) is list else [childNodeAttributes],
            list(itemgetter(*attrIndexes)(ParentNode.decisions)) if len(attrIndexes) > 1 else [ParentNode.decisions[attrIndexes[0]]],
            availableAttrValue
        )
        nodes.append(node)

    return nodes

def printNode(Node, slide):
    if Node.children:
        print(" " * slide, end="")
        if Node.question:
            print(Node.question, end=" -> ")
        print("Atrybut", Node.attributeIndex)

        for child in Node.children:
            printNode(child, slide+4)
    else:
        print(" " * slide, end="")
        print(Node.question, "->", Node.finalDecision)