import logging

# from http://stackoverflow.com/questions/21953835/run-subprocess-and-print-output-to-logging/21978778#21978778
def log_subprocess_output(pipe, subproc_name= '??'):

    if pipe:
        for line in pipe.split(b"\n"):
            logging.info('[subprocess {}] {}'.format(subproc_name, line.decode("utf-8")))


def correctNumberDemarcation(swcFile):

    with open(swcFile, 'r') as fle:

        text = fle.readlines()

    textCorrected = []

    for lne in text:
        if not lne.startswith("#"):
            lneCorrected = lne.replace(",", ".")
        else:
            lneCorrected = lne
        textCorrected.append(lneCorrected)

    with open(swcFile, 'w') as fle:
        fle.writelines(textCorrected)


