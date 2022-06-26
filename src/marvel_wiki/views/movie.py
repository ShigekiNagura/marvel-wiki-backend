from marvel_wiki.utils.exception_handler import handle_except
from rest_framework.views import APIView
from rest_framework.response import Response
from marvel_wiki.use_case.movie import MovieUseCase
from marvel_wiki.domain.movie import (
    getMoviesFilter,
    postMovieData,
    putMovieData
)
from rest_framework.exceptions import ParseError

class MovieView(APIView):
    def get(self, request, format=None):
        params = {
            "offset": int(request.query_params["offset"]),
            "limit": int(request.query_params["limit"])
        }
        with handle_except():
            filter = getMoviesFilter(**params)
            uc = MovieUseCase()
            ret = uc.get_movies(filter)
            return Response(ret.dict())
    
    def post(self, request, format=None):
        with handle_except():
            data = postMovieData(**request.data)
            uc = MovieUseCase()
            ret = uc.insert_movie(data)
            return Response(ret.dict())

class UpdateDeleteMovieView(APIView):
    def put(self, request, **kwargs):
        with handle_except():
            data = putMovieData(**{
                "id": int(kwargs["MovieId"]),
                **request.data
            })
            uc = MovieUseCase()
            ret = uc.update_movie(data)
            return Response(ret.dict())
        
    def delete(self, request, **kwargs):
        with handle_except():
            id = int(kwargs["MovieId"])
            uc = MovieUseCase()
            uc.delete_movie(id)
            return Response({
                "success": True
            })