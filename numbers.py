"""
        Demo using and formatting numbers
"""

# Convert input

allowence = float(input("How much is your allowence?   "))
snacks = float(input("Amount spent on snacks?   "))
video_games = float(input("Spent on video games?    "))


# Equations

spent = snacks + video_games

remaining = allowence - snacks - video_games


# Display 

print(f"You recieve {allowence: ,.2f}")
print(f"You spend{spent: ,.2f} a month.")
print(f"You have {remaining: ,.2f} left")


