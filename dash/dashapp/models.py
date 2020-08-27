from django.db import models
import datetime
from django.utils import timezone
from django.utils.translation import ugettext, ugettext_lazy as _
from datetime import timedelta

STATUS_CHOICES = (
    ('act','Active'),
    ('inact','Inactive') 
)

# Create your models here.

class Visitor(models.Model):
    name = models.CharField(max_length=25)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,null=True)
    email = models.EmailField(default = None)
    page_visits = models.PositiveIntegerField(default=0)
    session_start = models.DateTimeField(null=True,default=timezone.now())
    last_update = models.DateTimeField(null=True,default=None)


    def __init__(self, *args, **kwargs):
        super(Visitor, self).__init__(*args, **kwargs)
        self.session_start = timezone.now()
        self.last_update = timezone.now()

    def _time_on_site(self):
        """
        Attempts to determine the amount of time a visitor has spent on the
        site based upon their information that's in the database.
        """
        if self.session_start:
            seconds = (self.last_update - self.session_start).seconds

            hours = seconds / 3600
            seconds -= hours * 3600
            minutes = seconds / 60
            seconds -= minutes * 60

            return u'%i:%02i:%02i' % (hours, minutes, seconds)
        else:
            return ugettext(u'unknown')
    time_on_site = property(_time_on_site)

    class Meta:
        verbose_name = 'Visitor'
        verbose_name_plural = 'Visitors'

    def __str__(self):
        return self.name


class UntrackedUserAgent(models.Model):
    keyword = models.CharField(_('keyword'), max_length=100, help_text=_('Part or all of a user-agent string.  For example, "Googlebot" here will be found in "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)" and that visitor will not be tracked.'))

    def __unicode__(self):
        return self.keyword

    class Meta:
        ordering = ('keyword',)
        verbose_name = _('Untracked User-Agent')
        verbose_name_plural = _('Untracked User-Agents')

class BannedIP(models.Model):
    ip_address = models.GenericIPAddressField('IP Address', help_text=_('The IP address that should be banned'))

    def __unicode__(self):
        return self.ip_address

    class Meta:
        ordering = ('ip_address',)
        verbose_name = _('Banned IP')
        verbose_name_plural = _('Banned IPs')

