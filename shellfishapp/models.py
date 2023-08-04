from django.db import models
import datetime
import os
import requests

class TaxonmyDistributionInsert(models.Model):
    CrusteceanSubgroup = models.CharField(max_length=500, blank=True)
    CrusteceanSubgroupType = models.CharField(max_length=500, blank=True)
    Kingdom = models.CharField(max_length=500, blank=True)
    Phylum = models.CharField(max_length=500, blank=True)
    SubPhylum = models.CharField(max_length=500, blank=True)
    Class = models.CharField(max_length=500, blank=True)
    SubClass = models.CharField(max_length=500, blank=True)
    SuperOrder = models.CharField(max_length=500, blank=True)
    Order = models.CharField(max_length=500, blank=True)
    SubOrder = models.CharField(max_length=500, blank=True)
    InfraOrder = models.CharField(max_length=500, blank=True)
    SuperFamily = models.CharField(max_length=500, blank=True)
    Family = models.CharField(max_length=500, blank=True)
    SubFamily = models.CharField(max_length=500, blank=True)
    Genus = models.CharField(max_length=500, blank=True)
    ScientificName = models.CharField(max_length=500, blank=True)
    TaxonomicRank = models.CharField(max_length=500, blank=True)
    Subspecies = models.CharField(max_length=500, blank=True)
    Environment = models.CharField(max_length=500, blank=True)
    CommonName = models.CharField(max_length=500, blank=True)
    ConservationStatus = models.CharField(max_length=500, blank=True)
    PopulationStatus = models.CharField(max_length=500, blank=True)
    AcceptedValidName = models.TextField(max_length=500, blank=True)
    Author = models.CharField(max_length=500, blank=True)
    MainReference = models.TextField(max_length=500, blank=True)
    DistributionInIndia = models.TextField(max_length=1000, blank=True)
    DistributionOutsideOfIndia = models.TextField(max_length=1000, blank=True)
    class Meta:
        db_table = "taxonmydistribution"

class GeneralInformationInsert(models.Model):
    ShrimpPrawnID = models.IntegerField()
    ScientificName = models.CharField(max_length=500)
    Environment = models.CharField(max_length=500, blank=True)
    CommonName = models.CharField(max_length=500, blank=True)
    ConservationStatus = models.CharField(max_length=500, blank=True)
    PopulationStatus = models.CharField(max_length=500, blank=True)
    DistributionInIndia = models.TextField(max_length=1000, blank=True)
    DistributionOutsideOfIndia = models.TextField(max_length=1000, blank=True)
    class Meta:
        db_table = "generalinformation"

class SynonymsInsert(models.Model):
    ShrimpPrawnID = models.IntegerField()
    ScientificName = models.CharField(max_length=500)
    Synonym = models.CharField(max_length=500, blank=True)
    Synonymy = models.CharField(max_length=500, blank=True)
    Status = models.CharField(max_length=500, blank=True)
    Valid = models.CharField(max_length=500, blank=True)
    Author = models.CharField(max_length=500, blank=True)
    class Meta:
        db_table = "synonyms"


class MorphologicalInsert(models.Model):
    ShrimpPrawnID = models.IntegerField()
    ScientificName = models.CharField(max_length=100)
    ShortDescription = models.TextField(max_length=2000, blank=True)
    BodyNature = models.TextField(max_length=2000, blank=True)
    Eyes = models.CharField(max_length=500, blank=True)
    RostrumNature = models.TextField(max_length=2000, blank=True)
    RostralTeethFormula = models.CharField(max_length=500, blank=True)
    CarapaceNature = models.CharField(max_length=500, blank=True)
    AntennuleSegments = models.CharField(max_length=500, blank=True)
    AntennalSegments = models.CharField(max_length=500, blank=True)
    MouthSegments = models.CharField(max_length=500, blank=True)
    AbdominalSomites = models.CharField(max_length=500, blank=True)
    ThridMaxilliped = models.CharField(max_length=500, blank=True)
    Pereoopod_I = models.CharField(max_length=500, blank=True)
    Pereoopod_II = models.CharField(max_length=500, blank=True)
    Pereoopod_III = models.CharField(max_length=500, blank=True)
    SternalPlate = models.CharField(max_length=500, blank=True)
    TelsonNature = models.CharField(max_length=500, blank=True)
    SexualSystem = models.CharField(max_length=500, blank=True)
    SecondarySexualSystem = models.CharField(max_length=500, blank=True)
    SexualDimorphism = models.CharField(max_length=500, blank=True)
    SpecificRemarks = models.CharField(max_length=500, blank=True)
    Colouration = models.TextField(max_length=2000, blank=True)
    class Meta:
        db_table = "morphological"


