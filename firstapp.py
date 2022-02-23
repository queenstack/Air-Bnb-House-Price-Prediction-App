
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image

image=Image.open('pillow-bed.jpg')
st.image(image,caption='welcome')

st.write(""" AIRBNB HOUSE PRICE PREDICT APP!"""
)


model=pickle.load(open('rfmodel(rf).pkl','rb'))

rfscaler=pickle.load(open('rfscaler.pkl','rb'))



st.sidebar.header('User input parameters')

def user_input_features():
    Room_type=st.sidebar.selectbox('Room type',('Private room','Entire room','Shared room'))
    
    Region_hood=st.sidebar.selectbox('Region',('North Region','Central Region','East Region','West Region'))
   
     
   
        
    Host_id=st.number_input('what is the host ID')
    host_list_count=st.number_input('Host listing count')
    longitude=st.number_input('Building longitudinal location')
    latitude=st.number_input('Building latitudinal location')

          
    minimum_nights=st.number_input('How many nights will you be staying for')
    availability=st.number_input('For how many days is the building available')
    last_rev_month=st.number_input('On which month was the last review',max_value=12,
                                                                    min_value=1,step=1) 
    last_rev_year=st.number_input('On which year was the last review',max_value=2022,
                                                                    min_value=2012,step=1)
    last_rev_day=st.number_input('On what day was the last review',max_value=31,
                                                                    min_value=1,step=1)
    No_reviews=st.number_input('No of reviews recieved')
    reviews_per_month=st.number_input('How many reviews per month')
    
    
    if Room_type=='Entire home/Apt':
        Entire=1
        Private=0
        Shared=0

    if Room_type=='Private room':
        Entire=0
        Private=1
        Shared=0    
      
    if Room_type=='Shared room':
        Entire=0
        Private=0
        Shared=1
        
    if Region_hood=='Central Region':
        central=1
        North=0
        East=0
        West=0
        North_East=0
        
    if Region_hood=='North Region':
        central=0
        North=1
        East=0
        West=0
        North_East=0
    
    if Region_hood=='East Region':
        central=0
        North=0
        East=1
        West=0
        North_East=0
        
    if Region_hood=='West Region':
        central=0
        North=0
        East=0
        West=1
        North_East=0 
        
    if Region_hood=='North_East Region':
        central=0
        North=0
        East=0
        West=0
        North_East=1   
        
    data={'latitude':latitude,
          'host_id':Host_id,
         'longitude':longitude,
         'last_review_month':last_rev_month,
         'last_review_year':last_rev_year,
         'last_review_day':last_rev_day,
         'reviews_per_month':reviews_per_month,
          'minimum_nights':minimum_nights,
          'number_of_reviews':No_reviews,
          'calculated_host_listings_counts':host_list_count,
          'availiability_365':availability,
          'room_type_private room':Private,
          'room_type_shared_room':Shared,
         'neighbourhood_group_west Region':West,
          'neighbourhood_group_East Region':East,
         'neighbourhood_group_North_East Region':North_East,
         'neighbourhood_group_North Region':North
         }
    
    features =pd.DataFrame(data,index=[0])
    return features
    
input_df=user_input_features()
input_df=rfscaler.transform(input_df)
    
if st.button('PREDICT'):
    result=model.predict(input_df)
    st.write(f'This room will cost you $',int(result[0]))
    
    
