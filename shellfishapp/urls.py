from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('home', views.home, name='home_page'),
    path("register", views.register_request, name="register"),
    path('login', views.login_request, name='login_page'),
    path('logout', views.logout_request, name='logout'),
    path('', views.search, name='search_page'),
    path('ScientificName_search', views.ScientificName_Search, name='ScientificName_Search'),
    path('get_scientific_names/', views.get_scientific_names, name='get_scientific_names'),
    path('image_info/', views.image_info, name='image_info'),
    path('all_imgview/', views.all_imgview, name='all_imgview'),
    
    path('search/autocomplete/', views.autocomplete, name='autocomplete'),
    path('search/autocomplete1/', views.autocomplete1, name='autocomplete1'),
    path('search/autocomplete2/', views.autocomplete2, name='autocomplete2'),
    path('search/autocomplete3/', views.autocomplete3, name='autocomplete3'),
    
    
    path('my-search/',views.SearchView.as_view(), name='search_view'),
    #path('search/', views.search5, name='search_view'),
    #path('search1/', views.search_view14, name='search_view1'),
    


#paths for ShrimpPrawns TaxonomyAndDistribution   
    path('taxoadd/', views.taxoadd, name='taxo_add'),
    path('view/', views.viewpage, name='View_page'),
    path('taxoview/', views.taxoview, name='taxo_view'),
    path('UA_taxoview/', views.UA_taxoview, name='UA_taxo_view'),
    path('taxoedit/<int:id>', views.taxoedit, name='taxo_edit'),
    path('taxoupdate/<int:id>', views.taxoupdate, name='taxo_update'),
    path('taxodelete/<int:id>', views.taxodelete, name='taxo_delete'),
    path('taxasearch', views.taxasearch, name='taxa_search'),

    
    path('distsearch', views.distsearch, name='dist_search'),

#paths for ShrimpPrawn Synonyms
    path('synadd/', views.synadd, name='syn_add'),
    path('synview/', views.synview, name='syn_view'),
    path('UA_synview/', views.UA_synview, name='UA_syn_view'),
    path('synedit/<int:id>', views.synedit, name='syn_edit'),
    path('synupdate/<int:id>', views.synupdate, name='syn_update'),
    path('syndelete/<int:id>', views.syndelete, name='syn_delete'),
    path('synsearch', views.synsearch, name='syn_search'),

#paths for ShrimpPrawn Morphological   
    path('morphoadd/', views.morphoadd, name='morpho_add'),
    path('morphoview/', views.morphoview, name='morpho_view'),
    path('UA_morphoview/', views.UA_morphoview, name='UA_morpho_view'),
    path('morphoedit/<int:id>', views.morphoedit, name='morpho_edit'),
    path('morphoupdate/<int:id>', views.morphoupdate, name='morpho_update'),
    path('morphodelete/<int:id>', views.morphodelete, name='morpho_delete'),
    path('morphosearch', views.morphosearch, name='morpho_search'),

#paths for ShrimpPrawn Typespecimen 
    path('speciadd/', views.speciadd, name='speci_add'),
    path('speciview/', views.speciview, name='speci_view'),
    path('UA_speciview/', views.UA_speciview, name='UA_speci_view'),
    path('speciedit/<int:id>', views.speciedit, name='speci_edit'),
    path('speciupdate/<int:id>', views.speciupdate, name='speci_update'),
    path('specidelete/<int:id>', views.specidelete, name='speci_delete'),
    path('specisearch', views.specisearch, name='speci_search'),


#paths for ShrimpPrawn Biology  
    path('bioadd/', views.bioadd, name='bio_add'),
    path('bioview/', views.bioview, name='bio_view'),
    path('UA_bioview/', views.UA_bioview, name='UA_bio_view'),
    path('bioedit/<int:id>', views.bioedit, name='bio_edit'),
    path('bioupdate/<int:id>', views.bioupdate, name='bio_update'),
    path('biodelete/<int:id>', views.biodelete, name='bio_delete'),
    path('biosearch', views.biosearch, name='bio_search'),




