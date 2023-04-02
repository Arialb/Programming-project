print("")
print("________ Executing ... __________")
print("")
from pandas import *
import pandas as pd
#np.dtype (df, align=False, copy=False, low_memory = False)

# DATA ACCESS
# Read the dataset using a dataset reader that relies on Pandas
class gff3_databasereader():
	def readata(self):
		headers = ['seqid', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attribute']
		df = pd.read_csv("Homo_sapiens.GRCh38.85 (3).gff3.gz", 
		delimiter = '\t',  #the delimiter between column is the tab
		comment = '#',  #the lines indicated with '#' are comments
		names = headers)  #names for the columns
		na_values = '.'  #dovrebbe sostituire il punto con None type
		return gff3_database(df)
#print(df)
#type_of_df = type(df)
#print(f'The dataframe df is of type {type_of_df}')
#print("")


#OPERATIONS
# Type of operation = tipo di feature (gene, transciptt, mrna)
class gff3_database():

	def __init__(self,df):
		self.df=df

	def get_dataframe(self):
		return self.df

	def types(self):
		return self.df.dtypes

	def unique_sequences(self):
		return self.df['seqid'].unique()

	def unique_types(self):
		return self.df['type'].unique()

	def number_of_features(self):
		return self.df['source'].value_counts()

	def number_of_entries(self):
		return self.df['type'].value_counts()

	def new_dataset(self):
		return self.df.loc[self.df['type'] == 'chromosome']

	def fraction_of_unassembled_sequences(self):
		return "Total number of sequences: ", self.df.shape[0]
		"Number of unassembled sequences: ", self.df.loc[self.df['type'] == 'supercontig'].shape[0]
		" -> Fraction of unassembled sequences: ", float(self.df.loc[self.df['type'] == 'supercontig'].shape[0] / self.df.shape[0])

	def only_entries_from_source(self):
		array = ['ensembl', 'ensembl_havana', 'havana']
		return self.df.loc[self.df['source'].isin(array)]

	def entries_from_each_type(self):
		tdf= gff3_database(self.df).only_entries_from_source()
		group_type= tdf.groupby('type')
		return pd.DataFrame({'type':group_type.groups.keys(),'count':group_type.size().array})

	def gene_names_from_dataset(self):
		array = ['ensembl', 'ensembl_havana', 'havana']
		df2 = self.df.loc[self.df['source'].isin(array)]
		column_attribute = df2['attribute']
		l = []
		for single_attribute in column_attribute:
			string_attribute = str(single_attribute)
			for element in string_attribute.split(";"):
				if "Name=" in element:
					i = element.find("Name=")
					l.append(element[i+5:])
					break
		return pd.DataFrame(l)
gino=gff3_databasereader().readata()

#pandas.DataFrame.count#
     
