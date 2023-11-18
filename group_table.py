import customtkinter as ctk
from group_matches import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("1250x703")
app.title("Tornament Manager")

frame_1 = ctk.CTkFrame(master= app, height= 80, width= 400)
frame_1.pack(pady= 20)

label_1 = ctk.CTkLabel(master= frame_1, text= "Group Table.",
                       font=('Arial',16,'bold'))
label_1.pack(padx= 10, pady= 10)


frame_2 = ctk.CTkFrame(master= app, fg_color='gray17')
frame_2.pack(pady=5, padx=20, fill="both", expand=True)

# image used for unkown teams
unknown = ctk.CTkImage(Image.open('Images/Unknown.png'), size= (16, 16))

############
# Group A


group_a = ctk.CTkFrame(master= frame_2, fg_color='green', width= 400, height= 120)
group_a.place(relx= 0.1, rely= 0.05)
label_a = ctk.CTkLabel(master= group_a, text= 'Group\nA', font=('Arial',16,'bold'))
label_a.place(relx= 0.06, rely= .3)

# collum head
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= 'Teams').place(relx= 0.28, rely= 0)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= 'G').place(relx= 0.54, rely= 0)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= 'W').place(relx= 0.59, rely= 0)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= 'D').place(relx= 0.64, rely= 0)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= 'L').place(relx= 0.69, rely= 0)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= 'GS').place(relx= 0.73, rely= 0)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= 'GR').place(relx= 0.78, rely= 0)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= 'GD').place(relx= 0.83, rely= 0)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= 'P').place(relx= 0.89, rely= 0)


# Entry 1
Best_gA = best_teams['A']
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Best_gA[0].country).place(relx= 0.28, rely= 0.2)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.2)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Best_gA[0].wins).place(relx= 0.59, rely= 0.2)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Best_gA[0].draws).place(relx= 0.64, rely= 0.2)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Best_gA[0].losses).place(relx= 0.69, rely= 0.2)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Best_gA[0].goals_for).place(relx= 0.74, rely= 0.2)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Best_gA[0].goals_against).place(relx= 0.79, rely= 0.2)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Best_gA[0].goals_diff).place(relx= 0.84, rely= 0.2)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Best_gA[0].points).place(relx= 0.89, rely= 0.2)
# image Team 1
if os.path.exists('Images/'+Best_gA[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gA[0].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_a, image= img1, text= '')
    label_1.place(relx= 0.222, rely= 0.2)
else:
    label_1 = ctk.CTkLabel(master= group_a, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.2)

# Entry 2
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Best_gA[1].country).place(relx= 0.28, rely= 0.4)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.4)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Best_gA[1].wins).place(relx= 0.59, rely= 0.4)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Best_gA[1].draws).place(relx= 0.64, rely= 0.4)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Best_gA[1].losses).place(relx= 0.69, rely= 0.4)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Best_gA[1].goals_for).place(relx= 0.74, rely= 0.4)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Best_gA[1].goals_against).place(relx= 0.79, rely= 0.4)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Best_gA[1].goals_diff).place(relx= 0.84, rely= 0.4)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Best_gA[1].points).place(relx= 0.89, rely= 0.4)
# image Team 2
if os.path.exists('Images/'+Best_gA[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gA[1].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_a, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.4)
else:
    label_1 = ctk.CTkLabel(master= group_a, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.4)

# Entry 3
Worst_gA = worst_teams['A']
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Worst_gA[0].country).place(relx= 0.28, rely= 0.6)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.6)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Worst_gA[0].wins).place(relx= 0.59, rely= 0.6)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Worst_gA[0].draws).place(relx= 0.64, rely= 0.6)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Worst_gA[0].losses).place(relx= 0.69, rely= 0.6)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Worst_gA[0].goals_for).place(relx= 0.74, rely= 0.6)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Worst_gA[0].goals_against).place(relx= 0.79, rely= 0.6)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Worst_gA[0].goals_diff).place(relx= 0.84, rely= 0.6)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Worst_gA[0].points).place(relx= 0.89, rely= 0.6)
# image Team 3
if os.path.exists('Images/'+Worst_gA[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Worst_gA[0].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_a, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.6)
else:
    label_1 = ctk.CTkLabel(master= group_a, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.6)

# Entry 4
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Worst_gA[1].country).place(relx= 0.28, rely= 0.8)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.8)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Worst_gA[1].wins).place(relx= 0.59, rely= 0.8)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Worst_gA[1].draws).place(relx= 0.64, rely= 0.8)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Worst_gA[1].losses).place(relx= 0.69, rely= 0.8)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Worst_gA[1].goals_for).place(relx= 0.74, rely= 0.8)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Worst_gA[1].goals_against).place(relx= 0.79, rely= 0.8)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Worst_gA[1].goals_diff).place(relx= 0.84, rely= 0.8)
entry = ctk.CTkLabel(master= group_a, width= 300, height= 29, anchor= 'w', text= Worst_gA[1].points).place(relx= 0.89, rely= 0.8)
# image Team 4
if os.path.exists('Images/'+Worst_gA[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Worst_gA[1].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_a, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.8)
else:
    label_1 = ctk.CTkLabel(master= group_a, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.8)

############
# Group B
group_b = ctk.CTkFrame(master= frame_2, fg_color='green', width= 400, height= 120)
group_b.place(relx= 0.58, rely= 0.05)
label_b = ctk.CTkLabel(master= group_b, text= 'Group\nB', font=('Arial',16,'bold'))
label_b.place(relx= 0.06, rely= .3)

# collum head
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= 'Teams').place(relx= 0.28, rely= 0)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= 'G').place(relx= 0.54, rely= 0)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= 'W').place(relx= 0.59, rely= 0)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= 'D').place(relx= 0.64, rely= 0)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= 'L').place(relx= 0.69, rely= 0)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= 'GS').place(relx= 0.73, rely= 0)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= 'GR').place(relx= 0.78, rely= 0)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= 'GD').place(relx= 0.83, rely= 0)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= 'P').place(relx= 0.89, rely= 0)

