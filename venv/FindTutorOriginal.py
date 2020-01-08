import Objects as ob
import pickle
from datetime import date
import calendar


def FindTutor(Subject,Day,Time):
    Matches=[]
    MatchesName=[]
    SubjNoMatch=[]
    SubjNoMatchNames=[]
    Tutorlist=ob.Tutors()
    Tutorlist.get_tutorlist()
    Tutorlist=Tutorlist.TutorList
    #Day should be an input as either M Tu W Th F Sa Su
    for tutor in Tutorlist:
        if tutor.Avail[Day]['Start']!='Un' and tutor.Avail[Day]['End']!='Un':
            if int(tutor.Avail[Day]['Start'])<=Time and int(tutor.Avail[Day]['End'])>Time:
                for subj in tutor.Subjects:
                    Name = tutor.FirstName + ' ' + tutor.LastName
                    if subj == Subject:
                        Matches.append(tutor)
                        MatchesName.append(Name)
                    else:
                        SubjNoMatch.append(tutor)
                        SubjNoMatchNames.append(Name)
    if MatchesName!=[]:
        return MatchesName
    elif Matches!=[]:
        return Matches
    elif SubjNoMatch!=[]:
        return SubjNoMatch
    elif SubjNoMatchNames!=[]:
        return SubjNoMatchNames
    else:
        return ("No Matches for this timeslot")

print(FindTutor('Math','Tu',1830))


