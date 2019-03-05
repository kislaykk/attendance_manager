import sqlite3
conn=sqlite3.connect('attend')
cur=conn.cursor()
print('*___ welcome to the attendance manager___*')
while True:
    print('what do you want to do?\n1.manage your attendance\n2.delete all your data\n3.start your database\n4.to check status\n5.to quit\n\n\n\n')
    fd=int(input()) #first decision
    if fd==1:
            #block for managing attendance
            sd=int(input('what do you want to do next?\n1.update attendance\n2.change attendance data'))
            if sd==1:
                print('input the s.no. corresponding to the subject to update attendance')
                cur.execute('SELECT sn,sub FROM subjects')
                for row in cur:
                    print(row[0],row[1])
                conn.commit()
                up=int(input())
                cur.execute('SELECT attended, happened FROM subjects WHERE sn =?',(up,))
                row = cur.fetchone()
                new=row[0]+1
                tot=row[1]+1
                bunk=int(input('1. attended the class 2. missed the class '))
                if bunk==1:
                    cur.execute('UPDATE subjects SET attended =? WHERE sn = ?',(new,up))
                    cur.execute('UPDATE subjects SET happened =? WHERE sn = ?',(tot,up))
                elif bunk==2:
                    cur.execute('UPDATE subjects SET happened =? WHERE sn = ?',(tot,up))
            elif sd==2:
                cur.execute('SELECT * FROM subjects')
                for row in cur:
                    print(row[0],row[1],row[2],row[3])
                print("\nwhat do you want to edit?\n1. subject's name\n2.attended classes\n3.number of classes that happened")
                dec=int(input())
                if dec==1:
                    subin=int(input("input the sno,whose subject name is to be changed"))
                    newsub=input("input the new subject name")
                    cur.execute("UPDATE subjects SET sub =? WHERE sn=?",(newsub,subin))
                elif dec==2:
                    subin=input("input the sno,whose number of attended classes has to be changed is to be changed")
                    newsub=int(input("input the new number"))
                    cur.execute("UPDATE subjects SET attended =? WHERE sn=?",(newsub,subin))
                elif dec==3:
                    subin=int(input("input the sno,whose number of occurence of classes has to be changed "))
                    newsub=int(input("input the new number"))
                    cur.execute("UPDATE subjects SET happened =? WHERE sn=?",(newsub,subin))

            conn.commit()

    elif fd==2:
        cur.execute('DROP TABLE IF EXISTS student')
        cur.execute('DROP TABLE IF EXISTS subjects')
        #block to delete all the student database
        conn.commit()
        exit=input('do you want to continue(y/n?)')

        if exit is 'n':
            conn.commit()
            conn.close()
            break
        elif exit is 'y':
            continue

    elif fd==3:

        #block to start new account

        name=input('insert your name:')
        roll=int(input('input your roll number:'))
        cur.execute('CREATE TABLE student(name TEXT,roll INTEGER)')
        cur.execute('CREATE TABLE subjects(sn INTEGER,sub TEXT,attended INTEGER,happened INTEGER)')

        cur.execute('INSERT INTO student (name,roll) VALUES(?,?)',(name,roll))
        print('table is created')

        n_sub=int(input('what is the number of subjects?'))
        for i in range(n_sub):
            print('input the no.',i+1,'subject')
            subj=input()
            cur.execute('INSERT INTO subjects (sn,sub,attended,happened) VALUES(?,?,?,?)',(i+1,subj,0,0))
            conn.commit()
        exit=input('do you want to continue(y/n?)')
        if exit is 'n':
            conn.commit()
            conn.close()
            break
        elif exit is 'y':
            continue
    elif fd==4:
        cur.execute('SELECT * FROM subjects')
        for row in cur:
            try:
                print(row[1],':',(row[2]/row[3])*100,"%","attended:",row[2],"out of",row[3])
            except:
                print("no class happened in",row[1])
        conn.commit()
        exit=input('do you want to continue(y/n?)')
        if exit is 'n':
            conn.commit()
            conn.close()
            break
        elif exit is 'y':
            continue
    elif fd==5:
        break
        conn.commit()
        conn.close()
    else:
        print('wrong choice')
