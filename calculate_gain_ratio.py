import functions
import calculate_entropy

def calculate(Node, countOccurValuesFromColumns, information):
    T = functions.calculateT(countOccurValuesFromColumns)
    countAttributes = len(Node.attributes[0])

    gainRatio = []
    for x in range(countAttributes):
        availableAttributeValues = countOccurValuesFromColumns[x].keys()
        ps = [countOccurValuesFromColumns[x][attributeValue] / T for attributeValue in availableAttributeValues]
        entropy = calculate_entropy.calculate(ps)

        # TODO sure ???!
        if entropy == 0:
            gainRatio.append(0)
            continue

        availableDecisionValues = list(set(Node.decisions))
        ps = [Node.decisions.count(availableDecisionValue)/len(Node.decisions) for availableDecisionValue in availableDecisionValues]
        gainRatio.append((calculate_entropy.calculate(ps)-information[x])/entropy)

    return gainRatio
