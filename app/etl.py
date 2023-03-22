import pandas as pd


netflix=pd.read_csv("Datasets/amazon_prime_titles.csv")
hulu=pd.read_csv("Datasets/hulu_titles.csv")
disney_plus=pd.read_csv("Datasets/disney_plus_titles.csv")
amazon_prime=pd.read_csv("Datasets/amazon_prime_titles.csv")

amazon_prime.insert(0,"id", ("a"+amazon_prime["show_id"]))

disney_plus.insert(0,"id", ("d"+disney_plus["show_id"]))

hulu.insert(0,"id", ("h"+hulu["show_id"]))

netflix.insert(0,"id", ("n"+amazon_prime["show_id"]))

amazon_prime['platform']='amazonPrime'; disney_plus['platform']='disney'; netflix['platform']='netflix'; hulu['platform']='hulu'

DF_Proyect = pd.concat([amazon_prime, netflix, disney_plus, hulu], axis=0)
DF_Proyect.reset_index(drop=True, inplace=True)

DF_Proyect.rating.fillna('g', inplace=True)

DF_Proyect['type'] = DF_Proyect['type'].str.lower()
DF_Proyect['title'] = DF_Proyect['title'].str.lower()
DF_Proyect['director'] = DF_Proyect['director'].str.lower()
DF_Proyect['cast'] = DF_Proyect['cast'].str.lower()
DF_Proyect['country'] = DF_Proyect['country'].str.lower()
DF_Proyect['date_added'] = DF_Proyect['date_added'].str.lower()
DF_Proyect['rating'] = DF_Proyect['rating'].str.lower()
DF_Proyect['listed_in'] = DF_Proyect['listed_in'].str.lower()
DF_Proyect['description'] = DF_Proyect['description'].str.lower()
DF_Proyect['platform'] = DF_Proyect['platform'].str.lower()

DF_Proyect['duration']=DF_Proyect['duration'].astype(str)

DF_Proyect['duration_int']= DF_Proyect['duration'].apply(lambda x:x.split()[0])
DF_Proyect['duration_type']=DF_Proyect['duration'].apply(lambda x:str(x.split()[1:]))
DF_Proyect['duration_type'] = DF_Proyect['duration_type'].apply(lambda x: x.replace("['min']",'min')) 
DF_Proyect['duration_type'] = DF_Proyect['duration_type'].apply(lambda x: x.replace("['Seasons']",'season')) 
DF_Proyect['duration_type'] = DF_Proyect['duration_type'].apply(lambda x: x.replace("['Season']",'season')) 

DF_Proyect=DF_Proyect.drop(['duration'], axis=1)

DF_Proyect["date_added"] = pd.to_datetime(DF_Proyect['date_added'], errors='coerce')
DF_Proyect['date_added'] = DF_Proyect['date_added'].dt.strftime("%Y-%m-%d")

d1 = pd.read_parquet("Datasets/ratings/1.gzip")
d2 = pd.read_parquet("Datasets/ratings/2.gzip")
d3 = pd.read_parquet("Datasets/ratings/3.gzip")
d4 = pd.read_parquet("Datasets/ratings/4.gzip")
d5 = pd.read_parquet("Datasets/ratings/5.gzip")
d6 = pd.read_parquet("Datasets/ratings/6.gzip")
d7 = pd.read_parquet("Datasets/ratings/7.gzip")
d8 = pd.read_parquet("Datasets/ratings/8.gzip")

df_todos = [d1,d2,d3,d4,d5,d6,d7,d8]
DF_ratings_all = pd.concat(df_todos)


DF_ratings_all.reset_index(drop=True, inplace=True)

DF_scoreprom = pd.DataFrame(DF_ratings_all.groupby(['movieId'],as_index=False)['rating'].mean())

DF_scoreprom.reset_index(drop=True)

df_r = pd.merge(left=DF_Proyect, right=DF_scoreprom, how='left', left_on='id', right_on='movieId')
df_r.drop(columns='movieId', inplace=True)

print(df_r)