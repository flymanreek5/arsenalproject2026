import pandas as pd

def analyze_premier_league_2025():
    # Data based on the 2025/26 Premier League final standings
    data = [
        {"Pos": 1, "Team": "Arsenal", "P": 38, "W": 26, "D": 7, "L": 5, "GF": 71, "GA": 27, "Pts": 85},
        {"Pos": 2, "Team": "Man City", "P": 38, "W": 23, "D": 9, "L": 6, "GF": 77, "GA": 35, "Pts": 78},
        {"Pos": 3, "Team": "Man Utd", "P": 38, "W": 20, "D": 11, "L": 7, "GF": 69, "GA": 50, "Pts": 71},
        {"Pos": 4, "Team": "Aston Villa", "P": 38, "W": 19, "D": 8, "L": 11, "GF": 56, "GA": 49, "Pts": 65},
        {"Pos": 5, "Team": "Liverpool", "P": 38, "W": 17, "D": 9, "L": 12, "GF": 63, "GA": 53, "Pts": 60},
        {"Pos": 6, "Team": "Bournemouth", "P": 38, "W": 13, "D": 18, "L": 7, "GF": 58, "GA": 54, "Pts": 57},
        {"Pos": 7, "Team": "Sunderland", "P": 38, "W": 14, "D": 12, "L": 12, "GF": 42, "GA": 48, "Pts": 54},
        {"Pos": 8, "Team": "Brighton", "P": 38, "W": 14, "D": 11, "L": 13, "GF": 52, "GA": 46, "Pts": 53},
        {"Pos": 9, "Team": "Brentford", "P": 38, "W": 14, "D": 11, "L": 13, "GF": 55, "GA": 52, "Pts": 53},
        {"Pos": 10, "Team": "Chelsea", "P": 38, "W": 14, "D": 10, "L": 14, "GF": 58, "GA": 52, "Pts": 52},
        {"Pos": 11, "Team": "Fulham", "P": 38, "W": 15, "D": 7, "L": 16, "GF": 47, "GA": 51, "Pts": 52},
        {"Pos": 12, "Team": "Newcastle", "P": 38, "W": 14, "D": 7, "L": 17, "GF": 53, "GA": 55, "Pts": 49},
        {"Pos": 13, "Team": "Everton", "P": 38, "W": 13, "D": 10, "L": 15, "GF": 47, "GA": 50, "Pts": 49},
        {"Pos": 14, "Team": "Leeds Utd", "P": 38, "W": 11, "D": 14, "L": 13, "GF": 49, "GA": 56, "Pts": 47},
        {"Pos": 15, "Team": "Crystal Palace", "P": 38, "W": 11, "D": 12, "L": 15, "GF": 41, "GA": 51, "Pts": 45},
        {"Pos": 16, "Team": "Notts Forest", "P": 38, "W": 11, "D": 11, "L": 16, "GF": 48, "GA": 51, "Pts": 44},
        {"Pos": 17, "Team": "Tottenham", "P": 38, "W": 10, "D": 11, "L": 17, "GF": 48, "GA": 57, "Pts": 41},
        {"Pos": 18, "Team": "West Ham", "P": 38, "W": 10, "D": 9, "L": 19, "GF": 46, "GA": 65, "Pts": 39},
        {"Pos": 19, "Team": "Burnley", "P": 38, "W": 4, "D": 10, "L": 24, "GF": 38, "GA": 75, "Pts": 22},
        {"Pos": 20, "Team": "Wolves", "P": 38, "W": 3, "D": 11, "L": 24, "GF": 27, "GA": 68, "Pts": 20}
    ]

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Calculate Goal Difference (GD)
    df["GD"] = df["GF"] - df["GA"]

    # Reorder columns to standard football table format
    df = df[["Pos", "Team", "P", "W", "D", "L", "GF", "GA", "GD", "Pts"]]

    print("=" * 65)
    print("       ENGLISH PREMIER LEAGUE 2025/26 FINAL STANDINGS")
    print("=" * 65)
    print(df.to_string(index=False))
    print("=" * 65)

    # Highlighting key zones
    print("\n🏆 **Champions:** Arsenal (85 Pts)")
    print("🇪🇺 **Champions League Spots:** Arsenal, Man City, Man Utd, Aston Villa")
    print("🔴 **Relegated Teams:** West Ham, Burnley, Wolves\n")

if __name__ == "__main__":
    analyze_premier_league_2025()