class TypeSpecimenInsert(models.Model):
    ShrimpPrawnID = models.IntegerField()
    ScientificName = models.CharField(max_length=500)
    TypeSpecimenStatus = models.CharField(max_length=500, blank=True)
    TypeSpecimenRepository = models.CharField(max_length=1000, blank=True)
    TypeLocality = models.CharField(max_length=500, blank=True)
    Author = models.CharField(max_length=500, blank=True)
    TypeSpecimenCatalogueNumber = models.CharField(max_length=500, blank=True)
    URL = models.CharField(max_length=500, blank=True)
    Source = models.CharField(max_length=500, blank=True)
    class Meta:
        db_table = "typespecimen"


class BiologyInsert(models.Model):
    ShrimpPrawnID = models.IntegerField()
    ScientificName = models.CharField(max_length=500)
    Ecology_Habitat = models.CharField(max_length=500, blank=True)
    LifeCycleAndMatingBehaviour = models.CharField(max_length=500, blank=True)
    LifeSpan = models.CharField(max_length=500, blank=True)
    SymbioticRelationship = models.CharField(max_length=500, blank=True)
    DepthRanges = models.CharField(max_length=500, blank=True)
    Biology = models.CharField(max_length=500, blank=True)
    Sex = models.CharField(max_length=500, blank=True)
    SizeRangesTotalLength = models.CharField(max_length=500, blank=True)
    SizeRangesCarapaceLength = models.CharField(max_length=500, blank=True)
    ReproductionStrategy = models.CharField(max_length=500, blank=True)
    BreedingSeason = models.CharField(max_length=500, blank=True)
    SexualDimorphism = models.CharField(max_length=500, blank=True)
    MoltingFrequency = models.CharField(max_length=500, blank=True)
    BreedingFrequency = models.CharField(max_length=500, blank=True)
    AgeSexualMaturity = models.CharField(max_length=500, blank=True)
    Fecundity = models.CharField(max_length=500, blank=True)
    LarvalDevelopment = models.CharField(max_length=500, blank=True)
    Group = models.CharField(max_length=500, blank=True)
    Mobility = models.CharField(max_length=500, blank=True)
    Dispersion = models.CharField(max_length=500, blank=True)
    FeedingBehaviour = models.CharField(max_length=500, blank=True)
    FeedingType = models.CharField(max_length=500, blank=True)
    FoodItems = models.CharField(max_length=500, blank=True)
    CommericalImportance = models.CharField(max_length=500, blank=True)
    EcologicalUtlity = models.CharField(max_length=500, blank=True)
    EconomicUtility = models.CharField(max_length=500, blank=True)
    AquacultureUtility = models.CharField(max_length=500, blank=True)
    ConsumerUtility = models.CharField(max_length=500, blank=True)
    Competitors = models.CharField(max_length=500, blank=True)
    EcologicalImpact = models.CharField(max_length=500, blank=True)
    EconomicImpact = models.CharField(max_length=500, blank=True)
    Comments = models.CharField(max_length=500, blank=True)

    class Meta:
        db_table = "biology"




class TypeLocalityInsert(models.Model):
    ShrimpPrawnID = models.IntegerField()
    ScientificName = models.CharField(max_length=500)
    GBIFID = models.CharField(max_length=500, blank=True)
    Family = models.CharField(max_length=500, blank=True)
    Genus = models.CharField(max_length=500, blank=True)
    Author = models.CharField(max_length=500, blank=True)
    TaxonRank = models.CharField(max_length=1000, blank=True)
    CountryCode = models.CharField(max_length=500, blank=True)
    Locality = models.CharField(max_length=500, blank=True)
    StateProvince = models.CharField(max_length=500, blank=True)
    OccurrenceStatus = models.CharField(max_length=500, blank=True)
    IndividualCount = models.CharField(max_length=500, blank=True)
    Latitude = models.CharField(max_length=500, blank=True)
    Longitude = models.CharField(max_length=500, blank=True)
    RecordBasis = models.CharField(max_length=500, blank=True)
    InstitutionCode = models.CharField(max_length=500, blank=True)
    CatalogueNumber = models.CharField(max_length=500, blank=True)
    IdentifiedBy = models.CharField(max_length=500, blank=True)
    License = models.CharField(max_length=500, blank=True)
    TypeStatus = models.CharField(max_length=500, blank=True)
    EstablishmentMeans = models.CharField(max_length=500, blank=True)
    TypeSpecimenStatus = models.CharField(max_length=500, blank=True)
    TypeSpecimenRepository = models.CharField(max_length=1000, blank=True)
    TypeLocality = models.CharField(max_length=500, blank=True)
    Author = models.CharField(max_length=500, blank=True)
    TypeSpecimenCatalogueNumber = models.CharField(max_length=500, blank=True)
    URL = models.CharField(max_length=500, blank=True)
    Source = models.CharField(max_length=500, blank=True)
    class Meta:
        db_table = "typelocality"



