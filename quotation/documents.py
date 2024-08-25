from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry

from .models import SalesQuotation

@registry.register_document
class QuotationDocument(Document):
    class Index:
        name = "quotation"
        settings = {"number_of_shards":1, "number_of_replicas":0}
        
    
    class Django:
        model = SalesQuotation
        fields = ["title",] #unique_id if present
    