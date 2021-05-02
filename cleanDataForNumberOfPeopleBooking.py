# cleaning data
import pandas as pd


df = pd.read_csv('hotel_bookings.csv',
                 parse_dates= {"date" : ["arrival_date_year","arrival_date_month","arrival_date_day_of_month"]},
                 keep_date_col=True)
print(df.head())

to_drop = ['reservation_status_date',
           'total_of_special_requests',
           'required_car_parking_spaces',
           'adr',
           'customer_type',
           'days_in_waiting_list',
           'company',
           'agent',
           'deposit_type',
           'booking_changes',
           'assigned_room_type',
           'reserved_room_type',
           'previous_bookings_not_canceled',
           'previous_cancellations',
           'is_repeated_guest',
           'distribution_channel',
           'meal',
           'babies',
           'children',
           'stays_in_week_nights',
           'stays_in_weekend_nights',
           'lead_time',
           'is_canceled']

df.drop(to_drop, inplace=True, axis=1)
df = df[df.reservation_status != 'Canceled']
groupbydate = df.groupby("date")["adults"].count()
#groupbydate.to_csv(r'C:\Users\calvi\Documents\College\UNCC\Spring 2021\ITSC 3155\Final Project\Python code\hotelgrouped.csv')

#setting up for line chart