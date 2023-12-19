from django.db import models
import datetime

#  models here.


class qc_datasheet_mueller_hinton_agar_theory(models.Model):
        class Meta:
             verbose_name_plural = "MUELLER HINTON AGAR Q.C Theory part"

        Appearance=models.CharField(max_length=150,default='Conformity / Specifications')
        color=models.CharField(max_length=100,default='Pale Yellow')
        pH_value=models.CharField(max_length=50,default='7.3 +/-0.1')
        micro_biology_activity_res=models.CharField(max_length=100,default='Incubation 24 hours at 33-37° C')
  



        Microbiological_state=models.CharField(max_length=250,default='Thickness/In process Control (not the default value just aplace holder)')

        Escherichia_coli_ATCC_25922_Antibiotic=models.CharField(max_length=250,default="Ampicillin 10 ug")                                        
        Ampicillin_10_ug_zone_size=models.CharField(max_length=250,default="16 - 22mm",)
    
        Staphylococcus_aureus_ATCC_29213_Antiboitic=models.CharField(max_length=250,default='Linezolid 10μg')
        Linezolid_10μg_zone_size=models.CharField(max_length=250,default="21-27 mm",)

        Pseudomonas_aeruginosa_ATCC_27853_Antiboitic=models.CharField(max_length=250,default='Ciprofloxacin 15μg')
        Ciprofloxacin_15μg_zone_size=models.CharField(max_length=250,default="25-33 mm",)

        Enterococcus_faecalis_ATCC_29212_Antiboitic=models.CharField(max_length=250,default='Trimethoprim sulfamethoxazole 1.25/23.μg \n & Vancomycin 5μg')
        Trimethoprim_sulfamethoxazole_125_23_μg_zone_size=models.CharField(max_length=250,default="15 - 21 mm", )
        Vancomycin_5μg_zone_size=models.CharField(max_length=250,default="26 - 34 mm", )
  


class qc_datasheet_mueller_hinton_agar(models.Model):
    class Meta:
        verbose_name_plural = "MUELLER HINTON AGAR Q.C"

    date_today=datetime.datetime.now
    
    ph_value=[('7',"7"),
              ('7.1',"7.1"),
              ('7.2',"7.2"),
              ('7.3',"7.3"),
              ('7.4',"7.4"),
                ('7.5',"7.5"),
                ('7.6',"7.6"),

              
              ]
    
    micr_bioloy_activity=[
        ("33","33"),
        ("34","34"),
        ("35","35"),
        ("36","36"),
        ("37","37")
    ]

    Ampicillin_10_ug_zone_size_chioce=[
        ("16 mm", "16 mm"),
        ("17 mm", "17 mm"),
        ("18 mm", "18 mm"),
        ("19 mm", "19 mm"),
        ("20 mm", "20 mm"),
        ("21 mm", "21 mm"),
        ("22 mm", "22 mm"),
        ]
    
    Linezolid_10μg_zone_size_choice=[
        ("21 mm", "21 mm"),
        ("22 mm", "22 mm"),
         ("23 mm", "23 mm"),
        ("24 mm", "24 mm"),
        ("25 mm", "25 mm"),
        ("26 mm", "26 mm"),
        ("27 mm", "27 mm"),       
       
        ]
    

    Ciprofloxacin_15μg_zone_size_choice=[
        ("25 mm", "25 mm"),
        ("26 mm", "26 mm"),
        ("27 mm", "27 mm"),       
       ("28 mm", "28 mm"),
        ("29 mm", "29 mm"),
        ("30 mm", "30 mm"),       
       ("31 mm", "31 mm"),
        ("22 mm", "32 mm"),
        ("33 mm", "33 mm"),       
       
    ]
    
    Trimethoprim_sulfamethoxazole_125_23_μg_zone_size_choice=[
        
        ("15 mm", "15 mm"),       
        ("16 mm", "16 mm"),
        ("17 mm", "17 mm"),
        ("18 mm", "18 mm"),
        ("19 mm", "19 mm"),
        ("20 mm", "20 mm"),
        ("21 mm", "21 mm"),
       
    ]

    Vancomycin_5μg_zone_size_choice=[
        
        ("26 mm", "26 mm"),
        ("27 mm", "27 mm"),       
        ("28 mm", "28 mm"),
        ("29 mm", "29 mm"),
        ("30 mm", "30 mm"),       
        ("31 mm", "31 mm"),
        ("22 mm", "32 mm"),
        ("33 mm", "33 mm"),       
        ("34 mm", "34 mm"),       
       
    ]



    lot_no_con='MP06'+str(datetime.datetime.now().day)+str(datetime.datetime.now().month)+str(datetime.datetime.now().strftime('%y'))
    Material_code=models.CharField(max_length=50,default='MP06')
    Lot_No=models.CharField(max_length=100,default=lot_no_con)
    mfg_date=models.DateField(default=date_today)
    Expiry_date=models.DateField(default=date_today)
    Appearance=models.CharField(max_length=150,default='CONFORME')
    color=models.CharField(max_length=100,default='CONFORME')
    pH_value=models.CharField(max_length=50,default='7.0',choices=ph_value)
    micro_biology_activity_res=models.CharField(max_length=100,default='35',choices=micr_bioloy_activity)
  



    Microbiological_state=models.CharField(max_length=250,default='CONFORME')

    Escherichia_coli_ATCC_25922_Antibiotic=models.CharField(max_length=250,default="Ampicillin 10 ug")                                        
    Ampicillin_10_ug_zone_size=models.CharField(max_length=250,default="19 mm", choices=Ampicillin_10_ug_zone_size_chioce)
    
    Staphylococcus_aureus_ATCC_29213_Antiboitic=models.CharField(max_length=250,default='Linezolid 10μg')
    Linezolid_10μg_zone_size=models.CharField(max_length=250,default="23 mm", choices=Linezolid_10μg_zone_size_choice)

    Pseudomonas_aeruginosa_ATCC_27853_Antiboitic=models.CharField(max_length=250,default='Ciprofloxacin 15μg')
    Ciprofloxacin_15μg_zone_size=models.CharField(max_length=250,default="32 mm", choices=Ciprofloxacin_15μg_zone_size_choice)

    Enterococcus_faecalis_ATCC_29212_Antiboitic=models.CharField(max_length=250,default='Trimethoprim sulfamethoxazole 1.25/23.μg \n & Vancomycin 5μg')
    Trimethoprim_sulfamethoxazole_125_23_μg_zone_size=models.CharField(max_length=250,default="19 mm", choices=Trimethoprim_sulfamethoxazole_125_23_μg_zone_size_choice)
    Vancomycin_5μg_zone_size    =models.CharField(max_length=250,default="30 mm", choices=Vancomycin_5μg_zone_size_choice)
  
    def __str__(self):
        return f"{self.Lot_No}"