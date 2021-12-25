import sys
import matplotlib.pyplot as plt
import numpy as np
import CIE_XYZ_Curve

# sRGB Primaries which make a gamut in chromaticity diagram
sRGB_Primary_R = [0.64, 0.33]
sRGB_Primary_G = [0.30, 0.60]
sRGB_Primary_B = [0.15, 0.06]

# Chromaticity coordinate of white by using illuminant D65
xw = 0.3127
yw = 0.3290
Yw = 1

# white point of xyY color space
WhitePoint_xyY = [xw, Yw, Yw]

def GetLuminance_From_sRGB_Primaries_with_white_of_xyY():
    a = np.array([
          [sRGB_Primary_R[0]/sRGB_Primary_R[1], sRGB_Primary_G[0]/sRGB_Primary_G[1], sRGB_Primary_B[0]/sRGB_Primary_B[1]],
          [1, 1, 1],
          [(1.0-sRGB_Primary_R[0]-sRGB_Primary_R[1])/sRGB_Primary_R[1], (1.0-sRGB_Primary_G[0]-sRGB_Primary_G[1])/sRGB_Primary_G[1], (1.0 - sRGB_Primary_B[0] - sRGB_Primary_B[1])/sRGB_Primary_B[1]]])
    inva = np.linalg.inv(a);
    whtePoint_xyY = [xw / yw, 1, (1.0 - xw - yw) / yw]
    Y = np.matmul(inva, whtePoint_xyY)
    return Y

def GetMatrix_sRGB_to_xyY():
    Y = GetLuminance_From_sRGB_Primaries_with_white_of_xyY()
    sRGB_to_xyY = np.array([
                    [sRGB_Primary_R[0]/sRGB_Primary_R[1]*Y[0], sRGB_Primary_G[0]/sRGB_Primary_G[1]*Y[1], sRGB_Primary_B[0]/sRGB_Primary_B[1]*Y[2]],
                    [Y[0], Y[1], Y[2]],
                    [(1.0-sRGB_Primary_R[0]-sRGB_Primary_R[1])/sRGB_Primary_R[1]*Y[0], (1.0-sRGB_Primary_G[0]-sRGB_Primary_G[1])/sRGB_Primary_G[1]*Y[1], (1.0-sRGB_Primary_B[0]-sRGB_Primary_B[1])/sRGB_Primary_B[1]*Y[2]],
                ])
    return sRGB_to_xyY

def GetMatrix_xyY_to_sRGB():
    sRGB_to_xyY = GetMatrix_sRGB_to_xyY()
    xyY_to_sRGB = np.linalg.inv(sRGB_to_xyY)
    return xyY_to_sRGB

print('[Yr, Yg, Yb] : {0}'.format(GetLuminance_From_sRGB_Primaries_with_white_of_xyY()))
print('[sRGB to xyY] : \n{0}'.format(GetMatrix_sRGB_to_xyY()))
print('[xyY to sRGB] : \n{0}'.format(GetMatrix_xyY_to_sRGB()))

whitepoint_sRGB = np.matmul(GetMatrix_xyY_to_sRGB(), WhitePoint_xyY);
print('[White point of sRGB] : {0}'.format(whitepoint_sRGB))

