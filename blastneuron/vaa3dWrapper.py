import subprocess32
import logging
from .executables import vaa3d
import pathlib2


def runPreProcessing(inFile, outFile, timeout=30 * 60):

    assert pathlib2.Path(inFile).is_file(), "Input File {} not found".format(inFile)

    pluginLabel = "blastneuron;pre_processing"

    toRun = [
        vaa3d,
        "-x", "blastneuron",
        "-f", "pre_processing",
        "-p", "#i {} #o {} #s 1 #r 0".format(inFile, outFile)
    ]
    try:

        compProc = subprocess32.call(toRun,
                                     timeout=timeout
                                     )
    except subprocess32.TimeoutExpired as te:
        print(te.message)
        logging.error("{} Process did not finish within {} seconds!!!".format(pluginLabel, timeout))

    except OSError as ose:
        print(ose.message)
        logging.error("{} OSError while running vaa3d plugin, for example,"
                      "a file is non existant".format(pluginLabel))
    except ValueError as ve:
        print(ve.message)
        logging.error("{} Invalid arguments passed to the subprocess".format(pluginLabel))

    except Exception as spe:
        print(spe.message)

def runSWCSort(inFile, outFile, timeout=30 * 60):

    assert pathlib2.Path(inFile).is_file(), "Input File {} not found".format(inFile)

    pluginLabel = "sort_swc"

    toRun = [
        vaa3d,
        "-x", "sort_neuron_swc",
        "-f", "sort_swc",
        "-i", inFile,
        "-o", outFile
    ]
    try:

        compProc = subprocess32.call(toRun,
                                     timeout=timeout
                                     )
    except subprocess32.TimeoutExpired as te:
        print(te.message)
        logging.error("{} Process did not finish within {} seconds!!!".format(pluginLabel, timeout))

    except OSError as ose:
        print(ose.message)
        logging.error("{} OSError while running vaa3d plugin, for example,"
                      "a file is non existant".format(pluginLabel))
    except ValueError as ve:
        print(ve.message)
        logging.error("{} Invalid arguments passed to the subprocess".format(pluginLabel))

    except Exception as spe:
        print(spe.message)

def runInvProjSWC(refSWC, testSWC, outFile, timeout=30 * 60):

    assert pathlib2.Path(refSWC).is_file(), "Input File {} not found".format(refSWC)
    assert pathlib2.Path(testSWC).is_file(), "Input File {} not found".format(testSWC)

    pluginLabel = "blastneuron;inverse_projection"

    toRun = [
        vaa3d, "-x", "blastneuron", "-f", "inverse_projection",
        "-p", "#t {} #s {} #o {}".format(refSWC, testSWC, outFile)
    ]
    try:
        compProc = subprocess32.call(toRun,
                                  timeout=timeout
                                  )
    except subprocess32.TimeoutExpired as te:
        print(te.message)
        logging.error("{} Process did not finish within {} seconds!!!".format(pluginLabel, timeout))

    except OSError as ose:
        print(ose.message)
        logging.error("{} OSError while running vaa3d plugin, for example,"
                      "a file is non existant".format(pluginLabel))
    except ValueError as ve:
        print(ve.message)
        logging.error("{} Invalid arguments passed to the subprocess".format(pluginLabel))

    except Exception as spe:
        print(spe.message)

