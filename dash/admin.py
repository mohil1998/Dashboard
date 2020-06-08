from django.contrib import admin
from .models import FilesDB,Dashboard,Graph

# Register your models here.
admin.site.register(FilesDB)
admin.site.register(Dashboard)
admin.site.register(Graph)
