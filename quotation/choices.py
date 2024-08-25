from django.db import models

class ActiveStatus(models.TextChoices):
    ACTIVE = "active", "Active"
    INACTIVE = "inactive", "Inactive"
    
class ValuationMethod(models.TextChoices):
    FIFO = "FIFO", "First In First Out"
 
class StockKeepingMethod(models.TextChoices):
    INDEPENDENT = "independent", "Independent Stock Keeping"
    BATCH = "batch", "Batch Stock Keeping"
    
class VerificationChoices(models.TextChoices):
    PENDING = "pending", "Pending"
    NOTVERIFIED = "not_verified", "Not Verified"
    EVALUATION = "under_evaluation", "Under Evaluation"
    VERIFIED = "verified", "Verified"
    

class ReportDateChoices(models.TextChoices):
    TODAY = "today", "Today"
    DAYS_7 = "7_days", "Last 7 Days"
    DAYS_30 = "30_days", "Last 30 Days"
    CUSTOM = "custom", "Custom Range"
    YEARLY = "yearly", "Year to date"
    
class DatePicker(models.TextChoices):
    NP = "np", "Nepali"
    EN = "en", "English"


class AdjustmentType(models.TextChoices):
    ADDITION = "addition", "Addition"
    DEDUCTION = "deduction", "Deduction"
    

class UniqueIdEntity(models.TextChoices):
    INVOICE = "invoice", "Invoice"
    RETURN = "return", "RETURN"
    

class StatusChoices(models.TextChoices):
    DRAFT = "draft", "Draft"
    SUBMIT_FOR_APPROVAL = "submitted_for_approval", "Submitted for Approval"
    APPROVED = "approved", "Approved"
    CANCELLED = "cancelled", "Cancelled"
    PENDING = "pending", "Pending"

class PageRequest(models.TextChoices):
    LISTING = "listing", "Listing"
    DETAIL = "detail", "Detail" 
   
   
class PayeeChoices(models.TextChoices):
    SUPPLIER = "supplier", "Supplier"
    CUSTOMER = "customer", "Customer"
    EMPLOYEE = "employee", "Emloyee"
    
    
class UsedStatusChoices(models.TextChoices):
    NOTUSED = "not used", "Not Used"
    PARTIAL = "partial", "Partial"
    COMPLETE = "complete", "Complete"
 
class DiscountConf(models.TextChoices):
    ITEM = "item_wise_discount", "Item-wise Discount"
    BILL = "bill_discount", "Total Bill Discount"
    

class VatChoices(models.TextChoices):
    ZERO = "0", "0% VAT"
    THIRTEEN = "13", "13% VAT"
    NONVAT = "non vatable", "Non Vatable"
 
class PaymentMethod(models.TextChoices):
    CASH = "cash", "Cash"
    CHEQUE = "cheque", "Cheque"
    BANK_TRANSFER = "banktransfer", "Bank Transfer"

class ServiceChoices(models.TextChoices):
    IAM = "PR100", "IAM"
    SUPPLIER_MASTER = "PR200", "Supplier Master"
    CUSTOMER_MASTER = "PR300", "Customer Master"
    EMPLOYEE_MASTER = "PR400", "Employee Master"
    PAYMENT_TERM = "PR500", "Payment Term"
    CONFIGURATION = "PR600", "Configuration"
    VALIDATION = "PR700", "Validation"
    REPORTING = "PR800", "Reporting"
    PRODUCT_MASTER = "PR900", "Product Master"
    INVENTORY = "PR1000", "Inventory"
    PURCHASE = "PR1100", "Purchase"
    SALES = "PR1200", "Sales"
    ACCOUNTING = "PR1300", "Accounting"
    EXPENSE = "PR1400", "Expense"
    NOTIFICATION = "PR1500", "Notification"
    ACTIVITY_LOG = "PR1600", "Activity Log"
    EMAIL = "PR1700", "Email"
    EXPORT = "PR1800", "Export"
    DOCUMENT = "PR1900", "Document"
    PORTAL_AUTHENTICATION = "PR2000", "Portal Authentication"
    WEBSITE = "PR2100", "Website"
    PACKAGE = "PR2200", "Package"
    CAMPAIGN = "PR2300", "Campaign"
    CONTRACT = "PR2400", "Contract"
    TMS = "PR2500", "TMS"
    PAYMENT = "PR2600", "Payment"
    CDXE = "PR2700", "CDXE"
    E_BILLING = "PR2800", "E-billing"


class SetupPanelTitle(models.TextChoices):
    PRODUCT_CREATION = 'product_creation', 'Product Creation'
    PRODUCT_AND_INVENTORY_FETCHING = 'product_and_inventory_fetching', 'Product and Inventory Fetching'
    PRODUCT_SEARCH = 'product_search', 'Product Search'

