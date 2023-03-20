import pandas as pd


def etl(df1, df2, df3, df4):
    # The 4 csv are imported for create the dataframes

    netflix=df1
    hulu=df2
    disney_plus=df3
    amazon_prime=df4
 
        #'id' field 
    amazon_prime.insert(0,"id", ("a"+amazon_prime["show_id"]))

    disney_plus.insert(0,"id", ("d"+disney_plus["show_id"]))

    hulu.insert(0,"id", ("h"+hulu["show_id"]))

    netflix.insert(0,"id", ("n"+amazon_prime["show_id"]))

        #'platform' field
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
    DF_Proyect['duration_type'] = DF_Proyect['duration_type'].str.lower()

    DF_Proyect['duration']=DF_Proyect['duration'].astype(str)

    DF_Proyect['duration_int']= DF_Proyect['duration'].apply(lambda x:x.split()[0])
    DF_Proyect['duration_type']=DF_Proyect['duration'].apply(lambda x:str(x.split()[1:]))


    #Remove duration column
    DF_Proyect=DF_Proyect.drop(['duration'], axis=1)

    DF_Proyect["date_added"] = pd.to_datetime(DF_Proyect['date_added'], errors='coerce')
    DF_Proyect['date_added'] = DF_Proyect['date_added'].dt.strftime("%Y-%m-%d")



 
    return DF_Proyect


netflix=pd.read_csv("Datasets\\amazon_prime_titles.csv")
hulu=pd.read_csv("Datasets\\hulu_titles.csv")
disney_plus=pd.read_csv("Datasets\\disney_plus_titles.csv")
amazon_prime=pd.read_csv("Datasets\\amazon_prime_titles.csv")

DF_Total = etl(netflix, hulu, disney_plus, amazon_prime)

