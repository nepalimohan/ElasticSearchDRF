from django.db import models
from quotation import choices
from quotation import models as dashmodels

# Create your models here.
class SalesOrder(models.Model):
    tenant_id = models.CharField(max_length=255, blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    order_date = models.DateField()
    delivery_date = models.DateField()
    customer = models.JSONField(null=True)
    narration = models.TextField(blank=True)
    document = models.JSONField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    amount = models.FloatField(default=0)
    non_vatable_amount = models.FloatField(default=0)
    vatable_amount = models.FloatField(default=0)
    vat_amount = models.FloatField(default=0)
    discount_percentage = models.FloatField(default=0)
    discount_amount = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    subtotal = models.FloatField(default=0)
    payment_term = models.IntegerField(blank=True, null=True)
    entry_by = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=50, choices=choices.StatusChoices.choices, default='draft')
    approval_user = models.CharField(max_length=255, blank=True, null=True)
    approved_by = models.CharField(max_length=255, blank=True, null=True)
    approved_date = models.DateField(blank=True, null=True)
    approved_comment = models.TextField(blank=True,null = True)
    cancelled_by = models.CharField(max_length=255, blank=True, null=True)
    cancelled_date = models.DateField(blank=True, null=True)
    cancelled_comment = models.TextField(blank=True, null=True)
    submit_for_approval_comment = models.TextField(blank=True, null=True)
    submit_for_approval_date = models.DateField(blank=True, null=True)
    grn_verified = models.BooleanField(default=False)
    invoice_created = models.BooleanField(default=False)
    close = models.BooleanField(default=False)
    invoice_status = models.CharField(max_length=50, choices=choices.UsedStatusChoices.choices, default=choices.UsedStatusChoices.NOTUSED)
    delivery_note_status = models.CharField(max_length=50, choices=choices.UsedStatusChoices.choices, default=choices.UsedStatusChoices.NOTUSED)
    approved_date_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'SalesOrder'
        ordering = ['-id']
        
    def save(self, *args, **kwargs):
        if self.unique_id == "" or self.unique_id is None:
            self.unique_id = dashmodels.ID.createID("SOR", self.tenant_id)
        super().save(*args, **kwargs)
        
class SalesOrderItem(models.Model):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.PROTECT, related_name='items', blank=True, null=True)
    product_id = models.IntegerField()
    uom = models.CharField(max_length=255)
    quantity = models.FloatField(default=0)
    invoice_count = models.FloatField(default=0)
    delivery_note_count = models.FloatField(default=0)
    rate = models.FloatField()
    discount_percent = models.FloatField(null=True, blank=True)
    discount_amount = models.FloatField(null=True, blank=True)
    amount = models.FloatField(default=0)
    vat = models.CharField(max_length=255, choices=choices.VatChoices.choices, blank=True)
    vat_amount = models.FloatField(default=0)
    item_total = models.FloatField(default=0)
    invoice_status = models.CharField(max_length=50, choices=choices.UsedStatusChoices.choices, default=choices.UsedStatusChoices.NOTUSED)
    delivery_note_status = models.CharField(max_length=50, choices=choices.UsedStatusChoices.choices, default=choices.UsedStatusChoices.NOTUSED)

    
    class Meta:
        db_table = 'SalesOrderItem'
        ordering = ['-id']