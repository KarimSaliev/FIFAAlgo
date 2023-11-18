import customtkinter as ctk
from PIL import Image
import os.path
from FinalGUI import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


root = ctk.CTk()
root.geometry("1250x703")
root.title("Tornament Manager")

# frame for information text
frame_1 = ctk.CTkFrame(master= root, height= 80, width= 400)
frame_1.pack(pady= 20)
# information text
label_1 = ctk.CTkLabel(master= frame_1, text= "Tournament Tree",
                       font=('Arial',16,'bold'))
label_1.pack(padx= 10, pady= 10)

# frame were the matches will be shown
frame_2 = ctk.CTkFrame(master= root, fg_color='gray17')
frame_2.pack(pady=5, padx=20, fill="both", expand=True)

# image used for unkown teams
unknown = ctk.CTkImage(Image.open('Images/Unknown.png'), size= (30, 30))


# round of 16 left side
game_1 = ctk.CTkFrame(master= frame_2, fg_color='gray10', width= 150, height= 120)
game_1.place(relx = 0.02, rely= 0.01)
label = ctk.CTkLabel(master= game_1, width= 100, height= 29, anchor= 'w', text= Best_gA[0].country, font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.3)
label = ctk.CTkLabel(master= game_1, width= 100, height= 29, anchor= 'w', text= Best_gB[1].country, font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.77)
label = ctk.CTkLabel(master= game_1, width= 10, height= 29, anchor= 'w', text= r16_goalst1[0], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.1)
label = ctk.CTkLabel(master= game_1, width= 10, height= 29, anchor= 'w', text= r16_goalst2[0], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.6)
if os.path.exists('Images/'+Best_gA[0].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gA[0].country+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_1, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.03)
else:
    label_1 = ctk.CTkLabel(master= game_1, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.05)
if os.path.exists('Images/'+Best_gB[1].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gB[1].country+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_1, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.5)
else:
    label_1 = ctk.CTkLabel(master= game_1, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.52)


game_2 = ctk.CTkFrame(master= frame_2, fg_color='gray10', width= 150, height= 120)
game_2.place(relx = 0.02, rely= 0.26)
label = ctk.CTkLabel(master= game_2, width= 100, height= 29, anchor= 'w', text= Best_gC[0].country, font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.3)
label = ctk.CTkLabel(master= game_2, width= 100, height= 29, anchor= 'w', text= Best_gD[1].country, font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.77)
label = ctk.CTkLabel(master= game_2, width= 10, height= 29, anchor= 'w', text= r16_goalst1[1], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.1)
label = ctk.CTkLabel(master= game_2, width= 10, height= 29, anchor= 'w', text= r16_goalst2[1], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.6)
if os.path.exists('Images/'+Best_gC[0].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gC[0].country+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_2, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.03)
else:
    label_1 = ctk.CTkLabel(master= game_2, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.05)
if os.path.exists('Images/'+Best_gD[1].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gD[1].country+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_2, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.5)
else:
    label_1 = ctk.CTkLabel(master= game_2, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.52)


game_3 = ctk.CTkFrame(master= frame_2, fg_color='gray10', width= 150, height= 120)
game_3.place(relx = 0.02, rely= 0.51)
label = ctk.CTkLabel(master= game_3, width= 100, height= 29, anchor= 'w', text= Best_gE[0].country, font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.3)
label = ctk.CTkLabel(master= game_3, width= 100, height= 29, anchor= 'w', text= Best_gF[1].country, font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.77)
label = ctk.CTkLabel(master= game_3, width= 10, height= 29, anchor= 'w', text= r16_goalst1[2], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.1)
label = ctk.CTkLabel(master= game_3, width= 10, height= 29, anchor= 'w', text= r16_goalst2[2], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.6)
if os.path.exists('Images/'+Best_gE[0].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gE[0].country+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_3, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.03)
else:
    label_1 = ctk.CTkLabel(master= game_3, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.05)
