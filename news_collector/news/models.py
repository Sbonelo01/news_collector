from django.contrib.postgres.fields import ArrayField
from django.db import migrations, models

# Create your models here.
class Headline(models.Model):
  title = models.CharField(max_length=200, primary_key=True                                                                                                                                                                                 
    )
  image = models.URLField(null=True, blank=True)
  url = models.TextField()

  def __str__(self):
    return self.title[0]
    #return self.image[0]
    #return self.url[0]

# new_headline = Headline()
# new_headline.title = title
# new_headline.url = link
# new_headline.image = image_src
# new_headline.save()
