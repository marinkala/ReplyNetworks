import pandas as pd
import numpy as np
import ast
import collections as c
import matplotlib.pyplot as plt

convs=pd.read_csv('../data/bbAllFullConvosMoreAWCorrectTimeZone.csv',sep=';')
convs.allNames=convs.allNames.apply(lambda x: ast.literal_eval(x))
sup=pd.read_csv('../data/bbContextOntopicRepliesBothSidesDF.csv',sep=';')

for i in xrange(5):
    userCol='convoUser'+str(i)
    convs[userCol]=convs.allNames.apply(lambda x: x[i] if len(x)>i else 0)

for i in xrange(5):
    userCol='convoUser'+str(i)
    followCol='followersUser'+str(i)
    friendCol='friendsUser'+str(i)
    faveCol='favesUser'+str(i)
    tweetCount='tweetCountUser'+str(i)
    convs[followCol]=0
    convs[friendCol]=0
    convs[faveCol]=0
    convs[tweetCount]=0
    #temp=pd.merge(left=convs, right=sup[['username','followCount','friendCount','faveCount','tweetCount']],how='left', left_on=userCol, right_on='username')
    #convs[[followCol,friendCol,faveCol,tweetCount]]=temp[['followCount','friendCount','faveCount','tweetCount']]
    #MERGING is NOT WORKING HERE
    for index, row in convs.iterrows():
        t=sup.followCount[sup.username==row[userCol]].unique()
        if len(t)>0:
            convs.loc[index,followCol]=t[0]
        else:
            convs.loc[index,followCol]=np.nan
        
        t=sup.friendCount[sup.username==row[userCol]].unique()
        if len(t)>0:
            convs.loc[index,friendCol]=t[0]
        else:
            convs.loc[index,friendCol]=np.nan
        
        t=sup.faveCount[sup.username==row[userCol]].unique()
        if len(t)>0:
            convs.loc[index,faveCol]=t[0]
        else:
            convs.loc[index,faveCol]=np.nan
        
        t=sup.tweetCount[sup.username==row[userCol]].unique()
        if len(t)>0:
            convs.loc[index,tweetCount]=t[0]
        else:
            convs.loc[index,tweetCount]=np.nan
convs.to_csv('../data/bbAllFullConvosMoreAWCorrectTimeZone.csv',sep=';', index=False)