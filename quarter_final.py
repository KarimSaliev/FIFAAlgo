import customtkinter as ctk
from PIL import Image
import os.path
from round_of_16 import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


root = ctk.CTk()
root.geometry("1250x703")
root.title("Tornament Manager")

# frame for information text
frame_1 = ctk.CTkFrame(master= root, height= 80, width= 400)
frame_1.pack(pady= 20)
# information text
label_1 = ctk.CTkLabel(master= frame_1, text= "Please fill in the match outcomes for the quarter finals.",
                       font=('Arial',16,'bold'))
label_1.pack(padx= 10, pady= 10)

# frame were the matches will be shown
frame_2 = ctk.CTkFrame(master= root, fg_color='gray17')
frame_2.pack(pady=5, padx=20, fill="both", expand=True)

# image used for unkown teams
unknown = ctk.CTkImage(Image.open('Images/Unknown.png'), size= (45, 45))

goalQF_var1=ctk.StringVar()
goalQF_var2=ctk.StringVar()
goalQF_var3=ctk.StringVar()
goalQF_var4=ctk.StringVar()
goalQF_var5=ctk.StringVar()
goalQF_var6=ctk.StringVar()
goalQF_var7=ctk.StringVar()
goalQF_var8=ctk.StringVar()

# game 1
game_1 = ctk.CTkFrame(master= frame_2, fg_color='green', width= 1000, height= 60)
game_1.pack(padx= 20, pady= 5)
# vs
label_1 = ctk.CTkLabel(master= game_1, text= "vs",
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.49, rely= 0.35)
# team 1
label_1 = ctk.CTkLabel(master= game_1, text= QF_teams[0],
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.2, rely= 0.35)
# team 2
label_1 = ctk.CTkLabel(master= game_1, text= QF_teams[1],
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.72, rely= 0.35)

# image team 1
if os.path.exists('Images/'+QF_teams[0]+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+QF_teams[0]+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_1, image= img1, text= '')
    label_1.place(relx= 0.3, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_1, image= unknown, text= '')
    label_1.place(relx= 0.3, rely= 0.125)

# image team 2
if os.path.exists('Images/'+QF_teams[1]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+QF_teams[1]+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_1, image= img2, text= '')
    label_1.place(relx= 0.64, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_1, image= unknown, text= '')
    label_1.place(relx= 0.64, rely= 0.125)


# goal entries
entry1 = ctk.CTkEntry(master= game_1, width= 50, height= 40, textvariable= goalQF_var1)
entry1.place(relx= 0.4, rely= 0.2)
entry1 = ctk.CTkEntry(master= game_1, width= 50, height= 40, textvariable= goalQF_var2)
entry1.place(relx= 0.55, rely= 0.2)



# game 2
game_2 = ctk.CTkFrame(master= frame_2, fg_color='green', width= 1000, height= 60)
game_2.pack(padx= 20, pady= 5)
# vs
label_1 = ctk.CTkLabel(master= game_2, text= "vs",
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.49, rely= 0.35)
# team 1
label_1 = ctk.CTkLabel(master= game_2, text= QF_teams[2],
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.2, rely= 0.35)
# team 2
label_1 = ctk.CTkLabel(master= game_2, text= QF_teams[3],
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.72, rely= 0.35)

# image team 1
if os.path.exists('Images/'+QF_teams[2]+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+QF_teams[2]+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_2, image= img1, text= '')
    label_1.place(relx= 0.3, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_2, image= unknown, text= '')
    label_1.place(relx= 0.3, rely= 0.125)

# image team 2
if os.path.exists('Images/'+QF_teams[3]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+QF_teams[3]+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_2, image= img2, text= '')
    label_1.place(relx= 0.64, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_2, image= unknown, text= '')
    label_1.place(relx= 0.64, rely= 0.125)


# goal entries
entry1 = ctk.CTkEntry(master= game_2, width= 50, height= 40, textvariable= goalQF_var3)
entry1.place(relx= 0.4, rely= 0.2)
entry1 = ctk.CTkEntry(master= game_2, width= 50, height= 40, textvariable= goalQF_var4)
entry1.place(relx= 0.55, rely= 0.2)

# game 3
game_3 = ctk.CTkFrame(master= frame_2, fg_color='green', width= 1000, height= 60)
game_3.pack(padx= 20, pady= 5)
# vs
label_1 = ctk.CTkLabel(master= game_3, text= "vs",
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.49, rely= 0.35)
# team 1
label_1 = ctk.CTkLabel(master= game_3, text= QF_teams[4],
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.2, rely= 0.35)
# team 2
label_1 = ctk.CTkLabel(master= game_3, text= QF_teams[5],
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.72, rely= 0.35)

