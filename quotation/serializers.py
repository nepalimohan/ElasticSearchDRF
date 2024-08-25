# from rest_framework import serializers
# from .models import SalesQuotationMain, SalesQuotationItem

# class SalesQuotationItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SalesQuotationItem
#         fields = [
#             'product_id',
#             'uom',
#             'quantity',
#             'rate',
#             'discount_amount',
#             'discount_percent',
#             'vat',
#             'vat_amount',
#             'amount',
#             'item_total',
#             'remaining',
#             'used_status',
#         ]

# class SalesQuotationSerializer(serializers.ModelSerializer):
#     items = SalesQuotationItemSerializer(many=True, read_only=True)

#     class Meta:
#         model = SalesQuotationMain
#         fields = [
#             'id',
#             'tenant_id',
#             'unique_id',
#             'title',
#             'quotation_number',
#             'quotation_date',
#             'valid_till',
#             'customer',
#             'narration',
#             'description',
#             'discount_amount',
#             'discount_percentage',
#             'vat_amount',
#             'vatable_amount',
#             'non_vatable_amount',
#             'grand_total',
#             'subtotal',
#             'approved_date_time',
#             'status',
#             'entry_by',
#             'approval_user',
#             'approved_by',
#             'approved_date',
#             'approved_comment',
#             'submit_for_approved_comment',
#             'submit_for_approved_date',
#             'cancelled_by',
#             'cancelled_date',
#             'cancelled_comment',
#             'submit_for_approval_date',
#             'used_status',
#             'items',  # Include related items
#         ]