class OccurrenceInsert(models.Model):
    GBIFID = models.CharField(max_length=500, blank=True)
    Family = models.CharField(max_length=500, blank=True)
    Genus = models.CharField(max_length=500, blank=True)
    ShrimpPrawnID = models.IntegerField()
    ScientificName = models.CharField(max_length=500)
    Author = models.CharField(max_length=500, blank=True)
    TaxonRank = models.CharField(max_length=1000, blank=True)
    CountryCode = models.CharField(max_length=500, blank=True)
    Locality = models.CharField(max_length=500, blank=True)
    StateProvince = models.CharField(max_length=500, blank=True)
    OccurrenceStatus = models.CharField(max_length=500, blank=True)
    IndividualCount = models.CharField(max_length=500, blank=True)
    Latitude = models.CharField(max_length=500, blank=True)
    Longitude = models.CharField(max_length=500, blank=True)
    RecordBasis = models.CharField(max_length=500, blank=True)
    InstitutionCode = models.CharField(max_length=500, blank=True)
    CatalogueNumber = models.CharField(max_length=500, blank=True)
    IdentifiedBy = models.CharField(max_length=500, blank=True)
    License = models.CharField(max_length=500, blank=True)
    TypeStatus = models.CharField(max_length=500, blank=True)
    EstablishmentMeans = models.CharField(max_length=500, blank=True)
    class Meta:
        db_table = "occurrence"




def filepath(request, filename):
    old_filename = filename
    timenow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s", (timenow, old_filename)
    return os.path.join('uploads/', filename)



class ImageInsert(models.Model):
    ShrimpPrawnID = models.IntegerField()
    ScientificName = models.CharField(max_length=500)
    Image1 = models.ImageField(upload_to="images/", null=True, blank=True)
    Image2 = models.ImageField(upload_to="images/", null=True, blank=True)
    Image3 = models.ImageField(upload_to="images/", null=True, blank=True)
    class Meta:
        db_table = "image"

class Crab_ImageInsert(models.Model):
    CrabID = models.IntegerField() 
    ScientificName = models.CharField(max_length=500)
    Image1 = models.ImageField(upload_to="images/", null=True, blank=True)
    Image2 = models.ImageField(upload_to="images/", null=True, blank=True)
    Image3 = models.ImageField(upload_to="images/", null=True, blank=True)
    class Meta:
        db_table = "Crab_image"





class Crab_OccurrenceInsert(models.Model):
    CrabID = models.IntegerField()
    ScientificName = models.CharField(max_length=500)
    Locality = models.CharField(max_length=500, blank=True)
    State = models.CharField(max_length=500, blank=True)
    Latitude = models.CharField(max_length=500, blank=True)
    Longitude = models.CharField(max_length=500, blank=True)
    Source = models.CharField(max_length=500, blank=True)
    
    class Meta:
        db_table = "crab_occurrence"




class Crab_TypeSpecimenInsert(models.Model):
    CrabID = models.IntegerField()
    ScientificName = models.CharField(max_length=500)
    TypeSpecimen = models.CharField(max_length=500, blank=True)
    
    Geo_Unit_Locality = models.CharField(max_length=500, blank=True)
    Descriptor= models.CharField(max_length=500, blank=True)
    SpecimenCatalogueNumber = models.CharField(max_length=500, blank=True)
    
    class Meta:
        db_table = "crab_typespecimen"



class Crab_MorphologicalInsert(models.Model):
    CrabID = models.IntegerField()
    ScientificName = models.CharField(max_length=100)
    ShortDescription = models.TextField(max_length=2000, blank=True)
    BodyNature = models.TextField(max_length=2000, blank=True)
    Eyes = models.CharField(max_length=500, blank=True)
    CarapaceNature = models.CharField(max_length=500, blank=True)
    AntennalSegments = models.CharField(max_length=500, blank=True)
    ChilepedNature = models.CharField(max_length=500, blank=True)
    TelsonNature = models.CharField(max_length=500, blank=True) 
    SexualDimorphism = models.CharField(max_length=500, blank=True)
    HabitatAndEcology = models.CharField(max_length=500, blank=True)
    Biology = models.CharField(max_length=500, blank=True)
    SpecificRemarks = models.CharField(max_length=500, blank=True)
    Colouration = models.TextField(max_length=2000, blank=True)
    class Meta:
        db_table = "crab_morphological"


