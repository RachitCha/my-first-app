from django.db import models

# Create your models here.
class NationalNew(models.Model):

	news_heading = models.CharField(max_length = 600)
	news_subheading = models.CharField(max_length = 600, null = True, blank = True)
	news_paragraph_1 = models.TextField(null = True, blank = True)
	news_paragraph_2 = models.TextField(null = True, blank = True)
	news_paragraph_3 = models.TextField(null = True, blank = True)
	designed_paragraph = models.TextField(null = True, blank = True)
	news_photo = models.ImageField(upload_to = 'national_pic/', null = True, blank = True)
	news_video = models.FileField(upload_to = 'national_video/', null = True, blank = True)
	want_this_news_as_front_news = models.BooleanField()
	want_this_news_in_national_news_section = models.BooleanField()
	want_this_news_as_main_news = models.BooleanField()

	def __str__(self):
		return self.news_heading


class StateNew(models.Model):

	news_heading = models.CharField(max_length = 600)
	news_subheading = models.CharField(max_length = 600, null = True, blank = True)
	news_paragraph_1 = models.TextField(null = True, blank = True)
	news_paragraph_2 = models.TextField(null = True, blank = True)
	news_paragraph_3 = models.TextField(null = True, blank = True)
	designed_paragraph = models.TextField(null = True, blank = True)
	news_photo = models.ImageField(upload_to = 'state_pic/', null = True, blank = True)
	news_video = models.FileField(upload_to = 'state_video/', null = True, blank = True)
	want_this_news_as_front_news = models.BooleanField()
	want_this_news_in_state_news_section = models.BooleanField()
	want_this_news_as_main_news = models.BooleanField()

	def __str__(self):
		return self.news_heading


class HoshangabadNew(models.Model):

	news_heading = models.CharField(max_length = 600)
	news_subheading = models.CharField(max_length = 600, null = True, blank = True)
	news_paragraph_1 = models.TextField(null = True, blank = True)
	news_paragraph_2 = models.TextField(null = True, blank = True)
	news_paragraph_3 = models.TextField(null = True, blank = True)
	designed_paragraph = models.TextField(null = True, blank = True)
	news_photo = models.ImageField(upload_to = 'district_pic/', null = True, blank = True)
	news_video = models.FileField(upload_to = 'district_video/', null = True, blank = True)
	want_this_news_as_front_news = models.BooleanField()
	want_this_news_in_hoshangabad_news_section = models.BooleanField()
	want_this_news_as_main_news = models.BooleanField()

	def __str__(self):
		return self.news_heading


class SeoniNew(models.Model):

	news_heading = models.CharField(max_length = 600)
	news_subheading = models.CharField(max_length = 600, null = True, blank = True)
	news_paragraph_1 = models.TextField(null = True, blank = True)
	news_paragraph_2 = models.TextField(null = True, blank = True)
	news_paragraph_3 = models.TextField(null = True, blank = True)
	designed_paragraph = models.TextField(null = True, blank = True)
	news_photo = models.ImageField(upload_to = 'seoni_pic/', null = True, blank = True)
	news_video = models.FileField(upload_to = 'seoni_video/', null = True, blank = True)
	want_this_news_as_front_news = models.BooleanField()
	want_this_news_in_seoni_news_section = models.BooleanField()
	want_this_news_as_main_news = models.BooleanField()

	def __str__(self):
		return self.news_heading


class FrontNew(models.Model):

	news_heading = models.CharField(max_length = 600)
	news_subheading = models.CharField(max_length = 600, null = True, blank = True)
	news_paragraph_1 = models.TextField(null = True, blank = True)
	news_paragraph_2 = models.TextField(null = True, blank = True)
	news_paragraph_3 = models.TextField(null = True, blank = True)
	designed_paragraph = models.TextField(null = True, blank = True)
	news_photo = models.ImageField(upload_to = 'front_pic/', null = True, blank = True)
	news_video = models.FileField(upload_to = 'front_video/', null = True, blank = True)

	def __str__(self):
		return self.news_heading


class RochakNew(models.Model):

	news_heading = models.CharField(max_length = 600)
	news_subheading = models.CharField(max_length = 600, null = True, blank = True)
	news_paragraph_1 = models.TextField(null = True, blank = True)
	news_paragraph_2 = models.TextField(null = True, blank = True)
	news_paragraph_3 = models.TextField(null = True, blank = True)
	designed_paragraph = models.TextField(null = True, blank = True)
	news_photo = models.ImageField(upload_to = 'rochak_pic/', null = True, blank = True)
	news_video = models.FileField(upload_to = 'rochak_video/', null = True, blank = True)
	want_this_news_as_front_news = models.BooleanField()

	def __str__(self):
		return self.news_heading


class TopNew(models.Model):

	news_heading = models.CharField(max_length = 200)

	def __str__(self):
		return self.news_heading

