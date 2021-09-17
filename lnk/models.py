from django.db import models
from django.contrib.auth.models import User



#profile info
class profile (models.Model):
    user = models.OneToOneField(User, blank=False, on_delete=models.CASCADE,related_name='profiles')
    pics = models.CharField(max_length=100, blank=True)
    info = models.CharField(max_length=70, blank=True)
    

# social media link
class Social_Media (models.Model):
    user = models.OneToOneField(profile, blank=False, on_delete=models.CASCADE,related_name='slinks')
    fbk = models.URLField(max_length=1000, blank=True)
    twr = models.URLField(max_length=1000, blank=True)
    ins = models.URLField(max_length=1000, blank=True)
    whp = models.URLField(max_length=1000, blank=True)
    snt = models.URLField(max_length=1000, blank=True)
    gtb = models.URLField(max_length=1000, blank=True)


#links to things
class site_links (models.Model):
    users = models.ForeignKey(profile, blank=False, on_delete=models.CASCADE, related_name='name')
    url_link  = models.URLField(max_length=1000, blank=False)
    details = models.TextField(max_length=30, blank=False)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.details



#links feedback
class feedback (models.Model):
    user = models.ForeignKey(site_links, blank=False, on_delete=models.CASCADE,related_name='feeds')
    msg = models.TextField(max_length=100,blank=False)
