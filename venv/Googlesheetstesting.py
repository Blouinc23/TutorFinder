import gspread
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds=ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client=gspread.authorize(creds)

sheet=client.open("Tutor Sheet").get_worksheet(2)
test=sheet.get_all_values()
print(test)
print(test[1])
print(test[2])
#print(test[2].index(''))
print(str(test[2][7]))
print(test[2][7])
sheet.delete_row()

#test[row][column]








# str=[]
# str.append()
#
# vals=['123','125','fuck']
# sheet.insert_row(vals,size+1)