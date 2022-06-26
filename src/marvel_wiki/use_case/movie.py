from marvel_wiki.domain.movie import (
    getMoviesFilter,
    getMoviesRes,
    postMovieData,
    postMovieRes,
    putMovieData,
    putMovieRes,
    deleteMovieRes
)
from marvel_wiki.repos.movie import movie_repos

class MovieUseCase:
    def get_movies(self, filter:getMoviesFilter) -> getMoviesRes:
        return movie_repos.get_movies(filter)
    
    def insert_movie(self, data: postMovieData) -> postMovieRes:
        return movie_repos.insert_movie(data)
    
    def update_movie(self, data: putMovieData) -> putMovieRes:
        return movie_repos.update_movie(data)
    
    def delete_movie(self, id: int) -> deleteMovieRes:
        return movie_repos.delete_movie(id)