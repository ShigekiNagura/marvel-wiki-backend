from __future__ import annotations
import typing as t
from pydantic import BaseModel

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
    
class getMoviesRes(BaseModel):
    data: t.List[MovieItem]
    length: int
    
    @classmethod
    def get_mock(cls) -> getMoviesRes:
        return cls(**{
            "data": [MovieItem.get_mock()],
            "length": 1
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

class deleteMovieData(BaseModel):
    id: int
    
class deleteMovieRes(BaseModel):
    success: bool
    
    @classmethod
    def get_mock(cls) -> deleteMovieRes:
        return cls(**{
            "success": True
        })