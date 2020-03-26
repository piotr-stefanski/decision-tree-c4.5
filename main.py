import functions
import calculate_entropy
import calculate_information
import calculate_gain_ratio

def getGainRatioForData(attributes, decisions):
    # 2 liczba możliwych wartości atrybutów
    uniqueValues = functions.getCountOccurValuesFromColumns(attributes)
    countUniqueValues = [len(uniqueValues[i]) for i in uniqueValues]

    # 3 wyliczyć wystąpienia poszczególnych atrybutów w kolumnach
    countOccurValuesFromColumns = functions.getCountOccurValuesFromColumns(attributes)

    # wyliczanie entropii
    occursOfDecision = functions.getCountOccurValuesFromColumns(decisions)[0]
    entropy = calculate_entropy.calculate(
        calculate_entropy.calculatePs(occursOfDecision)
    )

    # wyliczanie zrównoważonego przyrostu informacji
    information = calculate_information.calculate(decisions, attributes, countOccurValuesFromColumns)
    gainRatio = calculate_gain_ratio.calculate(attributes, countOccurValuesFromColumns, information)

    return gainRatio

def isContinueToBuildingTree(gainRatios):
    return max(gainRatios) > 0