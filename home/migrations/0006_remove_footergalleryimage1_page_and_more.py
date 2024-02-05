# Generated by Django 5.0.1 on 2024-01-29 20:30

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_footer1_footergalleryimage1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footergalleryimage1',
            name='page',
        ),
        migrations.RemoveField(
            model_name='footergalleryimage1',
            name='image',
        ),
        migrations.AlterField(
            model_name='footergalleryimage',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='footer_images', to='home.footer'),
        ),
        migrations.DeleteModel(
            name='Footer1',
        ),
        migrations.DeleteModel(
            name='FooterGalleryImage1',
        ),
    ]
