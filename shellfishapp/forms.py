from django import forms
from .models import TaxonmyDistributionInsert, SynonymsInsert, MorphologicalInsert, TypeSpecimenInsert, BiologyInsert, ImageInsert, \
    OccurrenceInsert,Crab_TaxonmyDistributionInsert,Crab_MorphologicalInsert,Crab_SynonymsInsert,Crab_OccurrenceInsert,Crab_TypeSpecimenInsert,Lobster_SynonymsInsert,Lobster_TaxonmyDistributionInsert,Lobster_TypeSpecimenInsert,Lobster_MorphologicalInsert,Crab_ImageInsert, \
    Lobster_OccurrenceInsert, Lobster_ImageInsert,Location
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


GENDER = [("male", "Male"),
          ("female", "Female"), ]


# Create your forms here.
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, max_length=60)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    organization = forms.CharField(max_length=50)
    department = forms.CharField(max_length=50)
    designation = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=12)
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER))

    class Meta:
        model = User
        fields = (
            "username", "email", "first_name", "last_name", "gender", "phone", "organization", "department",
            "designation",
            "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=1000)



class TaxonmyDistributionForms(forms.ModelForm):
    class Meta:
        model = TaxonmyDistributionInsert
        fields = "__all__"

class GeneralInformationForms(forms.ModelForm):
    class Meta:
       model = TaxonmyDistributionInsert
       fields = [ 'ScientificName', 'Environment', 'CommonName', 'ConservationStatus', 'PopulationStatus', 'MainReference', 'DistributionInIndia', 'DistributionOutsideOfIndia']


class Crab_GeneralInformationForms(forms.ModelForm):
    class Meta:
       model = Crab_TaxonmyDistributionInsert
       fields = [ 'ScientificName', 'Environment', 'CommonName', 'ConservationStatus', 'PopulationStatus', 'MainReference', 'DistributionInIndia', 'DistributionOutsideOfIndia']



class Lobster_GeneralInformationForms(forms.ModelForm):
    class Meta:
       model = Lobster_TaxonmyDistributionInsert
       fields = [ 'ScientificName', 'Environment', 'CommonName', 'ConservationStatus', 'PopulationStatus', 'MainReference', 'DistributionInIndia', 'DistributionOutsideOfIndia']




class SynonymsForms(forms.ModelForm):
    class Meta:
        model = SynonymsInsert
        fields = "__all__"

class MorphologicalForms(forms.ModelForm):
    class Meta:
        model = MorphologicalInsert
        fields = "__all__"

class TypeSpecimenForms(forms.ModelForm):
    class Meta:
        model = TypeSpecimenInsert
        fields = "__all__"

class BiologyForms(forms.ModelForm):
    class Meta:
        model = BiologyInsert
        fields = "__all__"

class OccurrenceForms(forms.ModelForm):
    class Meta:
        model = OccurrenceInsert
        fields = "__all__"

class ImageForms(forms.ModelForm):
    class Meta:
        model = ImageInsert
        fields = "__all__"



class Crab_TaxonomyDistributionForms(forms.ModelForm):
    class Meta:
        model=Crab_TaxonmyDistributionInsert
        fields="__all__"

class Crab_MorphoLogicalForms(forms.ModelForm):
    class Meta:
        model=Crab_MorphologicalInsert
        fields="__all__"

class Crab_OccurrenceForms(forms.ModelForm):
    class Meta:
        model=Crab_OccurrenceInsert
        fields="__all__"

class Crab_TypeSpecimenForms(forms.ModelForm):
    class Meta:
        model=Crab_TypeSpecimenInsert
        fields="__all__"

class Crab_SynonymsForms(forms.ModelForm):
    class Meta:
        model=Crab_SynonymsInsert
        fields="__all__"

class Crab_ImageForms(forms.ModelForm):
    class Meta:
        model = Crab_ImageInsert
        fields = "__all__"



class Lobster_TaxonmyDistributionForms(forms.ModelForm):
    class Meta:
        model = Lobster_TaxonmyDistributionInsert
        fields = "__all__"

class Lobster_SynonymsForms(forms.ModelForm):
    class Meta:
        model = Lobster_SynonymsInsert
        fields = "__all__"

class Lobster_MorphologicalForms(forms.ModelForm):
    class Meta:
        model = Lobster_MorphologicalInsert
        fields = "__all__"

class Lobster_TypeSpecimenForms(forms.ModelForm):
    class Meta:
        model = Lobster_TypeSpecimenInsert
        fields = "__all__"

class Lobster_OccurrenceForms(forms.ModelForm):
    class Meta:
        model = Lobster_OccurrenceInsert
        fields = "__all__"

class Lobster_ImageForms(forms.ModelForm):
    class Meta:
        model = Lobster_ImageInsert
        fields = "__all__"



class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('latitude', 'longitude','ScientificName','ShrimpPrawnID')
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            
        }
        
        
class SearchForm(forms.Form):
    model_choice = forms.ChoiceField(choices=[('Crab_TaxonmyDistributionInsert', 'Crab'), ('Lobster_TaxonmyDistributionInsert', 'Lobster')])
    scientific_name = forms.CharField(max_length=500)

    model = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = kwargs['model'] if 'model' in kwargs else None

    def get_scientific_names(self):
        if self.model is None:
            raise Exception('The model attribute is not initialized.')

        scientific_names = []
        model_objects = self.model.objects.all()
        for model_object in model_objects:
            scientific_names.append(model_object.scientific_name)
        return scientific_names    