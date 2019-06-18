from django.db import models

# Create your models here.
 # add this
class Todo(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)

  def _str_(self):
    return self.title

class Shopping(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	price = models.FloatField()
	dateCreated = models.DateTimeField()
	in_stock = models.BooleanField(default=True)

	def _str_(self):
		return self.title