import tkinter
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("1250x703")
app.title("Tornament Manager")


# create team class
class Team():

    def __init__(self, country, group, goals_for=0, wins=0, losses=0, draws=0, points=0, goals_against=0, goals_diff=0):
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.points = points
        self.country = country
        self.group = group
        self.goals_for = goals_for
        self.goals_against = goals_against
        self.goals_diff = goals_diff


# to use the entrys as input
groupa_var1 = ctk.StringVar()
namea_var1 = ctk.StringVar()
namea_var2 = ctk.StringVar()
namea_var3 = ctk.StringVar()
namea_var4 = ctk.StringVar()

groupb_var1 = ctk.StringVar()
nameb_var1 = ctk.StringVar()
nameb_var2 = ctk.StringVar()
nameb_var3 = ctk.StringVar()
nameb_var4 = ctk.StringVar()

groupc_var1 = ctk.StringVar()
namec_var1 = ctk.StringVar()
namec_var2 = ctk.StringVar()
namec_var3 = ctk.StringVar()
namec_var4 = ctk.StringVar()

groupd_var1 = ctk.StringVar()
named_var1 = ctk.StringVar()
named_var2 = ctk.StringVar()
named_var3 = ctk.StringVar()
named_var4 = ctk.StringVar()

groupe_var1 = ctk.StringVar()
namee_var1 = ctk.StringVar()
namee_var2 = ctk.StringVar()
namee_var3 = ctk.StringVar()
namee_var4 = ctk.StringVar()

groupf_var1 = ctk.StringVar()
namef_var1 = ctk.StringVar()
namef_var2 = ctk.StringVar()
namef_var3 = ctk.StringVar()
namef_var4 = ctk.StringVar()

groupg_var1 = ctk.StringVar()
nameg_var1 = ctk.StringVar()
nameg_var2 = ctk.StringVar()
nameg_var3 = ctk.StringVar()
nameg_var4 = ctk.StringVar()

grouph_var1 = ctk.StringVar()
nameh_var1 = ctk.StringVar()
nameh_var2 = ctk.StringVar()
nameh_var3 = ctk.StringVar()
nameh_var4 = ctk.StringVar()

# create a list to put in the team names
teams = []


def create_teams():
    group = 'A'
    name = namea_var1.get()
    teams.append(Team(name, group))
    name = namea_var2.get()
    teams.append(Team(name, group))
    name = namea_var3.get()
    teams.append(Team(name, group))
    name = namea_var4.get()
    teams.append(Team(name, group))

    group = 'B'
    name = nameb_var1.get()
    teams.append(Team(name, group))
    name = nameb_var2.get()
    teams.append(Team(name, group))
    name = nameb_var3.get()
    teams.append(Team(name, group))
    name = nameb_var4.get()
    teams.append(Team(name, group))

    group = 'C'
    name = namec_var1.get()
    teams.append(Team(name, group))
    name = namec_var2.get()
    teams.append(Team(name, group))
    name = namec_var3.get()
    teams.append(Team(name, group))
    name = namec_var4.get()
    teams.append(Team(name, group))

    group = 'D'
    name = named_var1.get()
    teams.append(Team(name, group))
    name = named_var2.get()
    teams.append(Team(name, group))
    name = named_var3.get()
    teams.append(Team(name, group))
    name = named_var4.get()
    teams.append(Team(name, group))

    group = 'E'
    name = namee_var1.get()
    teams.append(Team(name, group))
    name = namee_var2.get()
    teams.append(Team(name, group))
    name = namee_var3.get()
    teams.append(Team(name, group))
    name = namee_var4.get()
    teams.append(Team(name, group))

    group = 'F'
    name = namef_var1.get()
    teams.append(Team(name, group))
    name = namef_var2.get()
    teams.append(Team(name, group))
    name = namef_var3.get()
    teams.append(Team(name, group))
    name = namef_var4.get()
    teams.append(Team(name, group))

    group = 'G'
    name = nameg_var1.get()
    teams.append(Team(name, group))
    name = nameg_var2.get()
    teams.append(Team(name, group))
    name = nameg_var3.get()
    teams.append(Team(name, group))
    name = nameg_var4.get()
    teams.append(Team(name, group))

    group = 'H'
    name = nameh_var1.get()
    teams.append(Team(name, group))
    name = nameh_var2.get()
    teams.append(Team(name, group))
    name = nameh_var3.get()
    teams.append(Team(name, group))
    name = nameh_var4.get()
    teams.append(Team(name, group))


