from urllib import response
from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
import requests

data_service_url = settings.DATA_SERVICE_URL


class BudgetHomeView(APIView):
    def get(self, request):
        minPrice = request.GET.get('minPrice', 0)
        maxPrice = request.GET.get('maxPrice', 100000000000000)

        print(minPrice)
        print(maxPrice)
        res = requests.post(data_service_url + '/query_data', json={
            "table": "home",
            "AND": [
                {
                    "column_name": "price",
                    "operator": "gte",
                    "value": minPrice
                },
                {
                    "column_name": "price",
                    "operator": "lte",
                    "value": maxPrice
                }
            ]
        })

        if res.status_code == 200:
            return Response(res.json())
        else:
            return Response('error')
