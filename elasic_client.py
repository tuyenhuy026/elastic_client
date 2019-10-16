from elasticsearch import Elasticsearch

from config import *

class Session:
	def __init__(self):
		self.es = Elasticsearch([{"host" : ELASTIC_HOST, "port" : ELASTIC_PORT}])	

	def update_elastic(self, _id, _body):
		response = self.es.index(index=BANGTIN_INDEX, doc_type=BANGTIN_DOCTYPE, id=_id, body=_body)
		return response
	
	def search_id_elastic(self, _id):
		result = self.es.get_source(index=BANGTIN_INDEX, doc_type=BANGTIN_DOCTYPE, id=_id)
		return result

	def update(self, _id, _sentimentality):
		article = self.search_id_elastic(_id)
		article["sentimentality"] = _sentimentality
		response = self.update_elastic(_id, article)
		return response
	
	def search(self, timeframe, category, keyword):
		pass



