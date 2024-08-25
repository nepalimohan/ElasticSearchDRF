from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from elasticsearch_dsl.query import MultiMatch, Q

# Create your views here.
from . import models, serializers, documents


class SearchAPIView(APIView):
    def get(self, request):
        q = request.GET.get('q')
        if q:
            # Search on both the title and customer name/email
            # query = MultiMatch(query=q, fields=['unique_id', 'title'], fuzziness="AUTO")
            query = Q("wildcard", title=f"*{q}*") | Q("wildcard", unique_id=f"*{q}*")
            search = documents.OrderDocument.search().query(query)
            response = search.execute()
            # Extract the IDs of the matched documents
            ids = [hit.meta.id for hit in response]
            print(ids)
            # Fetch full data from the database, including related Customer data
            orders = models.SalesOrder.objects.filter(id__in=ids)
            
            # Serialize the full data using ModelSerializer
            serializer = serializers.SalesOrderSerializer(orders, many=True)
            return Response(serializer.data)
        
        return Response('Not found', status=404)