if os.path.exists('Images/'+Best_gF[1].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gF[1].country+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_3, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.5)
else:
    label_1 = ctk.CTkLabel(master= game_3, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.52)


game_4 = ctk.CTkFrame(master= frame_2, fg_color='gray10', width= 150, height= 120)
game_4.place(relx = 0.02, rely= 0.76)
label = ctk.CTkLabel(master= game_4, width= 100, height= 29, anchor= 'w', text= Best_gG[0].country, font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.3)
label = ctk.CTkLabel(master= game_4, width= 100, height= 29, anchor= 'w', text= Best_gH[1].country, font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.77)
label = ctk.CTkLabel(master= game_4, width= 10, height= 29, anchor= 'w', text= r16_goalst1[3], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.1)
label = ctk.CTkLabel(master= game_4, width= 10, height= 29, anchor= 'w', text= r16_goalst2[3], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.6)
if os.path.exists('Images/'+Best_gG[0].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gG[0].country+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_4, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.03)
else:
    label_1 = ctk.CTkLabel(master= game_4, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.05)
if os.path.exists('Images/'+Best_gH[1].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gH[1].country+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_4, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.5)
else:
    label_1 = ctk.CTkLabel(master= game_4, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.52)


# round of 16 right side
game_5 = ctk.CTkFrame(master= frame_2, fg_color='gray10', width= 150, height= 120)
game_5.place(relx = 0.86, rely= 0.01)
label = ctk.CTkLabel(master= game_5, width= 100, height= 29, anchor= 'w', text= Best_gC[1].country, font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.3)
label = ctk.CTkLabel(master= game_5, width= 100, height= 29, anchor= 'w', text= Best_gD[0].country, font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.77)
label = ctk.CTkLabel(master= game_5, width= 10, height= 29, anchor= 'w', text= r16_goalst1[4], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.1)
label = ctk.CTkLabel(master= game_5, width= 10, height= 29, anchor= 'w', text= r16_goalst2[4], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.6)
if os.path.exists('Images/'+Best_gC[1].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gC[1].country+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_5, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.03)
else:
    label_1 = ctk.CTkLabel(master= game_5, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.05)
if os.path.exists('Images/'+Best_gD[0].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gD[0].country+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_5, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.5)
else:
    label_1 = ctk.CTkLabel(master= game_5, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.52)


game_6 = ctk.CTkFrame(master= frame_2, fg_color='gray10', width= 150, height= 120)
game_6.place(relx = 0.86, rely= 0.26)
label = ctk.CTkLabel(master= game_6, width= 100, height= 29, anchor= 'w', text= Best_gA[1].country, font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.3)
label = ctk.CTkLabel(master= game_6, width= 100, height= 29, anchor= 'w', text= Best_gB[0].country, font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.77)
label = ctk.CTkLabel(master= game_6, width= 10, height= 29, anchor= 'w', text= r16_goalst1[5], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.1)
label = ctk.CTkLabel(master= game_6, width= 10, height= 29, anchor= 'w', text= r16_goalst2[5], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.6)
if os.path.exists('Images/'+Best_gA[1].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gA[1].country+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_6, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.03)
else:
    label_1 = ctk.CTkLabel(master= game_6, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.05)
if os.path.exists('Images/'+Best_gB[0].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gB[0].country+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_6, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.5)
else:
    label_1 = ctk.CTkLabel(master= game_6, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.52)


game_7 = ctk.CTkFrame(master= frame_2, fg_color='gray10', width= 150, height= 120)
game_7.place(relx = 0.86, rely= 0.51)
label = ctk.CTkLabel(master= game_7, width= 100, height= 29, anchor= 'w', text= Best_gE[1].country, font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.3)
label = ctk.CTkLabel(master= game_7, width= 100, height= 29, anchor= 'w', text= Best_gF[0].country, font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.77)
label = ctk.CTkLabel(master= game_7, width= 10, height= 29, anchor= 'w', text= r16_goalst1[6], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.1)
label = ctk.CTkLabel(master= game_7, width= 10, height= 29, anchor= 'w', text= r16_goalst2[6], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.6)
if os.path.exists('Images/'+Best_gE[1].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gE[1].country+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_7, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.03)
else:
    label_1 = ctk.CTkLabel(master= game_7, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.05)