# Entry 1
Best_gB = best_teams['B']
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Best_gB[0].country).place(relx= 0.28, rely= 0.2)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.2)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Best_gB[0].wins).place(relx= 0.59, rely= 0.2)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Best_gB[0].draws).place(relx= 0.64, rely= 0.2)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Best_gB[0].losses).place(relx= 0.69, rely= 0.2)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Best_gB[0].goals_for).place(relx= 0.74, rely= 0.2)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Best_gB[0].goals_against).place(relx= 0.79, rely= 0.2)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Best_gB[0].goals_diff).place(relx= 0.84, rely= 0.2)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Best_gB[0].points).place(relx= 0.89, rely= 0.2)
# image Team 1
if os.path.exists('Images/'+Best_gB[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gB[0].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_b, image= img1, text= '')
    label_1.place(relx= 0.222, rely= 0.2)
else:
    label_1 = ctk.CTkLabel(master= group_b, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.2)

# Entry 2
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Best_gB[1].country).place(relx= 0.28, rely= 0.4)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.4)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Best_gB[1].wins).place(relx= 0.59, rely= 0.4)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Best_gB[1].draws).place(relx= 0.64, rely= 0.4)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Best_gB[1].losses).place(relx= 0.69, rely= 0.4)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Best_gB[1].goals_for).place(relx= 0.74, rely= 0.4)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Best_gB[1].goals_against).place(relx= 0.79, rely= 0.4)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Best_gB[1].goals_diff).place(relx= 0.84, rely= 0.4)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Best_gB[1].points).place(relx= 0.89, rely= 0.4)
# image Team 2
if os.path.exists('Images/'+Best_gB[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gB[1].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_b, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.4)
else:
    label_1 = ctk.CTkLabel(master= group_b, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.4)

# Entry 3
Worst_gB = worst_teams['B']
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Worst_gB[0].country).place(relx= 0.28, rely= 0.6)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.6)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Worst_gB[0].wins).place(relx= 0.59, rely= 0.6)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Worst_gB[0].draws).place(relx= 0.64, rely= 0.6)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Worst_gB[0].losses).place(relx= 0.69, rely= 0.6)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Worst_gB[0].goals_for).place(relx= 0.74, rely= 0.6)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Worst_gB[0].goals_against).place(relx= 0.79, rely= 0.6)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Worst_gB[0].goals_diff).place(relx= 0.84, rely= 0.6)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Worst_gB[0].points).place(relx= 0.89, rely= 0.6)
# image Team 3
if os.path.exists('Images/'+Worst_gB[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Worst_gB[0].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_b, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.6)
else:
    label_1 = ctk.CTkLabel(master= group_b, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.6)

# Entry 4
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Worst_gB[1].country).place(relx= 0.28, rely= 0.8)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.8)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Worst_gB[1].wins).place(relx= 0.59, rely= 0.8)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Worst_gB[1].draws).place(relx= 0.64, rely= 0.8)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Worst_gB[1].losses).place(relx= 0.69, rely= 0.8)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Worst_gB[1].goals_for).place(relx= 0.74, rely= 0.8)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Worst_gB[1].goals_against).place(relx= 0.79, rely= 0.8)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Worst_gB[1].goals_diff).place(relx= 0.84, rely= 0.8)
entry = ctk.CTkLabel(master= group_b, width= 300, height= 29, anchor= 'w', text= Worst_gB[1].points).place(relx= 0.89, rely= 0.8)
# image Team 4
if os.path.exists('Images/'+Worst_gB[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Worst_gB[1].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_b, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.8)
else:
    label_1 = ctk.CTkLabel(master= group_b, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.8)


############
# Group C
group_c = ctk.CTkFrame(master= frame_2, fg_color='green', width= 400, height= 120)
group_c.place(relx= 0.1, rely= 0.26)
label_c = ctk.CTkLabel(master= group_c, text= 'Group\nC', font=('Arial',16,'bold'))
label_c.place(relx= 0.06, rely= .3)

# collum head
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= 'Teams').place(relx= 0.28, rely= 0)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= 'G').place(relx= 0.54, rely= 0)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= 'W').place(relx= 0.59, rely= 0)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= 'D').place(relx= 0.64, rely= 0)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= 'L').place(relx= 0.69, rely= 0)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= 'GS').place(relx= 0.73, rely= 0)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= 'GR').place(relx= 0.78, rely= 0)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= 'GD').place(relx= 0.83, rely= 0)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= 'P').place(relx= 0.89, rely= 0)

