from marvel_wiki.domain.movie import (
    getMoviesFilter,
    getMoviesRes,
    postMovieData,
    postMovieRes,
    putMovieData,
    putMovieRes,
)

from marvel_wiki.models import Movie
from django.db import transaction
from rest_framework.exceptions import NotFound

class MovieRepos:
    def get_movies(self, filter: getMoviesFilter) -> getMoviesRes:
        records = Movie.objects.all()
        return getMoviesRes.build(records[filter.offset-1:filter.offset-1+filter.limit], len(records))
    
    def insert_movie(self, data: postMovieData) -> postMovieRes:
        with transaction.atomic():
            record = Movie.objects.create(
                title=data.title,
                summary=data.summary,
                published_at=data.published_at
            )
            return postMovieRes.from_orm(record)
    
    def update_movie(self, data: putMovieData) -> putMovieRes:
        record: Movie = Movie.objects.filter(id=data.id).first()
        if not record:
            raise NotFound
        
        with transaction.atomic():
            record.title = data.title
            record.summary = data.summary
            record.published_at = data.published_at
            record.save()
            
            return putMovieRes.from_orm(record)
    
    def delete_movie(self, id: int):
        record: Movie = Movie.objects.filter(id=id).first()
        if not record:
            raise NotFound
        
        record.delete()

movie_repos = MovieRepos()