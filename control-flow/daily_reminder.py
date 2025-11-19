# daily_reminder.py
# Ask the user for one task, its priority, and whether it's time-bound.
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Use match-case to customize the base message depending on priority
match priority:
    case "high":
        base_msg = f"'{task}' is a high priority task."
    case "medium":
        base_msg = f"'{task}' is a medium priority task."
    case "low":
        base_msg = f"'{task}' is a low priority task."
    case _:
        base_msg = f"'{task}' has an unknown priority (treated as low)."

# Modify message if it's time-bound
if time_bound == "yes":
    # time-sensitive — immediate action required
    reminder = f"Reminder: {base_msg} It requires immediate attention today!"
else:
    # not time-sensitive
    reminder = f"Note: {base_msg} Consider completing it when you have free time."

print()
print(reminder)
print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
