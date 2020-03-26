import calculate_entropy
import functions

def calculate(decisions, attributes, countOccurValuesFromColumns):
    countAttributes = len(attributes[0])
    T = functions.calculateT(countOccurValuesFromColumns)

    attributesInformations = []
    for x in range(countAttributes):
        availableAttributeValues = countOccurValuesFromColumns[x].keys()
        attributesOccurDecision = prepareLibraryAttributeCountDecisions(decisions, availableAttributeValues)

        for i, attribute in enumerate(attributes):
            attribute = attribute[x]
            attributesOccurDecision[attribute][decisions[i]] += 1

        attributeInfoValue = 0
        for attributeValue in availableAttributeValues:
            ps = [dupa/countOccurValuesFromColumns[x][attributeValue] for dupa in list(attributesOccurDecision[attributeValue].values())]
            entropy = calculate_entropy.calculate(ps)

            attributeInfoValue += countOccurValuesFromColumns[x][attributeValue] / T * entropy

        attributesInformations.append(attributeInfoValue)

    return attributesInformations

def prepareLibraryAttributeCountDecisions(decisions, availableAttributeValues):
    #jeszcze potrzeba liczbę możliwości dla itego atrybutu
    tmpLibrary = {}
    for attributeValue in availableAttributeValues:
        tmpLibrary[attributeValue] = {}
        for decision in list(set(decisions)):
            tmpLibrary[attributeValue][decision] = 0

    return tmpLibrary

