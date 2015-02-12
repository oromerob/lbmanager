from django.db import models
from datetime import datetime
from django.db.models.signals import post_save, post_delete
from django.contrib.admin.models import LogEntry

class ConfigDefaultAdmin(models.Model):
    enabled = models.BooleanField(default=True)
    def __unicode__(self):
        return u"%s" % self.name

class Server(ConfigDefaultAdmin):
    name = models.CharField(max_length=200)
    address = models.IPAddressField()
    ssh_user = models.CharField(max_length=200,null=True,blank=True)
    ssh_password = models.CharField(max_length=200,null=True,blank=True)
    ssh_port = models.IntegerField(default=22,null=True,blank=True)
    role_cluster = models.BooleanField(default=False)
    role_backend = models.BooleanField(default=False)
    role_frontend = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(Server, self).save(*args, **kwargs)
        group = Group.objects.get(pk=1)
        group.db_update()

    class Meta:
        verbose_name = 'Server'

class Group(ConfigDefaultAdmin):
    name = models.CharField(max_length=200)
    temp_dir = models.CharField(max_length=200)
    nginx_dir = models.CharField(max_length=200)
    ldirectord_conf = models.CharField(max_length=200)
    graph_dir = models.CharField(max_length=200)
    varnish_dir = models.CharField(max_length=200)
    cluster_servers = models.ManyToManyField(Server,null=True,blank=True)
    admin_port = models.IntegerField(default=8000,null=True,blank=True)
    app_path = models.CharField(max_length=200,default='/usr/local/src/lbmanager')
    enable_transfer = models.BooleanField(default=True)
    enable_reload = models.BooleanField(default=True)
    last_update = models.DateTimeField(null=True,blank=True)
    last_apply = models.DateTimeField(null=True,blank=True)
    version = models.IntegerField(default=0)

    def __unicode__(self):
        return u"%s" % (self.group.name)

    def db_update(self, save = True):
        self.version += 1
        self.last_update = datetime.now()
        if save: self.save()

    def apply(self):
        self.last_apply = datetime.now()
        self.save()

    class Meta:
        verbose_name = 'Group'

def db_update(sender, **kwargs):
    if sender in [ Group, LogEntry ]: save = False
    else: save = True
    group = Group.objects.get(pk=1)
    group.db_update( save = save )

post_save.connect(db_update, dispatch_uid = 'db_update')
post_delete.connect(db_update, dispatch_uid = 'db_update')
