# Generated from IsiLang.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

 

from isiExceptions import IsiSemanticException
from isiSymbol import IsiSymbol
from isiVariable import IsiVariable
from isiSymbolTable import IsiSymbolTable
from isiProgram import IsiProgram, AbstractCommand, ReadCommand, WriteCommand, AttribCommand, DecisionCommand, WhileCommand




def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\35")
        buf.write("\u00f0\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\5\17\u008b\n\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5\24")
        buf.write("\u009e\n\24\3\25\3\25\3\25\3\25\5\25\u00a4\n\25\3\26\3")
        buf.write("\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\5\26\u00b5\n\26\3\27\3\27\7\27\u00b9\n")
        buf.write("\27\f\27\16\27\u00bc\13\27\3\30\6\30\u00bf\n\30\r\30\16")
        buf.write("\30\u00c0\3\30\3\30\6\30\u00c5\n\30\r\30\16\30\u00c6\5")
        buf.write("\30\u00c9\n\30\3\31\3\31\7\31\u00cd\n\31\f\31\16\31\u00d0")
        buf.write("\13\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3")
        buf.write("\33\7\33\u00dc\n\33\f\33\16\33\u00df\13\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\34\3\34\3\34\3\34\7\34\u00ea\n\34\f\34")
        buf.write("\16\34\u00ed\13\34\3\34\3\34\3\u00dd\2\35\3\3\5\4\7\5")
        buf.write("\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35")
        buf.write("\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33")
        buf.write("\65\34\67\35\3\2\n\5\2,-//\61\61\4\2>>@@\3\2c|\5\2\62")
        buf.write(";C\\c|\3\2\62;\3\2$$\5\2\13\f\17\17\"\"\4\2\f\f\17\17")
        buf.write("\2\u00fe\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2")
        buf.write("-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3")
        buf.write("\2\2\2\2\67\3\2\2\2\39\3\2\2\2\5B\3\2\2\2\7K\3\2\2\2\t")
        buf.write("R\3\2\2\2\13X\3\2\2\2\ra\3\2\2\2\17f\3\2\2\2\21n\3\2\2")
        buf.write("\2\23q\3\2\2\2\25w\3\2\2\2\27\u0080\3\2\2\2\31\u0082\3")
        buf.write("\2\2\2\33\u0084\3\2\2\2\35\u008a\3\2\2\2\37\u008c\3\2")
        buf.write("\2\2!\u008e\3\2\2\2#\u0090\3\2\2\2%\u0092\3\2\2\2\'\u009d")
        buf.write("\3\2\2\2)\u00a3\3\2\2\2+\u00b4\3\2\2\2-\u00b6\3\2\2\2")
        buf.write("/\u00be\3\2\2\2\61\u00ca\3\2\2\2\63\u00d3\3\2\2\2\65\u00d7")
        buf.write("\3\2\2\2\67\u00e5\3\2\2\29:\7r\2\2:;\7t\2\2;<\7q\2\2<")
        buf.write("=\7i\2\2=>\7t\2\2>?\7c\2\2?@\7o\2\2@A\7c\2\2A\4\3\2\2")
        buf.write("\2BC\7h\2\2CD\7k\2\2DE\7o\2\2EF\7r\2\2FG\7t\2\2GH\7q\2")
        buf.write("\2HI\7i\2\2IJ\7=\2\2J\6\3\2\2\2KL\7p\2\2LM\7w\2\2MN\7")
        buf.write("o\2\2NO\7g\2\2OP\7t\2\2PQ\7q\2\2Q\b\3\2\2\2RS\7v\2\2S")
        buf.write("T\7g\2\2TU\7z\2\2UV\7v\2\2VW\7q\2\2W\n\3\2\2\2XY\7d\2")
        buf.write("\2YZ\7q\2\2Z[\7q\2\2[\\\7n\2\2\\]\7g\2\2]^\7c\2\2^_\7")
        buf.write("p\2\2_`\7q\2\2`\f\3\2\2\2ab\7n\2\2bc\7g\2\2cd\7k\2\2d")
        buf.write("e\7c\2\2e\16\3\2\2\2fg\7g\2\2gh\7u\2\2hi\7e\2\2ij\7t\2")
        buf.write("\2jk\7g\2\2kl\7x\2\2lm\7c\2\2m\20\3\2\2\2no\7u\2\2op\7")
        buf.write("g\2\2p\22\3\2\2\2qr\7u\2\2rs\7g\2\2st\7p\2\2tu\7c\2\2")
        buf.write("uv\7q\2\2v\24\3\2\2\2wx\7g\2\2xy\7p\2\2yz\7s\2\2z{\7w")
        buf.write("\2\2{|\7c\2\2|}\7p\2\2}~\7v\2\2~\177\7q\2\2\177\26\3\2")
        buf.write("\2\2\u0080\u0081\7*\2\2\u0081\30\3\2\2\2\u0082\u0083\7")
        buf.write("+\2\2\u0083\32\3\2\2\2\u0084\u0085\7=\2\2\u0085\34\3\2")
        buf.write("\2\2\u0086\u008b\t\2\2\2\u0087\u0088\7,\2\2\u0088\u008b")
        buf.write("\7,\2\2\u0089\u008b\7\'\2\2\u008a\u0086\3\2\2\2\u008a")
        buf.write("\u0087\3\2\2\2\u008a\u0089\3\2\2\2\u008b\36\3\2\2\2\u008c")
        buf.write("\u008d\7?\2\2\u008d \3\2\2\2\u008e\u008f\7.\2\2\u008f")
        buf.write("\"\3\2\2\2\u0090\u0091\7}\2\2\u0091$\3\2\2\2\u0092\u0093")
        buf.write("\7\177\2\2\u0093&\3\2\2\2\u0094\u009e\t\3\2\2\u0095\u0096")
        buf.write("\7@\2\2\u0096\u009e\7?\2\2\u0097\u0098\7>\2\2\u0098\u009e")
        buf.write("\7?\2\2\u0099\u009a\7?\2\2\u009a\u009e\7?\2\2\u009b\u009c")
        buf.write("\7#\2\2\u009c\u009e\7?\2\2\u009d\u0094\3\2\2\2\u009d\u0095")
        buf.write("\3\2\2\2\u009d\u0097\3\2\2\2\u009d\u0099\3\2\2\2\u009d")
        buf.write("\u009b\3\2\2\2\u009e(\3\2\2\2\u009f\u00a0\7(\2\2\u00a0")
        buf.write("\u00a4\7(\2\2\u00a1\u00a2\7~\2\2\u00a2\u00a4\7~\2\2\u00a3")
        buf.write("\u009f\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4*\3\2\2\2\u00a5")
        buf.write("\u00a6\7x\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8\7t\2\2\u00a8")
        buf.write("\u00a9\7f\2\2\u00a9\u00aa\7c\2\2\u00aa\u00ab\7f\2\2\u00ab")
        buf.write("\u00ac\7g\2\2\u00ac\u00ad\7k\2\2\u00ad\u00ae\7t\2\2\u00ae")
        buf.write("\u00b5\7q\2\2\u00af\u00b0\7h\2\2\u00b0\u00b1\7c\2\2\u00b1")
        buf.write("\u00b2\7n\2\2\u00b2\u00b3\7u\2\2\u00b3\u00b5\7q\2\2\u00b4")
        buf.write("\u00a5\3\2\2\2\u00b4\u00af\3\2\2\2\u00b5,\3\2\2\2\u00b6")
        buf.write("\u00ba\t\4\2\2\u00b7\u00b9\t\5\2\2\u00b8\u00b7\3\2\2\2")
        buf.write("\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3")
        buf.write("\2\2\2\u00bb.\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bd\u00bf")
        buf.write("\t\6\2\2\u00be\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0")
        buf.write("\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00c8\3\2\2\2")
        buf.write("\u00c2\u00c4\7\60\2\2\u00c3\u00c5\t\6\2\2\u00c4\u00c3")
        buf.write("\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6")
        buf.write("\u00c7\3\2\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00c2\3\2\2\2")
        buf.write("\u00c8\u00c9\3\2\2\2\u00c9\60\3\2\2\2\u00ca\u00ce\7$\2")
        buf.write("\2\u00cb\u00cd\n\7\2\2\u00cc\u00cb\3\2\2\2\u00cd\u00d0")
        buf.write("\3\2\2\2\u00ce\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf")
        buf.write("\u00d1\3\2\2\2\u00d0\u00ce\3\2\2\2\u00d1\u00d2\7$\2\2")
        buf.write("\u00d2\62\3\2\2\2\u00d3\u00d4\t\b\2\2\u00d4\u00d5\3\2")
        buf.write("\2\2\u00d5\u00d6\b\32\2\2\u00d6\64\3\2\2\2\u00d7\u00d8")
        buf.write("\7\61\2\2\u00d8\u00d9\7,\2\2\u00d9\u00dd\3\2\2\2\u00da")
        buf.write("\u00dc\13\2\2\2\u00db\u00da\3\2\2\2\u00dc\u00df\3\2\2")
        buf.write("\2\u00dd\u00de\3\2\2\2\u00dd\u00db\3\2\2\2\u00de\u00e0")
        buf.write("\3\2\2\2\u00df\u00dd\3\2\2\2\u00e0\u00e1\7,\2\2\u00e1")
        buf.write("\u00e2\7\61\2\2\u00e2\u00e3\3\2\2\2\u00e3\u00e4\b\33\2")
        buf.write("\2\u00e4\66\3\2\2\2\u00e5\u00e6\7\61\2\2\u00e6\u00e7\7")
        buf.write("\61\2\2\u00e7\u00eb\3\2\2\2\u00e8\u00ea\n\t\2\2\u00e9")
        buf.write("\u00e8\3\2\2\2\u00ea\u00ed\3\2\2\2\u00eb\u00e9\3\2\2\2")
        buf.write("\u00eb\u00ec\3\2\2\2\u00ec\u00ee\3\2\2\2\u00ed\u00eb\3")
        buf.write("\2\2\2\u00ee\u00ef\b\34\2\2\u00ef8\3\2\2\2\17\2\u008a")
        buf.write("\u009d\u00a3\u00b4\u00b8\u00ba\u00c0\u00c6\u00c8\u00ce")
        buf.write("\u00dd\u00eb\3\b\2\2")
        return buf.getvalue()


class IsiLangLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    AP = 11
    FP = 12
    SC = 13
    OP = 14
    ATTR = 15
    VIR = 16
    ACH = 17
    FCH = 18
    OPREL = 19
    OPLOG = 20
    BOOL = 21
    ID = 22
    NUMBER = 23
    TEXT = 24
    WS = 25
    MLCOMMENT = 26
    SLCOMMENT = 27

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'programa'", "'fimprog;'", "'numero'", "'texto'", "'booleano'", 
            "'leia'", "'escreva'", "'se'", "'senao'", "'enquanto'", "'('", 
            "')'", "';'", "'='", "','", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "AP", "FP", "SC", "OP", "ATTR", "VIR", "ACH", "FCH", "OPREL", 
            "OPLOG", "BOOL", "ID", "NUMBER", "TEXT", "WS", "MLCOMMENT", 
            "SLCOMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "AP", "FP", "SC", "OP", "ATTR", 
                  "VIR", "ACH", "FCH", "OPREL", "OPLOG", "BOOL", "ID", "NUMBER", 
                  "TEXT", "WS", "MLCOMMENT", "SLCOMMENT" ]

    grammarFileName = "IsiLang.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



    def setTipo(self, tipo):
      self._tipo = tipo
    def getTipo(self):
      return self._tipo


    def checkVar(self, varName):
      if not self._isiProgram._varTable.exists(varName):
        raise IsiSemanticException("Erro Semantico! A variavel {} NAO existe! ".format(varName))
      self._isiProgram._varTable.setUsed(varName)

    def checkVarType(self, var):
      if var.getTypeStr() != self._exprType and self._exprType != "any":
        raise IsiSemanticException("Erro Semantico! Esperava valor do tipo {}, mas recebeu {}, que possui tipo {}! ".format( self._exprType, var.getName(), var.getTypeStr()))

    def generatePyCode(self, outputname="stdOutput.py"):
        return self._isiProgram.generatePyTarget(outputname)

    def generateCCode(self, outputname="stdOutput.c"):
        return self._isiProgram.generateCTarget(outputname)
         


