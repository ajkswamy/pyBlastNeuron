#!/usr/bin/env bash
pkill Xvfb
Xvfb :30 -auth /dev/null &
ps -a|grep Xvfb
export DISPLAY=:30

python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangRAL.json
python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangRAL_Trh-F-700063.CNG.json
python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangRAL_Trh-F-700018.CNG.json
python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangRAL_Trh-M-500051.CNG.json

python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangAA1.json
python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangAA1_VGlut-F-300181.CNG.json
python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangAA1_VGlut-F-600290.CNG.json
python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangAA1_VGlut-F-500147.CNG.json


