from .models import Urls
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from os import getenv
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import datetime as dt


class GetRedirect(generics.GenericAPIView):
    """
        API to redirect to the long URL. Mark as exhausted if limited is true once redirected.
    """

    def get(self, *args, **kwargs):
        hash = kwargs.get('hash')
        try:
            inst, redirect_to = Urls.get_long_url(hash)
        except Urls.DoesNotExist:
            return JsonResponse({'detail': 'page not found'}, status=400)
        if inst.limited:
            inst.exhausted = True
            inst.save()
        return HttpResponseRedirect(redirect_to)


@method_decorator(csrf_exempt, name='dispatch')
class CreateNewShort(generics.GenericAPIView):
    """
        API to create new unique short url.
    """
    
    @swagger_auto_schema(request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                    'long_url': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="long url"
                        ),
                    'expires_in': openapi.Schema(
                        type=openapi.TYPE_STRING,
                        description="time in days"
                        ),
                    'limited': openapi.Schema(
                        type=openapi.TYPE_BOOLEAN,
                        description="if it can be used only once"
                        ),
                }),
        )
    def post(self, request):
        data = json.loads(request.body)
        long_url = data.get('long_url', False)
        expires_in = data.get('expires_in', None)
        limited = data.get('limited', False)

        if long_url:
            url = Urls(
                long_url=long_url,
                limited=limited
            )
            if expires_in:
                url.expires_in = dt.timedelta(days=int(expires_in))
            url.save()
            endpoint = reverse('short_url', kwargs={'hash':url.hash})
            return JsonResponse({'short': getenv('base') + endpoint}, status=201)
        else:
            return JsonResponse({'detail': 'long_url not passed'}, status=400)