class ServiceType(models.TextChoices):
    CREATION = "creation", "Creation"
    APPROVAL = "approval", "Approval"
    CANCELLATION = "cancellation", "Cancellation"
    SUBMITFORAPPROVAL = "submit_for_approval", "Submit for Approval"
    CANCEL_SUBMISSION = "cancel_submission ", "Cancel Submission"
    ACTIVE = "active", "Active"
    INACTIVE = "inactive", "Inactive"
    EDITION = "edition", "Edition"
    EXPORT = "export", "Export"
    EMAIL = "email", "Email"
    DOCUMENTADD = "document_add", "Document Add"
    DOCUMENTEDIT = "document_edit", "Document Edit"
    DOCUMENTDELETE = "document_delete", "Document Delete"
    ALERT = "alert", "Alert"
    REFERENCE = "reference", "Reference"
 
    
class AllFeatures(models.TextChoices):
    GROUP_MANAGEMENT = "PR101", "Group Management"
    PERMISSION_MANAGEMENT = "PR102", "Permission Management"
    USER_MANAGEMENT = "PR103", "User Management"
    SUPPLIER_CREATION = "PR201", "Supplier Creation"
    SUPPLIER_CATEGORY = "PR202", "Supplier Category"
    # Customer features
    CUSTOMER_CREATION = "PR301", "Customer Creation"
    CUSTOMER_CATEGORY = "PR302", "Customer Category"
    # Employee features
    EMPLOYEE_CREATION = "PR401", "Employee Creation"
    # Payment term features
    PAYMENT_TERM_CREATION = "PR501", "Payment Term Creation"
    # Configuration features
    APPROVAL_WORKFLOW_CONFIGURATIONS = "PR601", "Approval Workflow Configurations"
    PURCHASE_FLOW_CONFIGURATIONS = "PR602", "Purchase Flow Configurations"
    EXPENSE_CONFIGURATIONS = "PR603", "Expense Configurations"
    SALES_FLOW_CONFIGURATIONS = "PR604", "Sales Flow Configurations"
    PRODUCT_MASTER_CONFIGURATIONS = "PR605", "Product Master Configurations"
    GL_MAPPING_FOR_MASTER_SERVICES = "PR606", "GL Mapping for Master Services"
    DEFAULT_SETTINGS = "PR607", "Default Settings"
    # Validation service features
    LENGTH_VALIDATION = "PR701", "Length Validation"
    # Reporting service features
    INVENTORY_REPORTS = "PR801", "Inventory Reports"
    PURCHASE_REPORTS = "PR802", "Purchase Reports"
    SALES_REPORTS = "PR803", "Sales Reports"
    ACCOUNTING_REPORTS = "PR804", "Accounting Reports"
    # Product master features
    PRODUCT_CREATION = "PR901", "Product Creation"
    PRODUCT_CATEGORY = "PR902", "Product Category"
    UOM = "PR903", "UOM"
    VARIANT = "PR904", "Variant"
    # Inventory service features
    STOCK_ADJUSTMENT = "PR1001", "Stock Adjustment"
    # Purchase features
    PURCHASE_REQUISITION = "PR1101", "Purchase Requisition"
    PURCHASE_ORDER = "PR1102", "Purchase Order"
    GOODS_RECEIVED_NOTE = "PR1103", "Goods Received Note"
    RETURNS_GRN = "PR1104", "Returns GRN"
    PURCHASE_INVOICE = "PR1105", "Purchase Invoice"
    PURCHASE_RETURN = "PR1106", "Purchase Return"
    # Sales features
    SALES_QUOTATION = "PR1201", "Sales Quotation"
    SALES_ORDER = "PR1202", "Sales Order"
    DELIVERY_NOTE = "PR1203", "Delivery Note"
    RETURNS_DELIVERY_NOTE = "PR1204", "Returns Delivery Note"
    SALES_INVOICE = "PR1205", "Sales Invoice"
    SALES_RETURN = "PR1206", "Sales Return"
    # Accounting features
    CHART_OF_ACCOUNTS = "PR1301", "Chart of Accounts (COA)"
    JOURNAL_VOUCHER = "PR1302", "Journal Voucher"
    PAYMENT_VOUCHER = "PR1303", "Payment Voucher"
    RECEIPT_VOUCHER = "PR1304", "Receipt Voucher"
    BANK_ACCOUNT = "PR1305", "Bank Account"
    BILL_PAYMENT_RECEIVE = "PR1306", "Bill Payment/Receive"
    # Expense service features
    EXPENSE_CREATION = "PR1401", "Expense Creation"
    # Portal Authentication features
    PAM_GROUP_MANAGEMENT = "PR1501", "Group Management"
    PAM_PERMISSION_MANAGEMENT = "PR1502", "Permission Management"
    PAM_USER_MANAGEMENT = "PR1503", "User Management"
    # Website service features
    CONTENT_MANAGEMENT = "PR2101", "Content Management"
    PACKAGE_HANDLING = "PR2102", "Package Handling"
    POLICIES = "PR2103", "Policies"
    BLOG = "PR2104", "Blog"
    # Package service features
    SERVICE_AND_FEATURES = "PR2201", "Service and Features"
    MODULE_CREATION = "PR2202", "Module Creation"
    PACKAGE_CREATION = "PR2203", "Package Creation"
    # campaign features
    CAMPAIGN_CREATION = "PR2301", "Campaign Creation"
    # contract features
    CONTRACT_CREATION = "PR2401", "Contract Creation"
    # TMS features
    TENANT_CREATION = "PR2501", "Tenant Creation"
    SUBSCRIPTION_MANAGEMENT = "PR2502", "Subscription Management"
    # Payment Service features
    PAYMENT_MANAGEMENT = "PR2601", "Payment Management"
    # CDXE features
    CONNECTION = "PR2701", "Connection"
    DATA_ENTRY = "PR2702", "Data Entry"
    DATA_SHARING = "PR2703", "Data Sharing"
    REQUEST_MANAGEMENT = "PR2704", "Request Management"
    REPORT_SHARING = "PR2705", "Report Sharing"
    # EBilling features
    BILL_CREATION = "PR2801", "Bill Creation"
    BILL_RETURN = "PR2802", "Bill Return"
    PRODUCT_CAMPAIGN = "PR905", "Product Campaign"


