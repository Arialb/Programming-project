print("")
print("________ Executing ... __________")
print("")
from pandas import *
import pandas as pd

class gff3_databasereader():
	def readata(self):
		headers = ['seqid', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attribute']
		df = pd.read_csv("Homo_sapiens.GRCh38.85 (3).gff3.gz", 
		delimiter = '\t',  
		comment = '#',  
		names = headers)  
		na_values = '.'  
		return gff3_database(df)
class gff3_database():
	
	#decorator
	def _inactive(function):
		def wrapper(self, *args, **kwargs):
			if function.__name__ in ['number_of_entries']:
				return ('Operation is inactive')
			return function(self, *args, **kwargs)
		return wrapper

	def __init__(self,df):
		self.df=df

	@_inactive
	def get_dataframe(self):
		return self.df

	@_inactive
	def types(self):
		return pd.DataFrame(self.df.dtypes)

	@_inactive
	def unique_sequences(self):
		return pd.DataFrame(self.df['seqid'].unique())

	@_inactive
	def unique_types(self):
		return pd.DataFrame(self.df['type'].unique())
	@_inactive
	def number_of_features(self):
		return pd.DataFrame(self.df['source'].value_counts())
	
	@_inactive
	def number_of_entries(self):
		return pd.DataFrame(self.df['type'].value_counts())

	@_inactive
	def new_dataset(self):
		return pd.DataFrame(self.df.loc[self.df['type'] == 'chromosome'])

	@_inactive
	def fraction_of_unassembled_sequences(self):
		return ("Total number of sequences: ", self.df.shape[0],"Number of unassembled sequences: ", self.df.loc[self.df['type'] == 'supercontig'].shape[0]," -> Fraction of unassembled sequences: ", float(self.df.loc[self.df['type'] == 'supercontig'].shape[0] / self.df.shape[0]))

	@_inactive
	def only_entries_from_source(self):
		array = ['ensembl', 'ensembl_havana', 'havana']
		return pd.DataFrame(self.df.loc[self.df['source'].isin(array)])

	@_inactive
	def entries_from_each_type(self):
		tdf= gff3_database(self.df).only_entries_from_source()
		group_type= tdf.groupby('type')
		return pd.DataFrame({'type':group_type.groups.keys(),'count':group_type.size().array})

	@_inactive
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

     
