import functions
import main

data = functions.read_file('data/test3.txt')
rows = data.split('\n')

attributes, decisions = functions.getDecisionsAndAttributesFromRows(rows)

gainRatio = main.getGainRatioForData(attributes, decisions)
splitAttributeIndex = gainRatio.index(max(gainRatio))
functions.getNewNodesByAttribute(splitAttributeIndex, attributes, decisions)
