import time

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class NamesView(APIView):
    def get(self, request):
        time.sleep(2)
        return Response([
            {'fname': 'Kim', 'lname': 'Kimov', 'qs': '2021-06-17 17:22:12'},
            {'fname': 'Kim 1', 'lname': 'Kimov 1', 'qs': '2021-06-12 11:56:43'},
            {'fname': 'Kim 2', 'lname': 'Kimov 2', 'qs': '2021-07-14 23:47:32'},
        ])

