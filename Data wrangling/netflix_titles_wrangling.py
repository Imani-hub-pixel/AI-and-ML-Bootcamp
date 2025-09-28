"""
Title:Data wrangling project
Name:Faith chepngeno
date:28 september 2025
"""
import pandas as pd
import numpy as np
import datetime as dt
df=pd.read_csv(r"C:\Users\faith\OneDrive\Desktop\AI and ML Bootcamp\Data wrangling\netflix_titles.csv")
df
df.info()
print("Shape of the dataset (R x C):", df.shape)
print("Columns in the dataset:\n", df.columns.tolist())
print("Data types:\n", df.dtypes)
print("Missing values per column:\n", df.isnull().sum())
print("Number of duplicate rows:", df.duplicated().sum())

#structuring
#convert date_added to datetime
df['date_added']=pd.to_datetime(df['date_added'],format='mixed')
#separating the duration column into two columns of the value and unit
df[['duration_value','duration_unit']]=df['duration'].str.extract(r'(\d+)\s*(\w+)')
#change the duration value into numric
df['duration_value']=pd.to_numeric(df['duration_value'])
print(df[['duration_value','duration_unit']])

#Categorizing the show type into movies and tv shows(kids,teens,adults,)
#Categorizing ratings
kids = ["G","TV-Y","TV-G","TV-Y7"]
teens = ["PG","TV-PG","TV-Y7-FV","PG-13","TV-14"]
adults = ["R","NC-17","TV-MA"]

def categorize_rating(x):
    if x in kids:
        return "Kids"
    elif x in teens:
        return "Teens"
    elif x in adults:
        return "Adults"
    else:
        return "Unrated"

df["rating_group"] = df["rating"].apply(categorize_rating)
print(df[["rating","rating_group"]].head())

#Impute director values by using relationsip between cast and director
df['dir_cast']=df['director']+'---'+df['cast']
counts=df['dir_cast'].value_counts()#counts unique values
filtered_counts = counts[counts >= 3] #checks if repeated 3 or more times
filtered_values = filtered_counts.index #gets the values i.e. names
lst_dir_cast = list(filtered_values) #convert to list
dict_direcast = dict()
for i in lst_dir_cast :
    director,cast = i.split('---')
    dict_direcast[director]=cast
for i in range(len(dict_direcast)):
    df.loc[(df['director'].isna()) & (df['cast'] == list(dict_direcast.items())[i][1]),'director'] =list(dict_direcast.items())[i][0]
print(df['director'])

#Dealing with null values on the director column and making them not given
if df['director'].isnull().sum() > 0:
    df['director'] = df['director'].replace(r'^\s*$', np.nan, regex=True)
    df['director'] = df['director'].astype(str).str.replace('\u00A0', ' ', regex=False).str.strip()
    df['director'] = df['director'].replace('nan', np.nan)
    df.loc[df['director'].isna(), 'director'] = 'not given'
    df['director'].fillna('not given')
else:
    print(f"{df["director"]}")
print(df['director'])

#cleaning
print("Duplicated rows before cleaning:", df.duplicated().sum())
df=df.drop_duplicates()

#Use directors to fill missing countries
directors = df['director']
countries = df['country']
#pair each director with their country use zip() to get an iterator of tuples
pairs = zip(directors, countries)
# Convert the list of tuples into a dictionary
dir_cntry = dict(list(pairs))
# Director matched to Country values used to fill in null country values
for i in range(len(dir_cntry)): 
    df.loc[(df['country'].isna()) & (df['director'] == list(dir_cntry.items())[i][0]),'country'] = list(dir_cntry.items())[i][1]
print(df['country'])
# Assign Not Given to all other country fields
df.loc[df['country'].isna(),'country'] = 'Not Given'
# Assign Not Given to all other fields
df.loc[df['cast'].isna(), 'cast'] = 'Not Given'
print(df['cast'])


# dropping other row records that are null
df.drop(df[df['date_added'].isna()].index,axis=0)
df.drop(df[df['rating'].isna()].index,axis=0)
df.drop(df[df['duration_value'].isna()].index,axis=0)
df.drop(df[df['duration_unit'].isna()].index,axis=0)
#Errors
# check if there are any added_dates that come before release_year

sum(df['date_added'].dt.year < df['release_year'])
df.loc[(df['date_added'].dt.year < df['release_year']),['date_added','release_year']]
#There are 4 records with inconsistencies
#correcting the inconsistencies by replacing the release_year with the year from date_added
df.loc[(df['date_added'].dt.year < df['release_year']),'release_year']=df['date_added'].dt.year
# sample some of the records and check that they have been accurately replaced
df.iloc[[1551,1696,2920,3168]]
#Confirm that no more release_year inconsistencies
sum(df['date_added'].dt.year < df['release_year'])
