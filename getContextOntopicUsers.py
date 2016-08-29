import pandas as pd
import numpy as np
import sys

#slice=int(sys.argv[1])
iters=2000

#bbRepliers=np.fromfile('/home/mako0970/ReplyPaperNew/bbContextRepliers.csv', sep=',')
eastCoastOutRepliers=np.fromfile('/home/mako0970/ReplyPaperNew/data/EastCoastOutContextRepliers.csv', sep=',')

chunksize=5000
steps=40991
#204,957,018 tweetes reuires 21 slices of this running (204957018/(5000*2000))

for slice in range(12,22):
	ec_al=pd.DataFrame()
	print slice

	for i in xrange(slice*iters,(slice+1)*iters):
		try:        
			tp=pd.read_csv('/home/mako0970/ReplyPaperNew/data/Sandy_context_tweetsUserID.csv',sep=';',skiprows=chunksize*i,\
			nrows=chunksize,header=None)
		except pd.parser.CParserError:
			tp=pd.read_csv('/home/mako0970/ReplyPaperNew/data/Sandy_context_tweetsUserID.csv',sep=';',skiprows=chunksize*i+1,\
			nrows=1,header=None)            
			tp2=pd.read_csv('/home/mako0970/ReplyPaperNew/data/Sandy_context_tweetsUserID.csv',sep=';',skiprows=chunksize*i+3,\
			nrows=chunksize-3,header=None)
			tp.append(tp2)             
		print i, "th chunk"
    
		#bb=tp[tp.user_id.isin(bbRepliers)]
		ec=tp[tp[2].isin(eastCoastOutRepliers)]   
		ec_al=ec_al.append(ec,ignore_index=True)

	ec_al.to_csv('/home/mako0970/ReplyPaperNew/data/DataFrameSlices/eastCoastOutOntopicReplierTweets'+str(slice)+'.csv', sep=';')
