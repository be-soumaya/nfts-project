from locale import currency
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from rest_framework.decorators import api_view
from pymongo import MongoClient 
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
client = MongoClient('mongodb+srv://soumaya:soumaya1Atlas@cluster0.y9xab.mongodb.net/test?retryWrites=true&w=majority')
db = client['DjangoDB']
blockchain =  db['blockchain']
collection =  db['collection']
nft =  db['nft']
currency =  db['currency']



@api_view(['GET', 'POST'])
def blockchain_list(request):
    if request.method == 'GET':
        docs=blockchain.find()
     
        data = json.loads(dumps(docs)) 
        return JsonResponse(data, safe=False)
        # 'safe=False' for objects serialization
    

@api_view(['GET', 'POST'])
def collection_list(request):
    if request.method == 'GET':
        docs=collection.find()
        
        blockchain = request.GET.get('blockchain', None)
      
        if blockchain is not None:
            docs = collection.find({"blockchain": blockchain})
     
        data = json.loads(dumps(docs)) 
        return JsonResponse(data, safe=False)
        # 'safe=False' for objects serialization  
 
@api_view(['GET', 'POST'])
def nft_list(request):
    if request.method == 'GET':
        docs=nft.find()
        
        blockchain = request.GET.get('blockchain', None)
      
        if blockchain is not None:
            docs = nft.find({"blockchain": blockchain})

        collection = request.GET.get('collection', None)
      
        if collection is not None:
            docs = nft.find({"collection": collection})

        currency = request.GET.get('currency', None)
      
        if currency is not None:
            docs = nft.find({"currency": currency})
     
        data = json.loads(dumps(docs)) 
        return JsonResponse(data, safe=False)
        # 'safe=False' for objects serialization

@api_view(['GET', 'POST'])
def currency_list(request):
    if request.method == 'GET':
        docs=currency.find()
        
        blockchain = request.GET.get('blockchain', None)
      
        if blockchain is not None:
            docs = currency.find({"id_blockchain": blockchain})
     
        data = json.loads(dumps(docs)) 
        return JsonResponse(data, safe=False)
        # 'safe=False' for objects serialization
    

        