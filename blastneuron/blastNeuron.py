import sys
from blastneuron.vaa3dWrapper import runPreProcessing, runInvProjSWC, runSWCSort
from blastneuron.misc import parFileCheck
from blastneuron.auxFuncs import correctNumberDemarcation
import os
import logging
import filecmp
import shutil

def runRegMaxS(parFile, parNames):
    parsList = parFileCheck(parFile, parNames)

    for pars in parsList:
        print('Current Parameters:')
        for parN, parV in pars.iteritems():
            print('{}: {}'.format(parN, parV))

        resFile = pars['resFile']
        refSWC = pars['refSWC']
        testSWC = pars['testSWC']

        refStem = os.path.split(refSWC)[1][:-4]
        testStem = os.path.split(testSWC)[1][:-4]

        if os.path.isfile(resFile):

            ch = raw_input('File exists: ' + resFile + '\nDelete(y/n)?')
            if ch == 'y':
                os.remove(resFile)
            else:
                quit()

        resDir = os.path.split(resFile)[0]
        if not os.path.exists(resDir):
            raise(ValueError('Could not create result file in specified directory: {}'.format(resDir)))

        assert os.path.isfile(refSWC), 'Could  not find {}'.format(refSWC)
        assert os.path.isfile(testSWC), 'Could  not find {}'.format(testSWC)

        preProcessedDir = os.path.join(resDir, "PreProcessed")
        if not os.path.isdir(preProcessedDir):
            os.mkdir(preProcessedDir)

        test_pp = os.path.join(preProcessedDir, "{}.swc".format(testStem))
        ref_pp = os.path.join(preProcessedDir, "{}.swc".format(refStem))

        if not os.path.isfile(test_pp):
            runPreProcessing(testSWC, test_pp)
            correctNumberDemarcation(test_pp)

        if not os.path.isfile(ref_pp):
            runPreProcessing(refSWC, ref_pp)
            correctNumberDemarcation(ref_pp)

        sortedDir = os.path.join(resDir, "PreProcessed+Sorted")
        if not os.path.isdir(sortedDir):
            os.mkdir(sortedDir)

        test_pp_sorted = os.path.join(sortedDir, "{}.swc".format(testStem))
        ref_pp_sorted = os.path.join(sortedDir, "{}.swc".format(refStem))

        if not os.path.isfile(test_pp_sorted):
            runSWCSort(test_pp, test_pp_sorted)
            correctNumberDemarcation(test_pp_sorted)

        if not os.path.isfile(ref_pp_sorted):
            runSWCSort(ref_pp, ref_pp_sorted)
            correctNumberDemarcation(ref_pp_sorted)

        if filecmp.cmp(ref_pp_sorted, test_pp_sorted):
            shutil.copy(test_pp_sorted, resFile)
        else:
            try:
                runInvProjSWC(ref_pp_sorted, test_pp_sorted, resFile)
                correctNumberDemarcation(resFile)
            except IOError as ioe:
                # inverse projection fails if it does not finish within 1800s
                pass



if __name__ == '__main__':

    from blastneuron.blastNeuronPars import blastNeuronParNames
    assert len(sys.argv) == 2, 'Improper usage! Please use as \'python {} parFile\''.format(sys.argv[0])

    logging.basicConfig(level=logging.INFO)
    parFile = sys.argv[1]

    runRegMaxS(parFile, blastNeuronParNames)