import csv
from collections import defaultdict

FOLDER = '/home/gsunder/hackathon/04.04.14_Diversity_Open_Data_Hackathon/Data/1999-2014_Enrollment Profile/CSV Files/'
FILE_SUFFIX = 'Enrollment Profile'
FILE_DICT = {'2004': {'FA': 19, 'SP': 19, 'SU': 19}, '2005': {'FA': 19, 'SP': 19, 'SU': 19}, '2006': {'FA': 19, 'SP': 19, 'SU': 19},
             '2007': {'FA': 19, 'SP': 19, 'SU': 19}, '2008': {'FA': 19, 'SP': 19, 'SU': 19}, '2009': {'SP': 19, 'SU': 19}}
DEPTS = ['Agriculture', 'Architecture', 'Business Admin', 'Education', 'Engineering', 'G. Bush School of Govt',
         'Geosciences', 'Liberal Arts', 'Science', 'Veterinary Medicine', 'General Studies', 'Other - Special Populations']
ETHNICITY = ['International', 'Black', 'Am. Indian', 'Asian', 'Hispanic', 'White']
START_ROW = 7
START_COL = 1

classification = defaultdict(lambda : defaultdict(lambda: defaultdict(int)))

if __name__ == '__main__':
    for year in FILE_DICT:
        sem_dict = FILE_DICT[year]
        for sem in sem_dict:
            folder = year + '_' + sem + '_' + FILE_SUFFIX + '/'
            file = 'Table ' + str(sem_dict[sem]) + '-Table 1.csv'
            with open(FOLDER + folder + file) as data_file:
                data, row_idx = csv.reader(data_file), 0
                for row in data:
                    if row_idx >= START_ROW and row_idx - START_ROW < len(DEPTS):
                        col_idx = 0
                        for col in row:
                            if col_idx >= START_COL and (col_idx - START_COL)/2 < len(ETHNICITY):
                                col = col.replace(',','')
                                print row_idx, col_idx, DEPTS[row_idx - START_ROW], ETHNICITY[(col_idx - START_COL)/2], col
                                try:
                                    classification[year][DEPTS[row_idx - START_ROW]][ETHNICITY[(col_idx - START_COL)/2]] += int(col)
                                except:
                                    print 'Error converting data: [' + str(col) + ']'
                            col_idx += 1
                    row_idx += 1
                    
    
    print classification
                        
                        
