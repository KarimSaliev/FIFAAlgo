print("Welcome to the World Cup program. First of all we need to create all the teams that you would like to participate"
      " enter their country and group you want them in:")

class Team:

    def __init__(self, country, group, wins=0, losses=0, draws=0, goalsF=0, goalsA=0, goalsD=0, points=0):

        # constructor that initializes the team with the given country and group
        self.country = country
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.goalsF = goalsF
        self.goalsA = goalsA
        self.goalsD = goalsD
        self.group = group
        self.points = points




def create_teams():

    valid_groups = ["A", "B", "C", "D", "E", "F", "G", "H"]
    for i in range(0, 32):
        # prompt the user to enter the name of the country
        country = input(f'Name of {i + 1} country:')
        while True:
            # prompt the user to enter the group of the country
            Group = input(f'Group of {i + 1} country:')
            if Group in valid_groups:
                # if the group is valid, break out of the loop
                break
            else:
                # if the group is not valid, display an error message
                print("Invalid group, please enter a valid group")

        # append the team to the groups list
        groups[Group].append(Team(country, Group))




class Match:
    def __init__(self, team1, team2, score1=0, score2=0):
        # constructor that initializes the match with the given teams and scores
        self.team1 = team1
        self.team2 = team2
        self.score1 = score1
        self.score2 = score2


def play_one_match(match):

    while True:
        # prompt the user to enter the result of the match
        result = input(f"Enter the result of the match between {match.team1.country} and {match.team2.country}: "
                       f"(format 'x:y' where x and y are integers.) ")
        try:
            # split the result string and convert the parts to integers
            score1, score2 = map(int, result.split(':'))
            if score1 >= 0 and score2 >= 0:
                # if the scores are non-negative integers, break out of the loop
                break
            else:
                # if the result string is not in the correct format, display an error message
                print("Invalid input, scores should be non-negative integers.")
        except ValueError:
            print("Invalid input, please enter the result in the format 'x:y' where x and y are integers.")


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

    match.team1.goalsF += score1
    match.team2.goalsF += score2
    match.team1.goalsA += score2
    match.team2.goalsA += score1
    difference_team1 = score1 - score2
    difference_team2 = score2 - score1
    match.team1.goalsD += difference_team1
    match.team2.goalsD += difference_team2


def play_groups_matches(groups):
    for group, team_list in groups.items():
        print(f"Group {group}:")
        # loop through all the teams in the groups
        for i in range(len(team_list)):
            for j in range(i + 1, len(team_list)):
                team1 = team_list[i]
                team2 = team_list[j]
                # create a match object for the teams
                match = Match(team1, team2)
                print("\n")
                print(f"{team1.country} vs {team2.country}")
                # get the result of the match from the user
                play_one_match(match)
        print()



def select_best_teams(groups):
    top_teams = []

    # loop through all the teams in the groups
    for group, team_list in groups.items():
        # Sort the teams by points in descending order and then by goals difference and then by goals scored
        team_list.sort(key=lambda x: (x.points, x.goalsD, x.goalsF), reverse=True)

        # append the top two teams of each group
        top_teams.append(team_list[0].country)
        top_teams.append(team_list[1].country)

    return top_teams





def knockout_stage(teams):

    # play_match function takes 2 teams as input and prompts the user to enter the result of the match
    # it then returns the winning team
    def play_match(team1, team2):

        while True:
            result = input(f'Enter the result of the match between {team1} and {team2}: ')
            try:
                team1_score, team2_score = map(int, result.split(':'))
                if (team1_score >= 0) and (team2_score >= 0):
                    break
                else:
                    print("Invalid input, scores should be non-negative integers.")
            except ValueError:
                print("Invalid input, please enter the result in the format 'x:y' where x and y are integers.")

        # determine the winning team
        if team1_score > team2_score:
            return team1
        else:
            return team2

    # play the first round of matches
    # we couldn't use a loop since different teams play against each other
    team1 = play_match(round_of_16_teams[0], round_of_16_teams[3])
    team2 = play_match(round_of_16_teams[4], round_of_16_teams[7])
    team3 = play_match(round_of_16_teams[8], round_of_16_teams[11])
    team4 = play_match(round_of_16_teams[12], round_of_16_teams[15])
    team5 = play_match(round_of_16_teams[5], round_of_16_teams[6])
    team6 = play_match(round_of_16_teams[1], round_of_16_teams[2])
    team7 = play_match(round_of_16_teams[9], round_of_16_teams[10])
    team8 = play_match(round_of_16_teams[13], round_of_16_teams[14])

    # print the winning teams of 16 round
    print(f'\n {team1} ,{team2} ,{team3} ,{team4} ,{team5} ,{team6} ,{team7} ,{team8} advance to the next round!')

    # The quarter-final teams
    quarter_final_teams = [team1, team2, team3, team4, team5, team6, team7, team8]
    # The semi-final teams,Third place team, The finals teams
    semi_final_teams = []
    third_place_game = []
    final_teams = []


    # Quarter-finals begins
    print("\n Quarter Finals")
    for i in range(0,len(quarter_final_teams),2):
        team1 = quarter_final_teams[i]
        team2 = quarter_final_teams[i+1]
        winner = play_match(team1,team2)
        semi_final_teams.append(winner)
        third_place_game.append(winner)

    print(f"\n {semi_final_teams} advance to the Semi-Finals round!")
    # The semi-final begins
    print("\n Semi-Finals!")
    for i in range(0,len(semi_final_teams),2):
        team1 = semi_final_teams[i]
        team2 = semi_final_teams[i+1]
        winner = play_match(team1,team2)
        final_teams.append(winner)
        third_place_game.remove(winner)

    print(f"\n{third_place_game} will play for 3rd place!")
    print(f"\n{final_teams} will play for Championship!")
    #The third place match
    # 3rd Place game
    print("\n3rd place Game!")
    print(f"{third_place_game[0]} vs {third_place_game[1]}")
    winner = play_match(third_place_game[0], third_place_game[1])
    print(f"{winner} wins 3rd place!\n")

    #The Finals Match
    print("1st place Game!")
    print(f"{final_teams[0]} vs {final_teams[1]}")
    winner = play_match(final_teams[0], final_teams[1])
    print(f"{winner} wins the World Cup!\n")


groups = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': []}
create_teams()
play_groups_matches(groups)
round_of_16_teams = select_best_teams(groups)
knockout_stage(round_of_16_teams)