# Generated by Django 4.0.3 on 2022-06-02 05:39

from django.db import migrations, models
import shellfishapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BiologyInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShrimpPrawnID', models.IntegerField()),
                ('ScientificName', models.CharField(max_length=500)),
                ('Ecology_Habitat', models.CharField(blank=True, max_length=500)),
                ('LifeCycleAndMatingBehaviour', models.CharField(blank=True, max_length=500)),
                ('LifeSpan', models.CharField(blank=True, max_length=500)),
                ('SymbioticRelationship', models.CharField(blank=True, max_length=500)),
                ('DepthRanges', models.CharField(blank=True, max_length=500)),
                ('Biology', models.CharField(blank=True, max_length=500)),
                ('Sex', models.CharField(blank=True, max_length=500)),
                ('SizeRangesTotalLength', models.CharField(blank=True, max_length=500)),
                ('SizeRangesCarapaceLength', models.CharField(blank=True, max_length=500)),
                ('ReproductionStrategy', models.CharField(blank=True, max_length=500)),
                ('BreedingSeason', models.CharField(blank=True, max_length=500)),
                ('SexualDimorphism', models.CharField(blank=True, max_length=500)),
                ('MoltingFrequency', models.CharField(blank=True, max_length=500)),
                ('BreedingFrequency', models.CharField(blank=True, max_length=500)),
                ('AgeSexualMaturity', models.CharField(blank=True, max_length=500)),
                ('Fecundity', models.CharField(blank=True, max_length=500)),
                ('LarvalDevelopment', models.CharField(blank=True, max_length=500)),
                ('Group', models.CharField(blank=True, max_length=500)),
                ('Mobility', models.CharField(blank=True, max_length=500)),
                ('Dispersion', models.CharField(blank=True, max_length=500)),
                ('FeedingBehaviour', models.CharField(blank=True, max_length=500)),
                ('FeedingType', models.CharField(blank=True, max_length=500)),
                ('FoodItems', models.CharField(blank=True, max_length=500)),
                ('CommericalImportance', models.CharField(blank=True, max_length=500)),
                ('EcologicalUtlity', models.CharField(blank=True, max_length=500)),
                ('EconomicUtility', models.CharField(blank=True, max_length=500)),
                ('AquacultureUtility', models.CharField(blank=True, max_length=500)),
                ('ConsumerUtility', models.CharField(blank=True, max_length=500)),
                ('Competitors', models.CharField(blank=True, max_length=500)),
                ('EcologicalImpact', models.CharField(blank=True, max_length=500)),
                ('EconomicImpact', models.CharField(blank=True, max_length=500)),
                ('Comments', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'db_table': 'biology',
            },
        ),
        migrations.CreateModel(
            name='MorphologicalInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShrimpPrawnID', models.IntegerField()),
                ('ScientificName', models.CharField(max_length=100)),
                ('ShortDescription', models.TextField(blank=True, max_length=2000)),
                ('BodyNature', models.TextField(blank=True, max_length=2000)),
                ('Eyes', models.CharField(blank=True, max_length=500)),
                ('RostrumNature', models.TextField(blank=True, max_length=2000)),
                ('RostralTeethFormula', models.CharField(blank=True, max_length=500)),
                ('CarapaceNature', models.CharField(blank=True, max_length=500)),
                ('AntennuleSegments', models.CharField(blank=True, max_length=500)),
                ('AntennalSegments', models.CharField(blank=True, max_length=500)),
                ('MouthSegments', models.CharField(blank=True, max_length=500)),
                ('AbdominalSomites', models.CharField(blank=True, max_length=500)),
                ('ThridMaxilliped', models.CharField(blank=True, max_length=500)),
                ('Pereoopod_I', models.CharField(blank=True, max_length=500)),
                ('Pereoopod_II', models.CharField(blank=True, max_length=500)),
                ('Pereoopod_III', models.CharField(blank=True, max_length=500)),
                ('SternalPlate', models.CharField(blank=True, max_length=500)),
                ('TelsonNature', models.CharField(blank=True, max_length=500)),
                ('SexualSystem', models.CharField(blank=True, max_length=500)),
                ('SecondarySexualSystem', models.CharField(blank=True, max_length=500)),
                ('SexualDimorphism', models.CharField(blank=True, max_length=500)),
                ('SpecificRemarks', models.CharField(blank=True, max_length=500)),
                ('Colouration', models.TextField(blank=True, max_length=2000)),
            ],
            options={
                'db_table': 'morphological',
            },
        ),
        migrations.CreateModel(
            name='OccurrenceInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GBIFID', models.CharField(blank=True, max_length=500)),
                ('Family', models.CharField(blank=True, max_length=500)),
                ('Genus', models.CharField(blank=True, max_length=500)),
                ('ShrimpPrawnID', models.IntegerField()),
                ('ScientificName', models.CharField(max_length=500)),
                ('Author', models.CharField(blank=True, max_length=500)),
                ('TaxonRank', models.CharField(blank=True, max_length=1000)),
                ('CountryCode', models.CharField(blank=True, max_length=500)),
                ('Locality', models.CharField(blank=True, max_length=500)),
                ('StateProvince', models.CharField(blank=True, max_length=500)),
                ('OccurrenceStatus', models.CharField(blank=True, max_length=500)),
                ('IndividualCount', models.CharField(blank=True, max_length=500)),
                ('Latitude', models.CharField(blank=True, max_length=500)),
                ('Longitude', models.CharField(blank=True, max_length=500)),
                ('RecordBasis', models.CharField(blank=True, max_length=500)),
                ('InstitutionCode', models.CharField(blank=True, max_length=500)),
                ('CatalogueNumber', models.CharField(blank=True, max_length=500)),
                ('IdentifiedBy', models.CharField(blank=True, max_length=500)),
                ('License', models.CharField(blank=True, max_length=500)),
                ('TypeStatus', models.CharField(blank=True, max_length=500)),
                ('EstablishmentMeans', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'db_table': 'occurrence',
            },
        ),
        migrations.CreateModel(
            name='SynonymsInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShrimpPrawnID', models.IntegerField()),
                ('ScientificName', models.CharField(max_length=500)),
                ('Synonym', models.CharField(blank=True, max_length=500)),
                ('Synonymy', models.CharField(blank=True, max_length=500)),
                ('Status', models.CharField(blank=True, max_length=500)),
                ('Valid', models.CharField(blank=True, max_length=500)),
                ('Author', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'db_table': 'synonyms',
            },
        ),
        migrations.CreateModel(
            name='TaxonmyDistributionInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CrusteceanSubgroup', models.CharField(blank=True, max_length=500)),
                ('CrusteceanSubgroupType', models.CharField(blank=True, max_length=500)),
                ('Kingdom', models.CharField(blank=True, max_length=500)),
                ('Phylum', models.CharField(blank=True, max_length=500)),
                ('SubPhylum', models.CharField(blank=True, max_length=500)),
                ('Class', models.CharField(blank=True, max_length=500)),
                ('SubClass', models.CharField(blank=True, max_length=500)),
                ('SuperOrder', models.CharField(blank=True, max_length=500)),
                ('Order', models.CharField(blank=True, max_length=500)),
                ('SubOrder', models.CharField(blank=True, max_length=500)),
                ('InfraOrder', models.CharField(blank=True, max_length=500)),
                ('SuperFamily', models.CharField(blank=True, max_length=500)),
                ('Family', models.CharField(blank=True, max_length=500)),
                ('SubFamily', models.CharField(blank=True, max_length=500)),
                ('Genus', models.CharField(blank=True, max_length=500)),
                ('ScientificName', models.CharField(blank=True, max_length=500)),
                ('TaxonomicRank', models.CharField(blank=True, max_length=500)),
                ('Subspecies', models.CharField(blank=True, max_length=500)),
                ('Environment', models.CharField(blank=True, max_length=500)),
                ('CommonName', models.CharField(blank=True, max_length=500)),
                ('ConservationStatus', models.CharField(blank=True, max_length=500)),
                ('PopulationStatus', models.CharField(blank=True, max_length=500)),
                ('AcceptedValidName', models.TextField(blank=True, max_length=500)),
                ('Author', models.CharField(blank=True, max_length=500)),
                ('MainReference', models.TextField(blank=True, max_length=500)),
                ('DistributionInIndia', models.TextField(blank=True, max_length=1000)),
                ('DistributionOutsideOfIndia', models.TextField(blank=True, max_length=1000)),
            ],
            options={
                'db_table': 'taxonmydistribution',
            },
        ),
        migrations.CreateModel(
            name='TypeSpecimenInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShrimpPrawnID', models.IntegerField()),
                ('ScientificName', models.CharField(max_length=500)),
                ('TypeSpecimenStatus', models.CharField(blank=True, max_length=500)),
                ('TypeSpecimenRepository', models.CharField(blank=True, max_length=1000)),
                ('TypeLocality', models.CharField(blank=True, max_length=500)),
                ('Author', models.CharField(blank=True, max_length=500)),
                ('TypeSpecimenCatalogueNumber', models.CharField(blank=True, max_length=500)),
                ('URL', models.CharField(blank=True, max_length=500)),
                ('Source', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'db_table': 'typespecimen',
            },
        ),
    ]