class Crab_SynonymsInsert(models.Model):
    CrabID = models.IntegerField()
    ScientificName = models.CharField(max_length=500)
    Synonym = models.CharField(max_length=500, blank=True)
    Synonymy = models.CharField(max_length=500, blank=True)
    Status = models.CharField(max_length=500, blank=True)
    Valid = models.CharField(max_length=500, blank=True)
    Author = models.CharField(max_length=500, blank=True)
    class Meta:
        db_table = "crab_synonyms"

class Crab_TaxonmyDistributionInsert(models.Model):
    Kingdom = models.CharField(max_length=500, blank=True)
    Phylum = models.CharField(max_length=500, blank=True)
    SubPhylum = models.CharField(max_length=500, blank=True)
    Class = models.CharField(max_length=500, blank=True)
    SubClass = models.CharField(max_length=500, blank=True)
    SuperOrder = models.CharField(max_length=500, blank=True)
    Order = models.CharField(max_length=500, blank=True)
    SubOrder = models.CharField(max_length=500, blank=True)
    InfraOrder = models.CharField(max_length=500, blank=True)
    SuperFamily = models.CharField(max_length=500, blank=True)
    Family = models.CharField(max_length=500, blank=True)
    SubFamily = models.CharField(max_length=500, blank=True)
    Genus = models.CharField(max_length=500, blank=True)
    ScientificName = models.CharField(max_length=500, blank=True)
    TaxonomicRank = models.CharField(max_length=500, blank=True)
    Subspecies = models.CharField(max_length=500, blank=True)
    AcceptedValidName = models.TextField(max_length=500, blank=True)
    CommonName = models.CharField(max_length=500, blank=True)
    Author = models.CharField(max_length=500, blank=True)
    MainReference = models.TextField(max_length=500, blank=True)
    Environment = models.CharField(max_length=500, blank=True)
    ConservationStatus = models.CharField(max_length=500, blank=True)
    DistributionInIndia = models.TextField(max_length=1000, blank=True)
    DistributionOutsideOfIndia = models.TextField(max_length=1000, blank=True)
    PopulationStatus = models.CharField(max_length=500, blank=True)
    OriginType = models.TextField(max_length=1000, blank=True)
    class Meta:
        db_table = "crab_taxonmydistribution"





class Lobster_TaxonmyDistributionInsert(models.Model):
    LobsterID = models.AutoField(primary_key=True, serialize=False)
    Kingdom = models.CharField(max_length=500, blank=True, null=True)
    Phylum = models.CharField(max_length=500, blank=True, null=True)
    SubPhylum = models.CharField(max_length=500, blank=True, null=True)
    Class = models.CharField(max_length=500, blank=True, null=True)
    SubClass = models.CharField(max_length=500, blank=True, null=True)
    SuperOrder = models.CharField(max_length=500, blank=True, null=True)
    Order = models.CharField(max_length=500, blank=True, null=True)
    SubOrder = models.CharField(max_length=500, blank=True, null=True)
    InfraOrder = models.CharField(max_length=500, blank=True, null=True)
    SuperFamily = models.CharField(max_length=500, blank=True, null=True)
    Family = models.CharField(max_length=500, blank=True, null=True)
    SubFamily = models.CharField(max_length=500, blank=True, null=True)
    Genus = models.CharField(max_length=500, blank=True, null=True)
    ScientificName = models.CharField(max_length=500, blank=True, null=True)
    TaxonomicRank = models.CharField(max_length=500, blank=True, null=True)
    Subspecies = models.CharField(max_length=500, blank=True, null=True)
    AcceptedValidName = models.TextField(max_length=500, blank=True, null=True)
    CommonName = models.CharField(max_length=500, blank=True, null=True)
    Author = models.CharField(max_length=500, blank=True, null=True)
    MainReference = models.TextField(max_length=500, blank=True, null=True)
    Environment = models.CharField(max_length=500, blank=True, null=True)    
    ConservationStatus = models.CharField(max_length=500, blank=True, null=True)
    DistributionInIndia = models.TextField(max_length=1000, blank=True, null=True)
    DistributionOutsideOfIndia = models.TextField(max_length=1000, blank=True, null=True)
    PopulationStatus = models.CharField(max_length=500, blank=True, null=True)
    OriginType = models.TextField(max_length=1000, blank=True, null=True)
    DepthRange = models.TextField(max_length=1000, blank=True, null=True)
    class Meta:
        db_table = "lobster_taxonmydistribution"

