import sys
import matplotlib.pyplot as plt
import numpy as np
import CIE_XYZ_Curve

# 471 points per curves
# 360 nm to 830 nm

# declare functions
def SetWaveLengthGraph():
    major_xticks = list(range(400,800+100,100))
    minor_xticks = list(range(360-10,830+10,20))
    fig, ax = plt.subplots(figsize=(14,7))
    ax.set_xticks(major_xticks)
    ax.set_xticks(minor_xticks, minor=True)
    ax.set_xlim([360-10, 830+10]);
    #ax.tick_params(axis='x', labelsize=20, length=10, width=3, rotation=30)
    #ax.tick_params(axis='x', which='minor', length=5, width=2 )

def DrawCIE_RGB_Curve():
    SetWaveLengthGraph()
    CIE_RGB_X = np.zeros(CIE_XYZ_Curve.NumOfWavelengths)
    CIE_RGB_Z = np.zeros(CIE_XYZ_Curve.NumOfWavelengths)
    CIE_RGB_Y = np.zeros(CIE_XYZ_Curve.NumOfWavelengths)
    # convert from CIE XYZ color matching function to CIE RGB color matching function
    for i in range(0, CIE_XYZ_Curve.NumOfWavelengths):
        CIE_RGB = np.matmul(CIE_XYZ_Curve.matXYZ_TO_CIE_RGB
            , [CIE_XYZ_Curve.CIE_X[i], CIE_XYZ_Curve.CIE_Y[i], CIE_XYZ_Curve.CIE_Z[i]])
        CIE_RGB_X[i] = CIE_RGB[0]
        CIE_RGB_Y[i] = CIE_RGB[1]
        CIE_RGB_Z[i] = CIE_RGB[2]
    plt.title('CIE RGB color matching function(CIE RGB Curve)');
    plt.plot(CIE_XYZ_Curve.RangeWavelength, CIE_RGB_X, 'r', label='R')
    plt.plot(CIE_XYZ_Curve.RangeWavelength, CIE_RGB_Y, 'g', label='G')
    plt.plot(CIE_XYZ_Curve.RangeWavelength, CIE_RGB_Z, 'b', label='B')
    plt.legend()
    plt.show()

def DrawCIE_XYZ_Curve():
    SetWaveLengthGraph()
    plt.title('CIE XYZ color matching function(CIE XYZ Curve)')
    plt.plot(CIE_XYZ_Curve.RangeWavelength, CIE_XYZ_Curve.CIE_X, 'r', label='X')
    plt.plot(CIE_XYZ_Curve.RangeWavelength, CIE_XYZ_Curve.CIE_Y, 'g', label='Y')
    plt.plot(CIE_XYZ_Curve.RangeWavelength, CIE_XYZ_Curve.CIE_Z, 'b', label='Z')
    plt.legend()
    plt.show()

# main

print('Number of arguments: {}'.format(len(sys.argv)))
print('Argument(s) passed: {}'.format(str(sys.argv)))

selectedCurve = 0;
if (len(sys.argv) > 1):
    selectedCurve = int(sys.argv[1])

if (selectedCurve == 1):
    DrawCIE_XYZ_Curve()
else:
    DrawCIE_RGB_Curve()
