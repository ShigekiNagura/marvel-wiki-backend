from __future__ import annotations
import typing as t
from pydantic import BaseModel
from marvel_wiki.models import Movie
from loguru import logger

class MovieItem(BaseModel):
    id: int
    title: str
    summary: str
    published_at: str
    
    @classmethod
    def get_mock(cls) -> MovieItem:
        return cls(**{
            "id": 1,
            "title": "アイアンマン",
            "summary": "トニースタークがアイアンマンとなり、自身の会社の開発した武器を悪用する敵を倒す",
            "published_at": "2008-09-27"
        })
    
    @classmethod
    def build(cls, record: Movie) -> MovieItem:
        return cls(**{
            "id": record.id,
            "title": record.title,
            "summary": record.summary,
            "published_at": record.published_at.strftime('%Y-%m-%d')
        })
    
class getMoviesRes(BaseModel):
    data: t.List[MovieItem]
    length: int
    
    @classmethod
    def get_mock(cls) -> getMoviesRes:
        return cls(**{
            "data": [MovieItem.get_mock()],
            "length": 1
        })
    
    @classmethod
    def build(cls, records: t.List[Movie], length: int) -> getMoviesRes:
        return cls(**{
            "data": [MovieItem.build(record) for record in records],
            "length": length
        })

class getMoviesFilter(BaseModel):
    offset: int
    limit: int
    

class postMovieData(BaseModel):
    title: str
    summary: str
    published_at: str
    

class postMovieRes(BaseModel):
    id: int
    title: str
    summary: str
    published_at: str
    
    @classmethod
    def get_mock(cls) -> postMovieRes:
        return cls(**{
            "id": 1,
            "title": "アイアンマン",
            "summary": "トニースタークがアイアンマンとなり、自身の会社の開発した武器を悪用する敵を倒す",
            "published_at": "2008-09-27"
        })
        
    class Config:
        orm_mode = True
        
class putMovieData(BaseModel):
    id: int
    title: str
    summary: str
    published_at: str
    

class putMovieRes(BaseModel):
    id: int
    title: str
    summary: str
    published_at: str
    
    @classmethod
    def get_mock(cls) -> putMovieRes:
        return cls(**{
            "id": 1,
            "title": "アイアンマン",
            "summary": "トニースタークがアイアンマンとなり、自身の会社の開発した武器を悪用する敵を倒す",
            "published_at": "2008-09-27"
        })
    
    class Config:
        orm_mode = True