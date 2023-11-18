import customtkinter as ctk
from PIL import Image
import os.path
from group_table import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


root = ctk.CTk()
root.geometry("1250x703")
root.title("Tornament Manager")

# frame for information text
frame_1 = ctk.CTkFrame(master= root, height= 80, width= 400)
frame_1.pack(pady= 20)
# information text
label_1 = ctk.CTkLabel(master= frame_1, text= "Please fill in the match outcomes for the round of 16.",
                       font=('Arial',16,'bold'))
label_1.pack(padx= 10, pady= 10)

# frame were the matches will be shown
frame_2 = ctk.CTkFrame(master= root, fg_color='gray17')
frame_2.pack(pady=5, padx=20, fill="both", expand=True)

# image used for unkown teams
unknown = ctk.CTkImage(Image.open('Images/Unknown.png'), size= (45, 45))

# Team names for round of 16
Best_gA = best_teams['A']
Best_gB = best_teams['B']
Best_gC = best_teams['C']
Best_gD = best_teams['D']
Best_gE = best_teams['E']
Best_gF = best_teams['F']
Best_gG = best_teams['G']
Best_gH = best_teams['H']


goalr16_var1=ctk.StringVar()
goalr16_var2=ctk.StringVar()
goalr16_var3=ctk.StringVar()
goalr16_var4=ctk.StringVar()
goalr16_var5=ctk.StringVar()
goalr16_var6=ctk.StringVar()
goalr16_var7=ctk.StringVar()
goalr16_var8=ctk.StringVar()
goalr16_var9=ctk.StringVar()
goalr16_var10=ctk.StringVar()
goalr16_var11=ctk.StringVar()
goalr16_var12=ctk.StringVar()
goalr16_var13=ctk.StringVar()
goalr16_var14=ctk.StringVar()
goalr16_var15=ctk.StringVar()
goalr16_var16=ctk.StringVar()

# game 1
game_1 = ctk.CTkFrame(master= frame_2, fg_color='green', width= 1000, height= 60)
game_1.pack(padx= 20, pady= 5)
# vs
label_1 = ctk.CTkLabel(master= game_1, text= "vs",
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.49, rely= 0.35)
# team 1
label_1 = ctk.CTkLabel(master= game_1, text= Best_gA[0].country,
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.2, rely= 0.35)
# team 2
label_1 = ctk.CTkLabel(master= game_1, text= Best_gB[1].country,
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.72, rely= 0.35)