#paths for ShrimpPrawn Occurence
    path('occadd/', views.occadd, name='occ_add'),
    path('occview/', views.occview, name='occ_view'),
    path('UA_occview/', views.UA_occview, name='UA_occ_view'),
    path('occedit/<int:id>', views.occedit, name='occ_edit'),
    path('occupdate/<int:id>', views.occupdate, name='occ_update'),
    path('occdelete/<int:id>', views.occdelete, name='occ_delete'),
    path('occsearch', views.occsearch, name='occ_search'),

#Paths for ShrimpPrawn Image   
    path('imgadd/', views.imgadd, name='img_add'),
    path('imgview/', views.imgview, name='img_view'),
    path('imgedit/<int:id>', views.imgedit, name='img_edit'),
    path('imgupdate/<int:id>', views.imgupdate, name='img_update'),
    path('imgdelete/<int:id>', views.imgdelete, name='img_delete'),


#paths for ShrimpPrawn TypeLocality
    path('typelocalityadd/', views.add_location, name='typelocality_add'),
    path('typelocalityview/', views.view_location, name='typelocality_view'),




#paths for ShrimpPrawn GeneralInformation
    path('generalinformationadd/', views.generalinformationadd, name='generalinformation_add'),
    path('generalinformationview/', views.generalinformationview, name='generalinformation_view'),
    path('generalinformationedit/<int:id>', views.geninfoedit, name='generalinformation_edit'),
    path('generalinformationupdate/<int:id>', views.generalinformationupdate, name='generalinformation_update'),
    path('generalinformationdelete/<int:id>', views.generalinformationdelete, name='generalinformation_delete'),
    path('generalinformationsearch', views.generalinformationsearch, name='generalinformation_search'),

    
    

#paths for Crab Image
    path('Crab_imgadd/', views.Crab_imgadd, name='Crab_img_add'),
    path('Crab_imgview/', views.Crab_imgview, name='Crab_img_view'),
    path('Crab_imgedit/<int:id>', views.Crab_imgedit, name='Crab_img_edit'),
    path('Crab_imgupdate/<int:id>', views.Crab_imgupdate, name='Crab_img_update'),
    path('Crab_imgdelete/<int:id>', views.Crab_imgdelete, name='Crab_img_delete'),


#paths for Crab Taxonomy and Distribution
    path('Crab_taxoadd/', views.Crab_taxoadd, name='Crab_taxo_add'),
    path('Crab_taxoview/', views.Crab_taxoview, name='Crab_taxo_view'),
    path('UA_Crab_taxoview/', views.UA_Crab_taxoview, name='UA_Crab_taxo_view'),
    path('Crab_taxoedit/<int:id>', views.Crab_taxoedit, name='Crab_taxo_edit'),
    path('Crab_taxoupdate/<int:id>', views.Crab_taxoupdate, name='Crab_taxo_update'),
    path('Crab_taxodelete/<int:id>', views.Crab_taxodelete, name='Crab_taxo_delete'),
    path('Crab_taxasearch', views.Crab_taxasearch, name='Crab_taxa_search'),



#paths for Crab GeneralInformation
    path('Crab_generalinformationadd/', views.Crab_generalinformationadd, name='Crab_generalinformation_add'),
    path('Crab_generalinformationview/', views.Crab_generalinformationview, name='Crab_generalinformation_view'),
    path('Crab_generalinformationedit/<int:id>', views.Crab_geninfoedit, name='Crab_generalinformation_edit'),
    path('Crab_generalinformationupdate/<int:id>', views.Crab_generalinformationupdate, name='Crab_generalinformation_update'),
    path('Crab_generalinformationdelete/<int:id>', views.Crab_generalinformationdelete, name='Crab_generalinformation_delete'),
    path('Crab_generalinformationsearch', views.Crab_generalinformationsearch, name='Crab_generalinformation_search'),









