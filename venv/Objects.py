import tkinter as tk
import pickle
import os
import glob
import datetime
import calendar
import gspread
from pprint import pprint
from oauth2client.service_account import ServiceAccountCredentials
import time

StudentDir=''
TutorDir=''
StudentSheet=''
TutorSheet=''
class GoogleSheet(object):
    def __init__(self, Filename):
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        self.Creds = ServiceAccountCredentials.from_json_keyfile_name(os.getcwd() + "\\creds.json", scope)
        self.Client = gspread.authorize(self.Creds)
        self.Filename = Filename
        length=len(self.Client.open(Filename).worksheets())
        self.Sheetlist=[]
        for i in range(length):
            self.Sheetlist.append(self.Client.open(Filename).get_worksheet(i))
    #This only has sheets
    def get_sheet1(self):
        self.sheet1 = self.Client.open(self.Filename).get_worksheet(0)
    def get_sheet2(self):
        self.sheet2 = self.Client.open(self.Filename).get_worksheet(1)
    def get_sheet3(self):
        self.sheet3 = self.Client.open(self.Filename).get_worksheet(2)
    def get_sheet4(self):
        self.sheet4 = self.Client.open(self.Filename).get_worksheet(3)
    def get_sheet5(self):
        self.sheet5 = self.Client.open(self.Filename).get_worksheet(4)


class Directoy(object):
    def __init__(self,Dir=os.getcwd()):
        global StudentDir
        global TutorDir
        StudentDir=Dir+'\\Students\\'
        TutorDir=Dir+'\\Tutors\\'
        self.StudentDir=Dir+'\\Students\\'
        self.TutorDir=Dir+'\\Tutors\\'
        self.Dir=Dir
    def directory_test(self):
        #FullDir1=self.StudentDir
        #FullDir2=self.TutorDir
        FullDir1=StudentDir
        FullDir2=TutorDir
        if not os.path.exists(FullDir1):
            os.makedirs(FullDir1)
            print('Directory: ' + FullDir1 + ' Added')
        else:
            print('Directory Already present')
        if not os.path.exists(FullDir2):
            os.makedirs(FullDir2)
            print('Directory: ' + FullDir2 + ' Added')
        else:
            print('Directory Already Present')
    def directory_update(self,NewDir):
        self.StudentDir = NewDir + '\\Students\\'
        self.TutorDir = NewDir + '\\Tutors\\'
        self.Dir = NewDir


class Tutor(object):
    def __init__(self,FirstName,LastName,Email,Subjects,Avail):
        self.FirstName=FirstName
        self.LastName=LastName
        self.Subjects=Subjects
        self.Avail=Avail
        self.Email=Email
    def update_Avail(self,NewAvail):
        #NewAvail should be formatted as such
        #Example:
            #M:4pm-6pm Tu:5:30pm-8:30pm W:Unavailable Etc.
            #Avail={'M':{'Start':1600,'End':1800},'Tu':{'Start':1730,'End':2030}, 'W':{'Start':'Un','End':'Un'} Etc....}
        self.Avail=NewAvail
        self.update_database()
    def add_Subject(self,Subject):
        self.Subjects.append(Subject)
        self.update_database()
    def new_Subjects(self,SubjectsNew):
        self.Subjects = SubjectsNew
        self.update_database()
    def update_name(self,NewName):
        self.Name=NewName
        self.update_database()
    def update_avail(self,NewAvail):
        self.Avail=NewAvail
        self.update_database()
    def update_database(self):
        FileName = TutorDir+ str(self.FirstName) + str(' ' + self.LastName)
        File = open(FileName, 'wb')
        pickle.dump(self, File)
    def del_tutor(self):
        FileName =TutorDir + str(self.FirstName) + str(' ' + self.LastName)
        if os.path.exists(FileName):
            os.remove(FileName)
    def get_sessions(self):
        self.Sessions = Sessions
        pass
    def update_email(self,NewEmail):
        self.Email=NewEmail
    def sheet_update(self,Sheet):
        ##Sheet 1 will be name and email
        ##Sheet 2 will be name and availability
        ##Sheet 3 will be name and subjects

        #This is updating the name and email list
        S1Size=len(Sheet.Sheetlist[0].get_all_values())
        S1Vals=[self.FirstName+' ' + self.LastName,self.Email]
        Sheet.Sheetlist[0].insert_row(S1Vals,S1Size+1)

        #This is updating the Availability Chart
        S2Size = len(Sheet.Sheetlist[1].get_all_values())
        Days=['M','Tu','W','Th','Fr','Sa','Su']
        StrSet=[]
        for i in range(len(Days)):
            if self.Avail[Days[i]]['Start']!='Un' and self.Avail[Days[i]]['End']!='Un':
                StrSet.append(hourConversion(str(self.Avail[Days[i]]['Start'])) + '-' + hourConversion(str(self.Avail[Days[i]]['End'])))
            else:
                StrSet.append('Unavailable')
        S2Vals = [self.FirstName+' ' + self.LastName, StrSet[0],StrSet[1],StrSet[2]]
        Sheet.Sheetlist[1].insert_row(S2Vals, S2Size + 1)

        #This is updating the subject list
        for subject in self.Subjects:
            SheetVals=Sheet.Sheetlist[2].get_all_values()
            if subject in SheetVals:
                subjectLocation=SheetVals[0].index(subject)
                subjectLocationCol=subjectLocation+1
                Name=self.FirstName + ' ' + self.LastName
                if Name in Sheet.Sheetlist[2].col_values(subjectLocationCol):
                    pass
                else:
                    Sheet.Sheetlist[2].update_cell(len(Sheet.Sheetlist[2].col_values(subjectLocationCol))+1,subjectLocationCol,Name)
            else:
                endLocation=len(SheetVals[0])
                Sheet.Sheetlist[2].add_cols(subject)

                # for i in range(len(Sheet.Sheetlist[2].col_values(subjectLocationCol))):
                #     Sheet.Sheetlist[2].cell(i,subjectLocationCol)