# Entry 1
Best_gC = best_teams['C']
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Best_gC[0].country).place(relx= 0.28, rely= 0.2)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.2)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Best_gC[0].wins).place(relx= 0.59, rely= 0.2)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Best_gC[0].draws).place(relx= 0.64, rely= 0.2)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Best_gC[0].losses).place(relx= 0.69, rely= 0.2)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Best_gC[0].goals_for).place(relx= 0.74, rely= 0.2)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Best_gC[0].goals_against).place(relx= 0.79, rely= 0.2)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Best_gC[0].goals_diff).place(relx= 0.84, rely= 0.2)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Best_gC[0].points).place(relx= 0.89, rely= 0.2)
# image Team 1
if os.path.exists('Images/'+Best_gC[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gC[0].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_c, image= img1, text= '')
    label_1.place(relx= 0.222, rely= 0.2)
else:
    label_1 = ctk.CTkLabel(master= group_c, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.2)

# Entry 2
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Best_gC[1].country).place(relx= 0.28, rely= 0.4)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.4)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Best_gC[1].wins).place(relx= 0.59, rely= 0.4)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Best_gC[1].draws).place(relx= 0.64, rely= 0.4)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Best_gC[1].losses).place(relx= 0.69, rely= 0.4)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Best_gC[1].goals_for).place(relx= 0.74, rely= 0.4)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Best_gC[1].goals_against).place(relx= 0.79, rely= 0.4)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Best_gC[1].goals_diff).place(relx= 0.84, rely= 0.4)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Best_gC[1].points).place(relx= 0.89, rely= 0.4)
# image Team 2
if os.path.exists('Images/'+Best_gC[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gC[1].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_c, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.4)
else:
    label_1 = ctk.CTkLabel(master= group_c, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.4)

# Entry 3
Worst_gC = worst_teams['C']
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Worst_gC[0].country).place(relx= 0.28, rely= 0.6)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.6)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Worst_gC[0].wins).place(relx= 0.59, rely= 0.6)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Worst_gC[0].draws).place(relx= 0.64, rely= 0.6)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Worst_gC[0].losses).place(relx= 0.69, rely= 0.6)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Worst_gC[0].goals_for).place(relx= 0.74, rely= 0.6)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Worst_gC[0].goals_against).place(relx= 0.79, rely= 0.6)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Worst_gC[0].goals_diff).place(relx= 0.84, rely= 0.6)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Worst_gC[0].points).place(relx= 0.89, rely= 0.6)
# image Team 3
if os.path.exists('Images/'+Worst_gC[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Worst_gC[0].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_c, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.6)
else:
    label_1 = ctk.CTkLabel(master= group_c, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.6)

# Entry 4
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Worst_gC[1].country).place(relx= 0.28, rely= 0.8)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.8)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Worst_gC[1].wins).place(relx= 0.59, rely= 0.8)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Worst_gC[1].draws).place(relx= 0.64, rely= 0.8)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Worst_gC[1].losses).place(relx= 0.69, rely= 0.8)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Worst_gC[1].goals_for).place(relx= 0.74, rely= 0.8)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Worst_gC[1].goals_against).place(relx= 0.79, rely= 0.8)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Worst_gC[1].goals_diff).place(relx= 0.84, rely= 0.8)
entry = ctk.CTkLabel(master= group_c, width= 300, height= 29, anchor= 'w', text= Worst_gC[1].points).place(relx= 0.89, rely= 0.8)
# image Team 4
if os.path.exists('Images/'+Worst_gC[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Worst_gC[1].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_c, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.8)
else:
    label_1 = ctk.CTkLabel(master= group_c, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.8)


############
# Group D
group_d = ctk.CTkFrame(master= frame_2, fg_color='green', width= 400, height= 120)
group_d.place(relx= 0.58, rely= 0.26)
label_d = ctk.CTkLabel(master= group_d, text= 'Group\nD', font=('Arial',16,'bold'))
label_d.place(relx= 0.06, rely= .3)

# collum head
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= 'Teams').place(relx= 0.28, rely= 0)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= 'G').place(relx= 0.54, rely= 0)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= 'W').place(relx= 0.59, rely= 0)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= 'D').place(relx= 0.64, rely= 0)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= 'L').place(relx= 0.69, rely= 0)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= 'GS').place(relx= 0.73, rely= 0)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= 'GR').place(relx= 0.78, rely= 0)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= 'GD').place(relx= 0.83, rely= 0)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= 'P').place(relx= 0.89, rely= 0)

