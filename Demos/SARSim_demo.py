#-------------------------------------------------------------------------------
# Name:        SAR image simulator demo
# Purpose:
#
# Author:      vfomin
#
# Created:     08/06/2015
# Copyright:   (c) vfomin 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Numpy, Matplotplib
import numpy as np
import matplotlib.pyplot as plt

# Project
##import GlobalVariablesAerial as Sensor
import Sensors.GlobalVariablesCSK_HI as Sensor
import SARSim.SARSim_proto2 as SARSim

if __name__ == '__main__':

    xc = 0.0
    yc = Sensor.H * np.tan(55.0 * np.pi / 180.0)
    s = SARSim.SARSim(Sensor,verbose=False)
    # define SAR acquisition parameters:
    params = [[-3000, 3000], [54.995, 55.005], [xc, yc]]
    s.setParams(params)
    # set targets

    # a) stationary targets :
##    targets = [[xc, yc]]
##    targets = [[xc, yc], [xc-55, yc], [xc-212, yc]]
##    targets = [
##                [xc, yc],
##                [xc - 113.0, yc], [xc + 113.0, yc],
##                [xc - 113.0, yc + 213.0], [xc - 113.0, yc - 213.0],
##                [xc + 113.0, yc + 213.0], [xc + 113.0, yc - 213.0],
##                [xc, yc + 213.0], [xc, yc - 213.0]
##            ]

    # b) moving targets
##    targets = [[xc, yc, 0.0, 0.0]]
    targets = [[xc-500.0, yc-520.0], [xc, yc, 0.0, 0.0]]
##    targets = [[xc, yc, 0.0, 2.0]]
##    targets = [[xc, yc-50.0], [xc, yc+50, 10.0, 0.0]]
##    targets = [[xc, yc, 10.0, 0.0], [xc + 100.0, yc, -10.0, 0.0], [xc - 100.0, yc, 10.0, 10.0]]


##    targets = [[xc, yc - 50.0, 10.0, 0.0], [xc, yc - 25.0, 15.0, 0.0], [xc, yc, 30.0, 0.0], [xc, yc + 25.0 , 50.0, 0.0]]
##    targets = [[xc+2500, yc - 50.0, 0.0, 10.0], [xc+2500, yc - 25.0, 0.0, 15.0], [xc+2500, yc, 0.0, 30.0], [xc+2500, yc + 25.0 , 0.0, 50.0]]

    s.setTargets(targets)

    Srx, xArray, tArray = s.computeRawData()
##    SARSim.showResponse(Srx, [tArray[0],tArray[-1],xArray[0],xArray[-1]], 'Raw data', False)

    # data compression
    S_final, xArray, tArray = s.compressRawData2()
##    SARSim.showResponse(S_final, [tArray[0],tArray[-1],xArray[0],xArray[-1]], 'Compressed image', False)
    SARSim.showResponse(S_final, None, 'Compressed image', False)

    # linear interpolation from Range time to OY coordinates
##    S_final, yArray = SARSim.warpFromRangeTimeToRegularOYGrid(S_final, tArray, Sensor.H)
##    SARSim.showResponse(S_final, [yArray[0]-yc, yArray[-1]-yc,xArray[-1],xArray[0]], 'Compressed image - Ground range')

##    plt.imshow(np.abs(S_final))
##    plt.show()


    # Save
##    np.save("C:\\VFomin_folder\\PISE_project\\SAR-GMTI\\Data\\SARSim_CSK_HI_v1_0_0__v2_10_0", [S_final, xArray, yArray])

