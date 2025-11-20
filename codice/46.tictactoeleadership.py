def load_leaderboard(filename):
    leaderboard = {}
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        index = 1  # skip header

        while index < len(lines):
            line = lines[index].strip()
            parts = line.split(",")

            name = parts[0].strip()
            wins = int(parts[1])
            leaderboard[name] = wins

            index += 1

    except FileNotFoundError:
        print("Leaderboard file not found. Starting new leaderboard.")
    return leaderboard

def update_leaderboard(filename, leaderboard, winner):
    if winner in leaderboard:
        leaderboard[winner] += 1
    else:
        leaderboard[winner] = 1

    try:
        with open(filename, "w") as f:
            f.write("player,wins\n")  # header
            for name in leaderboard:
                f.write(name + "," + str(leaderboard[name]) + "\n")
    except Exception as e:
        print("Error writing leaderboard:", e)

        