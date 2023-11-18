import customtkinter as ctk
from PIL import Image
import os.path
from semi_final import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


root = ctk.CTk()
root.geometry("1250x703")
root.title("Tornament Manager")

# frame for information text
frame_1 = ctk.CTkFrame(master= root, height= 80, width= 400)
frame_1.pack(pady= 20)
# information text
label_1 = ctk.CTkLabel(master= frame_1, text= "Please fill in the match outcomes for the final and third place game.",
                       font=('Arial',16,'bold'))
label_1.pack(padx= 10, pady= 10)

# frame were the matches will be shown
frame_2 = ctk.CTkFrame(master= root, fg_color='gray17')
frame_2.pack(pady=5, padx=20, fill="both", expand=True)

# image used for unkown teams
unknown = ctk.CTkImage(Image.open('Images/Unknown.png'), size= (45, 45))

goalF_var1=ctk.StringVar()
goalF_var2=ctk.StringVar()
goalF_var3=ctk.StringVar()
goalF_var4=ctk.StringVar()


# game 1
game_1 = ctk.CTkFrame(master= frame_2, fg_color='green', width= 1000, height= 60)
game_1.pack(padx= 20, pady= 5)
# vs
label_1 = ctk.CTkLabel(master= game_1, text= "vs",
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.49, rely= 0.35)
# team 1
label_1 = ctk.CTkLabel(master= game_1, text= F_teams[0],
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.2, rely= 0.35)
# team 2
label_1 = ctk.CTkLabel(master= game_1, text= F_teams[1],
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.72, rely= 0.35)

# image team 1
if os.path.exists('Images/'+F_teams[0]+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+F_teams[0]+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_1, image= img1, text= '')
    label_1.place(relx= 0.3, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_1, image= unknown, text= '')
    label_1.place(relx= 0.3, rely= 0.125)

# image team 2
if os.path.exists('Images/'+F_teams[1]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+F_teams[1]+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_1, image= img2, text= '')
    label_1.place(relx= 0.64, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_1, image= unknown, text= '')
    label_1.place(relx= 0.64, rely= 0.125)


# goal entries
entry1 = ctk.CTkEntry(master= game_1, width= 50, height= 40, textvariable= goalF_var1)
entry1.place(relx= 0.4, rely= 0.2)
entry1 = ctk.CTkEntry(master= game_1, width= 50, height= 40, textvariable= goalF_var2)
entry1.place(relx= 0.55, rely= 0.2)



# game 2
game_2 = ctk.CTkFrame(master= frame_2, fg_color='green', width= 1000, height= 60)
game_2.pack(padx= 20, pady= 5)
# vs
label_1 = ctk.CTkLabel(master= game_2, text= "vs",
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.49, rely= 0.35)
# team 1
label_1 = ctk.CTkLabel(master= game_2, text= TP_teams[0],
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.2, rely= 0.35)
# team 2
label_1 = ctk.CTkLabel(master= game_2, text= TP_teams[1],
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.72, rely= 0.35)

# image team 1
if os.path.exists('Images/'+TP_teams[0]+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+TP_teams[0]+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_2, image= img1, text= '')
    label_1.place(relx= 0.3, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_2, image= unknown, text= '')
    label_1.place(relx= 0.3, rely= 0.125)

# image team 2
if os.path.exists('Images/'+TP_teams[1]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+TP_teams[1]+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_2, image= img2, text= '')
    label_1.place(relx= 0.64, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_2, image= unknown, text= '')
    label_1.place(relx= 0.64, rely= 0.125)


# goal entries
entry1 = ctk.CTkEntry(master= game_2, width= 50, height= 40, textvariable= goalF_var3)
entry1.place(relx= 0.4, rely= 0.2)
entry1 = ctk.CTkEntry(master= game_2, width= 50, height= 40, textvariable= goalF_var4)
entry1.place(relx= 0.55, rely= 0.2)


######
# Submit Button
submit_1 = ctk.CTkButton(master = frame_2, height= 45, width= 100, text= "Submit", command= root.destroy)
submit_1.place(relx= 0.915, rely = 0.92)

root.mainloop()

F_goalst1 = []
F_goalst2 = []

count2 = 0
def play_match(team1, team2):
    global count2
    count2 = count2+1
    team1_score = int(F_goalst1[count2-1])
    team2_score = int(F_goalst2[count2-1])

    if team1_score > team2_score:
        return team1
    else:
        return team2



def create_goals_F():

    goalF_t1g1= int(goalF_var1.get())
    F_goalst1.append(goalF_t1g1)

    goalF_t2g1= int(goalF_var2.get())
    F_goalst2.append(goalF_t2g1)

    goalF_t1g2= int(goalF_var3.get())
    F_goalst1.append(goalF_t1g2)

    goalF_t2g2= int(goalF_var4.get())
    F_goalst2.append(goalF_t2g2)

create_goals_F()

# third place match
winner = play_match(TP_teams[0], TP_teams[1])


# final match and add winner to champ list
champ = []
def final():
    winner = play_match(F_teams[0], F_teams[1])
    champ.append(winner)
final()