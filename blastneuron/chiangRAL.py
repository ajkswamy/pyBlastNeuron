# Ajayrama Kumaraswamy, 2017, LMU Munich

"""
Description:        This script is used to generate a parameter file required to run RegMaxS.py. This parameter file
                    should contain a json string of a list of dictionaries. Each dictionary is one BlastNeuron job that
                    contains BlastNeuron parameters. See core/RegMaxSPars.py for the description of the parameters.

Usage:              python <path to file>constructRegMaxSParFile.py

Action:             creates a parameter file for RegMaxS.py

Usage guidelines:   There are a couple of cases with examples shown below.
                    Read the comments therein.
                    Essentially edit the values of some variables in this script and run it.


"""
from numpy import pi, deg2rad
import os
import json
from blastneuron.blastNeuronPars import blastNeuronParNames

# obtaining the directory path containing the folder containing this file
# temp = os.path.split(os.path.abspath(__file__))[0]
# temp1 = os.path.split(temp)[0]

temp1 = "/home/aj/DataAndResults/morphology/"





# **********************************************************************************************************************

# # Case 2: Default or user defined parameters above, one reference SWC and several test SWCs, all in the same folder.
# # dirPath: directory containing the reference SWC and the test SWCs
# # refSWC: the reference SWC
# # testSWCFiles: file names of test SWC files in dirPath
# # parameter file generated by this script
# # parFile: the parameter file will be generated at this file path.
# # resPath: the testSWCs registered to the reference SWC will be generated in this directory when RegMaxS.py is run
# # with the parameter file generated by this running this script.
#
# # Usage: Replace dirPath, refSWC, expNames, resPath and parFile as required and run this file to generate parFile
# # Then run python <...>/RegMaxS.py parFile
# # -------------------------------------------

dirPath = os.path.join(temp1, 'OriginalData', 'chiangRAL')

# refSWC = os.path.join(temp1, 'OriginalData', 'chiangRAL', 'Trh-F-700063_Standardized.swc')
# resPath = os.path.join(temp1, 'BlastNeuron', "chiangRAL")
# parFile = os.path.join(temp1, 'ParFiles', 'BlastNeuron', 'chiangRAL.json')

# refSWC = os.path.join(temp1, 'OriginalData', 'chiangRAL', 'Trh-F-700063.CNG.swc')
# resPath = os.path.join(temp1, 'BlastNeuron', "chiangRAL_Trh-F-700063.CNG")
# parFile = os.path.join(temp1, 'ParFiles', 'BlastNeuron', 'chiangRAL_Trh-F-700063.CNG.json')

# refSWC = os.path.join(temp1, 'OriginalData', 'chiangRAL', 'Trh-F-700018.CNG.swc')
# resPath = os.path.join(temp1, 'BlastNeuron', "chiangRAL_Trh-F-700018.CNG")
# parFile = os.path.join(temp1, 'ParFiles', 'BlastNeuron', 'chiangRAL_Trh-F-700018.CNG.json')
#
# refSWC = os.path.join(temp1, 'OriginalData', 'chiangRAL', 'Trh-M-500051.CNG.swc')
# resPath = os.path.join(temp1, 'BlastNeuron', "chiangRAL_Trh-M-500051.CNG")
# parFile = os.path.join(temp1, 'ParFiles', 'BlastNeuron', 'chiangRAL_Trh-M-500051.CNG.json')

refSWC = os.path.join(temp1, 'OriginalData', 'chiangRAL', 'Trh-F-700063_Standardized.swc')
resPath = os.path.join(temp1, 'BlastNeuron_likeStandardized', "chiangRAL")
parFile = os.path.join(temp1, 'ParFiles', 'BlastNeuron', 'chiangRAL_likeStandardized.json')

testSWCFiles = [
    "Trh-F-700063_Standardized",
    "Trh-F-700063.CNG",
    "Trh-F-500050.CNG",
    "Trh-F-500106.CNG",
    "Trh-M-500051.CNG",
    "Trh-F-600071.CNG",
    "Trh-F-500093.CNG",
    "Trh-F-500148.CNG",
    "Trh-F-500154.CNG",
    "Trh-F-700018.CNG",
]

# -------------------------------------------

if not os.path.isdir(resPath):
    os.mkdir(resPath)
pars = []
for sfr in testSWCFiles:
    testSWC = os.path.join(dirPath, "{}.swc".format(sfr))
    resFile = os.path.join(resPath, "{}.swc".format(sfr))
    # obtains the list of variables in the current work space
    ns = vars()
    # forms the dictionary of parameters to be saved into the parameter file.
    pars.append({k: ns[k] for k in blastNeuronParNames})
# -------------------------------------------
# **********************************************************************************************************************

# write the parameters into the parameter file.
with open(parFile, 'w') as fle:
    json.dump(pars, fle)
