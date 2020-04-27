#Rohun Baxi
#2018/1/1 -> 2018/1/19

#imports
from tkinter import *

#declaring key global variables + values
global root
global canvas
global x
global tlist
global o
global blocklist

tlist = []
x = 0
o = -1
blocklist = []

#page setup
root = Tk()
root.title('IUT: Internet Usage Tracker')

canvas = Canvas(root, width = 800, height = 300, bg = 'light blue')
canvas.pack()



#class that holds entire code
class Summative():
    #global variables are constantly declared and called where necessary throughout the code
    
    global btInsert
    global pic

    #sets up title text and borders
    canvas.create_text(400,120, text = 'Internet Usage Tracker', font = 'Times 24 bold', tags = 'title')
    canvas.create_text(400,180, text = 'Manage your addiction, with the IUT', font = 'Times 16 italic', tags = 'sub')
    canvas.create_rectangle(50,20,750,280, width = 10, outline = 'black')
    canvas.create_rectangle(100,40,700,260, width = 10, outline = 'red')
    canvas.create_rectangle(160,70,650,230, width = 10, outline = 'blue') 

    def enter():
        #deletes all and sets up table for applications and time
        canvas.delete('all')
        btEnter.pack_forget()
        btTrack.pack_forget()
        btInfo.pack_forget()

        #table setup
        canvas.create_text(200,30, text = 'Application Name', font = 'Times 19 bold', tags = 'heading1')
        canvas.create_text(600,30, text = 'Time Spent (mins)', font = 'Times 19 bold', tags = 'heading2')

        canvas.create_line(0,60,800,60, fill = 'red')
        canvas.create_line(0,100,800,100, fill = 'red')
        canvas.create_line(0,140,800,140, fill = 'red')
        canvas.create_line(0,180,800,180, fill = 'red')
        canvas.create_line(0,220,800,220, fill = 'red')
        canvas.create_line(0,260,800,260, fill = 'red')
        canvas.create_line(400,0,400,300,fill = 'red')
        
        #for loop in order to place text
        for z in range(len(tlist)):
            if z == 0:
                canvas.create_text(200,80, text = tlist[z][0], font = 'Times 14', tags = 'entry1')
                canvas.create_text(600,80, text = tlist[z][1], font = 'Times 14', tags = 'entry2')
            elif z != 0:
                canvas.create_text(200,80+40*z, text = tlist[z][0], font = 'Times 14', tags = 'entry1')
                canvas.create_text(600,80+40*z, text = tlist[z][1], font = 'Times 14', tags = 'entry2')



        def entusg():
            #entries allow you to input app name + usage, also increasing x variable for positioning
            global e
            global f
            global x
            e = Entry(root)
            e.pack()
            e.delete(0, END)
            e.insert(0, 'App Name')
            f = Entry(root)
            f.pack()
            f.delete(0, END)
            f.insert(0, 'Time Spent (mins)')
            btEnt.pack_forget()
            btDel.pack_forget()
            btBack.pack_forget()
            btInsert.pack()
            x += 1
        def delusg():
            #gives entries so user can input what they want deleted, x position is reduced 
            global e
            global f
            global x
            e = Entry(root)
            e.pack()
            e.delete(0, END)
            e.insert(0, 'App Name')
            f = Entry(root)
            f.pack()
            f.delete(0, END)
            f.insert(0, 'Time Spent')
            btEnt.pack_forget()
            btDel.pack_forget()
            btBack.pack_forget()
            btDelete.pack()
            x -= 1
        def deleteprocess():
            global tlist

            #calls what was entered prevously in for loop for tlist range
            for y in range(len(tlist)):
                n1 = e.get()
                n2 = f.get()
                #if time and name match, both are popped from the list
                if n1 == tlist[y][0] and n2 == tlist[y][1]:
                    tlist.pop(y)
                    e.pack_forget()
                    f.pack_forget()
                    break
                #if name matches but time does not, the difference is found and kept 
                elif n1 == tlist[y][0] and n2 != tlist[y][1]:
                    tlist[y][1] = int(tlist[y][1])
                    n2 = int(n2)
                    tlist[y][1] = int(tlist[y][1]) - n2
                    if tlist[y][1] < 0:
                        tlist[y][1] = 0
                    e.pack_forget()
                    f.pack_forget()
                    break

            btDelete.pack_forget()
            e.pack_forget()
            e.pack_forget()
            btEnt.pack()
            btDel.pack()
            btBack.pack()

        def goback():
            #deletes everything and sets up the home page again
            canvas.delete('all')
            btEnter.pack()
            btTrack.pack()
            btInfo.pack()
            btEnt.pack_forget()          
            canvas.create_text(400,120, text = 'Internet Usage Tracker', font = 'Times 24 bold', tags = 'title')
            canvas.create_text(400,180, text = 'Manage your addiction, with the IUT', font = 'Times 16 italic', tags = 'sub')
            canvas.create_rectangle(50,20,750,280, width = 10, outline = 'black')
            canvas.create_rectangle(100,40,700,260, width = 10, outline = 'red')
            canvas.create_rectangle(160,70,650,230, width = 10, outline = 'blue')

            btBack.pack_forget()
            btInsert.pack_forget()
            btDel.pack_forget()
        def insert():
            #allows to insert an object onto the list
            y = f.get()
            n = e.get()
            global tlist
            keynumber = len(tlist) - 1
            global newtime
            global lucky
            global x
            global r
            global blocklist
            #if time is not a digit, this will prevent the entry
            if y.isdigit() == False:
                e.pack_forget()
                f.pack_forget()
                btEnt.pack()
                btDel.pack()
                btBack.pack()
                btInsert.pack_forget()
                x -= 1

            #otherwise, if all is good, it will append the entries into the main tlist and create text as such, showing it on screen 
            else:              
                newtime = []
                newtime.append(e.get())
                newtime.append(f.get())
                tlist.append(newtime)

                canvas.create_text(200,40 + 40*x, text = e.get(), font = 'Times 14', tags = 'newentrance')
                canvas.create_text(600,40 + 40*x, text = f.get(), font = 'Times 14', tags = 'newentrance')
                 
                e.pack_forget()
                f.pack_forget()
                btEnt.pack()
                btDel.pack()
                btBack.pack()
                btInsert.pack_forget()

                #if entry matches the blocklist, it deletes it from the list and makes sure the data can't be accesed (when the list is seen again, the entry is visually removed)
                if len(blocklist) > 0: 
                    if len(blocklist) == 1:
                        if n == blocklist[0]:
                            x -= 1
                            tlist.pop(len(tlist) - 1)
                            e.pack_forget()
                            f.pack_forget()
                            btEnt.pack()
                            btDel.pack()
                            btBack.pack()
                            btInsert.pack_forget()
                    elif len(blocklist) == 2:
                        if n == blocklist[0] or blocklist[1]:
                            x -= 1
                            tlist.pop(len(tlist) - 1)
                            e.pack_forget()
                            f.pack_forget()
                            btEnt.pack()
                            btDel.pack()
                            btBack.pack()
                            btInsert.pack_forget()
                    elif len(blocklist) == 3:
                        if n == blocklist[0] or blocklist[1] or blocklist[2]:
                            x -= 1
                            tlist.pop(len(tlist) - 1)
                            e.pack_forget()
                            f.pack_forget()
                            btEnt.pack()
                            btDel.pack()
                            btBack.pack()
                            btInsert.pack_forget()
                    elif len(blocklist) == 4:
                        if n == blocklist[0] or blocklist[1] or blocklist[2] or blocklist[3]:
                            x -= 1
                            tlist.pop(len(tlist) - 1)
                            e.pack_forget()
                            f.pack_forget()
                            btEnt.pack()
                            btDel.pack()
                            btBack.pack()
                            btInsert.pack_forget()
                    elif len(blocklist) >= 5:
                        if n == blocklist[0] or blocklist[1] or blocklist[2] or blocklist[3] or blocklist[4]:
                            x -= 1
                            tlist.pop(len(tlist) - 1)
                            e.pack_forget()
                            f.pack_forget()
                            btEnt.pack()
                            btDel.pack()
                            btBack.pack()
                            btInsert.pack_forget()



        #buttons corresponding to each of the functions
        btEnt = Button(root,text = 'Enter Usage', bd = 3, command = entusg)
        btEnt.pack()
        btDel = Button(root,text = 'Delete Usage', bd = 3, command = delusg)
        btDel.pack()
        btBack = Button(root,text = 'Go Back', bd = 3, command = goback)
        btBack.pack()
        btInsert = Button(root,text = 'Insert', bd = 3, command = insert)
        btDelete = Button(root,text = 'Delete', bd = 3, command = deleteprocess)
    def track():
        #setting up the track page (list of blocked app)
        canvas.delete('all')
        btEnter.pack_forget()
        btTrack.pack_forget()
        btInfo.pack_forget()

        global blocklist
        global o
        global g
        global btAnother
        #visual setup, for loop shows text within the blocklist
        canvas.create_text(400,30, text = 'Blocked Apps', font = 'Times 19 bold', tags = 'heading1')
        canvas.create_text(320,80, text = '1.', font = 'Times 14 bold')
        canvas.create_text(320,130, text = '2.', font = 'Times 14 bold')
        canvas.create_text(320,180, text = '3.', font = 'Times 14 bold')
        canvas.create_text(320,230, text = '4.', font = 'Times 14 bold')
        canvas.create_text(320,280, text = '5.', font = 'Times 14 bold')

        for z in range(len(blocklist)):
            canvas.create_text(410,80+50*z, text = blocklist[z], font = 'Times 14', tags = 'entries')

        def trackusg():
            #deletes all and setups track screen, creates entry for time range the usage list is relevant for (user-inputted)
            global TimeEnt
            canvas.delete('all')
            #instruction text
            canvas.create_text(400,235, text = 'Insert the period of time for which the current list of app usages are relevant for, to the nearest hour (i.e: 48)', font = 'Times 12', tags = 'inittext')
            canvas.create_text(400,255, text = 'This is in order to create appropraite stats for the app of your choosing.', font = 'Times 12', tags = 'inittext')

            canvas.create_text(320, 50, text = 'App Name:', font = 'Times 24 bold')
            canvas.create_text(320, 100, text = 'Total Time Spent:', font = 'Times 14 bold')
            canvas.create_text(320, 135, text = 'Usage/ Day:', font = 'Times 14 bold')
            canvas.create_text(320, 170, text = '% of Total Device Usage:', font = 'Times 14 bold')

            TimeEnt = Entry(root)
            TimeEnt.pack()
            TimeEnt.delete(0, END)
            TimeEnt.insert(0, 'Time Range? (hours)')

            btTrackk.pack_forget()
            btExem.pack_forget()
            btBackk.pack_forget()

            #packs submission button
            btSubmit.pack()
            
        def submit():
            #loads time entry into variable and creates entry for app name
            global TimeEnt
            global AppEnt
            global times
            times = TimeEnt.get()
            btSubmit.pack_forget()
            
            AppEnt = Entry(root)
            AppEnt.pack()
            AppEnt.delete(0, END)
            AppEnt.insert(0, 'App Name?')

            TimeEnt.pack_forget()

            btEnterr.pack()

            #if time entry was not digit, it returns to home menu
            if times.isdigit() == False:
                canvas.delete('all')
                TimeEnt.pack_forget()
                AppEnt.pack_forget()
                btEnterr.pack_forget()
                
                btTrackk.pack()
                btExem.pack()
                btBackk.pack()
                canvas.create_text(400,30, text = 'Blocked Apps', font = 'Times 19 bold', tags = 'heading1')
                canvas.create_text(320,80, text = '1.', font = 'Times 14 bold')
                canvas.create_text(320,130, text = '2.', font = 'Times 14 bold')
                canvas.create_text(320,180, text = '3.', font = 'Times 14 bold')
                canvas.create_text(320,230, text = '4.', font = 'Times 14 bold')
                canvas.create_text(320,280, text = '5.', font = 'Times 14 bold')

                for z in range(len(blocklist)):
                    canvas.create_text(410,80+50*z, text = blocklist[z], font = 'Times 14', tags = 'entries')

        def another():
            #deletes initial instruction text but keeps time, allowing you to renter app name, and go to enter
            global times
            global AppEnt
            canvas.delete('inittext')

            btAnother.pack_forget()
            btBackkk.pack_forget()

            AppEnt = Entry(root)
            AppEnt.pack()
            AppEnt.delete(0, END)
            AppEnt.insert(0, 'App Name?')

            btEnterr.pack()

            times = str(times)
            
            #if time is not a digit, return to menu
            if times.isdigit() == False:
                canvas.delete('all')
                TimeEnt.pack_forget()
                AppEnt.pack_forget()
                btEnterr.pack_forget()
                
                btTrackk.pack()
                btExem.pack()
                btBackk.pack()
                canvas.create_text(400,30, text = 'Blocked Apps', font = 'Times 19 bold', tags = 'heading1')
                canvas.create_text(320,80, text = '1.', font = 'Times 14 bold')
                canvas.create_text(320,130, text = '2.', font = 'Times 14 bold')
                canvas.create_text(320,180, text = '3.', font = 'Times 14 bold')
                canvas.create_text(320,230, text = '4.', font = 'Times 14 bold')
                canvas.create_text(320,280, text = '5.', font = 'Times 14 bold')

                for z in range(len(blocklist)):
                    canvas.create_text(410,80+50*z, text = blocklist[z], font = 'Times 14', tags = 'entries')

            #new instructions for user        
            canvas.create_text(400,235, text = 'As the period of time has already been inserted, simply add a new app of your choosing.', font = 'Times 12', tags = 'inittext')
            canvas.create_text(400,255, text = 'This will allow you to access the same stats page as before.', font = 'Times 12', tags = 'inittext')



        def enterr():
            #takes time and app input and delets instruction text
            global AppEnt
            global totaltime
            global TimeEnt
            global times
            global totaldeviceusg
            btEnterr.pack_forget()
            canvas.delete('inittext')
            
            #variables for all necessary values (total time, total device time, % time, etc.)
            times = int(times)
            appname = AppEnt.get()
            check = 0
            totaltime = 0
            timeusg = 0
            totaldeviceusg = 0
            spefappusg = 0

            #for loop that makes sure that the app input is in list and then does the math for the variables
            for y in range(len(tlist)):
                applicationtime = int(tlist[y][1])
                totaldeviceusg += applicationtime
                if appname == tlist[y][0]:
                    check += 2
                    canvas.create_text(480, 50, text = tlist[y][0], font = 'Times 24',tags = 'inittext')
                    totaltime += applicationtime
                    times = int(times)
                    timeusg = (totaltime*24)/times
                else:
                    pass
                spefappusg = (totaltime/totaldeviceusg) * 100

            #check to make sure the app actually exists in tlist, if not it returns to menu
            if check < 1:
                canvas.delete('all')
                AppEnt.pack_forget()

                btAnother.pack_forget()
                btBackkk.pack_forget()

                btTrackk.pack()
                btExem.pack()
                btBackk.pack()
                
                canvas.create_text(400,30, text = 'Blocked Apps', font = 'Times 19 bold', tags = 'heading1')
                canvas.create_text(320,80, text = '1.', font = 'Times 14 bold')
                canvas.create_text(320,130, text = '2.', font = 'Times 14 bold')
                canvas.create_text(320,180, text = '3.', font = 'Times 14 bold')
                canvas.create_text(320,230, text = '4.', font = 'Times 14 bold')
                canvas.create_text(320,280, text = '5.', font = 'Times 14 bold')

                for z in range(len(blocklist)):
                    canvas.create_text(410,80+50*z, text = blocklist[z], font = 'Times 14', tags = 'entries')
            else:
                pass

            timeusg = round(timeusg, 0)
            spefappusg = round(spefappusg, 0)

            #prints text depending on usage (if app usage and total usage are high, it prints pre-determined text to help the user, etc., etc.)
            if timeusg >= 180 and spefappusg >= 50:
                canvas.create_text(400,235, text = 'You appear to use this app for an extensive deal of time (3+ hours/ day).', font = 'Times 12', tags = 'inittext')
                canvas.create_text(400,255, text = 'Consituting the majority of your usage, it is likely that you are addicted to this app.', font = 'Times 12', tags = 'inittext')

                

            if timeusg >= 180 and spefappusg < 50:
                canvas.create_text(400,235, text = 'You appear to use this app for extensive deal of time (3+ hours/ day) but it is not a majority of your usage.', font = 'Times 12', tags = 'inittext')
                canvas.create_text(400,255, text = 'It appears to be that you are addicted to your device in general as you use it 6+ hours/ day.', font = 'Times 12', tags = 'inittext')

                

            if timeusg > 90 and timeusg < 180:
                canvas.create_text(400,235, text = 'You use this app for a moderate period of time every day (1.5-3 hours).', font = 'Times 12', tags = 'inittext')
                canvas.create_text(400,255, text = 'There are no major issues found with this usage but you can still improve.', font = 'Times 12', tags = 'inittext')

                

            if timeusg <= 90 and spefappusg <= 25:
                canvas.create_text(400,235, text = 'You use this app for a minimal and healthy period of time.', font = 'Times 12', tags = 'inittext')
                canvas.create_text(400,255, text = 'However, since daily usage still exceeds 6 hours/day, we recommend moderation on a whole.', font = 'Times 12', tags = 'inittext')
                

            if timeusg <= 90 and spefappusg > 25:
                canvas.create_text(400,235, text = 'You use this app and your device for a healthy amount of time.', font = 'Times 12', tags = 'inittext')
                canvas.create_text(400,255, text = 'No further actions are recommended; keep doing what you do.', font = 'Times 12', tags = 'inittext')

                
                


            totaltime = str(totaltime)
            timeusg = str(timeusg)
            spefappusg = str(spefappusg)
            

            #creates text for the specific calculated numbers            
            canvas.create_text(470, 100, text = totaltime + ' minutes', font = 'Times 14', tags = 'inittext')
            canvas.create_text(470, 135, text = timeusg + ' minutes/day', font = 'Times 14', tags = 'inittext')
            canvas.create_text(470, 170, text = spefappusg + ' %', font = 'Times 14', tags = 'inittext')
            
            btAnother.pack()
            btBackkk.pack()

            
            #check for whether app exists in tlist, if not return to menu
            if check < 1:
                canvas.delete('inittext')
                AppEnt.pack_forget()

                btAnother.pack_forget()
                btBackkk.pack_forget()

                btTrackk.pack()
                btExem.pack()
                btBackk.pack()
                
                canvas.create_text(400,30, text = 'Blocked Apps', font = 'Times 19 bold', tags = 'heading1')
                canvas.create_text(320,80, text = '1.', font = 'Times 14 bold')
                canvas.create_text(320,130, text = '2.', font = 'Times 14 bold')
                canvas.create_text(320,180, text = '3.', font = 'Times 14 bold')
                canvas.create_text(320,230, text = '4.', font = 'Times 14 bold')
                canvas.create_text(320,280, text = '5.', font = 'Times 14 bold')

                for z in range(len(blocklist)):
                    canvas.create_text(410,80+50*z, text = blocklist[z], font = 'Times 14', tags = 'entries')

            
            AppEnt.pack_forget()

        def submenu():
            #returns to the submenu with the block list if user chooses not to enter another app
            btAnother.pack_forget()
            btBackkk.pack_forget()

            canvas.delete('all')
            
            btTrackk.pack()
            btExem.pack()
            btBackk.pack()
            
            canvas.create_text(400,30, text = 'Blocked Apps', font = 'Times 19 bold', tags = 'heading1')
            canvas.create_text(320,80, text = '1.', font = 'Times 14 bold')
            canvas.create_text(320,130, text = '2.', font = 'Times 14 bold')
            canvas.create_text(320,180, text = '3.', font = 'Times 14 bold')
            canvas.create_text(320,230, text = '4.', font = 'Times 14 bold')
            canvas.create_text(320,280, text = '5.', font = 'Times 14 bold')

            for z in range(len(blocklist)):
                canvas.create_text(410,80+50*z, text = blocklist[z], font = 'Times 14', tags = 'entries')



        def blockusg():
            #creates entry where user can input an app name they want blocked from being entered into the main list later on
            global blocklist
            global o
            global g

            o += 1
            btTrackk.pack_forget()
            btExem.pack_forget()
            btBackk.pack_forget()

            g = Entry(root)
            g.pack()
            g.delete(0, END)
            g.insert(0, 'App Name?')

            btBlock.pack()

            #insructional text
            canvas.create_text(650,230, text  = 'This will block the inputted app', font = 'Times 12', tags = 'warning')
            canvas.create_text(650,250, text = 'from being resubmitted into the system.', font = 'Times 12', tags = 'warning')

        def block():
            #deletes instructional text 
            canvas.delete('warning')
            canvas.create_text(400,30, text = 'Blocked Apps', font = 'Times 19 bold', tags = 'heading1')
            canvas.create_text(320,80, text = '1.', font = 'Times 14 bold')
            canvas.create_text(320,130, text = '2.', font = 'Times 14 bold')
            canvas.create_text(320,180, text = '3.', font = 'Times 14 bold')
            canvas.create_text(320,230, text = '4.', font = 'Times 14 bold')
            canvas.create_text(320,280, text = '5.', font = 'Times 14 bold')

            for z in range(len(blocklist)):
                canvas.create_text(410,80+50*z, text = blocklist[z], font = 'Times 14', tags = 'entries')

            m = g.get()
            global o

            for z in range(len(blocklist)):
                if g.get() == blocklist[z]:
                    g.get == ''
                    g.pack_forget()
                    btTrackk.pack()
                    btExem.pack()
                    btBackk.pack()
                    btBlock.pack_forget()
            #appends input into blocklist and returns to submenu
            else:
                blocklist.append(g.get())
                canvas.create_text(410,80 + 50 * o, text = g.get(), font = 'Times 14', tags = 'entry1')
                btTrackk.pack()
                btExem.pack()
                btBackk.pack()
                g.pack_forget()
                btBlock.pack_forget()
               
        def gobackk():
            #returns back to home menu
            canvas.delete('all')
            btEnter.pack()
            btTrack.pack()
            btInfo.pack()
            btTrackk.pack_forget()          
            canvas.create_text(400,120, text = 'Internet Usage Tracker', font = 'Times 24 bold', tags = 'title')
            canvas.create_text(400,180, text = 'Manage your addiction, with the IUT', font = 'Times 16 italic', tags = 'sub')
            canvas.create_rectangle(50,20,750,280, width = 10, outline = 'black')
            canvas.create_rectangle(100,40,700,260, width = 10, outline = 'red')
            canvas.create_rectangle(160,70,650,230, width = 10, outline = 'blue')

            btBackk.pack_forget()
            btExem.pack_forget()
                        
        #buttons for the entire track section
        btTrackk = Button(root,text = 'Track Usage', bd = 3, command = trackusg)
        btTrackk.pack()
        btExem = Button(root,text = 'Block Certain Apps', bd = 3, command = blockusg)
        btExem.pack()
        btBackk = Button(root,text = 'Go Back', bd = 3, command = gobackk)
        btBackk.pack()

        
        btAnother = Button(root,text = 'Another App?', bd = 3, command = another)
        btBackkk = Button(root,text = 'Back to Submenu', bd = 3, command = submenu)
        btSubmit = Button(root,text = 'Submit', bd = 3, command = submit)
        btEnterr = Button(root,text = 'Enter', bd = 3, command = enterr)
        btBlock = Button(root,text = 'Permanently Block', bd = 3, command = block)

    def info():
        #overall informational section            
        def gobackhome():
            #returns back to main menu
            btGoBack.pack_forget()
            btWebBrowser.pack_forget()
            btEnter.pack()
            btTrack.pack()
            btInfo.pack()
            canvas.delete('all')
            canvas.create_text(400,120, text = 'Internet Usage Tracker', font = 'Times 24 bold', tags = 'title')
            canvas.create_text(400,180, text = 'Manage your addiction, with the IUT', font = 'Times 16 italic', tags = 'sub')
            canvas.create_rectangle(50,20,750,280, width = 10, outline = 'black')
            canvas.create_rectangle(100,40,700,260, width = 10, outline = 'red')
            canvas.create_rectangle(160,70,650,230, width = 10, outline = 'blue')

        #further information if user is interested
        def furtherinfo():
            canvas.delete('all')
            btFurtherInfo.pack_forget()
            btGoBack.pack()

            canvas.create_rectangle(50,20,750,280, width = 10, outline = 'red')
            canvas.create_text(400,55, text = 'Further Info', font = 'Times 24 bold', fill = 'blue')
            
            canvas.create_text(400,100, text = 'For those addicted to the internet, dopamine is released', font = 'Times 14')
            canvas.create_text(400,120, text = 'every time they do something enjoyable online.', font = 'Times 14')

            canvas.create_text(400,160, text = 'Those with addictive personalities find themselves attracted to this dopamine,', font = 'Times 14')
            canvas.create_text(400,180, text = 'potentially causing them to ignore real issues in favor of mindless web browsing.', font = 'Times 14')

            canvas.create_text(400,220, text = 'This is a serious issue as it can ruin the school and work life of many.', font = 'Times 14')
            canvas.create_text(400,240, text = 'Organizations such as the National Institute of Mental Health fight hard to prevent this.', font = 'Times 14')
        
        #deletes all title text and creates informational text for the app in general
        canvas.delete('all')
        btFurtherInfo = Button(root,text = 'Further Info', bd = 3,  command = furtherinfo)
        btFurtherInfo.pack()
        btGoBack = Button(root,text = 'Go Back', bd = 3, command = gobackhome)
        btGoBack.pack()
        btEnter.pack_forget()
        btTrack.pack_forget()
        btInfo.pack_forget()
        canvas.create_rectangle(50,20,750,280, width = 10, outline = 'red')
        canvas.create_text(400,55, text = 'Internet Addiction Info', font = 'Times 24 bold', fill = 'blue')
        canvas.create_text(400,100, text = 'Internet Addiction is a condition referring to excessive use of the Internet', font = 'Times 14')
        canvas.create_text(400,120, text = 'to the point of interference in the daily life of an individual.', font = 'Times 14')

        canvas.create_text(400,170, text = 'The purpose of this app is to allow you to track how much you use certain aplications', font = 'Times 14')
        canvas.create_text(400,190, text = 'in order to allow you to more effectively track and manage any possible condition.', font = 'Times 14')

        canvas.create_text(400,240, text = 'Concept and Code Created by Rohun Baxi', font = 'Times 14')

    #main menu buttons  
    global btEnter
    global btTrack
    global btInfo
    btEnter = Button(root, text = 'Enter/Delete Usage',  bd = 3, command = enter)
    btEnter.pack()
    btTrack = Button(root, text = 'Track/Block Usage',  bd = 3, command = track)
    btTrack.pack()
    btInfo = Button(root,text = 'Internet Addiction Info', bd = 3, command = info)
    btInfo.pack()

#runs class and main loop
Summative()
root.mainloop()

