from marvel_wiki.domain.movie import (
    getMoviesFilter,
    getMoviesRes,
    postMovieData,
    postMovieRes,
    putMovieData,
    putMovieRes,
    deleteMovieRes
)

class MovieRepos:
    def get_movies(self, filter: getMoviesFilter) -> getMoviesRes:
        return getMoviesRes.get_mock()
    
    def insert_movie(self, data: postMovieData) -> postMovieRes:
        return postMovieRes.get_mock()
    
    def update_movie(self, data: putMovieData) -> putMovieRes:
        return putMovieRes.get_mock()
    
    def delete_movie(self, id: int) -> deleteMovieRes:
        return deleteMovieRes.get_mock()

movie_repos = MovieRepos()