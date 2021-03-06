__author__ = 'obscure'

from pylab import *
from matplotlib import font_manager as fm
from matplotlib.transforms import Affine2D
from matplotlib.patches import Circle, Wedge, Polygon
import numpy as np

totaldata = [{"Scholarships": {"Federal": {"Need": "36163587", "Non-Need": "670050"}, "Institutional": {"Need": "30629944", "Non-Need": "1204691"}, "state": {"Need": "46031615", "Non-Need": "9659306"}, "Other Grants": {"Need": "17350566", "Non-Need": "7729152"}, "Total": {"Need": "130175712", "Non-Need": "19263199"}}, "Other": {"Tuition Waivers": {"Need": "4654348", "Non-Need": "24809936"}, "Parent Loans": {"Need": "20718998", "Non-Need": "7488234"}, "Athetic Awards": {"Need": "5579511", "Non-Need": "503848"}}, "Self-Help": {"Student Loans": {"Need": "66302723", "Non-Need": "43322090"}, "Federal Work Study": {"Need": "1661410", "Non-Need": 0}, "Total": {"Need": "402549", "Non-Need": "0"}, "State and Other": {"Need": "68366682", "Non-Need": "43322090"}}}, {"Scholarships": {"Federal": {"Need": "20953626", "Non-Need": "1206407"}, "Institutional": {"Need": "21794104", "Non-Need": "851378"}, "state": {"Need": "21636529", "Non-Need": "15996059"}, "Other Grants": {"Need": "8577966", "Non-Need": "8350911"}, "Total": {"Need": "72962225", "Non-Need": "26404755"}}, "Other": {"Tuition Waivers": {"Need": "4586720", "Non-Need": "28399828"}, "Parent Loans": {"Need": "2170205", "Non-Need": "5645269"}, "Athetic Awards": {"Need": "1128079", "Non-Need": "2657178"}}, "Self-Help": {"Student Loans": {"Need": "47338545", "Non-Need": "33007787"}, "Federal Work Study": {"Need": "1296145", "Non-Need": 0}, "Total": {"Need": "329501", "Non-Need": "0"}, "State and Other": {"Need": "48964191", "Non-Need": "33007787"}}}, {"Scholarships": {"Federal": {"Need": "36502441", "Non-Need": "533993"}, "Institutional": {"Need": "32454096", "Non-Need": "1896943"}, "state": {"Need": "46050585", "Non-Need": "9078326"}, "Other Grants": {"Need": "16970707", "Non-Need": "7067015"}, "Total": {"Need": "131977829", "Non-Need": "18576277"}}, "Other": {"Tuition Waivers": {"Need": "4775863", "Non-Need": "25844944"}, "Parent Loans": {"Need": "22216451", "Non-Need": "8506501"}, "Athetic Awards": {"Need": "3084271", "Non-Need": "428019"}}, "Self-Help": {"Student Loans": {"Need": "66919317", "Non-Need": "46215495"}, "Federal Work Study": {"Need": "1407865", "Non-Need": 0}, "Total": {"Need": "237274", "Non-Need": "0"}, "State and Other": {"Need": "68564455", "Non-Need": "46215495"}}}, {"Scholarships": {"Federal": {"Need": "18504413", "Non-Need": "1132009"}, "Institutional": {"Need": "21732772", "Non-Need": "803707"}, "state": {"Need": "17971960", "Non-Need": "13554902"}, "Other Grants": {"Need": "10203099", "Non-Need": "21702298"}, "Total": {"Need": "68412244", "Non-Need": "37192916"}}, "Other": {"Tuition Waivers": {"Need": "3813171", "Non-Need": "27380155"}, "Parent Loans": {"Need": "2301824", "Non-Need": "5205624"}, "Athetic Awards": {"Need": "1426041", "Non-Need": "2826936"}}, "Self-Help": {"Student Loans": {"Need": "44531976", "Non-Need": "36473820"}, "Federal Work Study": {"Need": "2409192", "Non-Need": 0}, "Total": {"Need": "524142", "Non-Need": "0"}, "State and Other": {"Need": "47465310", "Non-Need": "36473820"}}}, {"Scholarships": {"Federal": {"Need": "23409034", "Non-Need": "3470061"}, "Institutional": {"Need": "26204761", "Non-Need": "1307013"}, "state": {"Need": "23940686", "Non-Need": "16564989"}, "Other Grants": {"Need": "10994168", "Non-Need": "11101585"}, "Total": {"Need": "84548649", "Non-Need": "32443648"}}, "Other": {"Tuition Waivers": {"Need": "4587058", "Non-Need": "26093071"}, "Parent Loans": {"Need": "2152514", "Non-Need": "6810387"}, "Athetic Awards": {"Need": "1531624", "Non-Need": "3632341"}}, "Self-Help": {"Student Loans": {"Need": "48874812", "Non-Need": "41625483"}, "Federal Work Study": {"Need": "1336282", "Non-Need": 0}, "Total": {"Need": "264590", "Non-Need": "0"}, "State and Other": {"Need": "50475684", "Non-Need": "41625483"}}}, {"Scholarships": {"Federal": {"Need": "23239301", "Non-Need": "3306596"}, "Institutional": {"Need": "25185535", "Non-Need": "1061079"}, "state": {"Need": "22940823", "Non-Need": "15803762"}, "Other Grants": {"Need": "10853656", "Non-Need": "10872490"}, "Total": {"Need": "82219315", "Non-Need": "31043927"}}, "Other": {"Tuition Waivers": {"Need": "4543893", "Non-Need": "25579817"}, "Parent Loans": {"Need": "2107325", "Non-Need": "6384192"}, "Athetic Awards": {"Need": "1362477", "Non-Need": "3041681"}}, "Self-Help": {"Student Loans": {"Need": "48437171", "Non-Need": "37524227"}, "Federal Work Study": {"Need": "2032621", "Non-Need": 0}, "Total": {"Need": "577824", "Non-Need": "0"}, "State and Other": {"Need": "51047616", "Non-Need": "37524227"}}}, {"Scholarships": {"Federal": {"Need": "36518764", "Non-Need": "1065067"}, "Institutional": {"Need": "33568926", "Non-Need": "1226992"}, "state": {"Need": "40877831", "Non-Need": "8107121"}, "Other Grants": {"Need": "15933746", "Non-Need": "5978627"}, "Total": {"Need": "126899267", "Non-Need": "16377807"}}, "Other": {"Tuition Waivers": {"Need": "4049131", "Non-Need": "20009040"}, "Parent Loans": {"Need": "5278292", "Non-Need": "886383"}, "Athetic Awards": {"Need": "7431", "Non-Need": "35407"}}, "Self-Help": {"Student Loans": {"Need": "58977531", "Non-Need": "57530125"}, "Federal Work Study": {"Need": "1572642", "Non-Need": 0}, "Total": {"Need": "280028", "Non-Need": "0"}, "State and Other": {"Need": "60830201", "Non-Need": "57530125"}}}, {"Scholarships": {"Federal": {"Need": "26516077", "Non-Need": "4272681"}, "Institutional": {"Need": "21416756", "Non-Need": "1292628"}, "state": {"Need": "34407725", "Non-Need": "19540163"}, "Other Grants": {"Need": "11374084", "Non-Need": "11763677"}, "Total": {"Need": "93714642", "Non-Need": "36869149"}}, "Other": {"Tuition Waivers": {"Need": "2065705", "Non-Need": "22013245"}, "Parent Loans": {"Need": "2661977", "Non-Need": "8098791"}, "Athetic Awards": {"Need": "1706476", "Non-Need": "3829348"}}, "Self-Help": {"Student Loans": {"Need": "53701427", "Non-Need": "54686293"}, "Federal Work Study": {"Need": "1284641", "Non-Need": 0}, "Total": {"Need": "216204", "Non-Need": "0"}, "State and Other": {"Need": "55202272", "Non-Need": "54686293"}}}, {"Scholarships": {"Federal": {"Need": "43171465", "Non-Need": "755180"}, "Institutional": {"Need": "36629845", "Non-Need": "698140"}, "state": {"Need": "39769771", "Non-Need": "7556789"}, "Other Grants": {"Need": "17942982", "Non-Need": "5875047"}, "Total": {"Need": "137514063", "Non-Need": "14885156"}}, "Other": {"Tuition Waivers": {"Need": "6642876", "Non-Need": "23867203"}, "Parent Loans": {"Need": "3115850", "Non-Need": "234522"}, "Athetic Awards": {"Need": "7451", "Non-Need": "35891"}}, "Self-Help": {"Student Loans": {"Need": "70679131", "Non-Need": "41689203"}, "Federal Work Study": {"Need": "1343704", "Non-Need": 0}, "Total": {"Need": "285332", "Non-Need": "0"}, "State and Other": {"Need": "72308167", "Non-Need": "41689203"}}}]
labels = 'Scholarships', 'SelfHelp', 'Others'
sublabels1 = 'Federal', 'Institutional', 'state', 'other', 'total'
sublabels2 = 'Student Loans', 'Federal Work and study', 'State and others', 'Total'
sublabels3 = 'Tuition Waivers', 'Parent Loans', 'Other'
count = 0
for mydata in totaldata:
    count += 1
    toplist = []
    sublist = []
    subcount = 0
    for mysource in mydata.keys():
        ax = axes([0.1, 0.1, 0.6, 0.6])
        value = 0.0
        subcount += 1
        sublist = []
        for mysubsource in mydata[mysource]:
            subvalue = 0.0
            for condition in mydata[mysource][mysubsource]:
                value = value + float(mydata[mysource][mysubsource][condition])
                subvalue += float(mydata[mysource][mysubsource][condition])
            sublist.append(subvalue)
        toplist.append(value)
        fracs = toplist
        explode = (0, 0, 0)
        if mysource == 'Scholarships':
            templabels = sublabels1
        elif mysource == 'Self-Help':
            templabels = sublabels2
        else:
            templabels = sublabels3
        try:
            patches, texts, autotexts = pie(sublist, labels=templabels, autopct='%1.1f%%')
        except:
            print 'Error'
            print sublist, templabels
        proptease = fm.FontProperties()
        proptease.set_size('xx-small')
        setp(autotexts, fontproperties=proptease)
        setp(texts, fontproperties=proptease)
        rcParams['legend.fontsize'] = 7.0
        savefig("pie"+str(count)+str(subcount))
        clf()

    ax = axes([0.1, 0.1, 0.6, 0.6])
    fracs = toplist
    explode = (0, 0, 0)
    patches, texts, autotexts = pie(fracs, labels=labels, autopct='%1.1f%%')
    proptease = fm.FontProperties()
    proptease.set_size('xx-small')
    setp(autotexts, fontproperties=proptease)
    setp(texts, fontproperties=proptease)
    rcParams['legend.fontsize'] = 7.0
    savefig("pie"+str(count))
    clf()
