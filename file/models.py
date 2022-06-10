from django.db import models
# Create your models here.

# file sınıfı ve kaydedilmesini istediklerimiz
class File(models.Model):
    #user = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name='yazar')
    name = models.CharField(max_length=500, verbose_name="dersAdi")
    description = models.TextField(verbose_name="bolum")
    filepath= models.FileField(upload_to='files/', null=True, verbose_name="")
    pdf = models.FileField(upload_to='store/pdfs/')
    publishing_date = models.DateTimeField(verbose_name="Yayınlanma_Tarih")
    def __str__(self):
        return self.name + ": " + str(self.filepath)+ ": " + str(self.description)+ ": " + str(self.publishing_date)
    def delete(self, *args, **kwargs):
      self.pdf.delete()
      super().delete(*args, **kwargs)

#document sınıfı
class Document(models.Model):
    #user = models.OneToOneField("auth.user", on_delete=models.CASCADE)
    name = models.CharField(max_length=500, verbose_name="dersAdi")
    description = models.TextField(verbose_name="bolum")
    filepath= models.FileField(upload_to='files/', null=True, verbose_name="")
    pdf = models.FileField(upload_to='store/pdfs/')
    publishing_date = models.DateTimeField(verbose_name="Yayınlanma_Tarih")
    # fields of the model
    def __str__(self):
        return self.name + ": " + str(self.filepath) + ": " + str(self.description)+ ": " + str(self.publishing_date)


def user_directory_path(instance, filename):
  # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
  return 'user_{0}/{1}'.format(instance.user.id,filename)

class MyModel(models.Model):
 upload = models.FileField(upload_to=user_directory_path)

media = models.FileField(upload_to="media", null=True, blank=True)