if os.path.exists('Images/'+Best_gF[0].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gF[0].country+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_7, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.5)
else:
    label_1 = ctk.CTkLabel(master= game_7, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.52)


game_8 = ctk.CTkFrame(master= frame_2, fg_color='gray10', width= 150, height= 120)
game_8.place(relx = 0.86, rely= 0.76)
label = ctk.CTkLabel(master= game_8, width= 100, height= 29, anchor= 'w', text= Best_gG[1].country, font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.3)
label = ctk.CTkLabel(master= game_8, width= 100, height= 29, anchor= 'w', text= Best_gH[0].country, font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.77)
label = ctk.CTkLabel(master= game_8, width= 10, height= 29, anchor= 'w', text= r16_goalst1[7], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.1)
label = ctk.CTkLabel(master= game_8, width= 10, height= 29, anchor= 'w', text= r16_goalst2[7], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.6)
if os.path.exists('Images/'+Best_gG[1].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gG[1].country+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_8, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.03)
else:
    label_1 = ctk.CTkLabel(master= game_8, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.05)
if os.path.exists('Images/'+Best_gH[0].country+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+Best_gH[0].country+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_8, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.5)
else:
    label_1 = ctk.CTkLabel(master= game_8, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.52)


# quater final left side
game_9 = ctk.CTkFrame(master= frame_2, fg_color='gray10', width= 150, height= 120)
game_9.place(relx = 0.16, rely= 0.26)
label = ctk.CTkLabel(master= game_9, width= 100, height= 29, anchor= 'w', text= QF_teams[0], font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.3)
label = ctk.CTkLabel(master= game_9, width= 100, height= 29, anchor= 'w', text= QF_teams[1], font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.77)
label = ctk.CTkLabel(master= game_9, width= 10, height= 29, anchor= 'w', text= QF_goalst1[0], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.1)
label = ctk.CTkLabel(master= game_9, width= 10, height= 29, anchor= 'w', text= QF_goalst2[0], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.6)
if os.path.exists('Images/'+QF_teams[0]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+QF_teams[0]+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_9, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.03)
else:
    label_1 = ctk.CTkLabel(master= game_9, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.05)
if os.path.exists('Images/'+QF_teams[1]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+QF_teams[1]+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_9, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.5)
else:
    label_1 = ctk.CTkLabel(master= game_9, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.52)


game_10 = ctk.CTkFrame(master= frame_2, fg_color='gray10', width= 150, height= 120)
game_10.place(relx = 0.16, rely= 0.51)
label = ctk.CTkLabel(master= game_10, width= 100, height= 29, anchor= 'w', text= QF_teams[2], font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.3)
label = ctk.CTkLabel(master= game_10, width= 100, height= 29, anchor= 'w', text= QF_teams[3], font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.77)
label = ctk.CTkLabel(master= game_10, width= 10, height= 29, anchor= 'w', text= QF_goalst1[1], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.1)
label = ctk.CTkLabel(master= game_10, width= 10, height= 29, anchor= 'w', text= QF_goalst2[1], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.6)
if os.path.exists('Images/'+QF_teams[2]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+QF_teams[2]+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_10, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.03)
else:
    label_1 = ctk.CTkLabel(master= game_10, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.05)
if os.path.exists('Images/'+QF_teams[3]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+QF_teams[3]+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_10, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.5)
else:
    label_1 = ctk.CTkLabel(master= game_10, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.52)