# Entry 1
Best_gD = best_teams['D']
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Best_gD[0].country).place(relx= 0.28, rely= 0.2)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.2)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Best_gD[0].wins).place(relx= 0.59, rely= 0.2)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Best_gD[0].draws).place(relx= 0.64, rely= 0.2)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Best_gD[0].losses).place(relx= 0.69, rely= 0.2)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Best_gD[0].goals_for).place(relx= 0.74, rely= 0.2)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Best_gD[0].goals_against).place(relx= 0.79, rely= 0.2)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Best_gD[0].goals_diff).place(relx= 0.84, rely= 0.2)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Best_gD[0].points).place(relx= 0.89, rely= 0.2)
# image Team 1
if os.path.exists('Images/'+Best_gD[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gD[0].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_d, image= img1, text= '')
    label_1.place(relx= 0.222, rely= 0.2)
else:
    label_1 = ctk.CTkLabel(master= group_d, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.2)

# Entry 2
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Best_gD[1].country).place(relx= 0.28, rely= 0.4)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.4)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Best_gD[1].wins).place(relx= 0.59, rely= 0.4)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Best_gD[1].draws).place(relx= 0.64, rely= 0.4)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Best_gD[1].losses).place(relx= 0.69, rely= 0.4)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Best_gD[1].goals_for).place(relx= 0.74, rely= 0.4)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Best_gD[1].goals_against).place(relx= 0.79, rely= 0.4)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Best_gD[1].goals_diff).place(relx= 0.84, rely= 0.4)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Best_gD[1].points).place(relx= 0.89, rely= 0.4)
# image Team 2
if os.path.exists('Images/'+Best_gD[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gD[1].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_d, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.4)
else:
    label_1 = ctk.CTkLabel(master= group_d, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.4)

# Entry 3
Worst_gD = worst_teams['D']
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Worst_gD[0].country).place(relx= 0.28, rely= 0.6)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.6)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Worst_gD[0].wins).place(relx= 0.59, rely= 0.6)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Worst_gD[0].draws).place(relx= 0.64, rely= 0.6)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Worst_gD[0].losses).place(relx= 0.69, rely= 0.6)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Worst_gD[0].goals_for).place(relx= 0.74, rely= 0.6)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Worst_gD[0].goals_against).place(relx= 0.79, rely= 0.6)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Worst_gD[0].goals_diff).place(relx= 0.84, rely= 0.6)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Worst_gD[0].points).place(relx= 0.89, rely= 0.6)
# image Team 3
if os.path.exists('Images/'+Worst_gD[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Worst_gD[0].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_d, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.6)
else:
    label_1 = ctk.CTkLabel(master= group_d, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.6)

# Entry 4
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Worst_gD[1].country).place(relx= 0.28, rely= 0.8)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.8)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Worst_gD[1].wins).place(relx= 0.59, rely= 0.8)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Worst_gD[1].draws).place(relx= 0.64, rely= 0.8)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Worst_gD[1].losses).place(relx= 0.69, rely= 0.8)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Worst_gD[1].goals_for).place(relx= 0.74, rely= 0.8)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Worst_gD[1].goals_against).place(relx= 0.79, rely= 0.8)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Worst_gD[1].goals_diff).place(relx= 0.84, rely= 0.8)
entry = ctk.CTkLabel(master= group_d, width= 300, height= 29, anchor= 'w', text= Worst_gD[1].points).place(relx= 0.89, rely= 0.8)
# image Team 4
if os.path.exists('Images/'+Worst_gD[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Worst_gD[1].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_d, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.8)
else:
    label_1 = ctk.CTkLabel(master= group_d, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.8)


############
# Group E
group_e = ctk.CTkFrame(master= frame_2, fg_color='green', width= 400, height= 120)
group_e.place(relx= 0.1, rely= 0.47)
label_e = ctk.CTkLabel(master= group_e, text= 'Group\nE', font=('Arial',16,'bold'))
label_e.place(relx= 0.06, rely= .3)

# collum head
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= 'Teams').place(relx= 0.28, rely= 0)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= 'G').place(relx= 0.54, rely= 0)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= 'W').place(relx= 0.59, rely= 0)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= 'D').place(relx= 0.64, rely= 0)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= 'L').place(relx= 0.69, rely= 0)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= 'GS').place(relx= 0.73, rely= 0)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= 'GR').place(relx= 0.78, rely= 0)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= 'GD').place(relx= 0.83, rely= 0)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= 'P').place(relx= 0.89, rely= 0)

