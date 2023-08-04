from .forms import NewUserForm
import json

from django.http import JsonResponse,HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Count
from django.views.generic import TemplateView
from shellfishapp.models import TaxonmyDistributionInsert
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import authenticate
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_GET
from django.shortcuts import render, redirect
from .models import TaxonmyDistributionInsert, SynonymsInsert, MorphologicalInsert, TypeSpecimenInsert, BiologyInsert, \
    OccurrenceInsert, ImageInsert,Crab_SynonymsInsert,Crab_TaxonmyDistributionInsert,Crab_MorphologicalInsert,Crab_OccurrenceInsert,Crab_TypeSpecimenInsert,Lobster_MorphologicalInsert,Lobster_SynonymsInsert,Lobster_TaxonmyDistributionInsert,Lobster_TypeSpecimenInsert,Crab_ImageInsert, \
    Lobster_OccurrenceInsert, Lobster_ImageInsert,TypeLocalityInsert, TaxonmyDistributionInsert,Location
from django.contrib import messages
from .forms import SearchForm,TaxonmyDistributionForms, SynonymsForms, MorphologicalForms, TypeSpecimenForms, BiologyForms, OccurrenceForms, ImageForms, Crab_TaxonomyDistributionForms,Crab_MorphoLogicalForms,Crab_OccurrenceForms,Crab_SynonymsForms,Crab_TypeSpecimenForms,Crab_ImageForms, \
Lobster_MorphologicalForms, Lobster_SynonymsForms, Lobster_TaxonmyDistributionForms, Lobster_TypeSpecimenForms, Lobster_OccurrenceForms,Lobster_ImageForms,GeneralInformationForms,Crab_GeneralInformationForms,Lobster_GeneralInformationForms,LocationForm






def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        else:
            messages.error(request, "Account Creation failed")

        return redirect("home_page")

    form = NewUserForm()
    return render(request=request, template_name="shellfishapp/register.html", context={"register_form": form})




def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home_page")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('home_page')
    form = AuthenticationForm()
    return render(request=request, template_name="shellfishapp/login.html", context={"login_form": form})



