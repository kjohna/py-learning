"""implement a model for modeling and connecting logical circuit elements
http://interactivepython.org/runestone/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html
"""
class LogicGate:

    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return input("Enter Pin A input for gate " + self.getLabel() + "-->")
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return input("Enter Pin B input for gate " + self.getLabel() + "-->")
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")

class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0
"""my solution:
class NAndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        return int(not AndGate(self.getLabel()).getOutput())
"""
#instructor solution uses format below but with "super()" method to call
#performGateLogic() in the if statement. Python 2 requires using multiple
#inheritance https://stackoverflow.com/questions/1713038/super-fails-with-error-typeerror-argument-1-must-be-type-not-classobj-when
#Python 3 does not require the extra code
class NAndGate(AndGate, object):

    def performGateLogic(self):
        #if AndGate(self.getLabel()).performGateLogic() == 1:
        if super(NAndGate, self).performGateLogic() == 1:
            return 0
        else:
            return 1

class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0
"""my solution:
class NOrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        return int(not OrGate(self.getLabel()).getOutput())
"""
#instructor solution uses format below but with "super()" method to call
#performGateLogic() in the if statement. Python 2 requires using multiple
#inheritance https://stackoverflow.com/questions/1713038/super-fails-with-error-typeerror-argument-1-must-be-type-not-classobj-when
#Python 3 does not require the extra code
class NOrGate(OrGate, object):

    def performGateLogic(self):
        #if OrGate(self.getLabel()).performGateLogic() == 1:
        if super(NOrGate, self).performGateLogic() == 1:
            return 0
        else:
            return 1

class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return input("Enter Pin input for gate " + self.getLabel() + "-->")
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):

        pin = self.getPin()
        if pin == 1:
            return 0
        else:
            return 1

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate



def main():
    """
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")

    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    c3 = Connector(g3,g4)

    print g4.getOutput()
    """

    #test NAnd, NOr gates:
    g1 = OrGate("G1")
    g2 = NOrGate("G2")
    print g1.getLabel()
    print g1.getOutput()
    print g2.getLabel()
    print g2.getOutput()
    g3 = AndGate("G3")
    g4 = NAndGate("G4")
    print g3.getLabel()
    print g3.getOutput()
    print g4.getLabel()
    print g4.getOutput()

    """
    #self check
    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3, g4)
    print g4.getOutput()

    g5 = AndGate("G5")
    g6 = NotGate("G6")
    g7 = AndGate("G7")
    g8 = NotGate("G8")
    g9 = AndGate("G9")
    c4 = Connector(g5, g6)
    c5 = Connector(g6, g9)
    c6 = Connector(g7, g8)
    c7 = Connector(g8, g9)
    print g9.getOutput()
    """

main()
