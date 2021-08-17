class TBinaryDigits:
  miIndex = 0

  def __init__(self):
    miIndex = 0

  def GetIndex(self):
    return self.miIndex

  def SetIndex(self, iIndex):
    self.miIndex = iIndex

  def GetBitValue(self, iPosition):
    temp = 0

    if (self.miIndex) & (2 ** iPosition) > 0:
      temp = 1

    return temp
