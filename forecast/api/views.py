import datetime

from rest_framework.viewsets import ModelViewSet
# from .serializers import  DuLieu_ThoiTiet_Serializer
# from forecast.models import DuLieu_ThoiTiet
# from forecast.MoHinhDuDoan_all import chaymai,aloalo
# from forecast.MoHinhDuDoan_all import chaymai,aloalo
from datetime import date

class Forecast_HN(ModelViewSet):
    # serializer_class = DuLieu_ThoiTiet_Serializer
    def get_queryset(self):
        # chaymai()
        # date_hientai = date.today()
        # print(date_hientai)
        queryset = ['a', 1]
        # for i in range(6):
        #     date_hientai = date_hientai + datetime.timedelta(days=1)
        #     queryset = queryset | DuLieu_ThoiTiet.objects.filter(thoigian=date_hientai, id_thanhpho =1)
        return queryset