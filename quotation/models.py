from django.db import models
from . import choices as dashchoices
# from .documents import SalesQuotationMainDocument



# Create your models here.
class SalesQuotation(models.Model):
    title = models.CharField(max_length=255)
    quotation_number = models.CharField(max_length=255, blank=True)
    quotation_date = models.DateField()
    valid_till = models.DateField()
    narration = models.TextField(blank=True)
    

# class SalesQuotationMain(models.Model):
#     tenant_id = models.CharField(max_length=255, blank=True, null=True)
#     unique_id = models.CharField(max_length=255, blank=True, null=True)
#     title = models.CharField(max_length=255)
#     quotation_number = models.CharField(max_length=255, blank=True, null=True)
#     quotation_date = models.DateField()
#     valid_till = models.DateField()
#     customer = models.JSONField(null=True)
#     narration = models.TextField(blank=True)
#     description = models.TextField(blank=True, null=True)
#     document = models.JSONField(blank=True, null=True)
#     discount_amount = models.FloatField(default=0.0, null=True, blank=True)
#     discount_percentage = models.FloatField(default=0.0, null=True, blank=True)
#     vat_amount = models.FloatField(default=0.0, null=True, blank=True)
#     vatable_amount = models.FloatField(default=0.0, null=True, blank=True)
#     non_vatable_amount = models.FloatField(default=0.0, null=True, blank=True)
#     grand_total = models.FloatField(default=0.0, null=True, blank=True)
#     subtotal = models.FloatField(default=0.0, null=True, blank=True)
#     approved_date_time = models.DateTimeField(blank=True, null=True)
    
#     status = models.CharField(
#         choices=dashchoices.StatusChoices.choices,
#         default="draft",
#         null=True,
#         blank=True,
#         max_length=100,
#     )
    
#     entry_by = models.CharField(max_length=255, blank=True, null=True)
#     approval_user = models.CharField(max_length=255, blank=True, null=True)
#     approved_by = models.CharField(max_length=255, blank=True, null=True)
#     approved_date = models.DateField(blank=True, null=True)
#     approved_comment = models.TextField(blank=True, null=True)
#     submit_for_approved_comment = models.TextField(blank=True, null=True)
#     submit_for_approved_date = models.DateField(blank=True, null=True)
#     cancelled_by = models.CharField(max_length=255, blank=True, null=True)
#     cancelled_date = models.DateField(blank=True, null=True)
#     cancelled_comment = models.TextField(blank=True, null=True)
#     submit_for_approval_date = models.DateField(blank=True, null=True)
    
#     used_status = models.CharField(max_length=50, choices=dashchoices.UsedStatusChoices.choices, default="not used")

#     class Meta:
#         db_table = 'Quotation'
#         ordering = ['-id']
    
#     # def save(self, *args, **kwargs):
#     #     super().save(*args, **kwargs)
#     #     SalesQuotationMainDocument().update(self)

#     # def delete(self, *args, **kwargs):
#     #     SalesQuotationMainDocument().delete(self)
#     #     super().delete(*args, **kwargs)

        
# class SalesQuotationItem(models.Model):
#     quotation = models.ForeignKey(SalesQuotationMain, on_delete=models.PROTECT, related_name="quotation_items", blank=True, null=True)
#     product_id = models.IntegerField()
#     uom = models.CharField(max_length=255)
#     quantity = models.FloatField(default=0)
#     rate = models.FloatField(default=0)
#     discount_amount = models.FloatField(default=0)
#     discount_percent = models.FloatField(default=0)
#     vat = models.CharField(max_length=255, choices=dashchoices.VatChoices.choices, blank=True)
#     vat_amount = models.FloatField(default=0)
#     amount = models.FloatField(default=0)
#     item_total = models.FloatField(default=0)
#     remaining = models.FloatField(default=0)
#     used_status = models.CharField(max_length=50, choices=dashchoices.UsedStatusChoices.choices, default="not used")

#     class Meta:
#         db_table = 'QuotationItem'
#         ordering = ['-id']