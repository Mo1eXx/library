from dataclasses import dataclass


@dataclass
class Book:
    '''Базовый класс для всех книг.'''
    title: str
    author: str
    year: int
    status: bool = True
    id: int = 1
