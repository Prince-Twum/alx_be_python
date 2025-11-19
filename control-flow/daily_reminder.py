task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Match-case for priority
match priority:
    case "high":
        pr = "high"
    case "medium":
        pr = "medium"
    case "low":
        pr = "low"
    case _:
        pr = "low"   # default if invalid

# REQUIRED PRINT FORMATS BELOW
if time_bound == "yes":
    print(f"Reminder: '{task}' is a {pr} priority task that requires immediate attention today!")
else:
    print(f"Reminder: '{task}' is a {pr} priority task. Consider completing it when you have free time.")
