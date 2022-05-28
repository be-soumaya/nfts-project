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
collection =  db['NFT_sales']



@api_view(['GET', 'POST'])
def app_list(request):
    if request.method == 'GET':
        docs=collection.find({"Number_of_Sales": {"$eq": 5}})
        
        date = request.GET.get('date', None)
      
        if date is not None:
            docs = collection.find({"Date": date})
     
        data = json.loads(dumps(docs)) 
        return JsonResponse(data, safe=False)
        # 'safe=False' for objects serialization
    

        