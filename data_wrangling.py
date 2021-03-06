import pandas as pd

# sets display option
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 100)

# read from csv file
# Reads data from csv file and save to excel file - temporary disabled, to prevent loading big amount of data."
nypd_motor_vehicle_collisions = pd.read_csv('data/nypd_motor_vehicle_collisions.csv')
# print(nypd_motor_vehicle_collisions[['ZIP CODE']])
zip_code = nypd_motor_vehicle_collisions['ZIP CODE']
print(zip_code)
nypd_motor_vehicle_collisions_short = nypd_motor_vehicle_collisions.iloc[0:50000]
nypd_motor_vehicle_collisions_short.to_csv('data/short_data.csv')
print(nypd_motor_vehicle_collisions_short.shape)
nypd_motor_vehicle_collisions_short.to_excel('data/short_data.xlsx', index=0)

# nypd_motor_vehicle_collisions_short = pd.read_csv('data/nypd_motor_vehicle_collisions.csv')
# print(nypd_motor_vehicle_collisions_short.columns)
#
# # changing column names to lowercase
# nypd_motor_vehicle_collisions_short.columns = nypd_motor_vehicle_collisions_short.columns.str.lower()
# print(nypd_motor_vehicle_collisions_short.columns)
# print(f"Tyle jest danych :{nypd_motor_vehicle_collisions_short['collision_id'].count()}")
#
# # shows boroughs with highest amount of accidents
# most_accidents_boroughs = nypd_motor_vehicle_collisions_short.groupby('borough').agg(accidents_amount=('collision_id', 'count'),
#                                                                                      fatal_accidents=('number of persons killed', 'sum')
#                                                                                      ).sort_values(by='fatal_accidents',
#                                                                                                    ascending=False)
# print(most_accidents_boroughs)
#
# boroughs_collisions_df = nypd_motor_vehicle_collisions_short[['borough', 'collision_id']]
# brooklyn_collisions_df = boroughs_collisions_df[boroughs_collisions_df['borough'] == 'BROOKLYN']
# print(brooklyn_collisions_df['collision_id'].count())
#
#
#
#
"""Do zrobienia"""
# W kolumnie borough zmienic puste na "other"

# Wykresy

# Znale???? zastosowanie dla iloc i loc, i wyznaczania ramek danych

# dzielnice/ulice, kt??re maj?? powy??ej jakie?? ilo??ci wypadk??w

# Napisa?? funkcje dla wi??kszego profesjonalizmu