# quater final right side
game_11 = ctk.CTkFrame(master= frame_2, fg_color='gray10', width= 150, height= 120)
game_11.place(relx = 0.72, rely= 0.26)
label = ctk.CTkLabel(master= game_11, width= 100, height= 29, anchor= 'w', text= QF_teams[4], font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.3)
label = ctk.CTkLabel(master= game_11, width= 100, height= 29, anchor= 'w', text= QF_teams[5], font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.77)
label = ctk.CTkLabel(master= game_11, width= 10, height= 29, anchor= 'w', text= QF_goalst1[2], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.1)
label = ctk.CTkLabel(master= game_11, width= 10, height= 29, anchor= 'w', text= QF_goalst2[2], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.6)
if os.path.exists('Images/'+QF_teams[4]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+QF_teams[4]+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_11, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.03)
else:
    label_1 = ctk.CTkLabel(master= game_11, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.05)
if os.path.exists('Images/'+QF_teams[5]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+QF_teams[5]+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_11, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.5)
else:
    label_1 = ctk.CTkLabel(master= game_11, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.52)


game_12 = ctk.CTkFrame(master= frame_2, fg_color='gray10', width= 150, height= 120)
game_12.place(relx = 0.72, rely= 0.51)
label = ctk.CTkLabel(master= game_12, width= 100, height= 29, anchor= 'w', text= QF_teams[6], font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.3)
label = ctk.CTkLabel(master= game_12, width= 100, height= 29, anchor= 'w', text= QF_teams[7], font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.77)
label = ctk.CTkLabel(master= game_12, width= 10, height= 29, anchor= 'w', text= QF_goalst1[3], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.1)
label = ctk.CTkLabel(master= game_12, width= 10, height= 29, anchor= 'w', text= QF_goalst2[3], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.6)
if os.path.exists('Images/'+QF_teams[6]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+QF_teams[6]+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_12, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.03)
else:
    label_1 = ctk.CTkLabel(master= game_12, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.05)
if os.path.exists('Images/'+QF_teams[7]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+QF_teams[7]+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_12, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.5)
else:
    label_1 = ctk.CTkLabel(master= game_12, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.52)


# semi final left side
game_13 = ctk.CTkFrame(master= frame_2, fg_color='gray10', width= 150, height= 120)
game_13.place(relx = 0.30, rely= 0.38)
label = ctk.CTkLabel(master= game_13, width= 100, height= 29, anchor= 'w', text= SF_teams[0], font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.3)
label = ctk.CTkLabel(master= game_13, width= 100, height= 29, anchor= 'w', text= SF_teams[1], font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.77)
label = ctk.CTkLabel(master= game_13, width= 10, height= 29, anchor= 'w', text= SF_goalst1[0], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.1)
label = ctk.CTkLabel(master= game_13, width= 10, height= 29, anchor= 'w', text= SF_goalst2[0], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.6)
if os.path.exists('Images/'+SF_teams[0]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+SF_teams[0]+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_13, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.03)
else:
    label_1 = ctk.CTkLabel(master= game_13, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.05)
if os.path.exists('Images/'+SF_teams[1]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+SF_teams[1]+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_13, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.5)
else:
    label_1 = ctk.CTkLabel(master= game_13, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.52)


# semi final right side
game_14 = ctk.CTkFrame(master= frame_2, fg_color='gray10', width= 150, height= 120)
game_14.place(relx = 0.58, rely= 0.38)
label = ctk.CTkLabel(master= game_14, width= 100, height= 29, anchor= 'w', text= SF_teams[2], font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.3)
label = ctk.CTkLabel(master= game_14, width= 100, height= 29, anchor= 'w', text= SF_teams[3], font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.77)
label = ctk.CTkLabel(master= game_14, width= 10, height= 29, anchor= 'w', text= SF_goalst1[1], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.1)
label = ctk.CTkLabel(master= game_14, width= 10, height= 29, anchor= 'w', text= SF_goalst2[1], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.6)
if os.path.exists('Images/'+SF_teams[2]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+SF_teams[2]+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_14, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.03)
else:
    label_1 = ctk.CTkLabel(master= game_14, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.05)
