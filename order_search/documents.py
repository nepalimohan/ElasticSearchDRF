from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry

from .models import SalesOrder


@registry.register_document
class OrderDocument(Document):
    #incase to include 
    # customer_name = fields.TextField(attr="customer.name")
    # customer_email = fields.TextField(attr="customer.email")
    
    class Index:
        name = "quotation"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }
        
    
    class Django:
        model = SalesOrder
        fields = ["tenant_id","title", "unique_id", "order_date", "delivery_date", "entry_by"] #unique_id if present




# Then, use MultiMatch in your SearchView as before.
