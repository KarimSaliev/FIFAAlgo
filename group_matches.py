from PIL import Image
from create_teams import *
import os.path
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

##########################################################################################
##########################################################################################
##########################################################################################
# group a games


root = ctk.CTk()
root.geometry("1250x703")
root.title("Tornament Manager")

# frame for information text
frame_1 = ctk.CTkFrame(master=root, height=80, width=400)
frame_1.pack(pady=20)
# information text
label_1 = ctk.CTkLabel(master=frame_1, text="Please fill in the match outcomes for group A.",
                       font=('Arial', 16, 'bold'))
label_1.pack(padx=10, pady=10)

# frame were the matches will be shown
frame_2 = ctk.CTkFrame(master=root, fg_color='gray17')
frame_2.pack(pady=5, padx=20, fill="both", expand=True)

# image used for unkown teams
unknown = ctk.CTkImage(Image.open('Images/Unknown.png'), size=(52, 52))

goal_var1 = ctk.StringVar()
goal_var2 = ctk.StringVar()
goal_var3 = ctk.StringVar()
goal_var4 = ctk.StringVar()
goal_var5 = ctk.StringVar()
goal_var6 = ctk.StringVar()
goal_var7 = ctk.StringVar()
goal_var8 = ctk.StringVar()
goal_var9 = ctk.StringVar()
goal_var10 = ctk.StringVar()
goal_var11 = ctk.StringVar()
goal_var12 = ctk.StringVar()

