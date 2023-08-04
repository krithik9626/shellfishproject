from django.contrib import admin
from .models import TaxonmyDistributionInsert,MorphologicalInsert,SynonymsInsert,TypeSpecimenInsert,Crab_SynonymsInsert,Crab_ImageInsert,Crab_MorphologicalInsert,Crab_OccurrenceInsert,Crab_TaxonmyDistributionInsert,Crab_TypeSpecimenInsert
# Register your models here.

admin.site.site_header = "NBFGR Admin Panel"
admin.site.site_title = "ShellFish"
admin.site.index_title = "NBFGR"

@admin.register(TaxonmyDistributionInsert)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
TaxonmyDistributionInsert._meta.get_fields()]

@admin.register(MorphologicalInsert)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
MorphologicalInsert._meta.get_fields()]


@admin.register(TypeSpecimenInsert)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
TypeSpecimenInsert._meta.get_fields()]
  

@admin.register(SynonymsInsert)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
SynonymsInsert._meta.get_fields()]

@admin.register(Crab_TaxonmyDistributionInsert)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Crab_TaxonmyDistributionInsert._meta.get_fields()]


@admin.register(Crab_SynonymsInsert)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Crab_SynonymsInsert._meta.get_fields()]

@admin.register(Crab_MorphologicalInsert)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Crab_MorphologicalInsert._meta.get_fields()]

@admin.register(Crab_TypeSpecimenInsert)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Crab_TypeSpecimenInsert._meta.get_fields()]


@admin.register(Crab_OccurrenceInsert)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Crab_OccurrenceInsert._meta.get_fields()]

@admin.register(Crab_ImageInsert)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Crab_ImageInsert._meta.get_fields()]




