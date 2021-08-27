import FounderProbabilities as FP
import TransmissionProb as TP
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

fpandtp = np.array([FP.FPP1(FP.x), FP.FPP2(FP.x), FP.FPP3(FP.x), TP.TP4(FP.x), TP.TP5(FP.x), TP.TP6(FP.x), TP.TP7(FP.x), TP.TP8(FP.x), TP.TP9(FP.x)]).transpose()
print(fpandtp)
