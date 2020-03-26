import functions
import main
import Node

data = functions.read_file('data/test3.txt')
rows = data.split('\n')

attributes, decisions = functions.getDecisionsAndAttributesFromRows(rows)
rootNode = Node.Node(attributes, decisions)
