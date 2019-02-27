#!/usr/bin/env bash
pkill Xvfb
Xvfb :30 -auth /dev/null &
ps -a|grep Xvfb
export DISPLAY=:30
python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangLLC.json
python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangLLC_Gad1-F-000062.CNG.json 
python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangLLC_Cha-F-300331.CNG.json 
python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangLLC_Cha-F-000018.CNG.json 

python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangOMB.json 
python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangOMB_VGlut-F-500031.CNG.json 
python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangOMB_VGlut-F-500085.CNG.json 
python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangOMB_VGlut-F-600379.CNG.json 

# python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangOPSInt.json 
# python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangOPSInt_Trh-F-000047.CNG.json 
# python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangOPSInt_Trh-M-100018.CNG.json 
# python /home/aj/repos/pyBlastNeuron/blastneuron/blastNeuron.py /home/aj/DataAndResults/morphology/ParFiles/BlastNeuron/chiangOPSInt_Trh-M-900003.CNG.json 