def asg_groups():
    groups = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': []}
    for team in teams:
        groups[team.group].append(team)
    return groups


frame_1 = ctk.CTkFrame(master=app, height=80, width=400)
frame_1.pack(pady=20)

label_1 = ctk.CTkLabel(master=frame_1, text="Please fill in the competing teams.",
                       font=('Arial', 16, 'bold'))
label_1.pack(padx=10, pady=10)

frame_2 = ctk.CTkFrame(master=app, fg_color='gray17')
frame_2.pack(pady=5, padx=20, fill="both", expand=True)

############
# Group A
group_a = ctk.CTkFrame(master=frame_2, fg_color='green', width=400, height=120)
group_a.place(relx=0.1, rely=0.05)
label_a = ctk.CTkLabel(master=group_a, text='Group\nA', font=('Arial', 16, 'bold'))
label_a.place(relx=0.06, rely=.3)

# Entry 1
entry = ctk.CTkEntry(master=group_a, width=300, height=29, textvariable=namea_var1)
entry.place(relx=0.24, rely=0)

# Entry 2
entry = ctk.CTkEntry(master=group_a, width=300, height=29, textvariable=namea_var2)
entry.place(relx=0.24, rely=0.25)

# Entry 3
entry = ctk.CTkEntry(master=group_a, width=300, height=29, textvariable=namea_var3)
entry.place(relx=0.24, rely=0.5)

# Entry 4
entry = ctk.CTkEntry(master=group_a, width=300, height=29, textvariable=namea_var4)
entry.place(relx=0.24, rely=0.75)

############
# Group B
group_b = ctk.CTkFrame(master=frame_2, fg_color='green', width=400, height=120)
group_b.place(relx=0.58, rely=0.05)
label_b = ctk.CTkLabel(master=group_b, text='Group\nB', font=('Arial', 16, 'bold'))
label_b.place(relx=0.06, rely=.3)

# Entry 1
entry = ctk.CTkEntry(master=group_b, width=300, height=29, textvariable=nameb_var1)
entry.place(relx=0.24, rely=0)

# Entry 2
entry = ctk.CTkEntry(master=group_b, width=300, height=29, textvariable=nameb_var2)
entry.place(relx=0.24, rely=0.25)

# Entry 3
entry = ctk.CTkEntry(master=group_b, width=300, height=29, textvariable=nameb_var3)
entry.place(relx=0.24, rely=0.5)

# Entry 4
entry = ctk.CTkEntry(master=group_b, width=300, height=29, textvariable=nameb_var4)
entry.place(relx=0.24, rely=0.75)

############
# Group C
group_c = ctk.CTkFrame(master=frame_2, fg_color='green', width=400, height=120)
group_c.place(relx=0.1, rely=0.26)
label_c = ctk.CTkLabel(master=group_c, text='Group\nC', font=('Arial', 16, 'bold'))
label_c.place(relx=0.06, rely=.3)

# Entry 1
entry = ctk.CTkEntry(master=group_c, width=300, height=29, textvariable=namec_var1)
entry.place(relx=0.24, rely=0)

# Entry 2
entry = ctk.CTkEntry(master=group_c, width=300, height=29, textvariable=namec_var2)
entry.place(relx=0.24, rely=0.25)

# Entry 3
entry = ctk.CTkEntry(master=group_c, width=300, height=29, textvariable=namec_var3)
entry.place(relx=0.24, rely=0.5)

# Entry 4
entry = ctk.CTkEntry(master=group_c, width=300, height=29, textvariable=namec_var4)
entry.place(relx=0.24, rely=0.75)

############
# Group D
group_d = ctk.CTkFrame(master=frame_2, fg_color='green', width=400, height=120)
group_d.place(relx=0.58, rely=0.26)
label_d = ctk.CTkLabel(master=group_d, text='Group\nD', font=('Arial', 16, 'bold'))
label_d.place(relx=0.06, rely=.3)

# Entry 1
entry = ctk.CTkEntry(master=group_d, width=300, height=29, textvariable=named_var1)
entry.place(relx=0.24, rely=0)

# Entry 2
entry = ctk.CTkEntry(master=group_d, width=300, height=29, textvariable=named_var2)
entry.place(relx=0.24, rely=0.25)

# Entry 3
entry = ctk.CTkEntry(master=group_d, width=300, height=29, textvariable=named_var3)
entry.place(relx=0.24, rely=0.5)

