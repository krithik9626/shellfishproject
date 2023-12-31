# Generated by Django 4.0.3 on 2023-04-04 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shellfishapp', '0004_generalinformationinsert_lobster_imageinsert_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShrimpPrawnID', models.IntegerField()),
                ('ScientificName', models.CharField(max_length=500)),
                ('Image1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Image3', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'db_table': 'image',
            },
        ),
    ]