# game 1
game_1 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_1.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_1, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_1, text=namea_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_1, text=namea_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 1
if os.path.exists('Images/' + namea_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + namea_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_1, image=img1, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_1, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 2
if os.path.exists('Images/' + namea_var2.get() + '.png'):
    img2 = ctk.CTkImage(Image.open('Images/' + namea_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_1, image=img2, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_1, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_1, width=50, height=40, textvariable=goal_var1)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_1, width=50, height=40, textvariable=goal_var2)
entry1.place(relx=0.55, rely=0.25)

# game 2
game_2 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_2.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_2, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_2, text=namea_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_2, text=namea_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 3
if os.path.exists('Images/' + namea_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + namea_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_2, image=img3, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_2, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 4
if os.path.exists('Images/' + namea_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + namea_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_2, image=img4, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_2, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_2, width=50, height=40, textvariable=goal_var11)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_2, width=50, height=40, textvariable=goal_var12)
entry1.place(relx=0.55, rely=0.25)

# game 3
game_3 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_3.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_3, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_3, text=namea_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_3, text=namea_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 1
if os.path.exists('Images/' + namea_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + namea_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_3, image=img1, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_3, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 3
if os.path.exists('Images/' + namea_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + namea_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_3, image=img3, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_3, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_3, width=50, height=40, textvariable=goal_var3)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_3, width=50, height=40, textvariable=goal_var4)
entry1.place(relx=0.55, rely=0.25)

# game 4
game_4 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_4.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_4, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_4, text=namea_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_4, text=namea_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 4
if os.path.exists('Images/' + namea_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + namea_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_4, image=img4, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_4, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 2
if os.path.exists('Images/' + namea_var2.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + namea_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_4, image=img4, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_4, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_4, width=50, height=40, textvariable=goal_var10)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_4, width=50, height=40, textvariable=goal_var9)
entry1.place(relx=0.55, rely=0.25)

# game 5
game_5 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_5.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_5, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_5, text=namea_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_5, text=namea_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 4
if os.path.exists('Images/' + namea_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + namea_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_5, image=img4, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_5, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 1
if os.path.exists('Images/' + namea_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + namea_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_5, image=img1, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_5, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_5, width=50, height=40, textvariable=goal_var6)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_5, width=50, height=40, textvariable=goal_var5)
entry1.place(relx=0.55, rely=0.25)

# game 6
game_6 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_6.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_6, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_6, text=namea_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_6, text=namea_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 2
if os.path.exists('Images/' + namea_var2.get() + '.png'):
    img2 = ctk.CTkImage(Image.open('Images/' + namea_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_6, image=img2, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_6, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 3
if os.path.exists('Images/' + namea_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + namea_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_6, image=img3, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_6, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_6, width=50, height=40, textvariable=goal_var7)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_6, width=50, height=40, textvariable=goal_var8)
entry1.place(relx=0.55, rely=0.25)

#####
# Submit Button
submit_1 = ctk.CTkButton(master=frame_2, height=45, width=100, text="Submit", command=root.destroy)
submit_1.place(relx=0.915, rely=0.92)

root.mainloop()

##########################################################################################
##########################################################################################
##########################################################################################
# group b games


root = ctk.CTk()
root.geometry("1250x703")
root.title("Tornament Manager")

# frame for information text
frame_1 = ctk.CTkFrame(master=root, height=80, width=400)
frame_1.pack(pady=20)
# information text
label_1 = ctk.CTkLabel(master=frame_1, text="Please fill in the match outcomes for group B.",
                       font=('Arial', 16, 'bold'))
label_1.pack(padx=10, pady=10)

# frame were the matches will be shown
frame_2 = ctk.CTkFrame(master=root, fg_color='gray17')
frame_2.pack(pady=5, padx=20, fill="both", expand=True)

# image used for unkown teams
unknown = ctk.CTkImage(Image.open('Images/Unknown.png'), size=(52, 52))

goalb_var1 = ctk.StringVar()
goalb_var2 = ctk.StringVar()
goalb_var3 = ctk.StringVar()
goalb_var4 = ctk.StringVar()
goalb_var5 = ctk.StringVar()
goalb_var6 = ctk.StringVar()
goalb_var7 = ctk.StringVar()
goalb_var8 = ctk.StringVar()
goalb_var9 = ctk.StringVar()
goalb_var10 = ctk.StringVar()
goalb_var11 = ctk.StringVar()
goalb_var12 = ctk.StringVar()

# game 1
game_1 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_1.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_1, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_1, text=nameb_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_1, text=nameb_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 1
if os.path.exists('Images/' + nameb_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + nameb_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_1, image=img1, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_1, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 2
if os.path.exists('Images/' + nameb_var2.get() + '.png'):
    img2 = ctk.CTkImage(Image.open('Images/' + nameb_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_1, image=img2, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_1, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_1, width=50, height=40, textvariable=goalb_var1)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_1, width=50, height=40, textvariable=goalb_var2)
entry1.place(relx=0.55, rely=0.25)

# game 2
game_2 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_2.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_2, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_2, text=nameb_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_2, text=nameb_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 3
if os.path.exists('Images/' + nameb_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + nameb_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_2, image=img3, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_2, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 4
if os.path.exists('Images/' + nameb_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + nameb_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_2, image=img4, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_2, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_2, width=50, height=40, textvariable=goalb_var11)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_2, width=50, height=40, textvariable=goalb_var12)
entry1.place(relx=0.55, rely=0.25)

# game 3
game_3 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_3.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_3, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_3, text=nameb_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_3, text=nameb_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 1
if os.path.exists('Images/' + nameb_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + nameb_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_3, image=img1, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_3, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 3
if os.path.exists('Images/' + nameb_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + nameb_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_3, image=img3, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_3, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_3, width=50, height=40, textvariable=goalb_var3)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_3, width=50, height=40, textvariable=goalb_var4)
entry1.place(relx=0.55, rely=0.25)

# game 4
game_4 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_4.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_4, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_4, text=nameb_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_4, text=nameb_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 4
if os.path.exists('Images/' + nameb_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + nameb_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_4, image=img4, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_4, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 2
if os.path.exists('Images/' + nameb_var2.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + nameb_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_4, image=img4, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_4, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_4, width=50, height=40, textvariable=goalb_var10)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_4, width=50, height=40, textvariable=goalb_var9)
entry1.place(relx=0.55, rely=0.25)

# game 5
game_5 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_5.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_5, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_5, text=nameb_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_5, text=nameb_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 4
if os.path.exists('Images/' + nameb_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + nameb_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_5, image=img4, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_5, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 1
if os.path.exists('Images/' + nameb_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + nameb_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_5, image=img1, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_5, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_5, width=50, height=40, textvariable=goalb_var6)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_5, width=50, height=40, textvariable=goalb_var5)
entry1.place(relx=0.55, rely=0.25)

# game 6
game_6 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_6.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_6, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_6, text=nameb_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_6, text=nameb_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 2
if os.path.exists('Images/' + nameb_var2.get() + '.png'):
    img2 = ctk.CTkImage(Image.open('Images/' + nameb_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_6, image=img2, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_6, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 3
if os.path.exists('Images/' + nameb_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + nameb_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_6, image=img3, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_6, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_6, width=50, height=40, textvariable=goalb_var7)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_6, width=50, height=40, textvariable=goalb_var8)
entry1.place(relx=0.55, rely=0.25)

#####
# Submit Button
submit_1 = ctk.CTkButton(master=frame_2, height=45, width=100, text="Submit", command=root.destroy)
submit_1.place(relx=0.915, rely=0.92)

root.mainloop()

##########################################################################################
##########################################################################################
##########################################################################################
# group c games


root = ctk.CTk()
root.geometry("1250x703")
root.title("Tornament Manager")

# frame for information text
frame_1 = ctk.CTkFrame(master=root, height=80, width=400)
frame_1.pack(pady=20)
# information text
label_1 = ctk.CTkLabel(master=frame_1, text="Please fill in the match outcomes for group C.",
                       font=('Arial', 16, 'bold'))
label_1.pack(padx=10, pady=10)

# frame were the matches will be shown
frame_2 = ctk.CTkFrame(master=root, fg_color='gray17')
frame_2.pack(pady=5, padx=20, fill="both", expand=True)

# image used for unkown teams
unknown = ctk.CTkImage(Image.open('Images/Unknown.png'), size=(52, 52))

goalc_var1 = ctk.StringVar()
goalc_var2 = ctk.StringVar()
goalc_var3 = ctk.StringVar()
goalc_var4 = ctk.StringVar()
goalc_var5 = ctk.StringVar()
goalc_var6 = ctk.StringVar()
goalc_var7 = ctk.StringVar()
goalc_var8 = ctk.StringVar()
goalc_var9 = ctk.StringVar()
goalc_var10 = ctk.StringVar()
goalc_var11 = ctk.StringVar()
goalc_var12 = ctk.StringVar()

# game 1
game_1 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_1.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_1, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_1, text=namec_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_1, text=namec_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 1
if os.path.exists('Images/' + namec_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + namec_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_1, image=img1, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_1, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 2
if os.path.exists('Images/' + namec_var2.get() + '.png'):
    img2 = ctk.CTkImage(Image.open('Images/' + namec_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_1, image=img2, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_1, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_1, width=50, height=40, textvariable=goalc_var1)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_1, width=50, height=40, textvariable=goalc_var2)
entry1.place(relx=0.55, rely=0.25)

# game 2
game_2 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_2.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_2, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_2, text=namec_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_2, text=namec_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 3
if os.path.exists('Images/' + namec_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + namec_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_2, image=img3, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_2, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 4
if os.path.exists('Images/' + namec_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + namec_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_2, image=img4, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_2, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_2, width=50, height=40, textvariable=goalc_var11)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_2, width=50, height=40, textvariable=goalc_var12)
entry1.place(relx=0.55, rely=0.25)

# game 3
game_3 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_3.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_3, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_3, text=namec_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_3, text=namec_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 1
if os.path.exists('Images/' + namec_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + namec_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_3, image=img1, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_3, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 3
if os.path.exists('Images/' + namec_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + namec_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_3, image=img3, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_3, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_3, width=50, height=40, textvariable=goalc_var3)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_3, width=50, height=40, textvariable=goalc_var4)
entry1.place(relx=0.55, rely=0.25)

# game 4
game_4 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_4.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_4, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_4, text=namec_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_4, text=namec_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 4
if os.path.exists('Images/' + namec_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + namec_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_4, image=img4, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_4, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 2
if os.path.exists('Images/' + namec_var2.get() + '.png'):
    img2 = ctk.CTkImage(Image.open('Images/' + namec_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_4, image=img2, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_4, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_4, width=50, height=40, textvariable=goalc_var10)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_4, width=50, height=40, textvariable=goalc_var9)
entry1.place(relx=0.55, rely=0.25)

# game 5
game_5 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_5.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_5, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_5, text=namec_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_5, text=namec_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 4
if os.path.exists('Images/' + namec_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + namec_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_5, image=img4, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_5, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 1
if os.path.exists('Images/' + namec_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + namec_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_5, image=img1, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_5, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_5, width=50, height=40, textvariable=goalc_var6)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_5, width=50, height=40, textvariable=goalc_var5)
entry1.place(relx=0.55, rely=0.25)

# game 6
game_6 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_6.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_6, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_6, text=namec_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_6, text=namec_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 2
if os.path.exists('Images/' + namec_var2.get() + '.png'):
    img2 = ctk.CTkImage(Image.open('Images/' + namec_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_6, image=img2, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_6, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 3
if os.path.exists('Images/' + namec_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + namec_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_6, image=img3, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_6, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_6, width=50, height=40, textvariable=goalc_var7)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_6, width=50, height=40, textvariable=goalc_var8)
entry1.place(relx=0.55, rely=0.25)

#####
# Submit Button
submit_1 = ctk.CTkButton(master=frame_2, height=45, width=100, text="Submit", command=root.destroy)
submit_1.place(relx=0.915, rely=0.92)

root.mainloop()

##########################################################################################
##########################################################################################
##########################################################################################
# group d games


root = ctk.CTk()
root.geometry("1250x703")
root.title("Tornament Manager")

# frame for information text
frame_1 = ctk.CTkFrame(master=root, height=80, width=400)
frame_1.pack(pady=20)
# information text
label_1 = ctk.CTkLabel(master=frame_1, text="Please fill in the match outcomes for group D.",
                       font=('Arial', 16, 'bold'))
label_1.pack(padx=10, pady=10)

# frame were the matches will be shown
frame_2 = ctk.CTkFrame(master=root, fg_color='gray17')
frame_2.pack(pady=5, padx=20, fill="both", expand=True)

# image used for unkown teams
unknown = ctk.CTkImage(Image.open('Images/Unknown.png'), size=(52, 52))

goald_var1 = ctk.StringVar()
goald_var2 = ctk.StringVar()
goald_var3 = ctk.StringVar()
goald_var4 = ctk.StringVar()
goald_var5 = ctk.StringVar()
goald_var6 = ctk.StringVar()
goald_var7 = ctk.StringVar()
goald_var8 = ctk.StringVar()
goald_var9 = ctk.StringVar()
goald_var10 = ctk.StringVar()
goald_var11 = ctk.StringVar()
goald_var12 = ctk.StringVar()

# game 1
game_1 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_1.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_1, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_1, text=named_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_1, text=named_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 1
if os.path.exists('Images/' + named_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + named_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_1, image=img1, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_1, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 2
if os.path.exists('Images/' + named_var2.get() + '.png'):
    img2 = ctk.CTkImage(Image.open('Images/' + named_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_1, image=img2, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_1, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_1, width=50, height=40, textvariable=goald_var1)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_1, width=50, height=40, textvariable=goald_var2)
entry1.place(relx=0.55, rely=0.25)

# game 2
game_2 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_2.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_2, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_2, text=named_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_2, text=named_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 3
if os.path.exists('Images/' + named_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + named_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_2, image=img3, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_2, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 4
if os.path.exists('Images/' + named_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + named_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_2, image=img4, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_2, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_2, width=50, height=40, textvariable=goald_var11)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_2, width=50, height=40, textvariable=goald_var12)
entry1.place(relx=0.55, rely=0.25)

# game 3
game_3 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_3.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_3, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_3, text=named_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_3, text=named_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 1
if os.path.exists('Images/' + named_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + named_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_3, image=img1, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_3, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 3
if os.path.exists('Images/' + named_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + named_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_3, image=img3, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_3, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_3, width=50, height=40, textvariable=goald_var3)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_3, width=50, height=40, textvariable=goald_var4)
entry1.place(relx=0.55, rely=0.25)

# game 4
game_4 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_4.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_4, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_4, text=named_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_4, text=named_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 4
if os.path.exists('Images/' + named_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + named_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_4, image=img4, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_4, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 2
if os.path.exists('Images/' + named_var2.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + named_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_4, image=img4, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_4, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_4, width=50, height=40, textvariable=goald_var10)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_4, width=50, height=40, textvariable=goald_var9)
entry1.place(relx=0.55, rely=0.25)

# game 5
game_5 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_5.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_5, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_5, text=named_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_5, text=named_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 4
if os.path.exists('Images/' + named_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + named_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_5, image=img4, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_5, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 1
if os.path.exists('Images/' + named_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + named_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_5, image=img1, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_5, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_5, width=50, height=40, textvariable=goald_var6)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_5, width=50, height=40, textvariable=goald_var5)
entry1.place(relx=0.55, rely=0.25)

# game 6
game_6 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_6.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_6, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_6, text=named_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_6, text=named_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 2
if os.path.exists('Images/' + named_var2.get() + '.png'):
    img2 = ctk.CTkImage(Image.open('Images/' + named_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_6, image=img2, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_6, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 3
if os.path.exists('Images/' + named_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + named_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_6, image=img3, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_6, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goal entries
entry1 = ctk.CTkEntry(master=game_6, width=50, height=40, textvariable=goald_var7)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_6, width=50, height=40, textvariable=goald_var8)
entry1.place(relx=0.55, rely=0.25)

#####
# Submit Button
submit_1 = ctk.CTkButton(master=frame_2, height=45, width=100, text="Submit", command=root.destroy)
submit_1.place(relx=0.915, rely=0.92)

root.mainloop()

##########################################################################################
##########################################################################################
##########################################################################################
# group e games


root = ctk.CTk()
root.geometry("1250x703")
root.title("Tornament Manager")

# frame for information text
frame_1 = ctk.CTkFrame(master=root, height=80, width=400)
frame_1.pack(pady=20)
# information text
label_1 = ctk.CTkLabel(master=frame_1, text="Please fill in the match outcomes for group E.",
                       font=('Arial', 16, 'bold'))
label_1.pack(padx=10, pady=10)

# frame were the matches will be shown
frame_2 = ctk.CTkFrame(master=root, fg_color='gray17')
frame_2.pack(pady=5, padx=20, fill="both", expand=True)

# image used for unkown teams
unknown = ctk.CTkImage(Image.open('Images/Unknown.png'), size=(52, 52))

goale_var1 = ctk.StringVar()
goale_var2 = ctk.StringVar()
goale_var3 = ctk.StringVar()
goale_var4 = ctk.StringVar()
goale_var5 = ctk.StringVar()
goale_var6 = ctk.StringVar()
goale_var7 = ctk.StringVar()
goale_var8 = ctk.StringVar()
goale_var9 = ctk.StringVar()
goale_var10 = ctk.StringVar()
goale_var11 = ctk.StringVar()
goale_var12 = ctk.StringVar()

# game 1
game_1 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_1.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_1, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_1, text=namee_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_1, text=namee_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 1
if os.path.exists('Images/' + namee_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + namee_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_1, image=img1, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_1, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 2
if os.path.exists('Images/' + namee_var2.get() + '.png'):
    img2 = ctk.CTkImage(Image.open('Images/' + namee_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_1, image=img2, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_1, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_1, width=50, height=40, textvariable=goale_var1)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_1, width=50, height=40, textvariable=goale_var2)
entry1.place(relx=0.55, rely=0.25)

# game 2
game_2 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_2.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_2, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_2, text=namee_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_2, text=namee_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 3
if os.path.exists('Images/' + namee_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + namee_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_2, image=img3, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_2, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 4
if os.path.exists('Images/' + namee_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + namee_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_2, image=img4, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_2, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_2, width=50, height=40, textvariable=goale_var11)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_2, width=50, height=40, textvariable=goale_var12)
entry1.place(relx=0.55, rely=0.25)

# game 3
game_3 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_3.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_3, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_3, text=namee_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_3, text=namee_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 1
if os.path.exists('Images/' + namee_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + namee_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_3, image=img1, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_3, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 3
if os.path.exists('Images/' + namee_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + namee_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_3, image=img3, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_3, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_3, width=50, height=40, textvariable=goale_var3)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_3, width=50, height=40, textvariable=goale_var4)
entry1.place(relx=0.55, rely=0.25)

# game 4
game_4 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_4.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_4, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_4, text=namee_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_4, text=namee_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 4
if os.path.exists('Images/' + namee_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + namee_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_4, image=img4, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_4, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 2
if os.path.exists('Images/' + namee_var2.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + namee_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_4, image=img4, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_4, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_4, width=50, height=40, textvariable=goale_var10)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_4, width=50, height=40, textvariable=goale_var9)
entry1.place(relx=0.55, rely=0.25)

# game 5
game_5 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_5.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_5, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_5, text=namee_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_5, text=namee_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 4
if os.path.exists('Images/' + namee_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + namee_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_5, image=img4, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_5, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 1
if os.path.exists('Images/' + namee_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + namee_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_5, image=img1, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_5, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_5, width=50, height=40, textvariable=goale_var6)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_5, width=50, height=40, textvariable=goale_var5)
entry1.place(relx=0.55, rely=0.25)

# game 6
game_6 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_6.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_6, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_6, text=namee_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_6, text=namee_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 2
if os.path.exists('Images/' + namee_var2.get() + '.png'):
    img2 = ctk.CTkImage(Image.open('Images/' + namee_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_6, image=img2, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_6, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 3
if os.path.exists('Images/' + namee_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + namee_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_6, image=img3, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_6, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_6, width=50, height=40, textvariable=goale_var7)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_6, width=50, height=40, textvariable=goale_var8)
entry1.place(relx=0.55, rely=0.25)

#####
# Submit Button
submit_1 = ctk.CTkButton(master=frame_2, height=45, width=100, text="Submit", command=root.destroy)
submit_1.place(relx=0.915, rely=0.92)

root.mainloop()

##########################################################################################
##########################################################################################
##########################################################################################
# group f games


root = ctk.CTk()
root.geometry("1250x703")
root.title("Tornament Manager")

# frame for information text
frame_1 = ctk.CTkFrame(master=root, height=80, width=400)
frame_1.pack(pady=20)
# information text
label_1 = ctk.CTkLabel(master=frame_1, text="Please fill in the match outcomes for group F.",
                       font=('Arial', 16, 'bold'))
label_1.pack(padx=10, pady=10)

# frame were the matches will be shown
frame_2 = ctk.CTkFrame(master=root, fg_color='gray17')
frame_2.pack(pady=5, padx=20, fill="both", expand=True)

# image used for unkown teams
unknown = ctk.CTkImage(Image.open('Images/Unknown.png'), size=(52, 52))

goalf_var1 = ctk.StringVar()
goalf_var2 = ctk.StringVar()
goalf_var3 = ctk.StringVar()
goalf_var4 = ctk.StringVar()
goalf_var5 = ctk.StringVar()
goalf_var6 = ctk.StringVar()
goalf_var7 = ctk.StringVar()
goalf_var8 = ctk.StringVar()
goalf_var9 = ctk.StringVar()
goalf_var10 = ctk.StringVar()
goalf_var11 = ctk.StringVar()
goalf_var12 = ctk.StringVar()

# game 1
game_1 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_1.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_1, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_1, text=namef_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_1, text=namef_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 1
if os.path.exists('Images/' + namef_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + namef_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_1, image=img1, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_1, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 2
if os.path.exists('Images/' + namef_var2.get() + '.png'):
    img2 = ctk.CTkImage(Image.open('Images/' + namef_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_1, image=img2, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_1, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_1, width=50, height=40, textvariable=goalf_var1)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_1, width=50, height=40, textvariable=goalf_var2)
entry1.place(relx=0.55, rely=0.25)

# game 2
game_2 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_2.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_2, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_2, text=namef_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_2, text=namef_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 3
if os.path.exists('Images/' + namef_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + namef_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_2, image=img3, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_2, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 4
if os.path.exists('Images/' + namef_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + namef_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_2, image=img4, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_2, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_2, width=50, height=40, textvariable=goalf_var11)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_2, width=50, height=40, textvariable=goalf_var12)
entry1.place(relx=0.55, rely=0.25)

# game 3
game_3 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_3.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_3, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_3, text=namef_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_3, text=namef_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 1
if os.path.exists('Images/' + namef_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + namef_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_3, image=img1, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_3, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 3
if os.path.exists('Images/' + namef_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + namef_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_3, image=img3, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_3, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_3, width=50, height=40, textvariable=goalf_var3)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_3, width=50, height=40, textvariable=goalf_var4)
entry1.place(relx=0.55, rely=0.25)

# game 4
game_4 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_4.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_4, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_4, text=namef_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_4, text=namef_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 4
if os.path.exists('Images/' + namef_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + namef_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_4, image=img4, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_4, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 2
if os.path.exists('Images/' + namef_var2.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + namef_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_4, image=img4, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_4, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_4, width=50, height=40, textvariable=goalf_var10)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_4, width=50, height=40, textvariable=goalf_var9)
entry1.place(relx=0.55, rely=0.25)

# game 5
game_5 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_5.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_5, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_5, text=namef_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_5, text=namef_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 4
if os.path.exists('Images/' + namef_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + namef_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_5, image=img4, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_5, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 1
if os.path.exists('Images/' + namef_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + namef_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_5, image=img1, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_5, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_5, width=50, height=40, textvariable=goalf_var6)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_5, width=50, height=40, textvariable=goalf_var5)
entry1.place(relx=0.55, rely=0.25)

# game 6
game_6 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_6.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_6, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_6, text=namef_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_6, text=namef_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 2
if os.path.exists('Images/' + namef_var2.get() + '.png'):
    img2 = ctk.CTkImage(Image.open('Images/' + namef_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_6, image=img2, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_6, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 3
if os.path.exists('Images/' + namef_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + namef_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_6, image=img3, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_6, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_6, width=50, height=40, textvariable=goalf_var7)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_6, width=50, height=40, textvariable=goalf_var8)
entry1.place(relx=0.55, rely=0.25)

#####
# Submit Button
submit_1 = ctk.CTkButton(master=frame_2, height=45, width=100, text="Submit", command=root.destroy)
submit_1.place(relx=0.915, rely=0.92)

root.mainloop()

##########################################################################################
##########################################################################################
##########################################################################################
# group g games


root = ctk.CTk()
root.geometry("1250x703")
root.title("Tornament Manager")

# frame for information text
frame_1 = ctk.CTkFrame(master=root, height=80, width=400)
frame_1.pack(pady=20)
# information text
label_1 = ctk.CTkLabel(master=frame_1, text="Please fill in the match outcomes for group G.",
                       font=('Arial', 16, 'bold'))
label_1.pack(padx=10, pady=10)

# frame were the matches will be shown
frame_2 = ctk.CTkFrame(master=root, fg_color='gray17')
frame_2.pack(pady=5, padx=20, fill="both", expand=True)

# image used for unkown teams
unknown = ctk.CTkImage(Image.open('Images/Unknown.png'), size=(52, 52))

goalg_var1 = ctk.StringVar()
goalg_var2 = ctk.StringVar()
goalg_var3 = ctk.StringVar()
goalg_var4 = ctk.StringVar()
goalg_var5 = ctk.StringVar()
goalg_var6 = ctk.StringVar()
goalg_var7 = ctk.StringVar()
goalg_var8 = ctk.StringVar()
goalg_var9 = ctk.StringVar()
goalg_var10 = ctk.StringVar()
goalg_var11 = ctk.StringVar()
goalg_var12 = ctk.StringVar()

# game 1
game_1 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_1.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_1, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_1, text=nameg_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_1, text=nameg_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 1
if os.path.exists('Images/' + nameg_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + nameg_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_1, image=img1, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_1, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 2
if os.path.exists('Images/' + nameg_var2.get() + '.png'):
    img2 = ctk.CTkImage(Image.open('Images/' + nameg_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_1, image=img2, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_1, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_1, width=50, height=40, textvariable=goalg_var1)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_1, width=50, height=40, textvariable=goalg_var2)
entry1.place(relx=0.55, rely=0.25)

# game 2
game_2 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_2.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_2, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_2, text=nameg_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_2, text=nameg_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 3
if os.path.exists('Images/' + nameg_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + nameg_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_2, image=img3, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_2, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 4
if os.path.exists('Images/' + nameg_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + nameg_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_2, image=img4, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_2, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_2, width=50, height=40, textvariable=goalg_var11)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_2, width=50, height=40, textvariable=goalg_var12)
entry1.place(relx=0.55, rely=0.25)

# game 3
game_3 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_3.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_3, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_3, text=nameg_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_3, text=nameg_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 1
if os.path.exists('Images/' + namee_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + nameg_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_3, image=img1, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_3, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 3
if os.path.exists('Images/' + nameg_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + nameg_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_3, image=img3, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_3, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_3, width=50, height=40, textvariable=goalg_var3)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_3, width=50, height=40, textvariable=goalg_var4)
entry1.place(relx=0.55, rely=0.25)

# game 4
game_4 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_4.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_4, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_4, text=nameg_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_4, text=nameg_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 4
if os.path.exists('Images/' + nameg_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + nameg_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_4, image=img4, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_4, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 2
if os.path.exists('Images/' + nameg_var2.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + nameg_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_4, image=img4, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_4, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_4, width=50, height=40, textvariable=goalg_var10)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_4, width=50, height=40, textvariable=goalg_var9)
entry1.place(relx=0.55, rely=0.25)

# game 5
game_5 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_5.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_5, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_5, text=nameg_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_5, text=nameg_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 4
if os.path.exists('Images/' + nameg_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + nameg_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_5, image=img4, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_5, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 1
if os.path.exists('Images/' + nameg_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + nameg_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_5, image=img1, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_5, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_5, width=50, height=40, textvariable=goalg_var6)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_5, width=50, height=40, textvariable=goalg_var5)
entry1.place(relx=0.55, rely=0.25)

# game 6
game_6 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_6.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_6, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_6, text=nameg_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_6, text=nameg_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 2
if os.path.exists('Images/' + nameg_var2.get() + '.png'):
    img2 = ctk.CTkImage(Image.open('Images/' + nameg_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_6, image=img2, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_6, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 3
if os.path.exists('Images/' + nameg_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + nameg_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_6, image=img3, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_6, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_6, width=50, height=40, textvariable=goalg_var7)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_6, width=50, height=40, textvariable=goalg_var8)
entry1.place(relx=0.55, rely=0.25)

#####
# Submit Button
submit_1 = ctk.CTkButton(master=frame_2, height=45, width=100, text="Submit", command=root.destroy)
submit_1.place(relx=0.915, rely=0.92)

root.mainloop()

##########################################################################################
##########################################################################################
##########################################################################################
# group h games


root = ctk.CTk()
root.geometry("1250x703")
root.title("Tornament Manager")

# frame for information text
frame_1 = ctk.CTkFrame(master=root, height=80, width=400)
frame_1.pack(pady=20)
# information text
label_1 = ctk.CTkLabel(master=frame_1, text="Please fill in the match outcomes for group H.",
                       font=('Arial', 16, 'bold'))
label_1.pack(padx=10, pady=10)

# frame were the matches will be shown
frame_2 = ctk.CTkFrame(master=root, fg_color='gray17')
frame_2.pack(pady=5, padx=20, fill="both", expand=True)

# image used for unkown teams
unknown = ctk.CTkImage(Image.open('Images/Unknown.png'), size=(52, 52))

goalh_var1 = ctk.StringVar()
goalh_var2 = ctk.StringVar()
goalh_var3 = ctk.StringVar()
goalh_var4 = ctk.StringVar()
goalh_var5 = ctk.StringVar()
goalh_var6 = ctk.StringVar()
goalh_var7 = ctk.StringVar()
goalh_var8 = ctk.StringVar()
goalh_var9 = ctk.StringVar()
goalh_var10 = ctk.StringVar()
goalh_var11 = ctk.StringVar()
goalh_var12 = ctk.StringVar()

# game 1
game_1 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_1.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_1, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_1, text=nameh_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_1, text=nameh_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 1
if os.path.exists('Images/' + nameh_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + nameh_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_1, image=img1, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_1, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 2
if os.path.exists('Images/' + nameh_var2.get() + '.png'):
    img2 = ctk.CTkImage(Image.open('Images/' + nameh_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_1, image=img2, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_1, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_1, width=50, height=40, textvariable=goalh_var1)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_1, width=50, height=40, textvariable=goalh_var2)
entry1.place(relx=0.55, rely=0.25)

# game 2
game_2 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_2.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_2, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_2, text=nameh_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_2, text=nameh_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 3
if os.path.exists('Images/' + nameh_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + nameh_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_2, image=img3, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_2, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 4
if os.path.exists('Images/' + nameh_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + nameh_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_2, image=img4, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_2, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_2, width=50, height=40, textvariable=goalh_var11)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_2, width=50, height=40, textvariable=goalh_var12)
entry1.place(relx=0.55, rely=0.25)

# game 3
game_3 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_3.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_3, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_3, text=nameh_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_3, text=nameh_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 1
if os.path.exists('Images/' + nameh_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + nameh_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_3, image=img1, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_3, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 3
if os.path.exists('Images/' + nameh_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + nameh_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_3, image=img3, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_3, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_3, width=50, height=40, textvariable=goalh_var3)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_3, width=50, height=40, textvariable=goalh_var4)
entry1.place(relx=0.55, rely=0.25)

# game 4
game_4 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_4.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_4, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_4, text=nameh_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_4, text=nameh_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 4
if os.path.exists('Images/' + nameh_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + nameh_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_4, image=img4, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_4, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 2
if os.path.exists('Images/' + nameh_var2.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + nameh_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_4, image=img4, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_4, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_4, width=50, height=40, textvariable=goalh_var10)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_4, width=50, height=40, textvariable=goalh_var9)
entry1.place(relx=0.55, rely=0.25)

# game 5
game_5 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_5.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_5, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 4
label_1 = ctk.CTkLabel(master=game_5, text=nameh_var4.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 1
label_1 = ctk.CTkLabel(master=game_5, text=nameh_var1.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 4
if os.path.exists('Images/' + nameh_var4.get() + '.png'):
    img4 = ctk.CTkImage(Image.open('Images/' + nameh_var4.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_5, image=img4, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_5, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 1
if os.path.exists('Images/' + nameh_var1.get() + '.png'):
    img1 = ctk.CTkImage(Image.open('Images/' + nameh_var1.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_5, image=img1, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_5, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_5, width=50, height=40, textvariable=goalh_var6)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_5, width=50, height=40, textvariable=goalh_var5)
entry1.place(relx=0.55, rely=0.25)

# game 6
game_6 = ctk.CTkFrame(master=frame_2, fg_color='green', width=1000, height=80)
game_6.pack(padx=20, pady=5)
# vs
label_1 = ctk.CTkLabel(master=game_6, text="vs",
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.49, rely=0.35)
# team 2
label_1 = ctk.CTkLabel(master=game_6, text=nameh_var2.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.2, rely=0.35)
# team 3
label_1 = ctk.CTkLabel(master=game_6, text=nameh_var3.get(),
                       font=('Arial', 16, 'bold'))
label_1.place(relx=0.72, rely=0.35)

# image team 2
if os.path.exists('Images/' + nameh_var2.get() + '.png'):
    img2 = ctk.CTkImage(Image.open('Images/' + nameh_var2.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_6, image=img2, text='')
    label_1.place(relx=0.3, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_6, image=unknown, text='')
    label_1.place(relx=0.3, rely=0.173)

# image team 3
if os.path.exists('Images/' + nameh_var3.get() + '.png'):
    img3 = ctk.CTkImage(Image.open('Images/' + nameh_var3.get() + '.png'), size=(60, 60))
    label_1 = ctk.CTkLabel(master=game_6, image=img3, text='')
    label_1.place(relx=0.64, rely=0.125)
else:
    label_1 = ctk.CTkLabel(master=game_6, image=unknown, text='')
    label_1.place(relx=0.64, rely=0.173)

# goale entries
entry1 = ctk.CTkEntry(master=game_6, width=50, height=40, textvariable=goalh_var7)
entry1.place(relx=0.4, rely=0.25)
entry1 = ctk.CTkEntry(master=game_6, width=50, height=40, textvariable=goalh_var8)
entry1.place(relx=0.55, rely=0.25)

#####
# Submit Button
submit_1 = ctk.CTkButton(master=frame_2, height=45, width=100, text="Submit", command=root.destroy)
submit_1.place(relx=0.915, rely=0.92)

root.mainloop()


# match clas
class Match:
    def __init__(self, team1, team2, score1=0, score2=0):
        self.team1 = team1
        self.team2 = team2
        self.score1 = score1
        self.score2 = score2


all_goalst1 = []
all_goalst2 = []

# play one match / count is for increasing the goals list
count = 0


def play_one_match(match):
    # Prompt the user to enter the scores for each team
    global count
    count = count + 1
    score1 = int(all_goalst1[count - 1])
    score2 = int(all_goalst2[count - 1])
    match.score1 = score1
    match.score2 = score2

    # Update the wins, losses, and draws for each team based on the scores
    if score1 > score2:
        match.team1.wins += 1
        match.team2.losses += 1
        match.team1.points += 3
    elif score1 < score2:
        match.team1.losses += 1
        match.team2.wins += 1
        match.team2.points += 3
    else:
        match.team1.draws += 1
        match.team2.draws += 1
        match.team1.points += 1
        match.team2.points += 1

    match.team1.goals_for += score1
    match.team2.goals_for += score2
    match.team1.goals_against += score2
    match.team2.goals_against += score1
    difference_team1 = score1 - score2
    difference_team2 = score2 - score1
    match.team1.goals_diff += difference_team1
    match.team2.goals_diff += difference_team2


# play the group matches
def play_groups_matches(groups):
    for group, team_list in groups.items():
        for i in range(len(team_list)):
            for j in range(i + 1, len(team_list)):
                team1 = team_list[i]
                team2 = team_list[j]
                match = Match(team1, team2)
                play_one_match(match)


# put all the goal entrys in two seperate lists

def create_goals():
    goal_t1g1 = int(goal_var1.get())
    all_goalst1.append(goal_t1g1)

    goal_t2g1 = int(goal_var2.get())
    all_goalst2.append(goal_t2g1)

    goal_t1g2 = int(goal_var3.get())
    all_goalst1.append(goal_t1g2)

    goal_t2g2 = int(goal_var4.get())
    all_goalst2.append(goal_t2g2)

    goal_t1g3 = int(goal_var5.get())
    all_goalst1.append(goal_t1g3)

    goal_t2g3 = int(goal_var6.get())
    all_goalst2.append(goal_t2g3)

    goal_t1g4 = int(goal_var7.get())
    all_goalst1.append(goal_t1g4)

    goal_t2g4 = int(goal_var8.get())
    all_goalst2.append(goal_t2g4)

    goal_t1g5 = int(goal_var9.get())
    all_goalst1.append(goal_t1g5)

    goal_t2g5 = int(goal_var10.get())
    all_goalst2.append(goal_t2g5)

    goal_t1g6 = int(goal_var11.get())
    all_goalst1.append(goal_t1g6)

    goal_t2g6 = int(goal_var12.get())
    all_goalst2.append(goal_t2g6)

    ######## group b

    goalb_t1g1 = int(goalb_var1.get())
    all_goalst1.append(goalb_t1g1)

    goalb_t2g1 = int(goalb_var2.get())
    all_goalst2.append(goalb_t2g1)

    goalb_t1g2 = int(goalb_var3.get())
    all_goalst1.append(goalb_t1g2)

    goalb_t2g2 = int(goalb_var4.get())
    all_goalst2.append(goalb_t2g2)

    goalb_t1g3 = int(goalb_var5.get())
    all_goalst1.append(goalb_t1g3)

    goalb_t2g3 = int(goalb_var6.get())
    all_goalst2.append(goalb_t2g3)

    goalb_t1g4 = int(goalb_var7.get())
    all_goalst1.append(goalb_t1g4)

    goalb_t2g4 = int(goalb_var8.get())
    all_goalst2.append(goalb_t2g4)

    goalb_t1g5 = int(goalb_var9.get())
    all_goalst1.append(goalb_t1g5)

    goalb_t2g5 = int(goalb_var10.get())
    all_goalst2.append(goalb_t2g5)

    goalb_t1g6 = int(goalb_var11.get())
    all_goalst1.append(goalb_t1g6)

    goalb_t2g6 = int(goalb_var12.get())
    all_goalst2.append(goalb_t2g6)

    ######## group c

    goalc_t1g1 = int(goalc_var1.get())
    all_goalst1.append(goalc_t1g1)

    goalc_t2g1 = int(goalc_var2.get())
    all_goalst2.append(goalc_t2g1)

    goalc_t1g2 = int(goalc_var3.get())
    all_goalst1.append(goalc_t1g2)

    goalc_t2g2 = int(goalc_var4.get())
    all_goalst2.append(goalc_t2g2)

    goalc_t1g3 = int(goalc_var5.get())
    all_goalst1.append(goalc_t1g3)

    goalc_t2g3 = int(goalc_var6.get())
    all_goalst2.append(goalc_t2g3)

    goalc_t1g4 = int(goalc_var7.get())
    all_goalst1.append(goalc_t1g4)

    goalc_t2g4 = int(goalc_var8.get())
    all_goalst2.append(goalc_t2g4)

    goalc_t1g5 = int(goalc_var9.get())
    all_goalst1.append(goalc_t1g5)

    goalc_t2g5 = int(goalc_var10.get())
    all_goalst2.append(goalc_t2g5)

    goalc_t1g6 = int(goalc_var11.get())
    all_goalst1.append(goalc_t1g6)

    goalc_t2g6 = int(goalc_var12.get())
    all_goalst2.append(goalc_t2g6)

    ######## group d

    goald_t1g1 = int(goald_var1.get())
    all_goalst1.append(goald_t1g1)

    goald_t2g1 = int(goald_var2.get())
    all_goalst2.append(goald_t2g1)

    goald_t1g2 = int(goald_var3.get())
    all_goalst1.append(goald_t1g2)

    goald_t2g2 = int(goald_var4.get())
    all_goalst2.append(goald_t2g2)

    goald_t1g3 = int(goald_var5.get())
    all_goalst1.append(goald_t1g3)

    goald_t2g3 = int(goald_var6.get())
    all_goalst2.append(goald_t2g3)

    goald_t1g4 = int(goald_var7.get())
    all_goalst1.append(goald_t1g4)

    goald_t2g4 = int(goald_var8.get())
    all_goalst2.append(goald_t2g4)

    goald_t1g5 = int(goald_var9.get())
    all_goalst1.append(goald_t1g5)

    goald_t2g5 = int(goald_var10.get())
    all_goalst2.append(goald_t2g5)

    goald_t1g6 = int(goald_var11.get())
    all_goalst1.append(goald_t1g6)

    goald_t2g6 = int(goald_var12.get())
    all_goalst2.append(goald_t2g6)

    ######## group e

    goale_t1g1 = int(goale_var1.get())
    all_goalst1.append(goale_t1g1)

    goale_t2g1 = int(goale_var2.get())
    all_goalst2.append(goale_t2g1)

    goale_t1g2 = int(goale_var3.get())
    all_goalst1.append(goale_t1g2)

    goale_t2g2 = int(goale_var4.get())
    all_goalst2.append(goale_t2g2)

    goale_t1g3 = int(goale_var5.get())
    all_goalst1.append(goale_t1g3)

    goale_t2g3 = int(goale_var6.get())
    all_goalst2.append(goale_t2g3)

    goale_t1g4 = int(goale_var7.get())
    all_goalst1.append(goale_t1g4)

    goale_t2g4 = int(goale_var8.get())
    all_goalst2.append(goale_t2g4)

    goale_t1g5 = int(goale_var9.get())
    all_goalst1.append(goale_t1g5)

    goale_t2g5 = int(goale_var10.get())
    all_goalst2.append(goale_t2g5)

    goale_t1g6 = int(goale_var11.get())
    all_goalst1.append(goale_t1g6)

    goale_t2g6 = int(goale_var12.get())
    all_goalst2.append(goale_t2g6)

    ######## group f

    goalf_t1g1 = int(goalf_var1.get())
    all_goalst1.append(goalf_t1g1)

    goalf_t2g1 = int(goalf_var2.get())
    all_goalst2.append(goalf_t2g1)

    goalf_t1g2 = int(goalf_var3.get())
    all_goalst1.append(goalf_t1g2)

    goalf_t2g2 = int(goalf_var4.get())
    all_goalst2.append(goalf_t2g2)

    goalf_t1g3 = int(goalf_var5.get())
    all_goalst1.append(goalf_t1g3)

    goalf_t2g3 = int(goalf_var6.get())
    all_goalst2.append(goalf_t2g3)

    goalf_t1g4 = int(goalf_var7.get())
    all_goalst1.append(goalf_t1g4)

    goalf_t2g4 = int(goalf_var8.get())
    all_goalst2.append(goalf_t2g4)

    goalf_t1g5 = int(goalf_var9.get())
    all_goalst1.append(goalf_t1g5)

    goalf_t2g5 = int(goalf_var10.get())
    all_goalst2.append(goalf_t2g5)

    goalf_t1g6 = int(goalf_var11.get())
    all_goalst1.append(goalf_t1g6)

    goalf_t2g6 = int(goalf_var12.get())
    all_goalst2.append(goalf_t2g6)

    ######## group g

    goalg_t1g1 = int(goalg_var1.get())
    all_goalst1.append(goalg_t1g1)

    goalg_t2g1 = int(goalg_var2.get())
    all_goalst2.append(goalg_t2g1)

    goalg_t1g2 = int(goalg_var3.get())
    all_goalst1.append(goalg_t1g2)

    goalg_t2g2 = int(goalg_var4.get())
    all_goalst2.append(goalg_t2g2)

    goalg_t1g3 = int(goalg_var5.get())
    all_goalst1.append(goalg_t1g3)

    goalg_t2g3 = int(goalg_var6.get())
    all_goalst2.append(goalg_t2g3)

    goalg_t1g4 = int(goalg_var7.get())
    all_goalst1.append(goalg_t1g4)

    goalg_t2g4 = int(goalg_var8.get())
    all_goalst2.append(goalg_t2g4)

    goalg_t1g5 = int(goalg_var9.get())
    all_goalst1.append(goalg_t1g5)

    goalg_t2g5 = int(goalg_var10.get())
    all_goalst2.append(goalg_t2g5)

    goalg_t1g6 = int(goalg_var11.get())
    all_goalst1.append(goalg_t1g6)

    goalg_t2g6 = int(goalg_var12.get())
    all_goalst2.append(goalg_t2g6)

    ######## group h

    goalh_t1g1 = int(goalh_var1.get())
    all_goalst1.append(goalh_t1g1)

    goalh_t2g1 = int(goalh_var2.get())
    all_goalst2.append(goalh_t2g1)

    goalh_t1g2 = int(goalh_var3.get())
    all_goalst1.append(goalh_t1g2)

    goalh_t2g2 = int(goalh_var4.get())
    all_goalst2.append(goalh_t2g2)

    goalh_t1g3 = int(goalh_var5.get())
    all_goalst1.append(goalh_t1g3)

    goalh_t2g3 = int(goalh_var6.get())
    all_goalst2.append(goalh_t2g3)

    goalh_t1g4 = int(goalh_var7.get())
    all_goalst1.append(goalh_t1g4)

    goalh_t2g4 = int(goalh_var8.get())
    all_goalst2.append(goalh_t2g4)

    goalh_t1g5 = int(goalh_var9.get())
    all_goalst1.append(goalh_t1g5)

    goalh_t2g5 = int(goalh_var10.get())
    all_goalst2.append(goalh_t2g5)

    goalh_t1g6 = int(goalh_var11.get())
    all_goalst1.append(goalh_t1g6)

    goalh_t2g6 = int(goalh_var12.get())
    all_goalst2.append(goalh_t2g6)

    play_groups_matches(groups)


create_goals()


# create a list for the best teams
def select_best_teams(groups):
    best_teams = {}

    # Sort the teams by points in ascending order
    for group, team_list in groups.items():
        best_teams[group] = []
        team_list.sort(key=lambda x: (x.points, x.goals_diff, x.goals_for), reverse=True)

        best_teams[group].append(team_list[0])
        best_teams[group].append(team_list[1])

    return best_teams


best_teams = select_best_teams(groups)


# create a list for the worst teams
def select_worst_teams(groups):
    worst_teams = {}

    # Sort the teams by points in ascending order
    for group, team_list in groups.items():
        worst_teams[group] = []
        team_list.sort(key=lambda x: (x.points, x.goals_diff, x.goals_for), reverse=True)

        worst_teams[group].append(team_list[2])
        worst_teams[group].append(team_list[3])

    return worst_teams


worst_teams = select_worst_teams(groups)