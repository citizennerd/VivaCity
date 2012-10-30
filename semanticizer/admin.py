from django.contrib import admin 
from semanticizer.models import *

class SemanticsSpecificationInline(admin.TabularInline):
    model = SemanticsSpecification
    
class GeoSemanticsSpecificationInline(admin.TabularInline):
    model = GeoSemanticsSpecification
class TimeSemanticsSpecificationInline(admin.TabularInline):
    model = TimeSemanticsSpecification

class SemanticsInLine(admin.StackedInline):
    model = Semantics
    inlines = [
        SemanticsSpecificationInline,
        GeoSemanticsSpecificationInline
    ]
    
class DataSetColumnInline(admin.ModelAdmin):
    model = DataSetColumn
    fields=["name"]
    
class DataSetAdmin(admin.ModelAdmin):
    list_display=('file', 'format')
    inlines = [
        SemanticsInLine,
    ]
class SemanticsAdmin(admin.ModelAdmin):
    model = Semantics
    inlines = [
        SemanticsSpecificationInline,
        GeoSemanticsSpecificationInline,
        TimeSemanticsSpecificationInline
    ]
    



admin.site.register(DataSetFormat)
admin.site.register(DataSet, DataSetAdmin)
admin.site.register(Semantics, SemanticsAdmin)
admin.site.register(SemanticsSpecification)
admin.site.register(SemanticsSpecificationPath)
admin.site.register(DataSetColumn,DataSetColumnInline)
admin.site.register(GeoSemanticsSpecification)