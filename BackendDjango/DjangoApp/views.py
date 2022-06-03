from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from rest_framework.decorators import api_view
from pymongo import MongoClient 
import json
from bson.json_util import dumps
from bson.objectid import ObjectId

# from django_elasticsearch_dsl_drf.constants import (
#     LOOKUP_FILTER_RANGE,
#     LOOKUP_QUERY_IN,
#     LOOKUP_QUERY_GT,
#     LOOKUP_QUERY_GTE,
#     LOOKUP_QUERY_LT,
#     LOOKUP_QUERY_LTE,
# )
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
    CompoundSearchFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
 
from DjangoApp.documents import *
from DjangoApp.serializers import *

class CollectionViewSet(DocumentViewSet):
    document = CollectionDocument
    serializer_class = CollectionDocumentSerializer
 
    # lookup_field = 'name'
    filter_backends = [
        FilteringFilterBackend,
        # OrderingFilterBackend,
        # DefaultOrderingFilterBackend,
        # SearchFilterBackend,
        CompoundSearchFilterBackend
    ]
 
    # Define search fields
    search_fields = (
        'name',
        'blockchain',
        'currency'

    )
    multi_match_search_fields = (  
        'name',
        'blockchain',
        'currency'
        )
    # Filter fields
    filter_fields = {
        'name':'name',
        'blockchain': 'blockchain',
        'currency': 'currency',
        'volume': 'volume',
        'floor_price': 'floor_price',
        'Owners': 'Owners',
        'items': 'items',
         
    }
 

class NftViewSet(DocumentViewSet):
    document = NftDocument
    serializer_class = NftDocumentSerializer
 
    # lookup_field = 'name'
    filter_backends = [
        FilteringFilterBackend,
        # OrderingFilterBackend,
        # DefaultOrderingFilterBackend,
        # SearchFilterBackend,
        CompoundSearchFilterBackend
    ]
 
    # Define search fields
    search_fields = (
        'name',
        'blockchain',
        'currency',
        'collection'

    )
    multi_match_search_fields = (  
        'name',
        'blockchain',
        'currency',
        'collection'
        )
    # Filter fields
    filter_fields = {
            'name':'name',
            'collection':'collection',
            'last_price':'last_price',
            'currency':'currency',
            'blockchain':'blockchain',
            'id':'id'
         
    }
 


class BlockchainViewSet(DocumentViewSet):
    document = BlockchainDocument
    serializer_class = BlockchainDocumentSerializer
 
    # lookup_field = 'name'
    filter_backends = [
        FilteringFilterBackend,
        # OrderingFilterBackend,
        # DefaultOrderingFilterBackend,
        # SearchFilterBackend,
        CompoundSearchFilterBackend
    ]
 
    # Define search fields
    search_fields = (
        'name',


    )
    multi_match_search_fields = (  
        'name',

        )
    # Filter fields
    filter_fields = {
        'name':'name',
        'id': 'id',

         
    }
 

    # # Define ordering fields
    # ordering_fields = {
    #     'name': 'name',
    #     'blockchain': 'blockchain.raw',
    #     'currency': 'currency.raw',
    #     'volume': 'volume',
    #     'floor_price': 'floor_price',
    #     'Owners': 'Owners',
    #     'items': 'items'
    # }

    # # Specify default ordering
    # ordering = ('name', 'floor_price',)   


# client = MongoClient('mongodb+srv://soumaya:soumaya1Atlas@cluster0.y9xab.mongodb.net/test?retryWrites=true&w=majority')
# db = client['DjangoDB']
# blockchain =  db['blockchain']
# collection =  db['collection']
# nft =  db['nft']
# currency =  db['currency']



# @api_view(['GET', 'POST'])
# def blockchain_list(request):
#     if request.method == 'GET':
#         docs=blockchain.find()
     
#         data = json.loads(dumps(docs)) 
#         return JsonResponse(data, safe=False)
#         # 'safe=False' for objects serialization
    

# @api_view(['GET', 'POST'])
# def collection_list(request):
#     if request.method == 'GET':
#         docs=collection.find()
        
#         blockchain = request.GET.get('blockchain', None)
      
#         if blockchain is not None:
#             docs = collection.find({"blockchain": blockchain})
     
#         data = json.loads(dumps(docs)) 
#         return JsonResponse(data, safe=False)
#         # 'safe=False' for objects serialization  
 
# @api_view(['GET', 'POST'])
# def nft_list(request):
#     if request.method == 'GET':
#         docs=nft.find()
        
#         blockchain = request.GET.get('blockchain', None)
      
#         if blockchain is not None:
#             docs = nft.find({"blockchain": blockchain})

#         collection = request.GET.get('collection', None)
      
#         if collection is not None:
#             docs = nft.find({"collection": collection})

#         currency = request.GET.get('currency', None)
      
#         if currency is not None:
#             docs = nft.find({"currency": currency})
     
#         data = json.loads(dumps(docs)) 
#         return JsonResponse(data, safe=False)
#         # 'safe=False' for objects serialization

# @api_view(['GET', 'POST'])
# def currency_list(request):
#     if request.method == 'GET':
#         docs=currency.find()
        
#         blockchain = request.GET.get('blockchain', None)
      
#         if blockchain is not None:
#             docs = currency.find({"id_blockchain": blockchain})
     
#         data = json.loads(dumps(docs)) 
#         return JsonResponse(data, safe=False)
#         # 'safe=False' for objects serialization
    

        