# Entry 1
Best_gE = best_teams['E']
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Best_gE[0].country).place(relx= 0.28, rely= 0.2)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.2)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Best_gE[0].wins).place(relx= 0.59, rely= 0.2)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Best_gE[0].draws).place(relx= 0.64, rely= 0.2)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Best_gE[0].losses).place(relx= 0.69, rely= 0.2)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Best_gE[0].goals_for).place(relx= 0.74, rely= 0.2)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Best_gE[0].goals_against).place(relx= 0.79, rely= 0.2)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Best_gE[0].goals_diff).place(relx= 0.84, rely= 0.2)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Best_gE[0].points).place(relx= 0.89, rely= 0.2)
# image Team 1
if os.path.exists('Images/'+Best_gE[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gE[0].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_e, image= img1, text= '')
    label_1.place(relx= 0.222, rely= 0.2)
else:
    label_1 = ctk.CTkLabel(master= group_e, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.2)

# Entry 2
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Best_gE[1].country).place(relx= 0.28, rely= 0.4)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.4)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Best_gE[1].wins).place(relx= 0.59, rely= 0.4)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Best_gE[1].draws).place(relx= 0.64, rely= 0.4)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Best_gE[1].losses).place(relx= 0.69, rely= 0.4)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Best_gE[1].goals_for).place(relx= 0.74, rely= 0.4)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Best_gE[1].goals_against).place(relx= 0.79, rely= 0.4)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Best_gE[1].goals_diff).place(relx= 0.84, rely= 0.4)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Best_gE[1].points).place(relx= 0.89, rely= 0.4)
# image Team 2
if os.path.exists('Images/'+Best_gE[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gE[1].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_e, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.4)
else:
    label_1 = ctk.CTkLabel(master= group_e, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.4)

# Entry 3
Worst_gE = worst_teams['E']
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Worst_gE[0].country).place(relx= 0.28, rely= 0.6)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.6)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Worst_gE[0].wins).place(relx= 0.59, rely= 0.6)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Worst_gE[0].draws).place(relx= 0.64, rely= 0.6)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Worst_gE[0].losses).place(relx= 0.69, rely= 0.6)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Worst_gE[0].goals_for).place(relx= 0.74, rely= 0.6)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Worst_gE[0].goals_against).place(relx= 0.79, rely= 0.6)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Worst_gE[0].goals_diff).place(relx= 0.84, rely= 0.6)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Worst_gE[0].points).place(relx= 0.89, rely= 0.6)
# image Team 3
if os.path.exists('Images/'+Worst_gE[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Worst_gE[0].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_e, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.6)
else:
    label_1 = ctk.CTkLabel(master= group_e, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.6)

# Entry 4
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Worst_gE[1].country).place(relx= 0.28, rely= 0.8)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.8)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Worst_gE[1].wins).place(relx= 0.59, rely= 0.8)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Worst_gE[1].draws).place(relx= 0.64, rely= 0.8)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Worst_gE[1].losses).place(relx= 0.69, rely= 0.8)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Worst_gE[1].goals_for).place(relx= 0.74, rely= 0.8)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Worst_gE[1].goals_against).place(relx= 0.79, rely= 0.8)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Worst_gE[1].goals_diff).place(relx= 0.84, rely= 0.8)
entry = ctk.CTkLabel(master= group_e, width= 300, height= 29, anchor= 'w', text= Worst_gE[1].points).place(relx= 0.89, rely= 0.8)
# image Team 4
if os.path.exists('Images/'+Worst_gE[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Worst_gE[1].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_e, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.8)
else:
    label_1 = ctk.CTkLabel(master= group_e, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.8)


############
# Group F
group_f = ctk.CTkFrame(master= frame_2, fg_color='green', width= 400, height= 120)
group_f.place(relx= 0.58, rely= 0.47)
label_f = ctk.CTkLabel(master= group_f, text= 'Group\nF', font=('Arial',16,'bold'))
label_f.place(relx= 0.06, rely= .3)

# collum head
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= 'Teams').place(relx= 0.28, rely= 0)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= 'G').place(relx= 0.54, rely= 0)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= 'W').place(relx= 0.59, rely= 0)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= 'D').place(relx= 0.64, rely= 0)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= 'L').place(relx= 0.69, rely= 0)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= 'GS').place(relx= 0.73, rely= 0)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= 'GR').place(relx= 0.78, rely= 0)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= 'GD').place(relx= 0.83, rely= 0)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= 'P').place(relx= 0.89, rely= 0)

