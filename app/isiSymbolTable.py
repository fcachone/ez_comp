import isiSymbol
from isiVariable import IsiVariable

class IsiSymbolTable:

    def __init__(self):
        self._hashTable = {}

    def add(self, symbol: IsiVariable):
        self._hashTable[symbol.getName()] = symbol
    
    def exists(self, symbolname: str):
        return (self._hashTable.get(symbolname, None) != None)

    def setUsed(self, varName):
        self._hashTable[varName].setUsed(True)

    def get(self, symbolname: str):
        return self._hashTable.get(symbolname, None)

    def checkUnused (self):
        for k in self._hashTable.keys():
            if not self._hashTable[k].getUsed():
                print("AVISO: variável '{}' não está sendo usada".format(k))

    def __str__(self):
        text=[]
        for k in self._hashTable.keys():
            text.append("Dict[{}] = {}\n".format(k, self._hashTable[k]))
        return "".join(text) 