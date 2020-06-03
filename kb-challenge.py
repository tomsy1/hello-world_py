import datetime
import pandas as pd
dt = datetime.datetime.today()


data = [
    {"Date": "01/06/2020",  "Swings": 350},
    {"Date": "02/06/2020",  "Swings": 370},
    {"Date": "03/06/2020", "Swings": 100},
]
df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])
max_swings = df['Swings'].max()
max_swings_date = df.iloc[df['Swings'].idxmax()]
total_swings = df['Swings'].sum()
days_in_month = 30
goal = 10000
goal_formatted = format(10000, ",d")
goal_average_daily_swings = round(goal / days_in_month)
current_day = dt.day
run_rate = round((total_swings / current_day)*days_in_month)
days_remaining = days_in_month - current_day
run_rate_goal = (((run_rate-goal)/goal)*100)+100
av_swings_day = (total_swings / current_day)




max_swings_date_formatted = (max_swings_date['Date'])

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
print ("The max number of swings in one day was: " + str(max_swings) + " which occured on " + max_swings_date_formatted.strftime("%A %d %B."))
print("Days remaining: " + str(days_remaining))


