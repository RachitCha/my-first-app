# Generated by Django 2.0.5 on 2020-04-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FrontNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_heading', models.CharField(max_length=600)),
                ('news_subheading', models.CharField(blank=True, max_length=600, null=True)),
                ('news_paragraph_1', models.TextField(blank=True, null=True)),
                ('news_paragraph_2', models.TextField(blank=True, null=True)),
                ('news_paragraph_3', models.TextField(blank=True, null=True)),
                ('designed_paragraph', models.TextField(blank=True, null=True)),
                ('news_photo', models.ImageField(blank=True, null=True, upload_to='front_pic/')),
                ('news_video', models.FileField(blank=True, null=True, upload_to='front_video/')),
            ],
        ),
        migrations.CreateModel(
            name='HoshangabadNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_heading', models.CharField(max_length=600)),
                ('news_subheading', models.CharField(blank=True, max_length=600, null=True)),
                ('news_paragraph_1', models.TextField(blank=True, null=True)),
                ('news_paragraph_2', models.TextField(blank=True, null=True)),
                ('news_paragraph_3', models.TextField(blank=True, null=True)),
                ('designed_paragraph', models.TextField(blank=True, null=True)),
                ('news_photo', models.ImageField(blank=True, null=True, upload_to='district_pic/')),
                ('news_video', models.FileField(blank=True, null=True, upload_to='district_video/')),
                ('want_this_news_as_front_news', models.BooleanField()),
                ('want_this_news_in_hoshangabad_news_section', models.BooleanField()),
                ('want_this_news_as_main_news', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='NationalNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_heading', models.CharField(max_length=600)),
                ('news_subheading', models.CharField(blank=True, max_length=600, null=True)),
                ('news_paragraph_1', models.TextField(blank=True, null=True)),
                ('news_paragraph_2', models.TextField(blank=True, null=True)),
                ('news_paragraph_3', models.TextField(blank=True, null=True)),
                ('designed_paragraph', models.TextField(blank=True, null=True)),
                ('news_photo', models.ImageField(blank=True, null=True, upload_to='national_pic/')),
                ('news_video', models.FileField(blank=True, null=True, upload_to='national_video/')),
                ('want_this_news_as_front_news', models.BooleanField()),
                ('want_this_news_in_national_news_section', models.BooleanField()),
                ('want_this_news_as_main_news', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='RochakNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_heading', models.CharField(max_length=600)),
                ('news_subheading', models.CharField(blank=True, max_length=600, null=True)),
                ('news_paragraph_1', models.TextField(blank=True, null=True)),
                ('news_paragraph_2', models.TextField(blank=True, null=True)),
                ('news_paragraph_3', models.TextField(blank=True, null=True)),
                ('designed_paragraph', models.TextField(blank=True, null=True)),
                ('news_photo', models.ImageField(blank=True, null=True, upload_to='rochak_pic/')),
                ('news_video', models.FileField(blank=True, null=True, upload_to='rochak_video/')),
                ('want_this_news_as_front_news', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='SeoniNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_heading', models.CharField(max_length=600)),
                ('news_subheading', models.CharField(blank=True, max_length=600, null=True)),
                ('news_paragraph_1', models.TextField(blank=True, null=True)),
                ('news_paragraph_2', models.TextField(blank=True, null=True)),
                ('news_paragraph_3', models.TextField(blank=True, null=True)),
                ('designed_paragraph', models.TextField(blank=True, null=True)),
                ('news_photo', models.ImageField(blank=True, null=True, upload_to='seoni_pic/')),
                ('news_video', models.FileField(blank=True, null=True, upload_to='seoni_video/')),
                ('want_this_news_as_front_news', models.BooleanField()),
                ('want_this_news_in_seoni_news_section', models.BooleanField()),
                ('want_this_news_as_main_news', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='StateNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_heading', models.CharField(max_length=600)),
                ('news_subheading', models.CharField(blank=True, max_length=600, null=True)),
                ('news_paragraph_1', models.TextField(blank=True, null=True)),
                ('news_paragraph_2', models.TextField(blank=True, null=True)),
                ('news_paragraph_3', models.TextField(blank=True, null=True)),
                ('designed_paragraph', models.TextField(blank=True, null=True)),
                ('news_photo', models.ImageField(blank=True, null=True, upload_to='state_pic/')),
                ('news_video', models.FileField(blank=True, null=True, upload_to='state_video/')),
                ('want_this_news_as_front_news', models.BooleanField()),
                ('want_this_news_in_state_news_section', models.BooleanField()),
                ('want_this_news_as_main_news', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TopNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_heading', models.CharField(max_length=200)),
            ],
        ),
    ]
