# Generated by Django 3.1.3 on 2022-03-31 09:08

from django.db import migrations, models
import insta.fields


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_auto_20220331_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=insta.fields.ThumbnailImageField(default=1, upload_to='insta/%Y/%m', verbose_name='IMAGE'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(max_length=30, null=True, verbose_name='TITLE'),
        ),
    ]