# Entry 4
entry = ctk.CTkEntry(master=group_d, width=300, height=29, textvariable=named_var4)
entry.place(relx=0.24, rely=0.75)

############
# Group E
group_e = ctk.CTkFrame(master=frame_2, fg_color='green', width=400, height=120)
group_e.place(relx=0.1, rely=0.47)
label_e = ctk.CTkLabel(master=group_e, text='Group\nE', font=('Arial', 16, 'bold'))
label_e.place(relx=0.06, rely=.3)

# Entry 1
entry = ctk.CTkEntry(master=group_e, width=300, height=29, textvariable=namee_var1)
entry.place(relx=0.24, rely=0)

# Entry 2
entry = ctk.CTkEntry(master=group_e, width=300, height=29, textvariable=namee_var2)
entry.place(relx=0.24, rely=0.25)

# Entry 3
entry = ctk.CTkEntry(master=group_e, width=300, height=29, textvariable=namee_var3)
entry.place(relx=0.24, rely=0.5)

# Entry 4
entry = ctk.CTkEntry(master=group_e, width=300, height=29, textvariable=namee_var4)
entry.place(relx=0.24, rely=0.75)

############
# Group F
group_f = ctk.CTkFrame(master=frame_2, fg_color='green', width=400, height=120)
group_f.place(relx=0.58, rely=0.47)
label_f = ctk.CTkLabel(master=group_f, text='Group\nF', font=('Arial', 16, 'bold'))
label_f.place(relx=0.06, rely=.3)

# Entry 1
entry = ctk.CTkEntry(master=group_f, width=300, height=29, textvariable=namef_var1)
entry.place(relx=0.24, rely=0)

# Entry 2
entry = ctk.CTkEntry(master=group_f, width=300, height=29, textvariable=namef_var2)
entry.place(relx=0.24, rely=0.25)

# Entry 3
entry = ctk.CTkEntry(master=group_f, width=300, height=29, textvariable=namef_var3)
entry.place(relx=0.24, rely=0.5)

# Entry 4
entry = ctk.CTkEntry(master=group_f, width=300, height=29, textvariable=namef_var4)
entry.place(relx=0.24, rely=0.75)

############
# Group G
group_g = ctk.CTkFrame(master=frame_2, fg_color='green', width=400, height=120)
group_g.place(relx=0.1, rely=0.68)
label_g = ctk.CTkLabel(master=group_g, text='Group\nG', font=('Arial', 16, 'bold'))
label_g.place(relx=0.06, rely=.3)

# Entry 1
entry = ctk.CTkEntry(master=group_g, width=300, height=29, textvariable=nameg_var1)
entry.place(relx=0.24, rely=0)

# Entry 2
entry = ctk.CTkEntry(master=group_g, width=300, height=29, textvariable=nameg_var2)
entry.place(relx=0.24, rely=0.25)

# Entry 3
entry = ctk.CTkEntry(master=group_g, width=300, height=29, textvariable=nameg_var3)
entry.place(relx=0.24, rely=0.5)

# Entry 4
entry = ctk.CTkEntry(master=group_g, width=300, height=29, textvariable=nameg_var4)
entry.place(relx=0.24, rely=0.75)

############
# Group H
group_h = ctk.CTkFrame(master=frame_2, fg_color='green', width=400, height=120)
group_h.place(relx=0.58, rely=0.68)
label_h = ctk.CTkLabel(master=group_h, text='Group\nH', font=('Arial', 16, 'bold'))
label_h.place(relx=0.06, rely=.3)

# Entry 1
entry = ctk.CTkEntry(master=group_h, width=300, height=29, textvariable=nameh_var1)
entry.place(relx=0.24, rely=0)

# Entry 2
entry = ctk.CTkEntry(master=group_h, width=300, height=29, textvariable=nameh_var2)
entry.place(relx=0.24, rely=0.25)

# Entry 3
entry = ctk.CTkEntry(master=group_h, width=300, height=29, textvariable=nameh_var3)
entry.place(relx=0.24, rely=0.5)

# Entry 4
entry = ctk.CTkEntry(master=group_h, width=300, height=29, textvariable=nameh_var4)
entry.place(relx=0.24, rely=0.75)

#####
# Submit Button
submit_1 = ctk.CTkButton(master=frame_2, height=45, width=100, text="Submit", command=app.destroy)
submit_1.place(relx=0.915, rely=0.92)

app.mainloop()

create_teams()
groups = asg_groups()