class Lobster_TypeSpecimenInsert(models.Model):
    #SpecimenID = models.AutoField(primary_key=True, serialize=False)
    LobsterID = models.IntegerField()
    ScientificName = models.CharField(max_length=500)
    TypeSpecimen = models.CharField(max_length=500, blank=True, null=True)    
    Geo_Unit_Locality = models.CharField(max_length=500, blank=True, null=True)
    Descriptor = models.CharField(max_length=500, blank=True, null=True)
    SpecimenCatalogueNumber = models.CharField(max_length=500, blank=True, null=True)
    Author = models.CharField(max_length=500, blank=True, null=True)
    class Meta:
        db_table = "lobster_typespecimen"

class Lobster_SynonymsInsert(models.Model):
    #SynonymsID = models.AutoField(primary_key=True, serialize=False)
    LobsterID = models.IntegerField()
    ScientificName = models.CharField(max_length=500)
    Synonym = models.CharField(max_length=500, blank=True, null=True)
    Synonymy = models.CharField(max_length=500, blank=True, null=True)
    Status = models.CharField(max_length=500, blank=True, null=True)
    Valid = models.CharField(max_length=500, blank=True, null=True)
    Author = models.CharField(max_length=500, blank=True, null=True)
    class Meta:
        db_table = "lobster_synonyms"

class Lobster_MorphologicalInsert(models.Model):
    #MorphoID = models.AutoField(primary_key=True, serialize=False)
    LobsterID = models.IntegerField()
    ScientificName = models.CharField(max_length=500)
    ShortDescription = models.TextField(max_length=2000, blank=True, null=True)
    BodyNature = models.TextField(max_length=2000, blank=True, null=True)
    Eyes = models.CharField(max_length=500, blank=True, null=True)    
    CarapaceNature = models.CharField(max_length=500, blank=True, null=True)
    AntennuleSegments = models.CharField(max_length=500, blank=True, null=True)
    AntennalPlate = models.CharField(max_length=500, blank=True, null=True)
    AbdominalSegments = models.CharField(max_length=500, blank=True, null=True)
    NatureofLegs = models.CharField(max_length=500, blank=True, null=True)
    TelsonNature = models.CharField(max_length=500, blank=True, null=True)
    SexualDimorphism = models.CharField(max_length=500, blank=True, null=True)
    HabitatAndEcology = models.CharField(max_length=500, blank=True, null=True)
    Biology = models.CharField(max_length=500, blank=True, null=True)
    SpecificRemarks = models.CharField(max_length=500, blank=True, null=True)
    Colouration = models.TextField(max_length=2000, blank=True, null=True)
    class Meta:
        db_table = "lobster_morphological"

class Lobster_OccurrenceInsert(models.Model):
    #OccurrenceID = models.AutoField(primary_key=True, serialize=False)
    LobsterID = models.IntegerField()
    ScientificName = models.CharField(max_length=500)
    Locality = models.CharField(max_length=500, blank=True, null=True)
    State = models.CharField(max_length=500, blank=True, null=True)
    Latitude = models.CharField(max_length=500, blank=True, null=True)
    Longitude = models.CharField(max_length=500, blank=True, null=True)
    #Source = models.CharField(max_length=500, blank=True, null=True)
    Reference = models.CharField(max_length=500, blank=True, null=True)
    class Meta:
        db_table = "lobster_occurrence" 

class Lobster_ImageInsert(models.Model):
    LobsterID = models.IntegerField() 
    ScientificName = models.CharField(max_length=500)
    Image1 = models.ImageField(upload_to="images/", null=True, blank=True)
    Image2 = models.ImageField(upload_to="images/", null=True, blank=True)
    Image3 = models.ImageField(upload_to="images/", null=True, blank=True)
    class Meta:
        db_table = "lobster_image"        


class Location(models.Model):
    ShrimpPrawnID = models.IntegerField()
    ScientificName = models.CharField(max_length=500)
    latitude =  models.CharField(max_length=500, blank=True, null=True)
    longitude =  models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=255,blank=True,null=True)

    def save(self, *args, **kwargs):
        # Get the name of the location based on the latitude and longitude
        self.name = self.get_location_name()

        super().save(*args, **kwargs)

    def get_location_name(self):
        url = f'https://nominatim.openstreetmap.org/reverse?lat={self.latitude}&lon={self.longitude}&format=json'

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if 'address' in data:
                # Combine the address fields into a single string
                address_fields = ['road', 'pedestrian', 'house_number', 'city', 'town', 'village', 'county', 'state', 'country']
                address_parts = [data['address'][field] for field in address_fields if field in data['address']]
                return ', '.join(address_parts)
        
        return None
    class Meta:
        db_table = "Location"