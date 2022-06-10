from django.db import models
from django.contrib.auth.models import User


#profilde yer almasını istediğimiz kayıtlar
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #bolum_name = models.OneToOneField(User, on_delete=models.CASCADE)
    #fakulte_name = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.user} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
       # img = Image.open(self.image.path)
        
        #if img.height > 300 or img.width > 300:
        #     output_size = (300,300)
        #     img.thumbnail(output_size)
         #    img.save(self.image.path)


#class User(AbstractUser):
#    username = models.CharField(max_length = 50, blank = True, null = True, unique = True)
#    email = models.EmailField(_('email address'), unique = False)
#    phone_no = models.CharField(max_length = 10)
#    USERNAME_FIELD = 'email'
#    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
#    def __str__(self):
#      return "{}".format(self.email)
    
      
#      ROLE_CHOICES = (
#          (OGRENCI, 'Ogrenci'),
#          (AKADEMISYEN, 'Akademisyen'),
#      )
#      role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
      # You can create Role model separately and add ManyToMany if user has more than one role