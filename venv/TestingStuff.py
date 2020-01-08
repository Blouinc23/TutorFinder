import Objects as ob
import os
import gspread


#Chris=ob.Tutor('Chris','Blouin',['Geometry','Math','Physics'],{'M':{'Start':1600,'End':1800},'Tu':{'Start':1730,'End':2030}, 'W':{'Start':'Un','End':'Un'}})
#Chris.update_database()

# Dir=ob.Directoy(Dir='C:\\Users\\mrmin\\Desktop\\Test')
# Dir.directory_test()
#
#Val=ob.Tutor('Val','White',['Geometry'],Avail={'M':{'Start':1600,'End':1800},'Tu':{'Start':1730,'End':2030}, 'W':{'Start':'Un','End':'Un'}})
#Val.update_database()
#
# caleb=ob.Student('Caleb','Shomo')
# caleb.update_database()
#
# test=ob.loadStudent('Caleb','Shomo')
# test2=ob.loadTutor('Val','White')
#
# print(test.FirstName)
# print(test2.Subjects)
#
# Dir=ob.Directoy(Dir=os.getcwd())
# Dir.directory_test()
#
# Val=ob.Tutor('Val','White',['Geometry'],Avail={'M':{'Start':1600,'End':1800},'Tu':{'Start':1730,'End':2030}, 'W':{'Start':'Un','End':'Un'}})
# Val.update_database()
#
# caleb=ob.Student('Caleb','Shomo')
# caleb.update_database()
#
# test=ob.loadStudent('Caleb','Shomo')
# test2=ob.loadTutor('Val','White')
#
# print(test.FirstName)
# print(test2.Subjects)


# Dir=ob.Directoy(Dir=os.getcwd())
# Dir.directory_test()
# sheet=ob.GoogleSheet('Python Test')
# sheet.get_sheet1()
# stuff=sheet.sheet1.get_all_values()
# print(stuff)
#
# Val=ob.loadTutor('Val','White')
# Days=['M','Tu','W']
# StrSet=[]
# #print(Val.Avail)
# #print(str(Val.Avail[Days[3]]['Start'])+'-'+str(Val.Avail[Days[3]]['End']))
# for i in range(len(Days)):
#     print(i)
#     StrSet.append(str(Val.Avail[Days[i]]['Start'])+'-'+str(Val.Avail[Days[i]]['End']))
# print(StrSet)

Dir=ob.Directoy(Dir=os.getcwd())
Dir.directory_test()
sheet=ob.GoogleSheet('Tutor Sheet')
print(sheet.Sheetlist[1])
Val=ob.loadTutor('Val','White')
Val.update_email('test@gmail.com')
Val.sheet_update(sheet)

print('this is a test')





# Str=ob.hourConversion(1115)
# print(Str)


# test=Str.replace('.',':')
# print(test)
# print(len(test))

# import time
# t = time.strptime('02:00', "%H:%M")
# timevalue_12hour = time.strftime( "%I:%M %p", t )
# print(timevalue_12hour)
#
# string = str(100)
# print(':'.join([string[i:i+1] for i in range(0, len(string), 2)]))

#s[:4] + '-' + s[4:]
#'3558-79ACB6'

# print('testing new stuff here')
# time=230
# print(str(time).zfill(4))
# TimeStr=str(time).zfill(4)[:2]+':'+str(time).zfill(4)[2:]
# print(TimeStr)
