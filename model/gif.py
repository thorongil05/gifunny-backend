from abc import ABC

class Gif(ABC):

    _name : str
    _url : str
    _rating : str
    _creator: str

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def url(self):
        return self._url
    
    @url.setter
    def url(self, value):
        self._url = value

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, value):
        self._rating = value

    @property
    def creator(self):
        return self._creator
    
    @creator.setter
    def creator(self, value):
        self._creator = value

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return f'{self.name} - {self.creator} - {self.url}'

    def __dict__(self) -> dict:
        return {
            'name': self.name,
            'url': self.url,
            'rating': self.rating,
            'creator': self.creator
        }