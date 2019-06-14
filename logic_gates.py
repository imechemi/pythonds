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
            return int(input("Enter pin A input for gate " + self.getLabel() + " ---> "))
        elif type(self.pinA) == int:
            return self.pinA 
        else:
            return self.pinA.getFrom().getOutput()
    
    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter pin B input for gate " + self.getLabel() + " ---> "))
        elif type(self.pinB) == int:
            return self.pinB 
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, gate):
        if self.pinA == None:
            self.pinA = gate
        elif self.pinB == None: 
            self.pinB = gate
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


class AndGate(BinaryGate):

    def __init__(self, n):
        super(AndGate, self).__init__(n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0


class NandGate(AndGate):

    def __init__(self, n):
        super(NandGate, self).__init__(n)

    def performGateLogic(self):
        res = super(NandGate, self).performGateLogic()
        if res == 0:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, n):
        super(OrGate, self).__init__(n)
    
    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NorGate(OrGate):

    def __init__(self, n):
        super(NorGate, self).__init__(n)
    
    def performGateLogic(self):
        res = super(NorGate, self).performGateLogic()
        if res == 0:
            return 1
        else:
            return 0


class XorGate(BinaryGate):

    def __init__(self, n):
        super(XorGate, self).__init__(n)

    def performGateLogic(self):
        if (self.pinA == self.pinB):
            return 0
        else:
            return 1



class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None 
    
    def getPin(self):
        if self.pin == None:
            return int(input("Enter pin input for gate " + self.getLabel() + " ---> "))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, gate):
        if self.pin == None:
            self.pin = gate
        else:
            raise RuntimeError("Error: NO EMPTY PINS")


class NotGate(UnaryGate):

    def __init__(self, n):
        super(NotGate, self).__init__(n)
    
    def performGateLogic(self):
        pin = self.getPin()
        
        if pin == 0:
            return 1
        else: 
            return 0

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        self.togate.setNextPin(self)

    def getFrom(self):
        return self.fromgate
    
    def getTo(self):
        return self.togate


class HalfAdder(BinaryGate):

    def __init__(self, n):
        super(HalfAdder, self).__init__(n)
        self.sum = None
        self.carry = None

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        self.sum = self.getSum(a, b)
        self.carry = self.getCarry(a, b)
        return (self.carry * 10 + self.sum)

    def getSum(self, a, b):
        xor_gate = XorGate('G1')
        xor_gate.setNextPin(a)
        xor_gate.setNextPin(b)
        return xor_gate.getOutput()

    def getCarry(self, a, b):
        and_gate = AndGate('G2')
        and_gate.setNextPin(a)
        and_gate.setNextPin(b)
        return and_gate.getOutput()

# g1 = AndGate('G1')
# g2 = AndGate('G2')
# g3 = OrGate('G3')
# g4 = NotGate('G4')

# c1 = Connector(g1, g3)
# c2 = Connector(g2, g3)
# c3 = Connector(g3, g4)
# print(g4.getOutput())

# a = NandGate('A')
# b = NandGate('B')
# c = NandGate('C')
# c4 = Connector(a, c)
# c5 = Connector(b, c)
# print(c.getOutput())


hadder = HalfAdder('H1')
print(hadder.getOutput())