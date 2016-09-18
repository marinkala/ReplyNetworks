import pandas as pd
import numpy as np
import sys

#slice=int(sys.argv[1])
iters=2000

#bbRepliers=np.fromfile('/home/mako0970/ReplyPaperNew/bbContextRepliers.csv', sep=',')
eastCoastOutRepliers=np.fromfile('/home/mako0970/ReplyPaperNew/data/EastCoastOutContextRepliers.csv', sep=',')
datatypes={'0': int, '2': int, '3': bool, '4': int, '5': int, '6': int, '7': int, '13': int,'14': bool, '15': int,\
'16': int,'17': int,'18': int,'19': int,'20':bool,'23': int,'24': int,'25': int}

chunksize=5000
steps=40991
#204,957,018 tweetes reuires 21 slices of this running (204957018/(5000*2000))

for slice in range(19,22):
	ec_al=pd.DataFrame()
	print slice

	for i in xrange(slice*iters,(slice+1)*iters):
		try:        
			tp=pd.read_csv('/home/mako0970/ReplyPaperNew/data/Sandy_context_tweetsUserID.csv',sep=';',skiprows=chunksize*i,\
			dtype=datatypes, nrows=chunksize,header=None)
			#print chunksize*i        
		except pd.parser.CParserError:
			tp=pd.read_csv('/home/mako0970/ReplyPaperNew/data/Sandy_context_tweetsUserID.csv',sep=';',skiprows=chunksize*i+1,\
			dtype=datatypes, nrows=1,header=None)            
			tp2=pd.read_csv('/home/mako0970/ReplyPaperNew/data/Sandy_context_tweetsUserID.csv',sep=';',skiprows=chunksize*i+3,\
			dtype=datatypes, nrows=chunksize-3,header=None)
			tp.append(tp2)             
		print i, "th chunk"
    
		#bb=tp[tp.user_id.isin(bbRepliers)]
		ec=tp[tp[2].isin(eastCoastOutRepliers)]   
		ec_al=ec_al.append(ec,ignore_index=True)

	ec_al.to_csv('/home/mako0970/ReplyPaperNew/data/DataFrameSlices/eastCoastOutOntopicReplierTweets'+str(slice)+'.csv', sep=';')
