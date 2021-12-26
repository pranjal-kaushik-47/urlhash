from short.models import Urls
from django.db.models import Q
from datetime import date

def delete_expired():
    print('------')
    expired = Urls.objects.filter(~Q(exhausted__in=[True]) | ~Q(expires_on__lt=date.today()))
    expired.delete()