def logout_request(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("search_page")


def home(request):
    return render(request, 'shellfishapp/home.html')



def search(request):
    distributions = TaxonmyDistributionInsert.objects.count()
    distributions1 = Crab_TaxonmyDistributionInsert.objects.count()
    distributions2 = Lobster_TaxonmyDistributionInsert.objects.count()
    distributions3 = TaxonmyDistributionInsert.objects.values('Order').annotate(count=Count('Order')).count()
    distributions4= TaxonmyDistributionInsert.objects.values('Order').distinct().count()
    distributions5 = TaxonmyDistributionInsert.objects.values('Genus').annotate(count=Count('Genus')).count()
    distributions6 = TaxonmyDistributionInsert.objects.values('Family').annotate(count=Count('Family')).count()
    distributions7 = TypeSpecimenInsert.objects.count()
    distributions8 = Crab_TaxonmyDistributionInsert.objects.values('Genus').annotate(count=Count('Genus')).count()
    distributions9 = Lobster_TaxonmyDistributionInsert.objects.values('Genus').annotate(count=Count('Genus')).count()
    distributions10 = Crab_TaxonmyDistributionInsert.objects.values('Family').annotate(count=Count('Family')).count()
    distributions11 = Lobster_TaxonmyDistributionInsert.objects.values('Family').annotate(count=Count('Family')).count()
    distributions12 = Crab_TaxonmyDistributionInsert.objects.values('Order').annotate(count=Count('Order')).count()
    distributions13 = Lobster_TaxonmyDistributionInsert.objects.values('Order').annotate(count=Count('Order')).count()
    distributions14 = Crab_TypeSpecimenInsert.objects.count()
    distributions15 = Lobster_TypeSpecimenInsert.objects.count()
    distributions16 = OccurrenceInsert.objects.count()
    distributions17 = Crab_OccurrenceInsert.objects.count()
    distributions18 = Lobster_OccurrenceInsert.objects.count()
    distributions19 = MorphologicalInsert.objects.count()
    distributions20 = BiologyInsert.objects.count()
    distributions21 = Crab_MorphologicalInsert.objects.values('Biology').annotate(count=Count('Biology')).count()
    distributions22 = Lobster_MorphologicalInsert.objects.values('Biology').annotate(count=Count('Biology')).count()
    distributions23 = Crab_MorphologicalInsert.objects.count()
    distributions24 = Lobster_MorphologicalInsert.objects.count()
    distributions25 = TaxonmyDistributionInsert.objects.filter(Environment__icontains='marine').count()
    distributions26 = TaxonmyDistributionInsert.objects.filter(Environment__icontains='brackish').count()
    distributions27 = TaxonmyDistributionInsert.objects.filter(Environment__icontains='freshwater').count()
    distributions28 = Crab_TaxonmyDistributionInsert.objects.filter(Environment__icontains='marine').count()
    distributions29 = Crab_TaxonmyDistributionInsert.objects.filter(Environment__icontains='brackish').count()
    distributions30 = Crab_TaxonmyDistributionInsert.objects.filter(Environment__icontains='freshwater ').count()
    distributions31 = Lobster_TaxonmyDistributionInsert.objects.filter(Environment__icontains='marine').count()
    distributions32 = Lobster_TaxonmyDistributionInsert.objects.filter(Environment__icontains='brackish').count()
    distributions33 = Lobster_TaxonmyDistributionInsert.objects.filter(Environment__icontains='freshwater ').count()
    
    
    return render(request, 'shellfishapp/Search.html',{'distributions': distributions,'distributions1': distributions1,'distributions2': distributions2,'distributions3': distributions3,'distributions4': distributions4,'distributions5': distributions5,'distributions6': distributions6,'distributions7': distributions7,'distributions8': distributions8,'distributions9': distributions9,'distributions10': distributions10,'distributions11': distributions11,'distributions12': distributions12,'distributions13': distributions13,'distributions14': distributions14,'distributions15': distributions15,'distributions16': distributions16,'distributions17': distributions17,'distributions18': distributions18,'distributions19': distributions19,'distributions20': distributions20,'distributions21': distributions21,'distributions22': distributions22,'distributions23': distributions23,'distributions24': distributions24,'distributions25': distributions25,'distributions26': distributions26,'distributions27': distributions27,'distributions28': distributions28,'distributions29': distributions29,'distributions30': distributions30,'distributions31': distributions31,'distributions32': distributions32,'distributions33': distributions33})







#Views of ShrimpPrawns_TaxonomyAndDistribution
#Function to add data to TaxonomyAndDistribution 
def taxoadd(request):
    if request.method == "POST":
        if request.POST.get('CrusteceanSubgroup') or \
                request.POST.get('CrusteceanSubgroupType') or \
                request.POST.get('Kingdom') or \
                request.POST.get('Phylum') or \
                request.POST.get('SubPhylum') or \
                request.POST.get('Class') or \
                request.POST.get('SubClass') or \
                request.POST.get('SuperOrder') or \
                request.POST.get('Order') or \
                request.POST.get('SubOrder') or \
                request.POST.get('InfraOrder') or \
                request.POST.get('SuperFamily') or \
                request.POST.get('Family') or \
                request.POST.get('SubFamily') or \
                request.POST.get('Genus') or \
                request.POST.get('ScientificName') or \
                request.POST.get('TaxonomicRank') or \
                request.POST.get('Subspecies') or \
                request.POST.get('Environment') or \
                request.POST.get('CommonName') or \
                request.POST.get('ConservationStatus') or \
                request.POST.get('PopulationStatus') or \
                request.POST.get('AcceptedValidName') or \
                request.POST.get('Author') or \
                request.POST.get('MainReference') or \
                request.POST.get('DistributionInIndia') or \
                request.POST.get('DistributionOutsideOfIndia'):
            saverecord = TaxonmyDistributionInsert()
            saverecord.CrusteceanSubgroup = request.POST.get('CrusteceanSubgroup')
            saverecord.CrusteceanSubgroupType = request.POST.get('CrusteceanSubgroupType')
            saverecord.Kingdom = request.POST.get('Kingdom')
            saverecord.Phylum = request.POST.get('Phylum')
            saverecord.SubPhylum = request.POST.get('SubPhylum')
            saverecord.Class = request.POST.get('Class')
            saverecord.SubClass = request.POST.get('SubClass')
            saverecord.SuperOrder = request.POST.get('SuperOrder')
            saverecord.Order = request.POST.get('Order')
            saverecord.SubOrder = request.POST.get('SubOrder')
            saverecord.InfraOrder = request.POST.get('InfraOrder')
            saverecord.SuperFamily = request.POST.get('SuperFamily')
            saverecord.Family = request.POST.get('Family')
            saverecord.SubFamily = request.POST.get('SubFamily')
            saverecord.Genus = request.POST.get('Genus')
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.TaxonomicRank = request.POST.get('TaxonomicRank')
            saverecord.Subspecies = request.POST.get('Subspecies')
            saverecord.Environment = request.POST.get('Environment')
            saverecord.CommonName = request.POST.get('CommonName')
            saverecord.ConservationStatus = request.POST.get('ConservationStatus')
            saverecord.PopulationStatus = request.POST.get('PopulationStatus')
            saverecord.AcceptedValidName = request.POST.get('AcceptedValidName')
            saverecord.Author = request.POST.get('Author')
            saverecord.MainReference = request.POST.get('MainReference')
            saverecord.DistributionInIndia = request.POST.get('DistributionInIndia')
            saverecord.DistributionOutsideOfIndia = request.POST.get('DistributionOutsideOfIndia')
            saverecord.save()
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/taxonomy_add.html')
    else:
        return render(request, 'shellfishapp/taxonomy_add.html')

def viewpage(request):
    result_display = TaxonmyDistributionInsert.objects.all()
    return render(request, 'shellfishapp/view_page.html', {'TaxonmyDistributionInsert': result_display})





def UA_taxoview(request):
    result_display = TaxonmyDistributionInsert.objects.all()
    p = Paginator(TaxonmyDistributionInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/UA_taxonomy_view.html', {'vw': vw, 'TaxonmyDistributionInsert': result_display})

def taxoview(request):
    result_display = TaxonmyDistributionInsert.objects.all()
    p = Paginator(TaxonmyDistributionInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/taxonomy_view.html', {'vw': vw, 'TaxonmyDistributionInsert': result_display})

def taxoedit(request,id):
    result_edit = TaxonmyDistributionInsert.objects.get(id=id)
    return render(request, 'shellfishapp/taxonomy_edit.html', {'TaxonmyDistributionInsert': result_edit})

def taxoupdate(request,id):
    result_update = TaxonmyDistributionInsert.objects.get(id=id)
    form = TaxonmyDistributionForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/taxonomy_edit.html', {'TaxonmyDistributionInsert': result_update})

def taxodelete(request,id):
    result_delete = TaxonmyDistributionInsert.objects.get(id=id)
    result_delete.delete()
    results = TaxonmyDistributionInsert.objects.all()
    return render(request, 'shellfishapp/taxonomy_view.html', {'TaxonmyDistributionInsert': results})

def taxasearch(request):
    SciName = TaxonmyDistributionInsert.objects.all()
    if request.method=="GET":
        chk = 0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = TaxonmyDistributionInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1
        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/taxonomy_search.html', {'TaxonmyDistributionInsert': SciName, 'chk': chk})


@require_GET
def autocomplete(request):
    term = request.GET.get('term')
    results = []
    if term is not None and len(term) >= 1:
        distributions = TaxonmyDistributionInsert.objects.filter(ScientificName__icontains=term)
        crab_results = Crab_TaxonmyDistributionInsert.objects.filter(ScientificName__icontains=term)
        lobster_results = Lobster_TaxonmyDistributionInsert.objects.filter(ScientificName__icontains=term)
        results = [distribution.ScientificName for distribution in distributions]
        results += [distribution.ScientificName for distribution in lobster_results]
        results += [distribution.ScientificName for distribution in crab_results]
    return JsonResponse(results, safe=False)
    
class SearchView(TemplateView):
    template_name = 'shellfishapp/autocomplete.html'   
    
@require_GET
def autocomplete1(request):
    term = request.GET.get('term')
    results = []
    if term is not None and len(term) >= 1:
        distributions = TaxonmyDistributionInsert.objects.filter(ScientificName__icontains=term)
        
        results = [distribution.ScientificName for distribution in distributions]
        
    return JsonResponse(results, safe=False)    
    
@require_GET
def autocomplete2(request):
    term = request.GET.get('term')
    results = []
    if term is not None and len(term) >= 1:
        
        crab_results = Crab_TaxonmyDistributionInsert.objects.filter(ScientificName__icontains=term)
        
        
        results += [distribution.ScientificName for distribution in crab_results]
    return JsonResponse(results, safe=False)
    
@require_GET
def autocomplete3(request):
    term = request.GET.get('term')
    results = []
    if term is not None and len(term) >= 1:
        
        lobster_results = Lobster_TaxonmyDistributionInsert.objects.filter(ScientificName__icontains=term)
        
        results += [distribution.ScientificName for distribution in lobster_results]
        
    return JsonResponse(results, safe=False)
    
    
    
    
def ScientificName_Search(request):
    SciName=TaxonmyDistributionInsert.objects.all()
    SciName1=Crab_TaxonmyDistributionInsert.objects.all()
    SciName2=Lobster_TaxonmyDistributionInsert.objects.all()
    SciName3=ImageInsert.objects.all()
    SciName4=Crab_ImageInsert.objects.all()
    SciName5=Lobster_ImageInsert.objects.all()



    if request.method=="GET":
        chk=0
        sn=request.GET.get('ScientificName')
        if sn and len(sn) >= 3:
            SciName=TaxonmyDistributionInsert.objects.filter(ScientificName__iexact=sn)
            SciName1=Crab_TaxonmyDistributionInsert.objects.filter(ScientificName__iexact=sn)
            SciName2=Lobster_TaxonmyDistributionInsert.objects.filter(ScientificName__iexact=sn)
            SciName3=ImageInsert.objects.filter(ScientificName__iexact=sn)
            SciName4=Crab_ImageInsert.objects.filter(ScientificName__iexact=sn)
            SciName5=Lobster_ImageInsert.objects.filter(ScientificName__iexact=sn)

            chk = 1
    if not (SciName.exists() or SciName1.exists() or SciName2.exists() or SciName3.exists() or SciName4.exists() or SciName5.exists()):
                
            chk = -1

    return render(request, 'shellfishapp/ScientificName_search.html', {'TaxonmyDistributionInsert': SciName,'Crab_TaxonmyDistributionInsert': SciName1,'Lobster_TaxonmyDistributionInsert': SciName2 ,'ImageInsert': SciName3,'Crab_ImageInsert': SciName4,'Lobster_ImageInsert': SciName5,'chk': chk})


def get_scientific_names(request):
    scientific_names = []

    # Retrieve all scientific names from each model
    scientific_names += list(TaxonmyDistributionInsert.objects.values_list('ScientificName', flat=True))
    scientific_names += list(Crab_TaxonmyDistributionInsert.objects.values_list('ScientificName', flat=True))
    scientific_names += list(Lobster_TaxonmyDistributionInsert.objects.values_list('ScientificName', flat=True))

    return JsonResponse(scientific_names, safe=False)











#views of ShrimpPrawn GeneralInformation


def generalinformationadd(request):
    scientificname = TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        if request.POST.get('ShrimpPrawnID') or \
                request.POST.get('ScientificName') or \
                request.POST.get('CommonName') or \
                request.POST.get('Environment') or \
                request.POST.get('PopulationStatus') or \
                request.POST.get('ConservationStatus') or \
                request.POST.get('DistributionInIndia') or \
                request.POST.get('DistributionOutsideOfIndia'):
            scientificname_obj = TaxonmyDistributionInsert.objects.get(ScientificName=request.POST.get('ScientificName'))
            
            saverecord = TaxonmyDistributionInsert()
            saverecord.Environment = request.POST.get('Environment')
            saverecord.CommonName = request.POST.get('CommonName')
            saverecord.ConservationStatus = request.POST.get('ConservationStatus')
            saverecord.PopulationStatus = request.POST.get('PopulationStatus')
            saverecord.DistributionInIndia = request.POST.get('DistributionInIndia')
            saverecord.DistributionOutsideOfIndia = request.POST.get('DistributionOutsideOfIndia')
            
            # Update the existing object instead of creating a new one
            scientificname_obj.Environment = saverecord.Environment
            scientificname_obj.CommonName = saverecord.CommonName
            scientificname_obj.ConservationStatus = saverecord.ConservationStatus
            scientificname_obj.PopulationStatus = saverecord.PopulationStatus
            scientificname_obj.DistributionInIndia = saverecord.DistributionInIndia
            scientificname_obj.DistributionOutsideOfIndia = saverecord.DistributionOutsideOfIndia
            
            scientificname_obj.save()
            
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/generalinformation_add.html', {'TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/generalinformation_add.html', {'TaxonmyDistributionInsert': scientificname})

    






def generalinformationview(request):
    result_display = TaxonmyDistributionInsert.objects.all()
    p = Paginator( TaxonmyDistributionInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/generalinformation_view.html', {'vw': vw, ' TaxonmyDistributionInsert': result_display})




def geninfoedit(request,id):
    result_edit = TaxonmyDistributionInsert.objects.get(id=id)
    return render(request, 'shellfishapp/generalinformation_edit.html', {'TaxonmyDistributionInsert': result_edit})



def generalinformationupdate(request,id):
    result_update =  TaxonmyDistributionInsert.objects.get(id=id)
    form = GeneralInformationForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/generalinformation_edit.html', {' TaxonmyDistributionInsert': result_update})

def generalinformationdelete(request,id):
    result_delete =  TaxonmyDistributionInsert.objects.get(id=id)
    result_delete.delete()
    results =  TaxonmyDistributionInsert.objects.all()
    return render(request, 'shellfishapp/generalinformation_view.html', {' TaxonmyDistributionInsert': results})

def generalinformationsearch(request):
    SciName = TaxonmyDistributionInsert.objects.all()
    if request.method=="GET":
        chk = 0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = TaxonmyDistributionInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/generalinformation_search.html', {'TaxonmyDistributionInsert': SciName, 'chk': chk})













#Views of ShrimpPrawn_Distribution
def distsearch(request):
    SciName = TaxonmyDistributionInsert.objects.all()
    if request.method=="GET":
        chk = 0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = TaxonmyDistributionInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/distribution_search.html', {'TaxonmyDistributionInsert': SciName,'chk': chk})












#Views of ShrimpPrawn_Synonyms
def synadd(request):
    scientificname = TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        if request.POST.get('ShrimpPrawnID') or \
                request.POST.get('Synonym') or \
                request.POST.get('Synonymy') or \
                request.POST.get('Status') or \
                request.POST.get('Valid') or \
                request.POST.get('Author'):
            saverecord = SynonymsInsert()
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.ShrimpPrawnID = request.POST.get('ShrimpPrawnID')
            saverecord.Synonym = request.POST.get('Synonym')
            saverecord.Synonymy = request.POST.get('Synonymy')
            saverecord.Status = request.POST.get('Status')
            saverecord.Valid = request.POST.get('Valid')
            saverecord.Author = request.POST.get('Author')
            saverecord.save()
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/synonyms_add.html', {'TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/synonyms_add.html', {'TaxonmyDistributionInsert': scientificname})

def synview(request):
    result_display = SynonymsInsert.objects.all()
    p = Paginator(SynonymsInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/synonyms_view.html', {'SynonymsInsert': result_display,'vw':vw})



def UA_synview(request):
    result_display = SynonymsInsert.objects.all()
    p = Paginator(SynonymsInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/UA_synonyms_view.html', {'SynonymsInsert': result_display,'vw':vw})

def synedit(request,id):
    result_edit = SynonymsInsert.objects.get(id=id)
    return render(request, 'shellfishapp/synonyms_edit.html', {'SynonymsInsert': result_edit})

def synupdate(request,id):
    result_update = SynonymsInsert.objects.get(id=id)
    form = SynonymsForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/synonyms_edit.html', {'SynonymsInsert': result_update})

def syndelete(request,id):
    result_delete = SynonymsInsert.objects.get(id=id)
    result_delete.delete()
    results = SynonymsInsert.objects.all()
    return render(request, 'shellfishapp/synonyms_view.html', {'SynonymsInsert': results})

def synsearch(request):
    SciName = SynonymsInsert.objects.all()
    if request.method=="GET":
        chk=0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = SynonymsInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/synonyms_search.html', {'SynonymsInsert': SciName,'chk':chk})












#Views of ShrimpPrawn_MorphologicalInsert
def morphoadd(request):
    scientificname = TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        if request.POST.get('ShrimpPrawnID') or \
                request.POST.get('ShortDescription') or \
                request.POST.get('BodyNature') or \
                request.POST.get('Eyes') or \
                request.POST.get('RostrumNature') or \
                request.POST.get('RostralTeethFormula') or \
                request.POST.get('CarapaceNature') or \
                request.POST.get('AntennuleSegments') or \
                request.POST.get('AntennalSegments') or \
                request.POST.get('MouthSegments') or \
                request.POST.get('AbdominalSomites') or \
                request.POST.get('ThridMaxilliped') or \
                request.POST.get('Pereoopod_I') or \
                request.POST.get('Pereoopod_II') or \
                request.POST.get('Pereoopod_III') or \
                request.POST.get('SternalPlate') or \
                request.POST.get('TelsonNature') or \
                request.POST.get('SexualSystem') or \
                request.POST.get('SecondarySexualSystem') or \
                request.POST.get('SexualDimorphism') or \
                request.POST.get('SpecificRemarks') or \
                request.POST.get('Colouration'):
            saverecord = MorphologicalInsert()
            saverecord.ShrimpPrawnID = request.POST.get('ShrimpPrawnID')
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.ShortDescription = request.POST.get('ShortDescription')
            saverecord.BodyNature = request.POST.get('BodyNature')
            saverecord.Eyes = request.POST.get('Eyes')
            saverecord.RostrumNature = request.POST.get('RostrumNature')
            saverecord.RostralTeethFormula = request.POST.get('RostralTeethFormula')
            saverecord.CarapaceNature = request.POST.get('CarapaceNature')
            saverecord.AntennuleSegments = request.POST.get('AntennuleSegments')
            saverecord.AntennalSegments = request.POST.get('AntennalSegments')
            saverecord.MouthSegments = request.POST.get('MouthSegments')
            saverecord.AbdominalSomites = request.POST.get('AbdominalSomites')
            saverecord.ThridMaxilliped = request.POST.get('ThridMaxilliped')
            saverecord.Pereoopod_I = request.POST.get('Pereoopod_I')
            saverecord.Pereoopod_II = request.POST.get('Pereoopod_II')
            saverecord.Pereoopod_III = request.POST.get('Pereoopod_III')
            saverecord.SternalPlate = request.POST.get('SternalPlate')
            saverecord.TelsonNature = request.POST.get('TelsonNature')
            saverecord.SexualSystem = request.POST.get('SexualSystem')
            saverecord.SecondarySexualSystem = request.POST.get('SecondarySexualSystem')
            saverecord.SexualDimorphism = request.POST.get('SexualDimorphism')
            saverecord.SpecificRemarks = request.POST.get('SpecificRemarks')
            saverecord.Colouration = request.POST.get('Colouration')
            saverecord.save()
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/morphological_add.html', {'TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/morphological_add.html', {'TaxonmyDistributionInsert': scientificname})

def morphoview(request):
    result_display = MorphologicalInsert.objects.all()
    p = Paginator(MorphologicalInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/morphological_view.html', {'MorphologicalInsert': result_display,'vw':vw})


def UA_morphoview(request):
    result_display = MorphologicalInsert.objects.all()
    p = Paginator(MorphologicalInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/UA_morphological_view.html', {'MorphologicalInsert': result_display,'vw':vw})



def morphoedit(request,id):
    result_edit = MorphologicalInsert.objects.get(id=id)
    return render(request, 'shellfishapp/morphological_edit.html', {'MorphologicalInsert': result_edit})

def morphoupdate(request,id):
    result_update = MorphologicalInsert.objects.get(id=id)
    form = MorphologicalForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Update Successfully")
    return render(request, "shellfishapp/morphological_edit.html", {"MorphologicalInsert": result_update})

def morphodelete(request,id):
    result_delete = MorphologicalInsert.objects.get(id=id)
    result_delete.delete()
    results = MorphologicalInsert.objects.all()
    return render(request, 'shellfishapp/morphological_view.html', {'MorphologicalInsert': results})

def morphosearch(request):
    SciName = MorphologicalInsert.objects.all()
    if request.method=="GET":
        chk=0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = MorphologicalInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/morphological_search.html', {'MorphologicalInsert': SciName,'chk':chk})











#Views of ShrimpPrawn_TypeSpecimen
def speciadd(request):
    scientificname = TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        if request.POST.get('ShrimpPrawnID') or \
                request.POST.get('TypeSpecimenStatus') or \
                request.POST.get('TypeSpecimenRepository') or \
                request.POST.get('TypeLocality') or \
                request.POST.get('Author') or \
                request.POST.get('TypeSpecimenCatalogueNumber') or \
                request.POST.get('URL') or \
                request.POST.get('Source'):
            saverecord = TypeSpecimenInsert()
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.ShrimpPrawnID = request.POST.get('ShrimpPrawnID')
            saverecord.TypeSpecimenStatus = request.POST.get('TypeSpecimenStatus')
            saverecord.TypeSpecimenRepository = request.POST.get('TypeSpecimenRepository')
            saverecord.TypeLocality = request.POST.get('TypeLocality')
            saverecord.Author = request.POST.get('Author')
            saverecord.TypeSpecimenCatalogueNumber = request.POST.get('TypeSpecimenCatalogueNumber')
            saverecord.URL = request.POST.get('URL')
            saverecord.Source = request.POST.get('Source')
            saverecord.save()
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/typespecimen_add.html', {'TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/typespecimen_add.html', {'TaxonmyDistributionInsert': scientificname})

def speciview(request):
    result_display = TypeSpecimenInsert.objects.all()
    p = Paginator(TypeSpecimenInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/typespecimen_view.html', {'TypeSpecimenInsert': result_display,'vw':vw})


def UA_speciview(request):
    result_display = TypeSpecimenInsert.objects.all()
    p = Paginator(TypeSpecimenInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/UA_typespecimen_view.html', {'TypeSpecimenInsert': result_display,'vw':vw})


def speciedit(request,id):
    result_edit = TypeSpecimenInsert.objects.get(id=id)
    return render(request, 'shellfishapp/typespecimen_edit.html', {'TypeSpecimenInsert': result_edit})

def speciupdate(request,id):
    result_update = TypeSpecimenInsert.objects.get(id=id)
    form = TypeSpecimenForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/typespecimen_edit.html', {'TypeSpecimenInsert': result_update})

def specidelete(request,id):
    result_delete = TypeSpecimenInsert.objects.get(id=id)
    result_delete.delete()
    results = TypeSpecimenInsert.objects.all()
    return render(request, 'shellfishapp/typespecimen_view.html', {'TypeSpecimenInsert': results})

def specisearch(request):
    SciName = TypeSpecimenInsert.objects.all()
    if request.method=="GET":
        chk=0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = TypeSpecimenInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/typespecimen_search.html', {'TypeSpecimenInsert': SciName,'chk':chk})













#All view of ShrimpPrawn_Biology
def bioadd(request):
    scientificname = TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        if request.POST.get('ShrimpPrawnID') or \
                request.POST.get('Ecology_Habitat') or \
                request.POST.get('LifeCycleAndMatingBehaviour') or \
                request.POST.get('LifeSpan') or \
                request.POST.get('SymbioticRelationship') or \
                request.POST.get('DepthRanges') or \
                request.POST.get('Biology') or \
                request.POST.get('Sex') or \
                request.POST.get('SizeRangesTotalLength') or \
                request.POST.get('SizeRangesCarapaceLength') or \
                request.POST.get('ReproductionStrategy') or \
                request.POST.get('BreedingSeason') or \
                request.POST.get('SexualDimorphism') or \
                request.POST.get('MoltingFrequency') or \
                request.POST.get('BreedingFrequency') or \
                request.POST.get('AgeSexualMaturity') or \
                request.POST.get('Fecundity') or \
                request.POST.get('LarvalDevelopment') or \
                request.POST.get('Group') or \
                request.POST.get('Mobility') or \
                request.POST.get('Dispersion') or \
                request.POST.get('FeedingBehaviour') or \
                request.POST.get('FeedingType') or \
                request.POST.get('FoodItems') or \
                request.POST.get('CommericalImportance') or \
                request.POST.get('EcologicalUtlity') or \
                request.POST.get('EconomicUtility') or \
                request.POST.get('AquacultureUtility') or \
                request.POST.get('ConsumerUtility') or \
                request.POST.get('Competitors') or \
                request.POST.get('EcologicalImpact') or \
                request.POST.get('EconomicImpact') or \
                request.POST.get('Comments'):
            saverecord = BiologyInsert()
            saverecord.ShrimpPrawnID = request.POST.get('ShrimpPrawnID')
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.Ecology_Habitat = request.POST.get('Ecology_Habitat')
            saverecord.LifeCycleAndMatingBehaviour = request.POST.get('LifeCycleAndMatingBehaviour')
            saverecord.LifeSpan = request.POST.get('LifeSpan')
            saverecord.SymbioticRelationship = request.POST.get('SymbioticRelationship')
            saverecord.DepthRanges = request.POST.get('DepthRanges')
            saverecord.Biology = request.POST.get('Biology')
            saverecord.Sex = request.POST.get('Sex')
            saverecord.SizeRangesTotalLength = request.POST.get('SizeRangesTotalLength')
            saverecord.SizeRangesCarapaceLength = request.POST.get('SizeRangesCarapaceLength')
            saverecord.ReproductionStrategy = request.POST.get('ReproductionStrategy')
            saverecord.BreedingSeason = request.POST.get('BreedingSeason')
            saverecord.SexualDimorphism = request.POST.get('SexualDimorphism')
            saverecord.MoltingFrequency = request.POST.get('MoltingFrequency')
            saverecord.BreedingFrequency = request.POST.get('BreedingFrequency')
            saverecord.AgeSexualMaturity = request.POST.get('AgeSexualMaturity')
            saverecord.Fecundity = request.POST.get('Fecundity')
            saverecord.LarvalDevelopment = request.POST.get('LarvalDevelopment')
            saverecord.Group = request.POST.get('Group')
            saverecord.Mobility = request.POST.get('Mobility')
            saverecord.Dispersion = request.POST.get('Dispersion')
            saverecord.FeedingBehaviour = request.POST.get('FeedingBehaviour')
            saverecord.FeedingType = request.POST.get('FeedingType')
            saverecord.FoodItems = request.POST.get('FoodItems')
            saverecord.CommericalImportance = request.POST.get('CommericalImportance')
            saverecord.EcologicalUtlity = request.POST.get('EcologicalUtlity')
            saverecord.EconomicUtility = request.POST.get('EconomicUtility')
            saverecord.AquacultureUtility = request.POST.get('AquacultureUtility')
            saverecord.ConsumerUtility = request.POST.get('ConsumerUtility')
            saverecord.Competitors = request.POST.get('Competitors')
            saverecord.EcologicalImpact = request.POST.get('EcologicalImpact')
            saverecord.EconomicImpact = request.POST.get('EconomicImpact')
            saverecord.Comments = request.POST.get('Comments')
            saverecord.save()
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/biology_add.html', {'TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/biology_add.html', {'TaxonmyDistributionInsert': scientificname})

def bioview(request):
    result_display = BiologyInsert.objects.all()
    p = Paginator(BiologyInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/biology_view.html', {'BiologyInsert': result_display,'vw':vw})



def UA_bioview(request):
    result_display = BiologyInsert.objects.all()
    p = Paginator(BiologyInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/UA_biology_view.html', {'BiologyInsert': result_display,'vw':vw})

def bioedit(request,id):
    result_edit = BiologyInsert.objects.get(id=id)
    return render(request, 'shellfishapp/biology_edit.html', {'BiologyInsert': result_edit})

def bioupdate(request,id):
    result_update = BiologyInsert.objects.get(id=id)
    form = BiologyForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/biology_edit.html', {'BiologyInsert': result_update})

def biodelete(request,id):
    result_delete = BiologyInsert.objects.get(id=id)
    result_delete.delete()
    results = BiologyInsert.objects.all()
    return render(request, 'shellfishapp/biology_view.html', {'BiologyInsert': results})

def biosearch(request):
    SciName = BiologyInsert.objects.all()
    if request.method=="GET":
        chk=0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = BiologyInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/biology_search.html', {'BiologyInsert': SciName,'chk':chk})











#All view of ShrimpPrawn_Occurenceinsert


def occview(request):
    result_display = OccurrenceInsert.objects.all()
    p = Paginator(OccurrenceInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/occurrence_view.html', {'OccurrenceInsert': result_display,'vw':vw})



def UA_occview(request):
    result_display = OccurrenceInsert.objects.all()
    p = Paginator(OccurrenceInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/UA_occurrence_view.html', {'OccurrenceInsert': result_display,'vw':vw})

def occedit(request,id):
    result_edit = OccurrenceInsert.objects.get(id=id)
    return render(request, 'shellfishapp/occurrence_edit.html', {'OccurrenceInsert': result_edit})

def occupdate(request,id):
    result_update = OccurrenceInsert.objects.get(id=id)
    form = OccurrenceForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/occurrence_edit.html', {'OccurrenceInsert': result_update})

def occdelete(request,id):
    result_delete = OccurrenceInsert.objects.get(id=id)
    result_delete.delete()
    results = OccurrenceInsert.objects.all()
    return render(request, 'shellfishapp/occurrence_view.html', {'OccurrenceInsert': results})

def occsearch(request):
    SciName = OccurrenceInsert.objects.all()
    if request.method=="GET":
        chk=0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = OccurrenceInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/occurrence_search.html', {'OccurrenceInsert': SciName,'chk':chk})












#Views of ShrimpPrawn_Image
def imgadd(request):
    scientificname = TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        form = ImageForms(request.POST, request.FILES)
        if form.is_valid():
            saverecord = ImageInsert()
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.ShrimpPrawnID = request.POST.get('ShrimpPrawnID')
            saverecord.Image1 = request.POST.get('Image1')
            saverecord.Image2 = request.POST.get('Image2')
            saverecord.Image3 = request.POST.get('Image3')
            form.save()
            messages.success(request, 'Images Added Successfully...!')
            return render(request, 'shellfishapp/image_add.html', {'TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/image_add.html', {'TaxonmyDistributionInsert': scientificname})

def imgview(request):
    p = Paginator(ImageInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/image_view.html', {'vw':vw})

def imgedit(request,id):
    result_edit = ImageInsert.objects.get(id=id)
    return render(request, 'shellfishapp/image_edit.html', {'ImageInsert': result_edit})



def imgdelete(request,id):
    result_delete = ImageInsert.objects.get(id=id)
    result_delete.delete()
    results = ImageInsert.objects.all()
    return render(request, 'shellfishapp/image_view.html', {'ImageInsert': results})



def imgupdate(request,id):
    result_update =ImageInsert.objects.get(id=id)
    if request.method == 'POST':
        form = ImageForms(request.POST,request.FILES, instance=result_update)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/image_edit.html', {'ImageInsert': result_update})










#All views of Crab_TaxonomyAndDistribution
def Crab_taxoadd(request):
    if request.method == "POST":
        if request.POST.get('Kingdom') or \
                request.POST.get('Phylum') or \
                request.POST.get('SubPhylum') or \
                request.POST.get('Class') or \
                request.POST.get('SubClass') or \
                request.POST.get('SuperOrder') or \
                request.POST.get('Order') or \
                request.POST.get('SubOrder') or \
                request.POST.get('InfraOrder') or \
                request.POST.get('SuperFamily') or \
                request.POST.get('Family') or \
                request.POST.get('SubFamily') or \
                request.POST.get('Genus') or \
                request.POST.get('ScientificName') or \
                request.POST.get('TaxonomicRank') or \
                request.POST.get('Subspecies') or \
                request.POST.get('Environment') or \
                request.POST.get('CommonName') or \
                request.POST.get('ConservationStatus') or \
                request.POST.get('PopulationStatus') or \
                request.POST.get('AcceptedValidName') or \
                request.POST.get('Author') or \
                request.POST.get('MainReference') or \
                request.POST.get('DistributionInIndia') or \
                request.POST.get('DistributionOutsideOfIndia') or \
                request.POST.get('OriginType'):
            saverecord = Crab_TaxonmyDistributionInsert()
            saverecord.Kingdom = request.POST.get('Kingdom')
            saverecord.Phylum = request.POST.get('Phylum')
            saverecord.SubPhylum = request.POST.get('SubPhylum')
            saverecord.Class = request.POST.get('Class')
            saverecord.SubClass = request.POST.get('SubClass')
            saverecord.SuperOrder = request.POST.get('SuperOrder')
            saverecord.Order = request.POST.get('Order')
            saverecord.SubOrder = request.POST.get('SubOrder')
            saverecord.InfraOrder = request.POST.get('InfraOrder')
            saverecord.SuperFamily = request.POST.get('SuperFamily')
            saverecord.Family = request.POST.get('Family')
            saverecord.SubFamily = request.POST.get('SubFamily')
            saverecord.Genus = request.POST.get('Genus')
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.TaxonomicRank = request.POST.get('TaxonomicRank')
            saverecord.Subspecies = request.POST.get('Subspecies')
            saverecord.Environment = request.POST.get('Environment')
            saverecord.CommonName = request.POST.get('CommonName')
            saverecord.ConservationStatus = request.POST.get('ConservationStatus')
            saverecord.PopulationStatus = request.POST.get('PopulationStatus')
            saverecord.AcceptedValidName = request.POST.get('AcceptedValidName')
            saverecord.Author = request.POST.get('Author')
            saverecord.MainReference = request.POST.get('MainReference')
            saverecord.DistributionInIndia = request.POST.get('DistributionInIndia')
            saverecord.DistributionOutsideOfIndia = request.POST.get('DistributionOutsideOfIndia')
            saverecord.OriginType = request.POST.get('OriginType')
            saverecord.save()
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/crab_taxonomy_add.html')
    else:
        return render(request, 'shellfishapp/crab_taxonomy_add.html')
    
def Crab_taxoview(request):
    result_display = Crab_TaxonmyDistributionInsert.objects.all()
    p = Paginator(Crab_TaxonmyDistributionInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/crab_taxonomy_view.html', {'vw': vw, 'Crab_TaxonmyDistributionInsert': result_display})

def UA_Crab_taxoview(request):
    result_display = Crab_TaxonmyDistributionInsert.objects.all()
    p = Paginator(Crab_TaxonmyDistributionInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/UA_crab_taxonomy_view.html', {'vw': vw, 'Crab_TaxonmyDistributionInsert': result_display})

def Crab_taxoedit(request,id):
    result_edit = Crab_TaxonmyDistributionInsert.objects.get(id=id)
    return render(request, 'shellfishapp/crab_taxonomy_edit.html', {'Crab_TaxonmyDistributionInsert': result_edit})

def Crab_taxoupdate(request,id):
    result_update = Crab_TaxonmyDistributionInsert.objects.get(id=id)
    form = Crab_TaxonomyDistributionForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/crab_taxonomy_edit.html', {'Crab_TaxonmyDistributionInsert': result_update})

def Crab_taxodelete(request,id):
    result_delete = Crab_TaxonmyDistributionInsert.objects.get(id=id)
    result_delete.delete()
    results = Crab_TaxonmyDistributionInsert.objects.all()
    return render(request, 'shellfishapp/crab_taxonomy_view.html', {'Crab_TaxonmyDistributionInsert': results})

def Crab_taxasearch(request):
    SciName = Crab_TaxonmyDistributionInsert.objects.all()
    if request.method=="GET":
        chk = 0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = Crab_TaxonmyDistributionInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/crab_taxonomy_search.html', {'Crab_TaxonmyDistributionInsert': SciName, 'chk': chk}) 




















#views of Crab GeneralInformation


def Crab_generalinformationadd(request):
    scientificname = Crab_TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        if request.POST.get('ShrimpPrawnID') or \
                request.POST.get('ScientificName') or \
                request.POST.get('CommonName') or \
                request.POST.get('Environment') or \
                request.POST.get('PopulationStatus') or \
                request.POST.get('ConservationStatus') or \
                request.POST.get('DistributionInIndia') or \
                request.POST.get('DistributionOutsideOfIndia'):
            scientificname_obj = Crab_TaxonmyDistributionInsert.objects.get(ScientificName=request.POST.get('ScientificName'))
            
            saverecord = Crab_TaxonmyDistributionInsert()
            saverecord.Environment = request.POST.get('Environment')
            saverecord.CommonName = request.POST.get('CommonName')
            saverecord.ConservationStatus = request.POST.get('ConservationStatus')
            saverecord.PopulationStatus = request.POST.get('PopulationStatus')
            saverecord.DistributionInIndia = request.POST.get('DistributionInIndia')
            saverecord.DistributionOutsideOfIndia = request.POST.get('DistributionOutsideOfIndia')
            
            # Update the existing object instead of creating a new one
            scientificname_obj.Environment = saverecord.Environment
            scientificname_obj.CommonName = saverecord.CommonName
            scientificname_obj.ConservationStatus = saverecord.ConservationStatus
            scientificname_obj.PopulationStatus = saverecord.PopulationStatus
            scientificname_obj.DistributionInIndia = saverecord.DistributionInIndia
            scientificname_obj.DistributionOutsideOfIndia = saverecord.DistributionOutsideOfIndia
            
            scientificname_obj.save()
            
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/crab_generalinformation_add.html', {'Crab_TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/crab_generalinformation_add.html', {'Crab_TaxonmyDistributionInsert': scientificname})

    






def Crab_generalinformationview(request):
    result_display = Crab_TaxonmyDistributionInsert.objects.all()
    p = Paginator( Crab_TaxonmyDistributionInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/crab_generalinformation_view.html', {'vw': vw, ' Crab_TaxonmyDistributionInsert': result_display})




def Crab_geninfoedit(request,id):
    result_edit = Crab_TaxonmyDistributionInsert.objects.get(id=id)
    return render(request, 'shellfishapp/crab_generalinformation_edit.html', {'Crab_TaxonmyDistributionInsert': result_edit})



def Crab_generalinformationupdate(request,id):
    result_update =  Crab_TaxonmyDistributionInsert.objects.get(id=id)
    form = Crab_GeneralInformationForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/crab_generalinformation_edit.html', {' Crab_TaxonmyDistributionInsert': result_update})

def Crab_generalinformationdelete(request,id):
    result_delete =  Crab_TaxonmyDistributionInsert.objects.get(id=id)
    result_delete.delete()
    results =  Crab_TaxonmyDistributionInsert.objects.all()
    return render(request, 'shellfishapp/crab_generalinformation_view.html', {' Crab_TaxonmyDistributionInsert': results})

def Crab_generalinformationsearch(request):
    SciName = Crab_TaxonmyDistributionInsert.objects.all()
    if request.method=="GET":
        chk = 0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = Crab_TaxonmyDistributionInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/crab_generalinformation_search.html', {'Crab_TaxonmyDistributionInsert': SciName, 'chk': chk})













#All views of CrabtypeSpecimen
def Crab_speciadd(request):
    scientificname = Crab_TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        if request.POST.get('ScientificName') or \
                request.POST.get('CrabID') or \
                request.POST.get('TypeSpecimen') or \
                request.POST.get('Geo_Unit_Locality') or \
                request.POST.get('Descriptor') or \
                request.POST.get('SpecimenCatalogueNumber'):
            saverecord = Crab_TypeSpecimenInsert()
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.CrabID = request.POST.get('CrabID')
            saverecord.TypeSpecimen = request.POST.get('TypeSpecimen')
            
            saverecord.Geo_Unit_Locality = request.POST.get('Geo_Unit_Locality')
            saverecord.Descriptor = request.POST.get('Descriptor')
            saverecord.SpecimenCatalogueNumber = request.POST.get('SpecimenCatalogueNumber')
            
            saverecord.save()
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/crab_typespecimen_add.html', {'Crab_TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/crab_typespecimen_add.html', {'Crab_TaxonmyDistributionInsert': scientificname})
    
def Crab_speciview(request):
    result_display = Crab_TypeSpecimenInsert.objects.all()
    p = Paginator(Crab_TypeSpecimenInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/crab_typespecimen_view.html', {'Crab_TypeSpecimenInsert': result_display,'vw':vw})

def UA_Crab_speciview(request):
    result_display = Crab_TypeSpecimenInsert.objects.all()
    p = Paginator(Crab_TypeSpecimenInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/UA_crab_typespecimen_view.html', {'Crab_TypeSpecimenInsert': result_display,'vw':vw})

def Crab_speciedit(request,id):
    result_edit = Crab_TypeSpecimenInsert.objects.get(id=id)
    return render(request, 'shellfishapp/crab_typespecimen_edit.html', {'Crab_TypeSpecimenInsert': result_edit})

def Crab_speciupdate(request,id):
    result_update = Crab_TypeSpecimenInsert.objects.get(id=id)
    form = Crab_TypeSpecimenForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/crab_typespecimen_edit.html', {'Crab_TypeSpecimenInsert': result_update})

def Crab_specidelete(request,id):
    result_delete = Crab_TypeSpecimenInsert.objects.get(id=id)
    result_delete.delete()
    results = Crab_TypeSpecimenInsert.objects.all()
    return render(request, 'shellfishapp/crab_typespecimen_view.html', {'Crab_TypeSpecimenInsert': results})

def Crab_specisearch(request):
    SciName = Crab_TypeSpecimenInsert.objects.all()
    if request.method=="GET":
        chk=0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = Crab_TypeSpecimenInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/crab_typespecimen_search.html', {'Crab_TypeSpecimenInsert': SciName,'chk':chk})

























#All views of Crab_Synonyms
def Crab_synadd(request):
    Species = Crab_TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        if request.POST.get('CrabID') or \
                request.POST.get('Synonym') or \
                request.POST.get('Synonymy') or \
                request.POST.get('Status') or \
                request.POST.get('Valid') or \
                request.POST.get('Author'):
            saverecord = Crab_SynonymsInsert()
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.CrabID = request.POST.get('CrabID')
            saverecord.Synonym = request.POST.get('Synonym')
            saverecord.Synonymy = request.POST.get('Synonymy')
            saverecord.Status = request.POST.get('Status')
            saverecord.Valid = request.POST.get('Valid')
            saverecord.Author = request.POST.get('Author')
            saverecord.save()
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/crab_synonyms_add.html', {'Crab_TaxonmyDistributionInsert': Species})
    else:
        return render(request, 'shellfishapp/crab_synonyms_add.html', {'Crab_TaxonmyDistributionInsert': Species})
    
def Crab_synview(request):
    result_display = Crab_SynonymsInsert.objects.all()
    p = Paginator(Crab_SynonymsInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/crab_synonyms_view.html', {'Crab_SynonymsInsert': result_display,'vw':vw})

def UA_Crab_synview(request):
    result_display = Crab_SynonymsInsert.objects.all()
    p = Paginator(Crab_SynonymsInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/UA_crab_synonyms_view.html', {'Crab_SynonymsInsert': result_display,'vw':vw})
def Crab_synedit(request,id):
    result_edit = Crab_SynonymsInsert.objects.get(id=id)
    return render(request, 'shellfishapp/crab_synonyms_edit.html', {'Crab_SynonymsInsert': result_edit})

def Crab_synupdate(request,id):
    result_update = Crab_SynonymsInsert.objects.get(id=id)
    form = Crab_SynonymsForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/crab_synonyms_edit.html', {'Crab_SynonymsInsert': result_update})

def Crab_syndelete(request,id):
    result_delete = Crab_SynonymsInsert.objects.get(id=id)
    result_delete.delete()
    results = Crab_SynonymsInsert.objects.all()
    return render(request, 'shellfishapp/crab_synonyms_view.html', {'Crab_SynonymsInsert': results})

def Crab_synsearch(request):
    SciName = Crab_SynonymsInsert.objects.all()
    if request.method=="GET":
        chk=0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = Crab_SynonymsInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/crab_synonyms_search.html', {'Crab_SynonymsInsert': SciName,'chk':chk})








#All views of Crab_Morphological
def Crab_morphoadd(request):
    scientificname = Crab_TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        if request.POST.get('CrabID') or \
                request.POST.get('ShortDescription') or \
                request.POST.get('BodyNature') or \
                request.POST.get('Eyes') or \
                request.POST.get('CarapaceNature') or \
                request.POST.get('AntennalSegments') or \
                request.POST.get('ChilepedNature') or \
                request.POST.get('TelsonNature') or \
                request.POST.get('SexualDimorphism') or \
                request.POST.get('HabitatAndEcology') or \
                request.POST.get('Biology') or \
                request.POST.get('SpecificRemarks') or \
                request.POST.get('Colouration'):
            saverecord = Crab_MorphologicalInsert()
            saverecord.CrabID = request.POST.get('CrabID')
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.ShortDescription = request.POST.get('ShortDescription')
            saverecord.BodyNature = request.POST.get('BodyNature')
            saverecord.Eyes = request.POST.get('Eyes')
            saverecord.CarapaceNature = request.POST.get('CarapaceNature')
            saverecord.AntennalSegments = request.POST.get('AntennalSegments')
            saverecord.ChilepedNature = request.POST.get('ChilepedNature')
            saverecord.TelsonNature = request.POST.get('TelsonNature')
            saverecord.SexualDimorphism = request.POST.get('SexualDimorphism')
            saverecord.HabitatAndEcology = request.POST.get('HabitatAndEcology')
            saverecord.Biology = request.POST.get('Biology')
            saverecord.SpecificRemarks = request.POST.get('SpecificRemarks')
            saverecord.Colouration = request.POST.get('Colouration')
            saverecord.save()
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/crab_morphological_add.html', {'Crab_TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/crab_morphological_add.html', {'Crab_TaxonmyDistributionInsert': scientificname})
    
def Crab_morphoview(request):
    result_display = Crab_MorphologicalInsert.objects.all()
    p = Paginator(Crab_MorphologicalInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/crab_morphological_view.html', {'Crab_MorphologicalInsert': result_display,'vw':vw})

def UA_Crab_morphoview(request):
    result_display = Crab_MorphologicalInsert.objects.all()
    p = Paginator(Crab_MorphologicalInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/UA_crab_morphological_view.html', {'Crab_MorphologicalInsert': result_display,'vw':vw})

def Crab_morphoedit(request,id):
    result_edit = Crab_MorphologicalInsert.objects.get(id=id)
    return render(request, 'shellfishapp/crab_morphological_edit.html', {'Crab_MorphologicalInsert': result_edit})

def Crab_morphoupdate(request,id):
    result_update = Crab_MorphologicalInsert.objects.get(id=id)
    form = Crab_MorphoLogicalForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Update Successfully")
    return render(request, "shellfishapp/crab_morphological_edit.html", {"Crab_MorphologicalInsert": result_update})

def Crab_morphodelete(request,id):
    result_delete = Crab_MorphologicalInsert.objects.get(id=id)
    result_delete.delete()
    results = Crab_MorphologicalInsert.objects.all()
    return render(request, 'shellfishapp/crab_morphological_view.html', {'Crab_MorphologicalInsert': results})

def Crab_morphosearch(request):
    SciName = Crab_MorphologicalInsert.objects.all()
    if request.method=="GET":
        chk=0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = Crab_MorphologicalInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/crab_morphological_search.html', {'Crab_MorphologicalInsert': SciName,'chk':chk})









#All view of Crab_Occurence
def Crab_occadd(request):
    scientificname = Crab_TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        if request.POST.get('CrabID') or \
                request.POST.get('ScientificName') or \
                request.POST.get('Locality') or \
                request.POST.get('State') or \
                request.POST.get('Latitude') or \
                request.POST.get('Longitude') or \
                request.POST.get('Source'):
                
            saverecord = Crab_OccurrenceInsert()
            saverecord.CrabID = request.POST.get('CrabID')
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.Locality = request.POST.get('Locality')
            saverecord.State = request.POST.get('State')
            saverecord.Latitude = request.POST.get('Latitude')
            saverecord.Longitude = request.POST.get('Longitude')
            saverecord.Source = request.POST.get('Source')
            saverecord.save()
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/crab_occurrence_add.html', {'Crab_TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/crab_occurrence_add.html', {'Crab_TaxonmyDistributionInsert': scientificname})

def Crab_occview(request):
    result_display = Crab_OccurrenceInsert.objects.all()
    p = Paginator(Crab_OccurrenceInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/crab_occurrence_view.html', {'Crab_OccurrenceInsert': result_display,'vw':vw})

def UA_Crab_occview(request):
    result_display = Crab_OccurrenceInsert.objects.all()
    p = Paginator(Crab_OccurrenceInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/UA_crab_occurrence_view.html', {'Crab_OccurrenceInsert': result_display,'vw':vw})

def Crab_occedit(request,id):
    result_edit = Crab_OccurrenceInsert.objects.get(id=id)
    return render(request, 'shellfishapp/crab_occurrence_edit.html', {'Crab_OccurrenceInsert': result_edit})

def Crab_occupdate(request,id):
    result_update = Crab_OccurrenceInsert.objects.get(id=id)
    form = Crab_OccurrenceForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/crab_occurrence_edit.html', {'Crab_OccurrenceInsert': result_update})

def Crab_occdelete(request,id):
    result_delete = Crab_OccurrenceInsert.objects.get(id=id)
    result_delete.delete()
    results = OccurrenceInsert.objects.all()
    return render(request, 'shellfishapp/Crab_occurrence_view.html', {'Crab_OccurrenceInsert': results})

def Crab_occsearch(request):
    SciName = Crab_OccurrenceInsert.objects.all()
    if request.method=="GET":
        chk=0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = Crab_OccurrenceInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/crab_occurrence_search.html', {'Crab_OccurrenceInsert': SciName,'chk':chk})


























#All views of Crab_image
def Crab_imgadd(request):
    scientificname= Crab_TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        form = Crab_ImageForms(request.POST, request.FILES)
        if form.is_valid():
            saverecord = Crab_ImageInsert()
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.CrabID = request.POST.get('CrabID')
            saverecord.Image1 = request.POST.get('Image1')
            saverecord.Image2 = request.POST.get('Image2')
            saverecord.Image3 = request.POST.get('Image3')
            form.save()
            messages.success(request, 'Images Added Successfully...!')
            return render(request, 'shellfishapp/crab_image_add.html', {'Crab_TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/crab_image_add.html', {'Crab_TaxonmyDistributionInsert': scientificname})


def Crab_imgview(request):
    #result_display = Crab_ImageInsert.objects.filter
    p = Paginator(Crab_ImageInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page) 
    #image = Crab_ImageInsert.objects.all()   {'image': image},    'Crab_ImageInsert': result_display,
    return render(request, 'shellfishapp/crab_image_view.html', {'vw':vw})

def Crab_imgedit(request,id):
    result_edit = Crab_ImageInsert.objects.get(id=id)
    return render(request, 'shellfishapp/crab_image_edit.html', {'Crab_ImageInsert': result_edit})



def Crab_imgdelete(request,id):
    result_delete = Crab_ImageInsert.objects.get(id=id)
    result_delete.delete()
    results = Crab_ImageInsert.objects.all()
    return render(request, 'shellfishapp/crab_image_view.html', {'Crab_ImageInsert': results})



def Crab_imgupdate(request,id):
    result_update = Crab_ImageInsert.objects.get(id=id)
    if request.method == 'POST':
        form = Crab_ImageForms(request.POST,request.FILES, instance=result_update)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/crab_image_edit.html', {'Crab_ImageInsert': result_update})











#lobster_taxonmydistribution ADD, VIEW, EDIT, UPDATE, DELETE, SEARCH

def lobster_taxoadd(request):
    if request.method == "POST":
        if request.POST.get('Kingdom') or \
                request.POST.get('Phylum') or \
                request.POST.get('SubPhylum') or \
                request.POST.get('Class') or \
                request.POST.get('SubClass') or \
                request.POST.get('SuperOrder') or \
                request.POST.get('Order') or \
                request.POST.get('SubOrder') or \
                request.POST.get('InfraOrder') or \
                request.POST.get('SuperFamily') or \
                request.POST.get('Family') or \
                request.POST.get('SubFamily') or \
                request.POST.get('Genus') or \
                request.POST.get('ScientificName') or \
                request.POST.get('TaxonomicRank') or \
                request.POST.get('Subspecies') or \
                request.POST.get('AcceptedValidName') or \
                request.POST.get('CommonName') or \
                request.POST.get('Author') or \
                request.POST.get('MainReference') or \
                request.POST.get('Environment') or \
                request.POST.get('ConservationStatus') or \
                request.POST.get('DistributionInIndia') or \
                request.POST.get('DistributionOutsideOfIndia') or \
                request.POST.get('PopulationStatus') or \
                request.POST.get('OriginType') or \
                request.POST.get('DepthRange'):
            saverecord = Lobster_TaxonmyDistributionInsert()
            saverecord.Kingdom = request.POST.get('Kingdom')
            saverecord.Phylum = request.POST.get('Phylum')
            saverecord.SubPhylum = request.POST.get('SubPhylum')
            saverecord.Class = request.POST.get('Class')
            saverecord.SubClass = request.POST.get('SubClass')
            saverecord.SuperOrder = request.POST.get('SuperOrder')
            saverecord.Order = request.POST.get('Order')
            saverecord.SubOrder = request.POST.get('SubOrder')
            saverecord.InfraOrder = request.POST.get('InfraOrder')
            saverecord.SuperFamily = request.POST.get('SuperFamily')
            saverecord.Family = request.POST.get('Family')
            saverecord.SubFamily = request.POST.get('SubFamily')
            saverecord.Genus = request.POST.get('Genus')
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.TaxonomicRank = request.POST.get('TaxonomicRank')
            saverecord.Subspecies = request.POST.get('Subspecies')
            saverecord.AcceptedValidName = request.POST.get('AcceptedValidName')
            saverecord.CommonName = request.POST.get('CommonName')
            saverecord.Author = request.POST.get('Author')
            saverecord.MainReference = request.POST.get('MainReference')
            saverecord.Environment = request.POST.get('Environment')
            saverecord.ConservationStatus = request.POST.get('ConservationStatus')
            saverecord.DistributionInIndia = request.POST.get('DistributionInIndia')
            saverecord.DistributionOutsideOfIndia = request.POST.get('DistributionOutsideOfIndia')
            saverecord.PopulationStatus = request.POST.get('PopulationStatus')
            saverecord.OriginType = request.POST.get('OriginType')
            saverecord.DepthRange = request.POST.get('DepthRange')
            saverecord.save()
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/lobster_taxonomy_add.html')
    else:
        return render(request, 'shellfishapp/lobster_taxonomy_add.html')

def lobster_taxoview(request):
    result_display = Lobster_TaxonmyDistributionInsert.objects.all()
# Set up Pagination
    p = Paginator(Lobster_TaxonmyDistributionInsert.objects.all(), 8)
    page = request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/lobster_taxonomy_view.html', {'Lobster_TaxonmyDistributionInsert': result_display,'vw': vw})

def UA_lobster_taxoview(request):
    result_display = Lobster_TaxonmyDistributionInsert.objects.all()
# Set up Pagination
    p = Paginator(Lobster_TaxonmyDistributionInsert.objects.all(), 8)
    page = request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/UA_lobster_taxonomy_view.html', {'Lobster_TaxonmyDistributionInsert': result_display,'vw': vw}) 

def lobster_taxoedit(request,id):
    result_edit = Lobster_TaxonmyDistributionInsert.objects.get(LobsterID=id)
    return render(request, 'shellfishapp/lobster_taxonomy_edit.html', {'Lobster_TaxonmyDistributionInsert': result_edit})

def lobster_taxoupdate(request,id):
    result_update = Lobster_TaxonmyDistributionInsert.objects.get(LobsterID=id)
    form = Lobster_TaxonmyDistributionForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/lobster_taxonomy_edit.html', {'Lobster_TaxonmyDistributionInsert': result_update})

def lobster_taxodelete(request,id):
    result_delete = Lobster_TaxonmyDistributionInsert.objects.get(LobsterID=id)
    result_delete.delete()
    results = Lobster_TaxonmyDistributionInsert.objects.all()
    return render(request, 'shellfishapp/lobster_taxonomy_view.html', {'Lobster_TaxonmyDistributionInsert': results})

def lobster_taxasearch(request):
    #chk = 0
    SciName = Lobster_TaxonmyDistributionInsert.objects.all()
    if request.method=="GET":
        chk = 0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = Lobster_TaxonmyDistributionInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/lobster_taxonomy_search.html', {'Lobster_TaxonmyDistributionInsert': SciName,'chk': chk})






#views of Lobster GeneralInformation


def Lobster_generalinformationadd(request):
    scientificname = Lobster_TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        if request.POST.get('LobsterID') or \
                request.POST.get('ScientificName') or \
                request.POST.get('CommonName') or \
                request.POST.get('Environment') or \
                request.POST.get('PopulationStatus') or \
                request.POST.get('ConservationStatus') or \
                request.POST.get('DistributionInIndia') or \
                request.POST.get('DistributionOutsideOfIndia'):
            scientificname_obj = Lobster_TaxonmyDistributionInsert.objects.get(ScientificName=request.POST.get('ScientificName'))
            
            saverecord = Lobster_TaxonmyDistributionInsert()
            saverecord.Environment = request.POST.get('Environment')
            saverecord.CommonName = request.POST.get('CommonName')
            saverecord.ConservationStatus = request.POST.get('ConservationStatus')
            saverecord.PopulationStatus = request.POST.get('PopulationStatus')
            saverecord.DistributionInIndia = request.POST.get('DistributionInIndia')
            saverecord.DistributionOutsideOfIndia = request.POST.get('DistributionOutsideOfIndia')
            
            # Update the existing object instead of creating a new one
            scientificname_obj.Environment = saverecord.Environment
            scientificname_obj.CommonName = saverecord.CommonName
            scientificname_obj.ConservationStatus = saverecord.ConservationStatus
            scientificname_obj.PopulationStatus = saverecord.PopulationStatus
            scientificname_obj.DistributionInIndia = saverecord.DistributionInIndia
            scientificname_obj.DistributionOutsideOfIndia = saverecord.DistributionOutsideOfIndia
            
            scientificname_obj.save()
            
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/lobster_generalinformation_add.html', {'Lobster_TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/lobster_generalinformation_add.html', {'Lobster_TaxonmyDistributionInsert': scientificname})

    






def Lobster_generalinformationview(request):
    result_display = Lobster_TaxonmyDistributionInsert.objects.all()
    p = Paginator( Lobster_TaxonmyDistributionInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/lobster_generalinformation_view.html', {'vw': vw, ' Lobster_TaxonmyDistributionInsert': result_display})




def Lobster_geninfoedit(request,id):
    result_edit = Lobster_TaxonmyDistributionInsert.objects.get(LobsterID=id)
    return render(request, 'shellfishapp/lobster_generalinformation_edit.html', {'Lobster_TaxonmyDistributionInsert': result_edit})



def Lobster_generalinformationupdate(request,id):
    result_update =  Lobster_TaxonmyDistributionInsert.objects.get(LobsterID=id)
    form = Lobster_GeneralInformationForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/lobster_generalinformation_edit.html', {' Loobster_TaxonmyDistributionInsert': result_update})

def Lobster_generalinformationdelete(request,id):
    result_delete =  Lobster_TaxonmyDistributionInsert.objects.get(LobsterID=id)
    result_delete.delete()
    results =  Lobster_TaxonmyDistributionInsert.objects.all()
    return render(request, 'shellfishapp/lobster_generalinformation_view.html', {' Lobster_TaxonmyDistributionInsert': results})

def Lobster_generalinformationsearch(request):
    SciName = Lobster_TaxonmyDistributionInsert.objects.all()
    if request.method=="GET":
        chk = 0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = Lobster_TaxonmyDistributionInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/lobster_generalinformation_search.html', {'Lobster_TaxonmyDistributionInsert': SciName, 'chk': chk})






















#lobster_synonyms ADD, VIEW, EDIT, UPDATE, DELETE, SEARCH

def lobster_synadd(request):
    scientificname = Lobster_TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        if request.POST.get('LobsterID') or \
                request.POST.get('Synonym') or \
                request.POST.get('Synonymy') or \
                request.POST.get('Status') or \
                request.POST.get('Valid') or \
                request.POST.get('Author'):
            saverecord = Lobster_SynonymsInsert()
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.LobsterID = request.POST.get('LobsterID')
            saverecord.Synonym = request.POST.get('Synonym')
            saverecord.Synonymy = request.POST.get('Synonymy')
            saverecord.Status = request.POST.get('Status')
            saverecord.Valid = request.POST.get('Valid')
            saverecord.Author = request.POST.get('Author')
            saverecord.save()
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/lobster_synonyms_add.html', {'Lobster_TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/lobster_synonyms_add.html', {'Lobster_TaxonmyDistributionInsert': scientificname})

def lobster_synview(request):
    result_display = Lobster_SynonymsInsert.objects.all()
    # Set up Pagination
    p = Paginator(Lobster_SynonymsInsert.objects.all(), 8)
    page = request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/lobster_synonyms_view.html', {'Lobster_SynonymsInsert': result_display,'vw': vw})

def UA_lobster_synview(request):
    result_display = Lobster_SynonymsInsert.objects.all()
    # Set up Pagination
    p = Paginator(Lobster_SynonymsInsert.objects.all(), 8)
    page = request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/UA_lobster_synonyms_view.html', {'Lobster_SynonymsInsert': result_display,'vw': vw})

def lobster_synedit(request,id):
    result_edit = Lobster_SynonymsInsert.objects.get(id=id)
    return render(request, 'shellfishapp/lobster_synonyms_edit.html', {'Lobster_SynonymsInsert': result_edit})

def lobster_synupdate(request,id):
    result_update = Lobster_SynonymsInsert.objects.get(id=id)
    form = Lobster_SynonymsForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/lobster_synonyms_edit.html', {'Lobster_SynonymsInsert': result_update})

def lobster_syndelete(request,id):
    result_delete = Lobster_SynonymsInsert.objects.get(id=id)
    result_delete.delete()
    results = Lobster_SynonymsInsert.objects.all()
    return render(request, 'shellfishapp/lobster_synonyms_view.html', {'Lobster_SynonymsInsert': results})

def lobster_synsearch(request):
    SciName = Lobster_SynonymsInsert.objects.all()
    if request.method=="GET":
        chk = 0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = Lobster_SynonymsInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/lobster_synonyms_search.html', {'Lobster_SynonymsInsert': SciName, 'chk': chk})






#lobster_morphological ADD, VIEW, EDIT, UPDATE, DELETE, SEARCH

def lobster_morphoadd(request):
    scientificname = Lobster_TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        if request.POST.get('LobsterID') or \
                request.POST.get('ScientificName') or \
                request.POST.get('ShortDescription') or \
                request.POST.get('BodyNature') or \
                request.POST.get('Eyes') or \
                request.POST.get('CarapaceNature') or \
                request.POST.get('AntennuleSegments') or \
                request.POST.get('AntennalPlate') or \
                request.POST.get('AbdominalSegments') or \
                request.POST.get('NatureofLegs') or \
                request.POST.get('TelsonNature') or \
                request.POST.get('SexualDimorphism') or \
                request.POST.get('SpecificRemarks') or \
                request.POST.get('Colouration'):
            saverecord = Lobster_MorphologicalInsert()
            saverecord.LobsterID = request.POST.get('LobsterID')
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.ShortDescription = request.POST.get('ShortDescription')
            saverecord.BodyNature = request.POST.get('BodyNature')
            saverecord.Eyes = request.POST.get('Eyes')
            saverecord.CarapaceNature = request.POST.get('CarapaceNature')
            saverecord.AntennuleSegments = request.POST.get('AntennuleSegments')
            saverecord.AntennalPlate = request.POST.get('AntennalPlate')
            saverecord.AbdominalSegments = request.POST.get('AbdominalSegments')
            saverecord.NatureofLegs = request.POST.get('NatureofLegs')
            saverecord.TelsonNature = request.POST.get('TelsonNature')
            saverecord.SexualDimorphism = request.POST.get('SexualDimorphism')
            saverecord.SpecificRemarks = request.POST.get('SpecificRemarks')
            saverecord.Colouration = request.POST.get('Colouration')
            saverecord.save()
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/lobster_morphological_add.html', {'Lobster_TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/lobster_morphological_add.html', {'Lobster_TaxonmyDistributionInsert': scientificname})

def lobster_morphoview(request):
    result_display = Lobster_MorphologicalInsert.objects.all()
    # Set up Pagination
    p = Paginator(Lobster_MorphologicalInsert.objects.all(), 8)
    page = request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/lobster_morphological_view.html', {'Lobster_MorphologicalInsert': result_display,'vw': vw})

def UA_lobster_morphoview(request):
    result_display = Lobster_MorphologicalInsert.objects.all()
    # Set up Pagination
    p = Paginator(Lobster_MorphologicalInsert.objects.all(), 8)
    page = request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/UA_lobster_morphological_view.html', {'Lobster_MorphologicalInsert': result_display,'vw': vw})

def lobster_morphoedit(request,id):
    result_edit = Lobster_MorphologicalInsert.objects.get(id=id)
    return render(request, 'shellfishapp/lobster_morphological_edit.html', {'Lobster_MorphologicalInsert': result_edit})

def lobster_morphoupdate(request,id):
    result_update = Lobster_MorphologicalInsert.objects.get(id=id)
    form = Lobster_MorphologicalForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Update Successfully")
    return render(request, "shellfishapp/lobster_morphological_edit.html", {"Lobster_MorphologicalInsert": result_update})

def lobster_morphodelete(request,id):
    result_delete = Lobster_MorphologicalInsert.objects.get(id=id)
    result_delete.delete()
    results = Lobster_MorphologicalInsert.objects.all()
    return render(request, 'shellfishapp/lobster_morphological_view.html', {'Lobster_MorphologicalInsert': results})

def lobster_morphosearch(request):
    SciName = Lobster_MorphologicalInsert.objects.all()
    if request.method=="GET":
        chk = 0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = Lobster_MorphologicalInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/lobster_morphological_search.html', {'Lobster_MorphologicalInsert': SciName, 'chk': chk})








#lobster_typespecimen ADD, VIEW, EDIT, UPDATE, DELETE, SEARCH

def lobster_speciadd(request):
    scientificname = Lobster_TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        if request.POST.get('LobsterID') or \
                request.POST.get('ScientificName') or \
                request.POST.get('TypeSpecimen') or \
                request.POST.get('Geo_Unit_Locality') or \
                request.POST.get('Descriptor') or \
                request.POST.get('SpecimenCatalogueNumber') or \
                request.POST.get('Author'):
            saverecord = Lobster_TypeSpecimenInsert()
            saverecord.LobsterID = request.POST.get('LobsterID')
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.TypeSpecimen = request.POST.get('TypeSpecimen')
            saverecord.Geo_Unit_Locality = request.POST.get('Geo_Unit_Locality')
            saverecord.Descriptor = request.POST.get('Descriptor')
            saverecord.SpecimenCatalogueNumber = request.POST.get('SpecimenCatalogueNumber')
            saverecord.Author = request.POST.get('Author')
            saverecord.save()
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/lobster_typespecimen_add.html', {'Lobster_TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/lobster_typespecimen_add.html', {'Lobster_TaxonmyDistributionInsert': scientificname})

def lobster_speciview(request):
    result_display = Lobster_TypeSpecimenInsert.objects.all()
    # Set up Pagination
    p = Paginator(Lobster_TypeSpecimenInsert.objects.all(), 8)
    page = request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/lobster_typespecimen_view.html', {'Lobster_TypeSpecimenInsert': result_display,'vw': vw})

def UA_lobster_speciview(request):
    result_display = Lobster_TypeSpecimenInsert.objects.all()
    # Set up Pagination
    p = Paginator(Lobster_TypeSpecimenInsert.objects.all(), 8)
    page = request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/UA_lobster_typespecimen_view.html', {'Lobster_TypeSpecimenInsert': result_display,'vw': vw})

def lobster_speciedit(request,id):
    result_edit = Lobster_TypeSpecimenInsert.objects.get(id=id)
    return render(request, 'shellfishapp/lobster_typespecimen_edit.html', {'Lobster_TypeSpecimenInsert': result_edit})

def lobster_speciupdate(request,id):
    result_update = Lobster_TypeSpecimenInsert.objects.get(id=id)
    form = Lobster_TypeSpecimenForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/lobster_typespecimen_edit.html', {'Lobster_TypeSpecimenInsert': result_update})

def lobster_specidelete(request,id):
    result_delete = Lobster_TypeSpecimenInsert.objects.get(id=id)
    result_delete.delete()
    results = Lobster_TypeSpecimenInsert.objects.all()
    return render(request, 'shellfishapp/lobster_typespecimen_view.html', {'Lobster_TypeSpecimenInsert': results})

def lobster_specisearch(request):
    SciName = Lobster_TypeSpecimenInsert.objects.all()
    if request.method=="GET":
        chk = 0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = Lobster_TypeSpecimenInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/lobster_typespecimen_search.html', {'Lobster_TypeSpecimenInsert': SciName, 'chk': chk})





#lobster_occurrence ADD, VIEW, EDIT, UPDATE, DELETE, SEARCH

def lobster_occadd(request):
    scientificname = Lobster_TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        if request.POST.get('LobsterID') or \
                request.POST.get('ScientificName') or \
                request.POST.get('Locality') or \
                request.POST.get('State') or \
                request.POST.get('Latitude') or \
                request.POST.get('Longitude') or \
                request.POST.get('Reference'):
            saverecord = Lobster_OccurrenceInsert()
            saverecord.LobsterID = request.POST.get('LobsterID')
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.Locality = request.POST.get('Locality')
            saverecord.State = request.POST.get('State')
            saverecord.Latitude = request.POST.get('Latitude')
            saverecord.Longitude = request.POST.get('Longitude')
            saverecord.Reference = request.POST.get('Reference')
            saverecord.save()
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/lobster_occurrence_add.html', {'Lobster_TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/lobster_occurrence_add.html', {'Lobster_TaxonmyDistributionInsert': scientificname})

def lobster_occview(request):
    result_display = Lobster_OccurrenceInsert.objects.all()
    # Set up Pagination
    p = Paginator(Lobster_OccurrenceInsert.objects.all(), 8)
    page = request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/lobster_occurrence_view.html', {'Lobster_OccurrenceInsert': result_display, 'vw': vw})

def UA_lobster_occview(request):
    result_display = Lobster_OccurrenceInsert.objects.all()
    # Set up Pagination
    p = Paginator(Lobster_OccurrenceInsert.objects.all(), 8)
    page = request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/UA_lobster_occurrence_view.html', {'Lobster_OccurrenceInsert': result_display, 'vw': vw})

def lobster_occedit(request,id):
    result_edit = Lobster_OccurrenceInsert.objects.get(id=id)
    return render(request, 'shellfishapp/lobster_occurrence_edit.html', {'Lobster_OccurrenceInsert': result_edit})

def lobster_occupdate(request,id):
    result_update = Lobster_OccurrenceInsert.objects.get(id=id)
    form = Lobster_OccurrenceForms(request.POST, instance=result_update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/lobster_occurrence_edit.html', {'Lobster_OccurrenceInsert': result_update})

def lobster_occdelete(request,id):
    result_delete = Lobster_OccurrenceInsert.objects.get(id=id)
    result_delete.delete()
    results = Lobster_OccurrenceInsert.objects.all()
    return render(request, 'shellfishapp/lobster_occurrence_view.html', {'Lobster_OccurrenceInsert': results})

def lobster_occsearch(request):
    SciName = Lobster_OccurrenceInsert.objects.all()
    if request.method=="GET":
        chk = 0
        sn = request.GET.get('ScientificName')
        if sn and len(sn) >= 3:  # Set a minimum length for the search query (e.g., 3 characters)
            SciName = Lobster_OccurrenceInsert.objects.filter(ScientificName__iexact=sn)  # Use iexact for case-insensitive exact match
            chk = 1

        if not SciName.exists():  # Check if no results were found
            chk = -1  # Set a flag to indicate no results were found
    return render(request, 'shellfishapp/lobster_occurrence_search.html', {'Lobster_OccurrenceInsert': SciName, 'chk': chk})






def lobster_imgadd(request):
    scientificname= Lobster_TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        form = Lobster_ImageForms(request.POST, request.FILES)
        if form.is_valid():
            saverecord = Lobster_ImageInsert()
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.LobsterID = request.POST.get('LobsterID')
            saverecord.Image1 = request.POST.get('Image1')
            saverecord.Image2 = request.POST.get('Image2')
            saverecord.Image3 = request.POST.get('Image3')
            form.save()
            messages.success(request, 'Images Added Successfully...!')
            return render(request, 'shellfishapp/lobster_image_add.html', {'Lobster_TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/lobster_image_add.html', {'Lobster_TaxonmyDistributionInsert': scientificname})


def lobster_imgview(request):
    #result_display = Crab_ImageInsert.objects.filter
    p = Paginator(Lobster_ImageInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page) 
    #image = Crab_ImageInsert.objects.all()   {'image': image},    'Crab_ImageInsert': result_display,
    return render(request, 'shellfishapp/lobster_image_view.html', {'vw':vw})

def lobster_imgedit(request,id):
    result_edit = Lobster_ImageInsert.objects.get(id=id)
    return render(request, 'shellfishapp/lobster_image_edit.html', {'Lobster_ImageInsert': result_edit})



def lobster_imgdelete(request,id):
    result_delete = Lobster_ImageInsert.objects.get(id=id)
    result_delete.delete()
    results = Lobster_ImageInsert.objects.all()
    return render(request, 'shellfishapp/lobster_image_view.html', {'Lobster_ImageInsert': results})



def lobster_imgupdate(request,id):
    result_update = Lobster_ImageInsert.objects.get(id=id)
    if request.method == 'POST':
        form = Lobster_ImageForms(request.POST,request.FILES, instance=result_update)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Update Successfully')
    return render(request, 'shellfishapp/lobster_image_edit.html', {'Lobster_ImageInsert': result_update})





#Views of ShrimpPrawn Type Locality


def typelocalityadd(request):
    scientificname = TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
        if request.POST.get('GBIFID') or \
                request.POST.get('Family') or \
                request.POST.get('Genus') or \
                request.POST.get('ShrimpPrawnID') or \
                request.POST.get('ScientificName') or \
                request.POST.get('Author') or \
                request.POST.get('TaxonRank') or \
                request.POST.get('CountryCode') or \
                request.POST.get('Locality') or \
                request.POST.get('StateProvince') or \
                request.POST.get('OccurrenceStatus') or \
                request.POST.get('IndividualCount') or \
                request.POST.get('Latitude') or \
                request.POST.get('Longitude') or \
                request.POST.get('RecordBasis') or \
                request.POST.get('InstitutionCode') or \
                request.POST.get('CatalogueNumber') or \
                request.POST.get('IdentifiedBy') or \
                request.POST.get('License') or \
                request.POST.get('TypeStatus') or \
                request.POST.get('EstablishmentMeans') or \
                request.POST.get('TypeSpecimenStatus') or \
                request.POST.get('TypeSpecimenRepository') or \
                request.POST.get('TypeLocality') or \
                request.POST.get('Author') or \
                request.POST.get('TypeSpecimenCatalogueNumber') or \
                request.POST.get('URL') or \
                request.POST.get('Source'):
            saverecord = TypeLocalityInsert()
            saverecord.GBIFID = request.POST.get('GBIFID')
            saverecord.Family = request.POST.get('Family')
            saverecord.Genus = request.POST.get('Genus')
            saverecord.ShrimpPrawnID = request.POST.get('ShrimpPrawnID')
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.Author = request.POST.get('Author')
            saverecord.TaxonRank = request.POST.get('TaxonRank')
            saverecord.CountryCode = request.POST.get('CountryCode')
            saverecord.Locality = request.POST.get('Locality')
            saverecord.StateProvince = request.POST.get('StateProvince')
            saverecord.OccurrenceStatus = request.POST.get('OccurrenceStatus')
            saverecord.IndividualCount = request.POST.get('IndividualCount')
            saverecord.Latitude = request.POST.get('Latitude')
            saverecord.Longitude = request.POST.get('Longitude')
            saverecord.RecordBasis = request.POST.get('RecordBasis')
            saverecord.InstitutionCode = request.POST.get('InstitutionCode')
            saverecord.CatalogueNumber = request.POST.get('CatalogueNumber')
            saverecord.IdentifiedBy = request.POST.get('IdentifiedBy')
            saverecord.License = request.POST.get('License')
            saverecord.TypeStatus = request.POST.get('TypeStatus')
            saverecord.EstablishmentMeans = request.POST.get('EstablishmentMeans')
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.ShrimpPrawnID = request.POST.get('ShrimpPrawnID')
            saverecord.TypeSpecimenStatus = request.POST.get('TypeSpecimenStatus')
            saverecord.TypeSpecimenRepository = request.POST.get('TypeSpecimenRepository')
            saverecord.TypeLocality = request.POST.get('TypeLocality')
            saverecord.Author = request.POST.get('Author')
            saverecord.TypeSpecimenCatalogueNumber = request.POST.get('TypeSpecimenCatalogueNumber')
            saverecord.URL = request.POST.get('URL')
            saverecord.Source = request.POST.get('Source')
            saverecord.save()
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/typelocality_add.html', {'TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/add_location.html', {'TaxonmyDistributionInsert': scientificname})
    



def add_location(request):
    scientificname = TaxonmyDistributionInsert.objects.all()
    if request.method == 'POST':

        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LocationForm()

    return render(request, 'shellfishapp/add_location.html', {'form': form,'TaxonmyDistributionInsert': scientificname})




def view_location(request):
    result_display = Location.objects.all()
    # Set up Pagination
    p = Paginator(Location.objects.all(), 5)
    page = request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/view_location.html', {'Location': result_display,'vw': vw})



def occadd(request):
    scientificname = TaxonmyDistributionInsert.objects.all()
    if request.method == "POST":
         form = LocationForm(request.POST)
         if form.is_valid():
            form.save()
         if request.POST.get('GBIFID') or \
                request.POST.get('Family') or \
                request.POST.get('Genus') or \
                request.POST.get('ShrimpPrawnID') or \
                request.POST.get('ScientificName') or \
                request.POST.get('Author') or \
                request.POST.get('TaxonRank') or \
                request.POST.get('CountryCode') or \
                request.POST.get('Locality') or \
                request.POST.get('StateProvince') or \
                request.POST.get('OccurrenceStatus') or \
                request.POST.get('IndividualCount') or \
                request.POST.get('Latitude') or \
                request.POST.get('Longitude') or \
                request.POST.get('RecordBasis') or \
                request.POST.get('InstitutionCode') or \
                request.POST.get('CatalogueNumber') or \
                request.POST.get('IdentifiedBy') or \
                request.POST.get('License') or \
                request.POST.get('TypeStatus') or \
                request.POST.get('EstablishmentMeans'):
            saverecord = OccurrenceInsert()
            saverecord.GBIFID = request.POST.get('GBIFID')
            saverecord.Family = request.POST.get('Family')
            saverecord.Genus = request.POST.get('Genus')
            saverecord.ShrimpPrawnID = request.POST.get('ShrimpPrawnID')
            saverecord.ScientificName = request.POST.get('ScientificName')
            saverecord.Author = request.POST.get('Author')
            saverecord.TaxonRank = request.POST.get('TaxonRank')
            saverecord.CountryCode = request.POST.get('CountryCode')
            saverecord.Locality = request.POST.get('Locality')
            saverecord.StateProvince = request.POST.get('StateProvince')
            saverecord.OccurrenceStatus = request.POST.get('OccurrenceStatus')
            saverecord.IndividualCount = request.POST.get('IndividualCount')
            saverecord.Latitude = request.POST.get('Latitude')
            saverecord.Longitude = request.POST.get('Longitude')
            saverecord.RecordBasis = request.POST.get('RecordBasis')
            saverecord.InstitutionCode = request.POST.get('InstitutionCode')
            saverecord.CatalogueNumber = request.POST.get('CatalogueNumber')
            saverecord.IdentifiedBy = request.POST.get('IdentifiedBy')
            saverecord.License = request.POST.get('License')
            saverecord.TypeStatus = request.POST.get('TypeStatus')
            saverecord.EstablishmentMeans = request.POST.get('EstablishmentMeans')
            saverecord.save()
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/occurrence_add.html', {'TaxonmyDistributionInsert': scientificname})
    else:
        form = LocationForm()
        return render(request, 'shellfishapp/occurrence_add.html', {'TaxonmyDistributionInsert': scientificname})




def OccLatLongadd(request):
    scientificname = TaxonmyDistributionInsert.objects.all()
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to success page
    
                
            scientificname_obj = OccurrenceInsert.objects.get(ScientificName=request.POST.get('ScientificName'))
            
            saverecord = OccurrenceInsert()
            saverecord.Latitude = request.POST.get('Latitude')
            saverecord.Longitude = request.POST.get('Longitude')
            
            # Update the existing object instead of creating a new one
            scientificname_obj.Latitude = saverecord.Latitude
            scientificname_obj.Longitude = saverecord.Longitude
            
            scientificname_obj.save()
            
            messages.success(request, 'Data Added Successfully...!')
            return render(request, 'shellfishapp/generalinformation_add.html', {'TaxonmyDistributionInsert': scientificname})
    else:
        return render(request, 'shellfishapp/generalinformation_add.html', {'TaxonmyDistributionInsert': scientificname})





#def image_info(request):
 #   result_display = OccurrenceInsert.objects.filter(ScientificName='Acetes indicus')
    
    
  #  return render(request, 'shellfishapp/image_info.html', {'Lobster_OccurrenceInsert': result_display})




def image_info(request):
    data_item = TaxonmyDistributionInsert.objects.get(id=1)# Retrieve a specific data item by filtering with an appropriate condition
    
    return render(request, 'shellfishapp/image_info.html', {'data_item': data_item})
    
    


def image_infoview(request):
    p = Paginator(ImageInsert.objects.all(), 5)
    
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/image_view.html', {'vw':vw})
    
    
    
    
    
    


def all_imgview(request):
    p = Paginator(ImageInsert.objects.all(), 5)
    page= request.GET.get('page')
    vw = p.get_page(page)
    return render(request, 'shellfishapp/all_image_view.html', {'vw':vw})