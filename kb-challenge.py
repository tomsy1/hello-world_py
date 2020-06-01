import datetime
dt = datetime.datetime.today()
#Average number of swings needed a day to reach 10,000



swing_count = {
    1:120,


}
days_in_month = 30
goal = 10000
goal_formatted = format(10000, ",d")
goal_average_daily_swings = round(goal / days_in_month)
total_swings = sum(swing_count.values())
current_day = dt.day
run_rate = round((total_swings / current_day)*days_in_month)
days_remaining = days_in_month - current_day
print("Goal number of swings: " + str(goal_formatted))
print("Average daily swings needed to reach goal: " + str(goal_average_daily_swings))
print("Total swings so far this month: " + str(total_swings))
print("Current run rate: " + str(run_rate))
print("Days remaining: " + str(days_remaining))


