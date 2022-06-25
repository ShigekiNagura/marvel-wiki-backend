from rest_framework.response import Response
from rest_framework.views import APIView

from marvel_wiki.use_case.blender import Blender


class SampleView(APIView):
    def get(self, request, format=None):
        print(Blender.TRANSFORMATION_MAP)
        return Response({"test": "test"})
