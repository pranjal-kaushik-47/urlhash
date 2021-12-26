from djongo import models
from datetime import timedelta, date

from utils import encode

class Urls(models.Model):
    _id = models.ObjectIdField()
    record_id = models.IntegerField(unique=True)
    hash = models.CharField(unique=True, max_length=1000)
    long_url = models.URLField()
    created_at = models.DateField(auto_now_add=True)
    expires_in = models.DurationField(default=timedelta(days=365*3))
    expires_on = models.DateField(null=True, blank=True)
    limited = models.BooleanField(default=False)
    exhausted = models.BooleanField(default=False)

    def save(self):
        last = Urls.objects.last()
        if not last:
            self.record_id = 1
        else:
            self.record_id = last.record_id + 1
        super(Urls, self).save()
        if not self.hash:
            self.hash = encode(self.record_id)
            self.save()
        if not self.expires_on:
            self.expires_on = self.created_at + self.expires_in
            self.save()

    @classmethod
    def get_long_url(cls, hash):
        # queryset = cls.objects.filter(expires_on__gte=date.today(), exhausted=False)
        inst = cls.objects.get(expires_on__gte=date.today(), exhausted__in=[False], hash=hash)
        return inst, inst.long_url