# image team 1
if os.path.exists('Images/'+QF_teams[4]+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+QF_teams[4]+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_3, image= img1, text= '')
    label_1.place(relx= 0.3, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_3, image= unknown, text= '')
    label_1.place(relx= 0.3, rely= 0.125)

# image team 2
if os.path.exists('Images/'+QF_teams[5]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+QF_teams[5]+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_3, image= img2, text= '')
    label_1.place(relx= 0.64, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_3, image= unknown, text= '')
    label_1.place(relx= 0.64, rely= 0.125)


# goal entries
entry1 = ctk.CTkEntry(master= game_3, width= 50, height= 40, textvariable= goalQF_var5)
entry1.place(relx= 0.4, rely= 0.2)
entry1 = ctk.CTkEntry(master= game_3, width= 50, height= 40, textvariable= goalQF_var6)
entry1.place(relx= 0.55, rely= 0.2)

# game 4
game_4 = ctk.CTkFrame(master= frame_2, fg_color='green', width= 1000, height= 60)
game_4.pack(padx= 20, pady= 5)
# vs
label_1 = ctk.CTkLabel(master= game_4, text= "vs",
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.49, rely= 0.35)
# team 1
label_1 = ctk.CTkLabel(master= game_4, text= QF_teams[6],
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.2, rely= 0.35)
# team 2
label_1 = ctk.CTkLabel(master= game_4, text= QF_teams[7],
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.72, rely= 0.35)

# image team 1
if os.path.exists('Images/'+QF_teams[6]+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+QF_teams[6]+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_4, image= img1, text= '')
    label_1.place(relx= 0.3, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_4, image= unknown, text= '')
    label_1.place(relx= 0.3, rely= 0.125)

# image team 2
if os.path.exists('Images/'+QF_teams[7]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+QF_teams[7]+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_4, image= img2, text= '')
    label_1.place(relx= 0.64, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_4, image= unknown, text= '')
    label_1.place(relx= 0.64, rely= 0.125)


# goal entries
entry1 = ctk.CTkEntry(master= game_4, width= 50, height= 40, textvariable= goalQF_var7)
entry1.place(relx= 0.4, rely= 0.2)
entry1 = ctk.CTkEntry(master= game_4, width= 50, height= 40, textvariable= goalQF_var8)
entry1.place(relx= 0.55, rely= 0.2)

######
# Submit Button
submit_1 = ctk.CTkButton(master = frame_2, height= 45, width= 100, text= "Submit", command= root.destroy)
submit_1.place(relx= 0.915, rely = 0.92)

root.mainloop()

QF_goalst1 = []
QF_goalst2 = []

count2 = 0
def play_match(team1, team2):
    global count2
    count2 = count2+1
    team1_score = int(QF_goalst1[count2-1])
    team2_score = int(QF_goalst2[count2-1])

    if team1_score > team2_score:
        return team1
    else:
        return team2



def create_goals_QF():

    goalQF_t1g1= int(goalQF_var1.get())
    QF_goalst1.append(goalQF_t1g1)

    goalQF_t2g1= int(goalQF_var2.get())
    QF_goalst2.append(goalQF_t2g1)

    goalQF_t1g2= int(goalQF_var3.get())
    QF_goalst1.append(goalQF_t1g2)

    goalQF_t2g2= int(goalQF_var4.get())
    QF_goalst2.append(goalQF_t2g2)

    goalQF_t1g3= int(goalQF_var5.get())
    QF_goalst1.append(goalQF_t1g3)

    goalQF_t2g3= int(goalQF_var6.get())
    QF_goalst2.append(goalQF_t2g3)

    goalQF_t1g4= int(goalQF_var7.get())
    QF_goalst1.append(goalQF_t1g4)

    goalQF_t2g4= int(goalQF_var8.get())
    QF_goalst2.append(goalQF_t2g4)

create_goals_QF()

# create list for the winner names
SF_teams = []
TP_teams = []
F_teams = []

# quarter final play matches
for i in range(0,len(QF_teams),2):
    team1 = QF_teams[i]
    team2 = QF_teams[i+1]
    winner = play_match(team1,team2)
    SF_teams.append(winner)
    TP_teams.append(winner)