import os
import sys

for inputFile in os.listdir('./'):
    if inputFile.startswith('ecal') and inputFile.endswith('.db'):

        baseName = inputFile.split('.')[0]
        textFile = baseName + '.txt'
        textHandle = open(textFile, 'w')
        textHandle.write('{\n')
        textHandle.write('    "destinationDatabase": "oracle://cms_orcon_prod/CMS_CONDITIONS",\n')
        textHandle.write('    "destinationTags": {\n')
        textHandle.write('        "%s": {}\n' % baseName)
        textHandle.write('    },\n')
        textHandle.write('    "inputTag": "%s",\n' % baseName)
        textHandle.write('    "since": null,\n')
        location = 'EB'
        readout = 'ptbin1 Full'
        correction = 'mean'
        if 'EE' in baseName:
            location = 'EE'
        if 'ZS' in baseName:
            readout = 'ZS'
        elif 'ptbin2' in baseName:
            readout = 'ptbin2 Full'
        elif 'ptbin3' in baseName:
            readout = 'ptbin3 Full'
        if 'sigma' in baseName:
            correction = 'sigma'
        textHandle.write('    "userText": "ECAL PF cluster regression %s %s %s 91X 2017 %s"\n' % (location, readout, correction, sys.argv[1]))
        textHandle.write('}\n')
        textHandle.close()
