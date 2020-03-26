import functions
import calculate_entropy

def calculate(attributes, countOccurValuesFromColumns, information):
    T = functions.calculateT(countOccurValuesFromColumns)
    countAttributes = len(attributes[0])

    gainRatio = []
    for x in range(countAttributes):
        availableAttributeValues = countOccurValuesFromColumns[x].keys()
        ps = [countOccurValuesFromColumns[x][attributeValue] / T for attributeValue in availableAttributeValues]
        entropy = calculate_entropy.calculate(ps)

        gainRatio.append((1-information[x])/entropy)

    return gainRatio
