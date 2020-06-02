import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('KB Swings').sheet1

col_vals = sheet.col_values(1)
# sum of list
col_sum = sum(col_vals)
#data = sheet.get_all_values()
#headers = data.pop()
#df = pd.DataFrame(data)
#print(df.head())
#print(df.shape)

#first_column = df.iloc[:, 1]
#print((first_column), he
#print(df.head())