#paths for Crab Synonyms
    path('Crab_synadd/', views.Crab_synadd, name='Crab_syn_add'),
    path('Crab_synview/', views.Crab_synview, name='Crab_syn_view'),
    path('UA_Crab_synview/', views.UA_Crab_synview, name='UA_Crab_syn_view'),
    path('Crab_synedit/<int:id>', views.Crab_synedit, name='Crab_syn_edit'),
    path('Crab_syndelete/<int:id>', views.Crab_syndelete, name='Crab_syn_delete'),
    path('Crab_synsearch', views.Crab_synsearch, name='Crab_syn_search'),
    path('Crab_synupdate/<int:id>', views.Crab_synupdate, name='Crab_syn_update'),


#paths for Crab Morphological
    path('Crab_morphoadd/', views.Crab_morphoadd, name='Crab_morpho_add'),
    path('Crab_morphoview/', views.Crab_morphoview, name='Crab_morpho_view'),
    path('UA_Crab_morphoview/', views.UA_Crab_morphoview, name='UA_Crab_morpho_view'),
    path('Crab_morphoedit/<int:id>', views.Crab_morphoedit, name='Crab_morpho_edit'),
    path('Crab_morphoupdate/<int:id>', views.Crab_morphoupdate, name='Crab_morpho_update'),
    path('Crab_morphodelete/<int:id>', views.Crab_morphodelete, name='Crab_morpho_delete'),
    path('Crab_morphosearch', views.Crab_morphosearch, name='Crab_morpho_search'),

    
#paths for Crab Typespecimen
    path('Crab_speciadd/', views.Crab_speciadd, name='Crab_speci_add'),
    path('Crab_speciview/', views.Crab_speciview, name='Crab_speci_view'),
    path('UA_Crab_speciview/', views.UA_Crab_speciview, name='UA_Crab_speci_view'),
    path('Crab_speciedit/<int:id>', views.Crab_speciedit, name='Crab_speci_edit'),
    path('Crab_speciupdate/<int:id>', views.Crab_speciupdate, name='Crab_speci_update'),
    path('Crab_specidelete/<int:id>', views.Crab_specidelete, name='Crab_speci_delete'),
    path('Crab_specisearch', views.Crab_specisearch, name='Crab_speci_search'),




#paths for Crab Occurrence
    path('crab_occadd/', views.Crab_occadd, name='Crab_occ_add'),
    path('Crab_occview/', views.Crab_occview, name='Crab_occ_view'),
    path('UA_Crab_occview/', views.UA_Crab_occview, name='UA_Crab_occ_view'),
    path('Crab_occedit/<int:id>', views.Crab_occedit, name='Crab_occ_edit'),
    path('Crab_occupdate/<int:id>', views.Crab_occupdate, name='Crab_occ_update'),
    path('Crab_occdelete/<int:id>', views.Crab_occdelete, name='Crab_occ_delete'),
    path('Crab_occsearch', views.Crab_occsearch, name='Crab_occ_search'),



#paths for lobster taxonomy and distribution
    path('lobster_taxoadd/', views.lobster_taxoadd, name='lobster_taxo_add'),
    path('lobster_taxoview/', views.lobster_taxoview, name='lobster_taxo_view'),
    path('UA_lobster_taxoview/', views.UA_lobster_taxoview, name='UA_lobster_taxo_view'),
    path('lobster_taxoedit/<int:id>', views.lobster_taxoedit, name='lobster_taxo_edit'),
    path('lobster_taxoupdate/<int:id>', views.lobster_taxoupdate, name='lobster_taxo_update'),
    path('lobster_taxodelete/<int:id>', views.lobster_taxodelete, name='lobster_taxo_delete'),
    path('lobster_taxasearch', views.lobster_taxasearch, name='lobster_taxa_search'),