class Tutors(object):
    def __init__(self):
        self.TutorList = []
    def get_tutorlist(self):
        self.temptutorlist=[]
        Names=os.listdir(TutorDir)
        for name in Names:
            FullDir=FileName+name
            with open(FullDir, "rb") as file:
                Tutor = pickle.load(file)
                self.temptutorlist.append(Tutor)
        self.TutorList=self.temptutorlist
        del self.temptutorlist
    def import_tutors(self,TutorDir):
        self.importlist=[]
        Names=os.listdir(TutorDir)
        for name in Names:
            FullDirTutor=TutorDir+name
            with open(FullDirtutor, "rb") as file:
                Tutor = pickle.load(file)
                self.importlist.append(Tutor)
        self.TutorList=self.importlist
        del self.importlist


class Student(object):
    def __init__(self,FirstName,LastName):
        self.FirstName=FirstName
        self.LastName = LastName
        self.update_database()
    def update_name(self,FirstNameNew,LastNameNew):
        self.FirstName = FirstNameNew
        self.LastName = LastNameNew
        self.update_database()
    def del_student(self):
        FileName = StudentDir + str(self.FirstName) + str(' ' + self.LastName)
        if os.path.exists(FileName):
            os.remove(FileName)
    def update_database(self):
        FileName =StudentDir + str(self.FirstName) + str(' ' + self.LastName)
        File = open(FileName, 'wb')
        pickle.dump(self, File)



def loadStudent(FirstName,LastName):
    Name=str(FirstName + ' '+ LastName)
    FullDir=StudentDir+Name
    with open(FullDir, "rb") as file:
        Student = pickle.load(file)
    return Student

def loadTutor(FirstName,LastName,Dir=TutorDir):
    Name = str(FirstName + ' ' + LastName)
    FullDir = TutorDir + Name
    with open(FullDir, "rb") as file:
        Tutor = pickle.load(file)
    return Tutor

def date_to_day_conversion(Date):
    #Should be formatted in Day/Month/Year
    Day,Month,Year=(int(x) for x in Date.split('/'))
    temp=datetime.date(Year,Month,Day)
    Daynum=temp.strftime('%w')
    if int(Daynum)==0:
        DayChar='Su'
        return DayChar
    elif int(Daynum)==1:
        DayChar='M'
        return DayChar
    elif int(Daynum)==2:
        DayChar='Tu'
        return DayChar
    elif int(Daynum)==3:
        DayChar='W'
        return DayChar
    elif int(Daynum)==4:
        DayChar='Th'
        return DayChar
    elif int(Daynum)==5:
        DayChar='F'
        return DayChar
    elif int(Daynum)==6:
        DayChar='Sa'
        return DayChar
    else:
        return Daynum


def findTutor(Subject, Date, Time, OutputFlag='Time and Subject'):
    #Date should be formatted in Day/Month/Year
    Matches = []
    MatchesName = []
    SubjNoMatch = []
    SubjNoMatchNames = []
    Day=date_to_day_conversion(Date)
    Tutorlist = Tutors()
    Tutorlist.get_tutorlist()
    Tutorlist = Tutorlist.TutorList

    for tutor in Tutorlist:
        Name = tutor.FirstName + ' ' + tutor.LastName
        if tutor.Avail[Day]['Start'] != 'Un' and tutor.Avail[Day]['End'] != 'Un':
            if int(tutor.Avail[Day]['Start']) <= Time and int(tutor.Avail[Day]['End']) > Time:
                if Subject in tutor.Subjects:

                    Matches.append(tutor)
                    MatchesName.append(Name)
                if Subject not in tutor.Subjects:
                    SubjNoMatch.append(tutor)
                    SubjNoMatchNames.append(Name)

    if OutputFlag=='Time and Subject':
        if Matches!=[] and MatchesName!=[]:
            return MatchesName
        else:
            print("No matches for both subject and timeslot")
            return

    if OutputFlag=='Time':
        if Matches!=[] and MatchesName!=[]:
            return MatchesName
        else:
            print("No matches for both subject and timeslot")
        if SubjNoMatch!=[] and SubjNoMatchNames!=[]:
            print("Matches reported do not have the subject required listed, but are available for tutoring")
            return SubjNoMatchNames
        else:
            print("No matches for just the timeslot")

def hourConversion(Val):
    TimeStr = str(Val).zfill(4)[:2] + ':' + str(Val).zfill(4)[2:]
    print(TimeStr)
    Temp=time.strptime(TimeStr,"%H:%M")
    StrTemp=time.strftime("%I:%M %p",Temp)
    if int(StrTemp[:1])==0:
        Str=StrTemp[1:]
        return Str
    else:
        Str=StrTemp
        return Str

