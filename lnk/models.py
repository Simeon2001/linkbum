from django.db import models
from django.contrib.auth.models import User



#profile info
class profile (models.Model):
    user = models.OneToOneField(User, blank=False, on_delete=models.CASCADE,related_name='profiles')
    pics = models.CharField(max_length=1000, blank=True,null=True)
    info = models.CharField(max_length=70, blank=True,null=True)

    def __str__(self):
        return self.user.username

    @property
    def blank(self):
        if self.pics == None and self.info == None:
            answer = True
            return answer
        else:
            answer = False
            return answer
    

# social media link
class Social_Media (models.Model):
    user = models.OneToOneField(profile, blank=False, on_delete=models.CASCADE,related_name='slinks')
    fbk = models.URLField(max_length=1000, blank=True, null=True)
    twr = models.URLField(max_length=1000, blank=True, null=True)
    ins = models.URLField(max_length=1000, blank=True, null=True)
    whp = models.URLField(max_length=1000, blank=True, null=True)
    snt = models.URLField(max_length=1000, blank=True, null=True)
    gtb = models.URLField(max_length=1000, blank=True, null=True)

    @property
    def empty(self):
        if self.fbk == None and self.twr == None and self.ins == None and self.whp == None and self.snt == None and self.gtb == None :
            answer = True
            return answer
        else:
            answer = False
            return answer


#links to things
class site_links (models.Model):
    users = models.ForeignKey(Social_Media, blank=False, on_delete=models.CASCADE, related_name='name')
    url_link  = models.URLField(max_length=1000, blank=False)
    details = models.TextField(max_length=30, blank=False)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.details



#links feedback
class feedback (models.Model):
    user = models.ForeignKey(site_links, blank=False, on_delete=models.CASCADE,related_name='feeds')
    msg = models.TextField(max_length=100,blank=False)
