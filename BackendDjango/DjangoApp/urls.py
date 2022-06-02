from django.urls import re_path as url
from DjangoApp import views 
# from rest_framework.routers import SimpleRouter

# router = SimpleRouter()
# router.register(
#     prefix=r'',
#     basename='collections',
#     viewset=views.CollectionViewSet
# )
# urlpatterns = router.urls
urlpatterns = [ 
    url('search_blockchain/',views.BlockchainViewSet.as_view({'get':'list'})),
    url('search_collection/',views.CollectionViewSet.as_view({'get':'list'})),
    url('search_nft/',views.NftViewSet.as_view({'get':'list'})),
    # url(r'^api/collections$', views.collection_list),
] 