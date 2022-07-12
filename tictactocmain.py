from tkinter import *
from tkinter import messagebox
import tictactoc as main


def multi():
    multiWindow=Toplevel(window)
    multiWindow.geometry('298x392')
    multiWindow.title("Tic Tac Toe MultiPlayer")

    player1L=Label(multiWindow, text=" Player1:",font="궁서체 12 bold")
    player2L=Label(multiWindow, text=" Player2:",font="궁서체 12 bold")
    player1L.grid(row=0, column=0)
    player2L.grid(row=1, column=0)
    player1E=Entry(multiWindow)
    player2E=Entry(multiWindow)
    player1E.grid(row=0, column=1, columnspan=2)
    player2E.grid(row=1, column=1, columnspan=2)

    button_list=[
        [' ',0], [' ',1], [' ',2] ,
        [' ',3], [' ',4], [' ',5],
        [' ',6], [' ',7], [' ',8]] 
    count=[0]
    player=[1]
    winner=[0]
    
    row_index=2
    col_index=0

    def process2(i):
        if button_list[i][0]!= " ":
            messagebox.showinfo('Tic-Tac-Toe','Button already Clicked!')
    
    for button_text in button_list:
        def process(t=button_text):
            
            if(t[0]==' ' ):
                main.click(button_list, player, t[1])

                Button(multiWindow, text=t[0], width=13, height=7, bg="gray",command=lambda k=t[1]: process2(k)).grid(row=t[1]//3+2, column=t[1]%3)

                count[0]+=1

                #check winner
                main.checkwinner(button_list, player, winner)

                if winner[0]!=0: #성공
                    playerlist=[]
                    playerlist.append(player1E.get())
                    playerlist.append(player2E.get())
                    messagebox.showinfo('Tic-Tac-Toe',"%s Wins"%playerlist[winner[0]-1])

                if(count[0]>8 and winner[0]==0):
                    messagebox.showinfo('Tic-Tac-Toe','Draw!')#성공
            else:
                messagebox.showinfo('Tic-Tac-Toe','Button already Clicked!')
    
        Button(multiWindow, text=button_text[0], width=13, height=7, bg="gray", command=process).grid(row=row_index, column=col_index)
        col_index +=1
        if(col_index>2):
            row_index+=1
            col_index=0
        
   

def single():
    singleWindow=Toplevel(window)
    singleWindow.geometry('298x370')
    singleWindow.title("Tic Tac SinglePlayer")

    player1L=Label(singleWindow, text=" Player1:",font="궁서체 12 bold")
    player1L.grid(row=0, column=0)
    player1E=Entry(singleWindow)
    player1E.grid(row=0, column=1, columnspan=2)

    button_list=[
        [' ',0], [' ',1], [' ',2] ,
        [' ',3], [' ',4], [' ',5],
        [' ',6], [' ',7], [' ',8]] 
    count=[0]
    player=[1]
    winner=[0]
    
    row_index=2
    col_index=0

    def process2(i):
        if button_list[i][0]!= " ":
            messagebox.showinfo('Tic-Tac-Toe','Button already Clicked!')
    
    for button_text in button_list:
        def process(t=button_text):
            
            if(t[0]==' ' ):
                main.click(button_list, player, t[1])

                Button(singleWindow, text=t[0], width=13, height=7, bg="gray",command=lambda k=t[1]: process2(k)).grid(row=t[1]//3+2, column=t[1]%3)

                count[0]+=1

                #check winner
                main.checkwinner(button_list, player, winner)

                if winner[0]!=0: #성공
                    messagebox.showinfo('Tic-Tac-Toe',"You Wins")

                if(count[0]>8 and winner[0]==0):
                    messagebox.showinfo('Tic-Tac-Toe','Draw!')#성공
                
            #컴퓨터가 플레이 
                if(count[0]<8 and winner[0]==0):
                    computerNumber=main.computer(button_list)
                    main.click(button_list, player, computerNumber)
                    Button(singleWindow, text=button_list[computerNumber][0], width=13, height=7, bg="gray",command=lambda k=computerNumber: process2(k)).grid(row=computerNumber//3+2, column=computerNumber%3)
                    count[0]+=1
                    main.checkwinner(button_list, player, winner)
                    if winner[0]!=0: #성공
                        messagebox.showinfo('Tic-Tac-Toe',"Computer Wins")
                    
            else:
                messagebox.showinfo('Tic-Tac-Toe','Button already Clicked!')
    
        Button(singleWindow, text=button_text[0], width=13, height=7, bg="gray", command=process).grid(row=row_index, column=col_index)
        col_index +=1
        if(col_index>2):
            row_index+=1
            col_index=0

   

def startFrame():
    window.title("Tic Tac Toe")
    window.geometry('300x400')
    head=Label(window, bg="gray", width=42, height=4)
    head.grid(row=0, column=0)
    mL=Label(window, text="Click above button to multiplay",fg="blue")
    mB=Button(window, text="   Multi Player   ", fg="blue", bg="lightblue", comman=multi)
    sB=Button(window, text="   Single Player  ", fg="blue",bg="lightblue", comman=single)
    sL=Label(window, text="Click above button to singleplay",fg="blue")
    mB.place(x=100, y=120)
    mL.place(x=60, y=150)
    sB.place(x=100, y=180)
    sL.place(x=60, y=210)
    

window=Tk()
startFrame()
window.mainloop()