class MainModule(models.TextChoices):
    MASTER = "master dashboard", "Master Dashboard"
    INVENTORY = "inventory", "Inventory"
    PURCHASE = "purchase", "Purchase"
    SALES = "sales", "Sales"
    ACCOUNTING = "accounting", "Accounting"
    EBILLING = "ebilling", "Ebilling"
    CDXE = "CDXE", "CDXE"
    REPORTING = "reporting","Reporting"
    

class ActionChoices(models.TextChoices):
    ADD_EDIT = "add_edit", "Add/Edit"
    VIEW = "view", "View"
    APPROVE_CANCEL = "approve_cancel", "Approve/Cancel"
    ACTIVE_INACTIVE = "active_inactive", "Active/Inactive"
    EXPORT = "export", "Export"
    OPEN_CLOSE = "open_close", "Open/Close"


class OrderSearchSelectParameter(models.TextChoices):
    DELIVERY_NOTE = "delivery_note", "Delivery Note"
    INVOICE = "invoice", "Invoice"
    

class InventoryTransactionType(models.TextChoices):
    SALES_INVOICE = "sales_invoice", "Sales Invoice"
    SALES_RETURN = "sales_return", "Sales Return"


class DeliveryNoteSearchSelectParameter(models.TextChoices):
    RETURN_DELIVERY = "return_delivery", "Return Delivery"
    INVOICE = "invoice", "Invoice"
    

class ConfigurationTypeChoices(models.TextChoices):
    APPROVAL_WORK = "approval_workflow", "Approval Workflow"
    PURCHASE_FLOW = "purchase_flow", "Purchase Flow"
    SALES_FLOW = "sales_flow", "Sales Flow"
    EXPENSE_CONF = "expense_configuration", "Expense Configuration"
    PRODUCT_FLOW = "product_configuration", "Product Configuration"
    GL_MAPPING = "gl_mapping", "GL Mapping"
    
class ConfigurationStatus(models.TextChoices):
    FLOW = "workflow", "Workflow"
    AUTOMATION = "accounting_automation", "Accounting Automation"
    DISCOUNTAMT = "discount_amount", "Discount Amount"
    AMOUNT = "amount", "Amount"
    BATCH_AND_SERIAL = "batch_serial", "Batch and Serial"
    STOCK_KEEPING = "stock_keeping", "Stock Keeping Mechanism"
    PRODUCT_GL = "product_gl", "Product GL Mapping"
    SUPPLIER = "supplier", "Supplier"
    CUSTOMER = "customer", "Customer"
    EMPLOYEE = "employee", "Employee"
    BANK = "bank", "Bank"
    FY_ESSENCE = "fy_essence", "FY Essence"
    UNIQUE_ID = "unique_id_generation", "Unique ID Generation" 
    
class ConfigTitle(models.TextChoices):
    BASIC = "basic", "Basic Approval"
    CUSTOM = "custom", "Custom Approval"
    BASIC_GRN = "basic_with_grn", "Basic flow with GRN"
    BASIC_N_GRN = "basic_without_grn", "Basic flow without GRN"
    BASIC_DN = "basic_with_delivery_note", "Basic flow with Delivery Note"
    BASIC_N_DN = "basic_without_delivery_note", "Basic flow without Delivery Note"
    GRIR = "gr_ir_account", "GR/IR Account"
    VAT_RECEIVABLE = "VAT_Receivable", "VAT Receivable"
    VAT_PAYABLE = "VAT_Payable", "VAT Payable"
    ACCOUNT_PAYABLE_VENDOR = "account_payable_supplier", "Account Payable Supplier"
    ACCOUNT_PAYABLE_EMPLOYEE = "account_payable_employee", "Account Payable Employee"
    ACCOUNT_RECEIVABLE = "account_receivable", "Account Receivable"
    BANK_GROUP = "bank_group", "Bank Group"
    ENABLE_BATCH = "enable_batch", "Enable Batch"
    EXPIRY = "expiry", "Expiry"
    INVENTORY_SETUP = "inventory_setup", "Setup Inventory Valuation on Purchase"
    UNIQUE_ID = "unique_id", "Unique ID generation"