import datetime
dt = datetime.datetime.today()
#Average number of swings needed a day to reach 10,000



swing_count = {
    1:350,
    2: 370,


}
days_in_month = 30
goal = 10000
goal_formatted = format(10000, ",d")
goal_average_daily_swings = round(goal / days_in_month)
total_swings = sum(swing_count.values())
current_day = dt.day
run_rate = round((total_swings / current_day)*days_in_month)
days_remaining = days_in_month - current_day
run_rate_goal = (((run_rate-goal)/goal)*100)+100
av_swings_day = (total_swings / current_day)
print (av_swings_day)



print("=================================================")
if run_rate_goal < 95.0:
    print (str.upper("Work harder you cunt the Campbell can do better!"))
else:
    print (str.upper("Great work, you are on track!"))
print("=================================================")
print("Goal number of swings: " + str(goal_formatted))
print("Average daily swings needed to reach goal: " + str(goal_average_daily_swings))
print("Total swings so far this month: " + str(total_swings))
print("Average swings a day: " + str(av_swings_day))
print("Current run rate: " + str(run_rate))
print ("The current run rate is " + str(run_rate_goal) + "% of goal")
print("Days remaining: " + str(days_remaining))


