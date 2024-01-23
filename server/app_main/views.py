from constance import config
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import News, Social, Update
from .serializers import NewsSerializer, SocialSerializer, UpdateSerializer


@api_view()
def latest_version(request, locale: str):
    if locale == "EN":
        return Response({"version": config.LATEST_EN_VERSION})
    else:
        return Response({"version": config.LATEST_RU_VERSION})


class UpdateView(APIView):
    def get(self, request, locale, version):
        try:
            update_from = Update.objects.get(
                published=True, lang=locale, version=version
            )
            if request.GET.get("beta_key") == config.BETA_KEY:
                update = Update.objects.filter(
                    published=True, lang=locale, previous=update_from
                ).last()
            else:
                update = Update.objects.filter(
                    published=True, lang=locale, previous=update_from, beta=False
                ).last()
            if update:
                return Response(UpdateSerializer(update).data)
            else:
                return Response({})
        except Update.DoesNotExist:
            return Response({})


class NewsListView(ListAPIView):
    serializer_class = NewsSerializer

    def get_queryset(self):
        return News.objects.filter(published=True, lang=self.kwargs["locale"])


class SocialsListView(ListAPIView):
    queryset = Social.objects.filter(published=True)
    serializer_class = SocialSerializer
