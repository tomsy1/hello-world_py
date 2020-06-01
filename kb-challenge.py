import datetime
dt = datetime.datetime.today()
#Average number of swings needed a day to reach 10,000



swing_count = {
    1:60,


}
days_in_month = 30
goal = 10000
goal_average_daily_swings = goal / days_in_month
total_swings = sum(swing_count.values())
current_day = dt.day
run_rate = (total_swings / current_day)*days_in_month
days_remaining = days_in_month - current_day
print("Goal number of swings: " + str(goal))
print("Average daily swings needed to reach goal: " + str(goal_average_daily_swings))
print("Total swings so far this month: " + str(total_swings))
print("Current run rate: " + str(run_rate))
print("Days remaining: " + str(days_remaining))


