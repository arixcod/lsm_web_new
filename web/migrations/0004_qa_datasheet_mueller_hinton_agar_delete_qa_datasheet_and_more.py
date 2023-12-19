# Generated by Django 4.2.7 on 2023-12-05 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_qa_datasheet_first_mueller_hinton_agar_escherichia_coli_atcc_25922_res_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='qa_datasheet_mueller_hinton_agar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Material_code', models.CharField(default='MP06', max_length=50)),
                ('Lot_No', models.CharField(default='MP0651223', max_length=100)),
                ('mfg_data', models.DateField(default=datetime.datetime.now)),
                ('Expiry_date', models.DateField(default=datetime.datetime.now)),
                ('Appearance_res', models.CharField(default='CONFORME', max_length=150)),
                ('Appearance_theory', models.CharField(editable=False, max_length=150)),
                ('color_res', models.CharField(default='CONFORME', max_length=100)),
                ('color_theory', models.CharField(editable=False, max_length=100)),
                ('pH_value', models.CharField(choices=[('7', '7'), ('7.1', '7.1'), ('7.2', '7.2'), ('7.3', '7.3'), ('7.4', '7.4'), ('7.5', '7.5'), ('7.6', '7.6')], default='7.0', max_length=50)),
                ('micro_biology_activity_res', models.CharField(choices=[('33', '33'), ('34', '34'), ('35', '35'), ('36', '36'), ('37', '37')], default='35', max_length=100)),
                ('Microbiological_state', models.CharField(default='CONFORME', max_length=250)),
                ('Escherichia_coli_ATCC_25922_Antibiotic', models.CharField(default='Ampicillin 10 ug', max_length=250)),
                ('Ampicillin_10_ug_zone_size', models.CharField(choices=[('16 mm', '16 mm'), ('17 mm', '17 mm'), ('18 mm', '18 mm'), ('19 mm', '19 mm'), ('20 mm', '20 mm'), ('21 mm', '21 mm'), ('22 mm', '22 mm')], default='16 mm', max_length=250)),
                ('Staphylococcus_aureus_ATCC_29213_Antiboitic', models.CharField(default='Linezolid 10μg', max_length=250)),
                ('Linezolid_10μg_zone_size', models.CharField(choices=[('21 mm', '21 mm'), ('22 mm', '22 mm'), ('23 mm', '23 mm'), ('24 mm', '24 mm'), ('25 mm', '25 mm'), ('26 mm', '26 mm'), ('27 mm', '27 mm')], default='16 mm', max_length=250)),
                ('Pseudomonas_aeruginosa_ATCC_27853_Antiboitic', models.CharField(default='Ciprofloxacin 15μg', max_length=250)),
                ('Ciprofloxacin_15μg_zone_size', models.CharField(choices=[('25 mm', '25 mm'), ('26 mm', '26 mm'), ('27 mm', '27 mm'), ('28 mm', '28 mm'), ('29 mm', '29 mm'), ('30 mm', '30 mm'), ('31 mm', '31 mm'), ('22 mm', '32 mm'), ('33 mm', '33 mm')], default='16 mm', max_length=250)),
                ('Enterococcus_faecalis_ATCC_29212_Antiboitic', models.CharField(default='Trimethoprim sulfamethoxazole 1.25/23.μg \n & Vancomycin 5μg', max_length=250)),
                ('Trimethoprim_sulfamethoxazole_125_23_μg_zone_size', models.CharField(choices=[('15 mm', '15 mm'), ('16 mm', '16 mm'), ('17 mm', '17 mm'), ('18 mm', '18 mm'), ('19 mm', '19 mm'), ('20 mm', '20 mm'), ('21 mm', '21 mm')], default='16 mm', max_length=250)),
                ('Vancomycin_5μg_zone_size', models.CharField(choices=[('26 mm', '26 mm'), ('27 mm', '27 mm'), ('28 mm', '28 mm'), ('29 mm', '29 mm'), ('30 mm', '30 mm'), ('31 mm', '31 mm'), ('22 mm', '32 mm'), ('33 mm', '33 mm'), ('34 mm', '34 mm')], default='16 mm', max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='qa_datasheet',
        ),
        migrations.DeleteModel(
            name='qa_datasheet_first_mueller_hinton_agar',
        ),
    ]