# Entry 1
Best_gF = best_teams['F']
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Best_gF[0].country).place(relx= 0.28, rely= 0.2)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.2)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Best_gF[0].wins).place(relx= 0.59, rely= 0.2)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Best_gF[0].draws).place(relx= 0.64, rely= 0.2)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Best_gF[0].losses).place(relx= 0.69, rely= 0.2)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Best_gF[0].goals_for).place(relx= 0.74, rely= 0.2)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Best_gF[0].goals_against).place(relx= 0.79, rely= 0.2)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Best_gF[0].goals_diff).place(relx= 0.84, rely= 0.2)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Best_gF[0].points).place(relx= 0.89, rely= 0.2)
# image Team 1
if os.path.exists('Images/'+Best_gF[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gF[0].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_f, image= img1, text= '')
    label_1.place(relx= 0.222, rely= 0.2)
else:
    label_1 = ctk.CTkLabel(master= group_f, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.2)

# Entry 2
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Best_gF[1].country).place(relx= 0.28, rely= 0.4)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.4)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Best_gF[1].wins).place(relx= 0.59, rely= 0.4)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Best_gF[1].draws).place(relx= 0.64, rely= 0.4)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Best_gF[1].losses).place(relx= 0.69, rely= 0.4)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Best_gF[1].goals_for).place(relx= 0.74, rely= 0.4)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Best_gF[1].goals_against).place(relx= 0.79, rely= 0.4)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Best_gF[1].goals_diff).place(relx= 0.84, rely= 0.4)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Best_gF[1].points).place(relx= 0.89, rely= 0.4)
# image Team 2
if os.path.exists('Images/'+Best_gF[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gF[1].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_f, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.4)
else:
    label_1 = ctk.CTkLabel(master= group_f, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.4)

# Entry 3
Worst_gF = worst_teams['F']
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Worst_gF[0].country).place(relx= 0.28, rely= 0.6)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.6)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Worst_gF[0].wins).place(relx= 0.59, rely= 0.6)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Worst_gF[0].draws).place(relx= 0.64, rely= 0.6)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Worst_gF[0].losses).place(relx= 0.69, rely= 0.6)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Worst_gF[0].goals_for).place(relx= 0.74, rely= 0.6)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Worst_gF[0].goals_against).place(relx= 0.79, rely= 0.6)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Worst_gF[0].goals_diff).place(relx= 0.84, rely= 0.6)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Worst_gF[0].points).place(relx= 0.89, rely= 0.6)
# image Team 3
if os.path.exists('Images/'+Worst_gF[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Worst_gF[0].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_f, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.6)
else:
    label_1 = ctk.CTkLabel(master= group_f, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.6)

# Entry 4
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Worst_gF[1].country).place(relx= 0.28, rely= 0.8)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.8)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Worst_gF[1].wins).place(relx= 0.59, rely= 0.8)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Worst_gF[1].draws).place(relx= 0.64, rely= 0.8)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Worst_gF[1].losses).place(relx= 0.69, rely= 0.8)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Worst_gF[1].goals_for).place(relx= 0.74, rely= 0.8)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Worst_gF[1].goals_against).place(relx= 0.79, rely= 0.8)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Worst_gF[1].goals_diff).place(relx= 0.84, rely= 0.8)
entry = ctk.CTkLabel(master= group_f, width= 300, height= 29, anchor= 'w', text= Worst_gF[1].points).place(relx= 0.89, rely= 0.8)
# image Team 4
if os.path.exists('Images/'+Worst_gF[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Worst_gF[1].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_f, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.8)
else:
    label_1 = ctk.CTkLabel(master= group_f, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.8)


############
# Group G
group_g = ctk.CTkFrame(master= frame_2, fg_color='green', width= 400, height= 120)
group_g.place(relx= 0.1, rely= 0.68)
label_g = ctk.CTkLabel(master= group_g, text= 'Group\nG', font=('Arial',16,'bold'))
label_g.place(relx= 0.06, rely= .3)

# collum head
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= 'Teams').place(relx= 0.28, rely= 0)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= 'G').place(relx= 0.54, rely= 0)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= 'W').place(relx= 0.59, rely= 0)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= 'D').place(relx= 0.64, rely= 0)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= 'L').place(relx= 0.69, rely= 0)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= 'GS').place(relx= 0.73, rely= 0)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= 'GR').place(relx= 0.78, rely= 0)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= 'GD').place(relx= 0.83, rely= 0)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= 'P').place(relx= 0.89, rely= 0)

