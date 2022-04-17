from urllib import response
from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.conf import settings
import requests

data_service_url = settings.DATA_SERVICE_URL


class BudgetHomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        minPrice = request.GET.get('minPrice', 0)
        maxPrice = request.GET.get('maxPrice', 100000000000000)

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

class SqftHomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        minSqft = request.GET.get('minSqft', 0)

        res = requests.post(data_service_url + '/query_data', json={
            "table": "home",
            "AND": [
                {
                    "column_name": "sqft_living",
                    "operator": "gte",
                    "value": minSqft
                }
            ]
        })

        if res.status_code == 200:
            return Response(res.json())
        else:
            return Response('error')

class AgeHomeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        year = request.GET.get('year', 0)

        res = requests.post(data_service_url + '/query_data', json={
            "table": "home",
            "OR": [
                {
                    "column_name": "yr_built",
                    "operator": "gte",
                    "value": year
                },
                {
                    "column_name": "yr_renovated",
                    "operator": "gte",
                    "value": year
                }
            ]
        })

        if res.status_code == 200:
            return Response(res.json())
        else:
            return Response('error')
