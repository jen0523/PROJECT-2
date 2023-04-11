from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    title= models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    ACTAKEN_Total= models.IntegerField(default=0, null=True, blank=True)
    ACTAKEN_Ratio= models.IntegerField(default=0, null=True, blank=True)

    created = models.DateTimeField (auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    ACTAKEN_TYPE = (
        ('x1', 'Requires Sanding'),
        ('y1', 'Requires Internal Repair'),
        ('z1', 'Requires External Repair'),
        ('x2', 'Brand new to Production'),
        ('y2', 'Scrapped'),
        ('z1', 'Return to Production'),

    )
    #owner=
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=ACTAKEN_TYPE)
    created = models.DateTimeField (auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value
    

class Tag(models.Model):
    name = models.CharField(max_length=500)
    created = models.DateTimeField (auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
        
    def __str__(self):
        return self.name


class History(models.Model):
    probe_card_id = models.CharField(max_length=500)
    tool_id = models.CharField(max_length=500)
    issue_by= models.CharField(max_length=500)
    user= models.CharField(max_length=500)
    comments = models.CharField(max_length=500)
    date = models.DateTimeField (auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
        
    def __str__(self):
        return self.probe_card_id
    
class Historyin(models.Model):
    probe_card_id = models.CharField(max_length=500)
    technician = models.CharField(max_length=500)
    burned_needles = models.CharField(max_length=500)
    melted_needles = models.CharField(max_length=500)
    bent_needles = models.CharField(max_length=500)
    phisical_issue = models.CharField(max_length=500)
    comments = models.CharField(max_length=500)
    probe_count_notes= models.CharField(max_length=500)
    action_taken = models.CharField(max_length=500)
    rework_sanding_cycles = models.CharField(max_length=500)
    date = models.DateTimeField (auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
        
    def __str__(self):
        return self.technician

class Historyadd(models.Model):
    probe_card_id = models.CharField(max_length=500)
    vendor_name= models.CharField(max_length=500)
    vendor = models.CharField(max_length=500)
    arrived = models.CharField(max_length=500)
    vendor_serial = models.CharField(max_length=500)
    comments = models.CharField(max_length=500)
    status = models.CharField(max_length=500)
    date = models.DateTimeField (auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.vendor
    
class Historyorder(models.Model):
    po_number = models.CharField(max_length=500)
    vendor = models.CharField(max_length=500)
    probe_card_id = models.CharField(max_length=500)
    vendor_name= models.CharField(max_length=500)
    quantity= models.CharField(max_length=500)
    price= models.CharField(max_length=500)
    order_date = models.CharField(max_length=500)
    date = models.DateTimeField (auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.po_number
    