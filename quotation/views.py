from django.shortcuts import render

from elasticsearch_dsl.query import MultiMatch
from .documents import QuotationDocument

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class SearchView(APIView):
    def get(self, request):
        q = request.GET.get('q')
        context = {}
        if q:
            print(q)
            #fuzziness - results similar words as well
            query = MultiMatch(query=q, fields=['title'], fuzziness="AUTO")
            search = QuotationDocument.search().query(query)
            response = search.execute()
            print(response)
            context['quotation'] = [
                {
                    "title": hit.title,
                    "id": hit.meta.id,
                    # Add other fields as necessary
                } 
                for hit in response
            ]
            return Response(context)
        return Response('Not found')
    

# from django_elasticsearch_dsl_drf.filter_backends import (
#     FilteringFilterBackend,
#     OrderingFilterBackend,
#     DefaultOrderingFilterBackend,
# )
# from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
# from django_elasticsearch_dsl_drf.constants import SUGGESTER_COMPLETION
# from .documents import SalesQuotationDocument
# from .serializers import SalesQuotationDocumentSerializer

# class SalesQuotationSearchView(DocumentViewSet):
#     document = SalesQuotationDocument
#     serializer_class = SalesQuotationDocumentSerializer
#     filter_backends = [
#         FilteringFilterBackend,
#         OrderingFilterBackend,
#         DefaultOrderingFilterBackend,
#     ]

#     # Define filtering
#     filter_fields = {
#         'title': 'title.raw',
#         'quotation_number': 'quotation_number.raw',
#         'customer': 'customer.raw',
#     }

#     # Define ordering
#     ordering_fields = {
#         'quotation_date': 'quotation_date',
#     }
#     ordering = ('quotation_date',)

#     def get_queryset(self):
#         # Get the original queryset
#         queryset = super().get_queryset()

#         # Get the search parameter
#         q = self.request.query_params.get('q', None)

#         if q:
#             # Perform a multi-field search
#             queryset = queryset.query(
#                 "multi_match",
#                 query=q,
#                 fields=[
#                     'title',
#                     'quotation_number',
#                     'customer',
#                     'description',
#                     'narration',
#                 ]
#             )

#         return queryset


# from rest_framework.response import Response
# from rest_framework.views import APIView
# from elasticsearch_dsl import Q
# from .documents import SalesQuotationMainDocument
# from .serializers import SalesQuotationSerializer

# class SalesQuotationSearchAPIView(APIView):

#     def get(self, request, *args, **kwargs):
#         # Get the search parameter
#         q = request.query_params.get('q', None)

#         # Start with a basic query
#         search = SalesQuotationMainDocument.search()

#         if q:
#             # Perform a multi-field search using `multi_match`
#             query = Q(
#                 "multi_match",
#                 query=q,
#                 fields=[
#                     'title',
#                     'quotation_number',
#                     'customer',
#                     'description',
#                     'narration',
#                 ]
#             )
#             search = search.query(query)

#         # Add ordering if needed
#         ordering = request.query_params.get('ordering', 'quotation_date')
#         search = search.sort(ordering)

#         # Execute the search
#         response = search.execute()

#         # Serialize the results
#         serializer = SalesQuotationSerializer(response, many=True)

#         # Add related items
#         for hit in response.hits:
#             hit.items = [
#                 {
#                     'product_id': item.product_id,
#                     'uom': item.uom,
#                     'quantity': item.quantity,
#                     'rate': item.rate,
#                     'discount_amount': item.discount_amount,
#                     'discount_percent': item.discount_percent,
#                     'vat': item.vat,
#                     'vat_amount': item.vat_amount,
#                     'amount': item.amount,
#                     'item_total': item.item_total,
#                     'remaining': item.remaining,
#                     'used_status': item.used_status,
#                 }
#                 for item in hit.items
#             ]

#         return Response(serializer.data)
