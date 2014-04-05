__author__ = 'obscure'
import os
import json


myroot = 'data'
listofyears = []
for root, subFolders, files in os.walk(myroot):
    for filename in files:
        count = 0
        keycount = 0
        myjson = {}
        myjson['Scholarships'] = {}
        myjson['Scholarships']['Federal'] = {}
        myjson['Scholarships']['state'] = {}
        myjson['Scholarships']['Institutional'] = {}
        myjson['Scholarships']['Other Grants'] = {}
        myjson['Scholarships']['Total'] = {}
        myjson['Self-Help'] = {}
        myjson['Self-Help']['Student Loans'] = {}
        myjson['Self-Help']['Federal Work Study'] = {}
        myjson['Self-Help']['State and Other'] = {}
        myjson['Self-Help']['Total'] = {}
        myjson['Other'] = {}
        myjson['Other']['Parent Loans'] = {}
        myjson['Other']['Tuition Waivers'] = {}
        myjson['Other']['Athetic Awards'] = {}
        print filename
        for line in open(os.path.join(root, filename), 'r'):
            line = line.replace(',', '')
            line = line.replace('$', '')
            count += 1
            if count < 13:
                print line
            values = line.split()
            if count < 6:
                keys = myjson['Scholarships'].keys()
                myjson['Scholarships'][keys[keycount]]['Need'] = values[0]
                if len(values) == 1 :
                    myjson['Scholarships'][keys[keycount]]['Non-Need'] = 0
                else:
                    myjson['Scholarships'][keys[keycount]]['Non-Need'] = values[1]
                keycount += 1
                if count == 5:
                    keycount = 0
            elif count < 10:
                keys = myjson['Self-Help'].keys()
                myjson['Self-Help'][keys[keycount]]['Need'] = values[0]
                if len(values) == 1:
                    myjson['Self-Help'][keys[keycount]]['Non-Need'] = 0
                else:
                    myjson['Self-Help'][keys[keycount]]['Non-Need'] = values[1]
                keycount += 1
                if count == 9:
                    keycount = 0
            elif count < 13:
                keys = myjson['Other'].keys()
                myjson['Other'][keys[keycount]]['Need'] = values[0]
                if len(values) == 1 :
                    myjson['Other'][keys[keycount]]['Non-Need'] = 0
                else:
                    myjson['Other'][keys[keycount]]['Non-Need'] = values[1]
                keycount += 1
        listofyears.append(myjson)

fp = open('final', 'w')
json.dump(listofyears, fp)











