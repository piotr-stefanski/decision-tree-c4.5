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

def getNewNodesByAttribute(attributeIndex, attributes, decisions):
    attrValues = [attribute[attributeIndex] for attribute in attributes]
    availableAttrValues = list(set(attrValues))

    nodes = []
    for availableAttrValue in availableAttrValues:
        attrIndexes = [i for i in range(len(attrValues)) if attrValues[i] == availableAttrValue]
        node = Node.Node(
            list(itemgetter(*attrIndexes)(attributes)),
            list(itemgetter(*attrIndexes)(decisions))
        )

        nodes.append(node)

    return nodes