if os.path.exists('Images/'+SF_teams[3]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+SF_teams[3]+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_14, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.5)
else:
    label_1 = ctk.CTkLabel(master= game_14, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.52)


# final
game_15 = ctk.CTkFrame(master= frame_2, fg_color='gray10', width= 150, height= 120)
game_15.place(relx = 0.44, rely= 0.38)
label = ctk.CTkLabel(master= game_15, width= 100, height= 29, anchor= 'w', text= F_teams[0], font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.3)
label = ctk.CTkLabel(master= game_15, width= 100, height= 29, anchor= 'w', text= F_teams[1], font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.77)
label = ctk.CTkLabel(master= game_15, width= 10, height= 29, anchor= 'w', text= F_goalst1[0], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.1)
label = ctk.CTkLabel(master= game_15, width= 10, height= 29, anchor= 'w', text= F_goalst2[0], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.6)
if os.path.exists('Images/'+F_teams[0]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+F_teams[0]+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_15, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.03)
else:
    label_1 = ctk.CTkLabel(master= game_15, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.05)
if os.path.exists('Images/'+F_teams[1]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+F_teams[1]+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_15, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.5)
else:
    label_1 = ctk.CTkLabel(master= game_15, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.52)


# third place
game_17 = ctk.CTkFrame(master= frame_2, fg_color='gray10', width= 150, height= 120)
game_17.place(relx = 0.44, rely= 0.7)
label = ctk.CTkLabel(master= game_17, width= 100, height= 29, anchor= 'w', text= TP_teams[0], font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.3)
label = ctk.CTkLabel(master= game_17, width= 100, height= 29, anchor= 'w', text= TP_teams[1], font=('Arial',16,'bold'))
label.place(relx= 0.05, rely= 0.77)
label = ctk.CTkLabel(master= game_17, width= 10, height= 29, anchor= 'w', text= F_goalst1[1], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.1)
label = ctk.CTkLabel(master= game_17, width= 10, height= 29, anchor= 'w', text= F_goalst2[1], font=('Arial',20,'bold'))
label.place(relx= 0.9, rely= 0.6)
if os.path.exists('Images/'+TP_teams[0]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+TP_teams[0]+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_17, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.03)
else:
    label_1 = ctk.CTkLabel(master= game_17, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.05)
if os.path.exists('Images/'+TP_teams[1]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+TP_teams[1]+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_17, image= img2, text= '')
    label_1.place(relx= 0.05, rely= 0.5)
else:
    label_1 = ctk.CTkLabel(master= game_17, image= unknown, text= '')
    label_1.place(relx= 0.07, rely= 0.52)


# show tournament winner
game_16 = ctk.CTkFrame(master= frame_2, fg_color='gray10', width= 150, height= 120)
game_16.place(relx = 0.44, rely= 0.07)
label = ctk.CTkLabel(master= game_16, width= 150, height= 29, text= 'Tournament \n Winner', font=('Arial',16,'bold'))
label.place(relx= 0, rely= 0.01)
label = ctk.CTkLabel(master= game_16, width= 150, height= 29, text= champ[0], font=('Arial',18,'bold'))
label.place(relx= 0, rely= 0.62)
if os.path.exists('Images/'+champ[0]+'.png'):
    img2 = ctk.CTkImage(Image.open('Images/'+champ[0]+'.png'), size= (35, 35))
    label_1 = ctk.CTkLabel(master= game_16, image= img2, text= '')
    label_1.place(relx= 0.40, rely= 0.35)
else:
    label_1 = ctk.CTkLabel(master= game_16, image= unknown, text= '')
    label_1.place(relx= 0.42, rely= 0.37)


root.mainloop()