# image team 1
if os.path.exists('Images/'+Best_gA[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gA[0].country+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_1, image= img1, text= '')
    label_1.place(relx= 0.3, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_1, image= unknown, text= '')
    label_1.place(relx= 0.3, rely= 0.125)

# image team 2
if os.path.exists('Images/'+Best_gB[1].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gB[1].country+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_1, image= img2, text= '')
    label_1.place(relx= 0.64, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_1, image= unknown, text= '')
    label_1.place(relx= 0.64, rely= 0.125)


# goal entries
entry1 = ctk.CTkEntry(master= game_1, width= 50, height= 40, textvariable= goalr16_var1)
entry1.place(relx= 0.4, rely= 0.2)
entry1 = ctk.CTkEntry(master= game_1, width= 50, height= 40, textvariable= goalr16_var2)
entry1.place(relx= 0.55, rely= 0.2)



# game 2
game_2 = ctk.CTkFrame(master= frame_2, fg_color='green', width= 1000, height= 60)
game_2.pack(padx= 20, pady= 5)
# vs
label_1 = ctk.CTkLabel(master= game_2, text= "vs",
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.49, rely= 0.35)
# team 1
label_1 = ctk.CTkLabel(master= game_2, text= Best_gC[0].country,
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.2, rely= 0.35)
# team 2
label_1 = ctk.CTkLabel(master= game_2, text= Best_gD[1].country,
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.72, rely= 0.35)

# image team 1
if os.path.exists('Images/'+Best_gC[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gC[0].country+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_2, image= img1, text= '')
    label_1.place(relx= 0.3, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_2, image= unknown, text= '')
    label_1.place(relx= 0.3, rely= 0.125)

# image team 2
if os.path.exists('Images/'+Best_gD[1].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gD[1].country+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_2, image= img2, text= '')
    label_1.place(relx= 0.64, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_2, image= unknown, text= '')
    label_1.place(relx= 0.64, rely= 0.125)


# goal entries
entry1 = ctk.CTkEntry(master= game_2, width= 50, height= 40, textvariable= goalr16_var3)
entry1.place(relx= 0.4, rely= 0.2)
entry1 = ctk.CTkEntry(master= game_2, width= 50, height= 40, textvariable= goalr16_var4)
entry1.place(relx= 0.55, rely= 0.2)

# game 3
game_3 = ctk.CTkFrame(master= frame_2, fg_color='green', width= 1000, height= 60)
game_3.pack(padx= 20, pady= 5)
# vs
label_1 = ctk.CTkLabel(master= game_3, text= "vs",
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.49, rely= 0.35)
# team 1
label_1 = ctk.CTkLabel(master= game_3, text= Best_gE[0].country,
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.2, rely= 0.35)
# team 2
label_1 = ctk.CTkLabel(master= game_3, text= Best_gF[1].country,
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.72, rely= 0.35)

# image team 1
if os.path.exists('Images/'+Best_gE[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gE[0].country+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_3, image= img1, text= '')
    label_1.place(relx= 0.3, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_3, image= unknown, text= '')
    label_1.place(relx= 0.3, rely= 0.125)

# image team 2
if os.path.exists('Images/'+Best_gF[1].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gF[1].country+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_3, image= img2, text= '')
    label_1.place(relx= 0.64, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_3, image= unknown, text= '')
    label_1.place(relx= 0.64, rely= 0.125)


# goal entries
entry1 = ctk.CTkEntry(master= game_3, width= 50, height= 40, textvariable= goalr16_var5)
entry1.place(relx= 0.4, rely= 0.2)
entry1 = ctk.CTkEntry(master= game_3, width= 50, height= 40, textvariable= goalr16_var6)
entry1.place(relx= 0.55, rely= 0.2)

# game 4
game_4 = ctk.CTkFrame(master= frame_2, fg_color='green', width= 1000, height= 60)
game_4.pack(padx= 20, pady= 5)
# vs
label_1 = ctk.CTkLabel(master= game_4, text= "vs",
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.49, rely= 0.35)
# team 1
label_1 = ctk.CTkLabel(master= game_4, text= Best_gG[0].country,
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.2, rely= 0.35)
# team 2
label_1 = ctk.CTkLabel(master= game_4, text= Best_gH[1].country,
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.72, rely= 0.35)

# image team 1
if os.path.exists('Images/'+Best_gG[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gG[0].country+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_4, image= img1, text= '')
    label_1.place(relx= 0.3, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_4, image= unknown, text= '')
    label_1.place(relx= 0.3, rely= 0.125)

# image team 2
if os.path.exists('Images/'+Best_gH[1].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gH[1].country+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_4, image= img2, text= '')
    label_1.place(relx= 0.64, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_4, image= unknown, text= '')
    label_1.place(relx= 0.64, rely= 0.125)


# goal entries
entry1 = ctk.CTkEntry(master= game_4, width= 50, height= 40, textvariable= goalr16_var7)
entry1.place(relx= 0.4, rely= 0.2)
entry1 = ctk.CTkEntry(master= game_4, width= 50, height= 40, textvariable= goalr16_var8)
entry1.place(relx= 0.55, rely= 0.2)

# game 5
game_5 = ctk.CTkFrame(master= frame_2, fg_color='green', width= 1000, height= 60)
game_5.pack(padx= 20, pady= 5)
# vs
label_1 = ctk.CTkLabel(master= game_5, text= "vs",
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.49, rely= 0.35)
# team 1
label_1 = ctk.CTkLabel(master= game_5, text= Best_gC[1].country,
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.2, rely= 0.35)
# team 2
label_1 = ctk.CTkLabel(master= game_5, text= Best_gD[0].country,
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.72, rely= 0.35)

# image team 1
if os.path.exists('Images/'+Best_gC[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gC[1].country+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_5, image= img1, text= '')
    label_1.place(relx= 0.3, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_5, image= unknown, text= '')
    label_1.place(relx= 0.3, rely= 0.125)

# image team 2
if os.path.exists('Images/'+Best_gD[0].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gD[0].country+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_5, image= img2, text= '')
    label_1.place(relx= 0.64, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_5, image= unknown, text= '')
    label_1.place(relx= 0.64, rely= 0.125)


# goal entries
entry1 = ctk.CTkEntry(master= game_5, width= 50, height= 40, textvariable= goalr16_var9)
entry1.place(relx= 0.4, rely= 0.2)
entry1 = ctk.CTkEntry(master= game_5, width= 50, height= 40, textvariable= goalr16_var10)
entry1.place(relx= 0.55, rely= 0.2)

# game 6
game_6 = ctk.CTkFrame(master= frame_2, fg_color='green', width= 1000, height= 60)
game_6.pack(padx= 20, pady= 5)
# vs
label_1 = ctk.CTkLabel(master= game_6, text= "vs",
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.49, rely= 0.35)
# team 1
label_1 = ctk.CTkLabel(master= game_6, text= Best_gA[1].country,
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.2, rely= 0.35)
# team 2
label_1 = ctk.CTkLabel(master= game_6, text= Best_gB[0].country,
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.72, rely= 0.35)

# image team 1
if os.path.exists('Images/'+Best_gA[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gA[1].country+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_6, image= img1, text= '')
    label_1.place(relx= 0.3, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_6, image= unknown, text= '')
    label_1.place(relx= 0.3, rely= 0.125)

# image team 2
if os.path.exists('Images/'+Best_gB[0].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gB[0].country+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_6, image= img2, text= '')
    label_1.place(relx= 0.64, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_6, image= unknown, text= '')
    label_1.place(relx= 0.64, rely= 0.125)


# goal entries
entry1 = ctk.CTkEntry(master= game_6, width= 50, height= 40, textvariable= goalr16_var11)
entry1.place(relx= 0.4, rely= 0.2)
entry1 = ctk.CTkEntry(master= game_6, width= 50, height= 40, textvariable= goalr16_var12)
entry1.place(relx= 0.55, rely= 0.2)

# game 7
game_7 = ctk.CTkFrame(master= frame_2, fg_color='green', width= 1000, height= 60)
game_7.pack(padx= 20, pady= 5)
# vs
label_1 = ctk.CTkLabel(master= game_7, text= "vs",
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.49, rely= 0.35)
# team 1
label_1 = ctk.CTkLabel(master= game_7, text= Best_gE[1].country,
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.2, rely= 0.35)
# team 2
label_1 = ctk.CTkLabel(master= game_7, text= Best_gF[0].country,
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.72, rely= 0.35)

# image team 1
if os.path.exists('Images/'+Best_gE[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gE[1].country+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_7, image= img1, text= '')
    label_1.place(relx= 0.3, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_7, image= unknown, text= '')
    label_1.place(relx= 0.3, rely= 0.125)

# image team 2
if os.path.exists('Images/'+Best_gF[0].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gF[0].country+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_7, image= img2, text= '')
    label_1.place(relx= 0.64, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_7, image= unknown, text= '')
    label_1.place(relx= 0.64, rely= 0.125)


# goal entries
entry1 = ctk.CTkEntry(master= game_7, width= 50, height= 40, textvariable= goalr16_var13)
entry1.place(relx= 0.4, rely= 0.2)
entry1 = ctk.CTkEntry(master= game_7, width= 50, height= 40, textvariable= goalr16_var14)
entry1.place(relx= 0.55, rely= 0.2)

# game 8
game_8 = ctk.CTkFrame(master= frame_2, fg_color='green', width= 1000, height= 60)
game_8.pack(padx= 20, pady= 5)
# vs
label_1 = ctk.CTkLabel(master= game_8, text= "vs",
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.49, rely= 0.35)
# team 1
label_1 = ctk.CTkLabel(master= game_8, text= Best_gG[1].country,
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.2, rely= 0.35)
# team 2
label_1 = ctk.CTkLabel(master= game_8, text= Best_gH[0].country,
                       font=('Arial',16,'bold'))
label_1.place(relx= 0.72, rely= 0.35)

# image team 1
if os.path.exists('Images/'+Best_gG[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gG[1].country+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_8, image= img1, text= '')
    label_1.place(relx= 0.3, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_8, image= unknown, text= '')
    label_1.place(relx= 0.3, rely= 0.125)

# image team 2
if os.path.exists('Images/'+Best_gH[0].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gH[0].country+'.png'), size= (52, 52))
    label_1 = ctk.CTkLabel(master= game_8, image= img2, text= '')
    label_1.place(relx= 0.64, rely= 0.08)
else:
    label_1 = ctk.CTkLabel(master= game_8, image= unknown, text= '')
    label_1.place(relx= 0.64, rely= 0.125)


# goal entries
entry1 = ctk.CTkEntry(master= game_8, width= 50, height= 40, textvariable= goalr16_var15)
entry1.place(relx= 0.4, rely= 0.2)
entry1 = ctk.CTkEntry(master= game_8, width= 50, height= 40, textvariable= goalr16_var16)
entry1.place(relx= 0.55, rely= 0.2)




#####
# Submit Button
submit_1 = ctk.CTkButton(master = frame_2, height= 45, width= 100, text= "Submit", command= root.destroy)
submit_1.place(relx= 0.915, rely = 0.92)

root.mainloop()

r16_goalst1 = []
r16_goalst2 = []

count2 = 0
def play_match(team1, team2):
    global count2
    count2 = count2+1
    team1_score = int(r16_goalst1[count2-1])
    team2_score = int(r16_goalst2[count2-1])

    if team1_score > team2_score:
        return team1
    else:
        return team2



def create_goals_r16():

    goalr16_t1g1= int(goalr16_var1.get())
    r16_goalst1.append(goalr16_t1g1)

    goalr16_t2g1= int(goalr16_var2.get())
    r16_goalst2.append(goalr16_t2g1)

    goalr16_t1g2= int(goalr16_var3.get())
    r16_goalst1.append(goalr16_t1g2)

    goalr16_t2g2= int(goalr16_var4.get())
    r16_goalst2.append(goalr16_t2g2)

    goalr16_t1g3= int(goalr16_var5.get())
    r16_goalst1.append(goalr16_t1g3)

    goalr16_t2g3= int(goalr16_var6.get())
    r16_goalst2.append(goalr16_t2g3)

    goalr16_t1g4= int(goalr16_var7.get())
    r16_goalst1.append(goalr16_t1g4)

    goalr16_t2g4= int(goalr16_var8.get())
    r16_goalst2.append(goalr16_t2g4)

    goalr16_t1g5= int(goalr16_var9.get())
    r16_goalst1.append(goalr16_t1g5)

    goalr16_t2g5= int(goalr16_var10.get())
    r16_goalst2.append(goalr16_t2g5)

    goalr16_t1g6= int(goalr16_var11.get())
    r16_goalst1.append(goalr16_t1g6)

    goalr16_t2g6= int(goalr16_var12.get())
    r16_goalst2.append(goalr16_t2g6)

    goalr16_t1g7= int(goalr16_var13.get())
    r16_goalst1.append(goalr16_t1g7)

    goalr16_t2g7= int(goalr16_var14.get())
    r16_goalst2.append(goalr16_t2g7)

    goalr16_t1g8= int(goalr16_var15.get())
    r16_goalst1.append(goalr16_t1g8)

    goalr16_t2g8= int(goalr16_var16.get())
    r16_goalst2.append(goalr16_t2g8)

create_goals_r16()

team1 = play_match(Best_gA[0].country, Best_gB[1].country)
team2 = play_match(Best_gC[0].country, Best_gD[1].country)
team3 = play_match(Best_gE[0].country, Best_gF[1].country)
team4 = play_match(Best_gG[0].country, Best_gH[1].country)
team5 = play_match(Best_gC[1].country, Best_gD[0].country)
team6 = play_match(Best_gA[1].country, Best_gB[0].country)
team7 = play_match(Best_gE[1].country, Best_gF[0].country)
team8 = play_match(Best_gG[1].country, Best_gH[0].country)

QF_teams = [team1, team2, team3, team4, team5, team6, team7, team8]