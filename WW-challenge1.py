import csv
import glob
import pandas as pd
import numpy as np
#import datetime
from datetime import datetime
import re


# set directory to read files from
source_dir = "C:\\Users\\abhij\\Documents\\Career\\013 - Wire Wheel\\coding_challenge\\coding_challenge\\gfz-data"
output_file = "C:\\Users\\abhij\\Documents\\Career\\013 - Wire Wheel\\coding_challenge\\coding_challenge\\challenge1.csv"

file_list = glob.glob(source_dir + '/*.TAB')

# create data frame, empty list, for loop to iterate through file_list, thus adding correct rows from each file to a master dataframe
frame = pd.DataFrame()
list_ = []
#setting column widths b/c of use of pd.read_fwf {fixed width file}
col_widths = [(0,6), (8,10), (11, 13), (14,16), (17,19), (20,23), (24,26), (27,29), (30, 32), (42, 45)]

for filename_ in file_list:

    df = pd.read_fwf(filename_, colspecs = col_widths, header = None)

    df = df.dropna(axis=0, subset=[4])
    df = df.dropna(axis=0, subset=[8])
    list_.append(df)

''' #Test on a single file
df = pd.read_fwf('C:\\Users\\abhij\\Documents\\Career\\013 - Wire Wheel\\coding_challenge\\coding_challenge\\gfz-data\\kp9706.tab', colspecs = col_widths, header = None)

#df = df[(df[8]>0)]
df = df.dropna(axis=0, subset=[4])
df = df.dropna(axis=0, subset=[8])
list_.append(df)
'''

frame = pd.concat(list_)
#provide column names since none provided in files
frame.columns = ['Date', '00-03h', '03-06h', '06-09h', '09-12h', '12-15h', '15-18h', '18-21h', '21-00h', 'AP']
#reorder dataframe to match desired output
frame = frame[['Date', 'AP', '00-03h', '03-06h', '06-09h', '09-12h', '12-15h', '15-18h', '18-21h', '21-00h']]
#sort dataframe by AP column, largest to smallest
frame.sort_values(by='AP', ascending = False, inplace=True)
#limit dataframe to top 50 by AP value
frame = frame.iloc[:50]


# function to ensure selecting the correct max value for KP_max column while leaving as string for formatting reasons
def kp_clean(row):

    kp_array = ['9', '9-', '8', '8-', '7', '7-', '6', '6-', '5', '5-', '4', '4-', '3', '3-', '2', '2-', '1', '1-']
    i = 0
    
    while i < len(kp_array):
        if kp_array[i] in row.values:
            return(kp_array[i])
        else:
            i += 1

# end function kp_clean

#function to reformat date
def date_clean(row):

    if isinstance(row[0], int):
        temp_date = (datetime.strptime((str(row[0])), '%y%m%d'))
        return temp_date.strftime('%Y/%m/%d')
    else:
        temp_date = (datetime.strptime(row[0], '%y%m%d'))
        return temp_date.strftime('%Y/%m/%d')
# end function date_clean

# original strip out 'o'
frame['00-03h'] = frame['00-03h'].str.replace('o','')
frame['03-06h'] = frame['03-06h'].str.replace('o','')
frame['06-09h'] = frame['06-09h'].str.replace('o','')
frame['09-12h'] = frame['09-12h'].str.replace('o','')
frame['12-15h'] = frame['12-15h'].str.replace('o','')
frame['15-18h'] = frame['15-18h'].str.replace('o','')
frame['18-21h'] = frame['18-21h'].str.replace('o','')
frame['21-00h'] = frame['21-00h'].str.replace('o','')


#using function to populate KP_Max
frame['KP_Max'] = frame.apply(kp_clean, axis=1)

#using function to reformat date
frame['Date'] = frame.apply(date_clean, axis=1)

print(frame)
frame.to_csv(output_file)