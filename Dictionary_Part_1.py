room = {'CS101':3004, 'CS102':4501, 'CS103':6755, 'NT110':1244, 'CM241':1411}
instructor = {'CS101':'Haynes', 'CS102':'Alvarado', 'CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee'}
time = {'CS101':'8:00 a.m.', 'CS102':'9:00 a.m.', 'CS103':'10:00 a.m.', 'NT110':'11:00 a.m.', 'CM241':'1:00 p.m.'}

course = input('Enter a Course Number: ')

if course in room and course in instructor and course in time:
    print(room[course])
    print(instructor[course])
    print(time[course])
else:
    print("This course number is not in this registry.")



#github link
#https://github.com/c-gue/Homework.git