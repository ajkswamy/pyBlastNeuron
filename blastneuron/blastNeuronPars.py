# Ajayrama Kumaraswamy, 2017, LMU Munich

"""
The input parameters of different Algorithms
"""

# **********************************************************************************************************************
"""
Parameters of Blast Neuron Local Alignment.
refSWC:                 string. The reference SWC file, to which testFile is registered.
                        Must be a valid SWC file on the file system.

testSWC:                string. The test SWC file which is registered to refSWC.
                        Must be a valid SWC file on the file system.

resFile:                string. This file will be created and the resulting SWC will be written into it.
                        It needs to be valid file reference.

"""
blastNeuronParNames = ['refSWC', 'testSWC', 'resFile']


