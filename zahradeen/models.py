from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
   name = models.CharField(max_length=50)
   slug = models.SlugField()
   parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True , related_name='children')

   class Meta:
      unique_together = ('slug', 'parent',)    
      verbose_name_plural = "categories"     

   def __str__(self):                           
      full_path = [self.name]                  
      k = self.parent
      while k is not None:
            full_path.append(k.name)
            k = k.parent
      return ' -> '.join(full_path[::-1])
     
     
class Portfolio(models.Model):
   name = models.CharField(max_length=50)
   slug = models.SlugField(unique=True)
   long_title = models.CharField( null=True, blank=True, max_length=100)
   description = RichTextField(null=True, blank=True,)
   image = models.ImageField(upload_to="portfolio_img")
   category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)
   client = models.CharField(max_length=50, blank=True, null=True)
   page_url = models.URLField(blank=True, null=True)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return self.name
   
   def get_absolute_url(self):
      return reverse("project-detail", kwargs={
         'pk': self.pk,
         'slug': self.slug,
      })
   
   
def image_upload_to(instance, filename):
   name = instance.portfolio.name
   slug = slugify(name)
   return 'project_img/%s/%s' %(slug, filename)
   
class ProjectImage(models.Model):
   portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
   image = models.ImageField(upload_to=image_upload_to)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   