# Entry 1
Best_gG = best_teams['G']
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Best_gG[0].country).place(relx= 0.28, rely= 0.2)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.2)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Best_gG[0].wins).place(relx= 0.59, rely= 0.2)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Best_gG[0].draws).place(relx= 0.64, rely= 0.2)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Best_gG[0].losses).place(relx= 0.69, rely= 0.2)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Best_gG[0].goals_for).place(relx= 0.74, rely= 0.2)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Best_gG[0].goals_against).place(relx= 0.79, rely= 0.2)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Best_gG[0].goals_diff).place(relx= 0.84, rely= 0.2)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Best_gG[0].points).place(relx= 0.89, rely= 0.2)
# image Team 1
if os.path.exists('Images/'+Best_gG[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gG[0].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_g, image= img1, text= '')
    label_1.place(relx= 0.222, rely= 0.2)
else:
    label_1 = ctk.CTkLabel(master= group_g, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.2)

# Entry 2
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Best_gG[1].country).place(relx= 0.28, rely= 0.4)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.4)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Best_gG[1].wins).place(relx= 0.59, rely= 0.4)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Best_gG[1].draws).place(relx= 0.64, rely= 0.4)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Best_gG[1].losses).place(relx= 0.69, rely= 0.4)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Best_gG[1].goals_for).place(relx= 0.74, rely= 0.4)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Best_gG[1].goals_against).place(relx= 0.79, rely= 0.4)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Best_gG[1].goals_diff).place(relx= 0.84, rely= 0.4)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Best_gG[1].points).place(relx= 0.89, rely= 0.4)
# image Team 2
if os.path.exists('Images/'+Best_gG[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gG[1].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_g, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.4)
else:
    label_1 = ctk.CTkLabel(master= group_g, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.4)

# Entry 3
Worst_gG = worst_teams['G']
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Worst_gG[0].country).place(relx= 0.28, rely= 0.6)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.6)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Worst_gG[0].wins).place(relx= 0.59, rely= 0.6)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Worst_gG[0].draws).place(relx= 0.64, rely= 0.6)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Worst_gG[0].losses).place(relx= 0.69, rely= 0.6)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Worst_gG[0].goals_for).place(relx= 0.74, rely= 0.6)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Worst_gG[0].goals_against).place(relx= 0.79, rely= 0.6)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Worst_gG[0].goals_diff).place(relx= 0.84, rely= 0.6)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Worst_gG[0].points).place(relx= 0.89, rely= 0.6)
# image Team 3
if os.path.exists('Images/'+Worst_gG[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Worst_gG[0].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_g, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.6)
else:
    label_1 = ctk.CTkLabel(master= group_g, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.6)

# Entry 4
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Worst_gG[1].country).place(relx= 0.28, rely= 0.8)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.8)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Worst_gG[1].wins).place(relx= 0.59, rely= 0.8)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Worst_gG[1].draws).place(relx= 0.64, rely= 0.8)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Worst_gG[1].losses).place(relx= 0.69, rely= 0.8)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Worst_gG[1].goals_for).place(relx= 0.74, rely= 0.8)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Worst_gG[1].goals_against).place(relx= 0.79, rely= 0.8)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Worst_gG[1].goals_diff).place(relx= 0.84, rely= 0.8)
entry = ctk.CTkLabel(master= group_g, width= 300, height= 29, anchor= 'w', text= Worst_gG[1].points).place(relx= 0.89, rely= 0.8)
# image Team 4
if os.path.exists('Images/'+Worst_gG[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Worst_gG[1].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_g, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.8)
else:
    label_1 = ctk.CTkLabel(master= group_g, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.8)


############
# Group H
group_h = ctk.CTkFrame(master= frame_2, fg_color='green', width= 400, height= 120)
group_h.place(relx= 0.58, rely= 0.68)
label_h = ctk.CTkLabel(master= group_h, text= 'Group\nH', font=('Arial',16,'bold'))
label_h.place(relx= 0.06, rely= .3)

# collum head
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= 'Teams').place(relx= 0.28, rely= 0)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= 'G').place(relx= 0.54, rely= 0)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= 'W').place(relx= 0.59, rely= 0)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= 'D').place(relx= 0.64, rely= 0)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= 'L').place(relx= 0.69, rely= 0)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= 'GS').place(relx= 0.73, rely= 0)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= 'GR').place(relx= 0.78, rely= 0)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= 'GD').place(relx= 0.83, rely= 0)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= 'P').place(relx= 0.89, rely= 0)