#paths for Lobster GeneralInformation
    path('Lobster_generalinformationadd/', views.Lobster_generalinformationadd, name='Lobster_generalinformation_add'),
    path('Lobster_generalinformationview/', views.Lobster_generalinformationview, name='Lobster_generalinformation_view'),
    path('Lobster_generalinformationedit/<int:id>', views.Lobster_geninfoedit, name='Lobster_generalinformation_edit'),
    path('Lobster_generalinformationupdate/<int:id>', views.Lobster_generalinformationupdate, name='Lobster_generalinformation_update'),
    path('Lobster_generalinformationdelete/<int:id>', views.Lobster_generalinformationdelete, name='Lobster_generalinformation_delete'),
    path('Lobster_generalinformationsearch', views.Lobster_generalinformationsearch, name='Lobster_generalinformation_search'),









#paths for lobster Synonyms 
    path('lobster_synadd/', views.lobster_synadd, name='lobster_syn_add'),
    path('lobster_synview/', views.lobster_synview, name='lobster_syn_view'),
    path('UA_lobster_synview/', views.UA_lobster_synview, name='UA_lobster_syn_view'),
    path('lobster_synedit/<int:id>', views.lobster_synedit, name='lobster_syn_edit'),
    path('lobster_synupdate/<int:id>', views.lobster_synupdate, name='lobster_syn_update'),
    path('lobster_syndelete/<int:id>', views.lobster_syndelete, name='lobster_syn_delete'),
    path('lobster_synsearch', views.lobster_synsearch, name='lobster_syn_search'),


#paths for lobster Morphological
    path('lobster_morphoadd/', views.lobster_morphoadd, name='lobster_morpho_add'),
    path('lobster_morphoview/', views.lobster_morphoview, name='lobster_morpho_view'),
    path('UA_lobster_morphoview/', views.UA_lobster_morphoview, name='UA_lobster_morpho_view'),
    path('lobster_morphoedit/<int:id>', views.lobster_morphoedit, name='lobster_morpho_edit'),
    path('lobster_morphoupdate/<int:id>', views.lobster_morphoupdate, name='lobster_morpho_update'),
    path('lobster_morphodelete/<int:id>', views.lobster_morphodelete, name='lobster_morpho_delete'),
    path('lobster_morphosearch', views.lobster_morphosearch, name='lobster_morpho_search'),



#paths for lobster typespecimen
    path('lobster_speciadd/', views.lobster_speciadd, name='lobster_speci_add'),
    path('lobster_speciview/', views.lobster_speciview, name='lobster_speci_view'),
    path('UA_lobster_speciview/', views.UA_lobster_speciview, name='UA_lobster_speci_view'),
    path('lobster_speciedit/<int:id>', views.lobster_speciedit, name='lobster_speci_edit'),
    path('lobster_speciupdate/<int:id>', views.lobster_speciupdate, name='lobster_speci_update'),
    path('lobster_specidelete/<int:id>', views.lobster_specidelete, name='lobster_speci_delete'),
    path('lobster_specisearch', views.lobster_specisearch, name='lobster_speci_search'),


#paths for lobster Occurrence
    path('lobster_occadd/', views.lobster_occadd, name='lobster_occ_add'),
    path('lobster_occview/', views.lobster_occview, name='lobster_occ_view'),
    path('UA_lobster_occview/', views.UA_lobster_occview, name='UA_lobster_occ_view'),
    path('lobster_occedit/<int:id>', views.lobster_occedit, name='lobster_occ_edit'),
    path('lobster_occupdate/<int:id>', views.lobster_occupdate, name='lobster_occ_update'),
    path('lobster_occdelete/<int:id>', views.lobster_occdelete, name='lobster_occ_delete'),
    path('lobster_occsearch', views.lobster_occsearch, name='lobster_occ_search'),


#paths for lobster images
    path('lobster_imgadd/', views.lobster_imgadd, name='lobster_img_add'),
    path('lobster_imgview/', views.lobster_imgview, name='lobster_img_view'),
    path('lobster_imgedit/<int:id>', views.lobster_imgedit, name='lobster_img_edit'),
    path('lobster_imgupdate/<int:id>', views.lobster_imgupdate, name='lobster_img_update'),
    path('lobster_imgdelete/<int:id>', views.lobster_imgdelete, name='lobster_img_delete'),
    

   

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
