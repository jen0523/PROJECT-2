from django.contrib import admin

# Register your models here.
from.models import Project, Review, Tag, History, Historyin, Historyadd, Historyorder    

admin.site.register(Project)
admin.site.register(Review)
admin.site.register(Tag)
admin.site.register(History)
admin.site.register(Historyin)
admin.site.register(Historyadd)
admin.site.register(Historyorder)