# Entry 1
Best_gH = best_teams['H']
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Best_gH[0].country).place(relx= 0.28, rely= 0.2)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.2)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Best_gH[0].wins).place(relx= 0.59, rely= 0.2)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Best_gH[0].draws).place(relx= 0.64, rely= 0.2)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Best_gH[0].losses).place(relx= 0.69, rely= 0.2)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Best_gH[0].goals_for).place(relx= 0.74, rely= 0.2)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Best_gH[0].goals_against).place(relx= 0.79, rely= 0.2)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Best_gH[0].goals_diff).place(relx= 0.84, rely= 0.2)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Best_gH[0].points).place(relx= 0.89, rely= 0.2)
# image Team 1
if os.path.exists('Images/'+Best_gH[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gH[0].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_h, image= img1, text= '')
    label_1.place(relx= 0.222, rely= 0.2)
else:
    label_1 = ctk.CTkLabel(master= group_h, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.2)

# Entry 2
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Best_gH[1].country).place(relx= 0.28, rely= 0.4)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.4)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Best_gH[1].wins).place(relx= 0.59, rely= 0.4)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Best_gH[1].draws).place(relx= 0.64, rely= 0.4)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Best_gH[1].losses).place(relx= 0.69, rely= 0.4)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Best_gH[1].goals_for).place(relx= 0.74, rely= 0.4)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Best_gH[1].goals_against).place(relx= 0.79, rely= 0.4)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Best_gH[1].goals_diff).place(relx= 0.84, rely= 0.4)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Best_gH[1].points).place(relx= 0.89, rely= 0.4)
# image Team 2
if os.path.exists('Images/'+Best_gH[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Best_gH[1].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_h, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.4)
else:
    label_1 = ctk.CTkLabel(master= group_h, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.4)

# Entry 3
Worst_gH = worst_teams['H']
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Worst_gH[0].country).place(relx= 0.28, rely= 0.6)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.6)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Worst_gH[0].wins).place(relx= 0.59, rely= 0.6)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Worst_gH[0].draws).place(relx= 0.64, rely= 0.6)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Worst_gH[0].losses).place(relx= 0.69, rely= 0.6)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Worst_gH[0].goals_for).place(relx= 0.74, rely= 0.6)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Worst_gH[0].goals_against).place(relx= 0.79, rely= 0.6)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Worst_gH[0].goals_diff).place(relx= 0.84, rely= 0.6)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Worst_gH[0].points).place(relx= 0.89, rely= 0.6)
# image Team 3
if os.path.exists('Images/'+Worst_gH[0].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Worst_gH[0].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_h, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.6)
else:
    label_1 = ctk.CTkLabel(master= group_h, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.6)

# Entry 4
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Worst_gH[1].country).place(relx= 0.28, rely= 0.8)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= '3').place(relx= 0.54, rely= 0.8)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Worst_gH[1].wins).place(relx= 0.59, rely= 0.8)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Worst_gH[1].draws).place(relx= 0.64, rely= 0.8)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Worst_gH[1].losses).place(relx= 0.69, rely= 0.8)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Worst_gH[1].goals_for).place(relx= 0.74, rely= 0.8)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Worst_gH[1].goals_against).place(relx= 0.79, rely= 0.8)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Worst_gH[1].goals_diff).place(relx= 0.84, rely= 0.8)
entry = ctk.CTkLabel(master= group_h, width= 300, height= 29, anchor= 'w', text= Worst_gH[1].points).place(relx= 0.89, rely= 0.8)
# image Team 4
if os.path.exists('Images/'+Worst_gH[1].country+'.png'):
    img1 = ctk.CTkImage(Image.open('Images/'+Worst_gH[1].country+'.png'), size= (18, 18))
    label_1 = ctk.CTkLabel(master= group_h, image= img1, text= '')
    label_1.place(relx= 0.225, rely= 0.8)
else:
    label_1 = ctk.CTkLabel(master= group_h, image= unknown, text= '')
    label_1.place(relx= 0.225, rely= 0.8)

#####
# Submit Button
submit_1 = ctk.CTkButton(master = frame_2, height= 45, width= 100, text= "Submit", command= app.destroy)
submit_1.place(relx= 0.915, rely = 0.92)

app.mainloop()