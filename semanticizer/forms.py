from django.forms import ModelForm

from semanticizer.models import * 

class DataSetForm(ModelForm):
    class Meta:
        model = DataSet
        
class SemanticsForm(ModelForm):
    class Meta:
        model = Semantics
        
class SemanticsSpecificationForm(ModelForm):
    class Meta:
        model = SemanticsSpecification