from behave import given, then, when

from marvel_wiki.use_case.movie import MovieUseCase
from marvel_wiki.domain.movie import (
    getMoviesFilter,
    postMovieData,
    putMovieData
)

from loguru import logger
from django.db import connections

# Given
@given('ユースケースのインスタンス化')
def step_given_instance_use_case(context):
    # idをリセット
    with connections["default"].cursor() as cursor:
        cursor.execute("ALTER TABLE movie AUTO_INCREMENT=0;")
    context.uc = MovieUseCase()

# Then
@then('データを取得する')
def step_then_get_data(context):
    logger.debug(f"ret : {context.ret}")
    
    # 一つ多めにlogger.debugを記述しないとなぜかその前が表示されない
    logger.debug("a")
    assert bool(context.ret)


# When
@when("get_moviesを呼び出す")
def step_when_call_get_movies(context):
    context.filter = getMoviesFilter(**{
        "offset": 1,
        "limit": 25
    })
    uc: MovieUseCase = context.uc
    context.ret = uc.get_movies(context.filter)
    

@when("title={title}, summary={summary}, published_at={published_at}の映画情報を登録する")
def step_when_call_insert_movie(context, title, summary, published_at):
    data = postMovieData(**{
        "title": title,
        "summary": summary,
        "published_at": published_at
    })
    uc: MovieUseCase = context.uc
    context.ret = uc.insert_movie(data)
    

@when("update_movieを呼び出す")
def step_when_call_update_movie(context):
    data = putMovieData(**{
        "id": 2,
        "title": "アイアンマン2",
        "summary": "アイアンマンの2作品目",
        "published_at": "2010-05-07"
    })
    uc: MovieUseCase = context.uc
    context.ret = uc.update_movie(data)

@when("delete_movieを呼び出し、id={id}を削除")
def step_when_call_delete_movie(context, id):
    uc: MovieUseCase = context.uc
    context.ret = uc.delete_movie(id)