from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from DjangoApp.models import *

@registry.register_document
class BlockchainDocument(Document):
    class Index:
        name ='blockchains'
        settings = {'number_of_shards':1,'number_of_replicas':0}

    class Django :
        model= Blockchain

        fields = [
            'name',
            'id'
        ]

@registry.register_document
class CollectionDocument(Document):
    class Index:
        name ='collections'
        settings = {'number_of_shards':1,'number_of_replicas':0}

    class Django :
        model= Collection

        fields = [
            'name',
            'volume',
            'floor_price',
            'Owners',
            'items',
            'blockchain',
            'currency'
        ]

@registry.register_document
class NftDocument(Document):
    class Index:
        name ='nfts'
        settings = {'number_of_shards':1,'number_of_replicas':0}

    class Django :
        model= Nft

        fields = [
            'name',
            'collection',
            'last_price',
            'currency',
            'blockchain'
        ]