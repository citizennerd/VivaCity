from django.contrib import admin
from postdoc.models import *

class DataModelAttributeInline(admin.TabularInline):
    model = DataModelAttribute
    fk_name = "model"

class DataModelAdmin(admin.ModelAdmin):
    model = DataModel
    inlines = [
        DataModelAttributeInline
    ]

admin.site.register(DataModel,DataModelAdmin)
admin.site.register(DataTag)
admin.site.register(ModelTags)
admin.site.register(DataModelAttribute)
admin.site.register(DataInstance)
admin.site.register(DataInstanceAttribute)