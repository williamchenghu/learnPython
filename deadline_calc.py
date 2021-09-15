from datetime import datetime

user_input = input("Hi, specify your goal and the deadline (DD.MM.YYYY). Separate them with colon.\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
current_date = datetime.today()
remaining_time = deadline_date - current_date

print(f"Hi, you still have {remaining_time.days} days to reach your goal of {goal}!")
