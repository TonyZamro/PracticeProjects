import requests
import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup 
year = input('Enter a year:')
URL = f'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value={year}'

retrieve = requests.get(URL)
file_content = retrieve.text

status = retrieve.status_code
print(status)

#Generate a beautiful soup object

soup = BeautifulSoup(file_content, 'lxml')

month_one_data = []
month_two_data = []
month_three_data = []
month_four_data = []
month_six_data = []
year_one_data = []
year_two_data = []
year_three_data = []
year_five_data = []
year_seven_data = []
year_ten_data = []
year_twenty_data = []
year_thirty_data = []
dates = []



table = soup.find('tbody')
for row in table.find_all('tr'):
    column = row.find_all('td')
    date = row.find('time')
    dates.append(date.text)
    one_month = column[10].text
    month_one_data.append(one_month)
    two_month = column[11].text
    month_two_data.append(two_month)
    three_month = column[12].text
    month_three_data.append(three_month)
    four_month = column[13].text
    month_four_data.append(four_month)
    six_month = column[14].text
    month_six_data.append(six_month)
    one_year = column[15].text
    year_one_data.append(one_year)
    two_year = column[16].text
    year_two_data.append(two_year)
    three_year = column[17].text
    year_three_data.append(three_year)
    five_year = column[18].text
    year_five_data.append(five_year)
    seven_year = column[19].text
    year_seven_data.append(seven_year)
    ten_year = column[20].text
    year_ten_data.append(ten_year)
    twenty_year = column[21].text
    year_twenty_data.append(twenty_year)
    thirty_year = column[22].text
    year_thirty_data.append(thirty_year)
df = pd.DataFrame({'Date': dates ,'1 month': month_one_data, '2 month': month_two_data, '3 month': month_three_data, '4 month': month_four_data, '6 month':month_six_data, \
        '1 year': year_one_data, '2 year': year_two_data, '3 year': year_three_data, '5 year': year_five_data, '7 year': year_seven_data, \
             '10 year': year_ten_data, '20 year': year_twenty_data, '30 year': year_thirty_data }).set_index('Date')
#Print dataframe to ensure the correct values are displayed
print(df)
modded_df = df.iloc[1]
print(modded_df)


#Convert df to csv using to_csv function
df.to_csv('Yield_Curve_Data.csv')
# df_values = pd.read_csv('Yield_Curve_Data.csv')
# print(df_values)


