from pydantic import BaseModel, Field, field_validator
import datetime

# Schema for movies
class Movie(BaseModel):
    id: int
    name: str
    overview: str
    year: int
    rating: float
    category: str

    class Config():
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "The Walking dead",
                "overview": "A group of survivors must band together to stay alive in a post-apocalyptic world.",
                "year": 2010,
                "rating": 8.1,
                "category": "Horror"
            }
        }

# Schema for movie updated
class MovieUpdate(BaseModel):
    name: str
    overview: str
    year: int
    rating: float
    category: str

    class Config():
        json_schema_extra = {
            "example": {
                "name": "The Walking dead",
                "overview": "A group of survivors must band together to stay alive in a post-apocalyptic world.",
                "year": 2010,
                "rating": 8.1,
                "category": "Horror"
            }
        }

# Schema for movie create
class MovieCreate(BaseModel):
    name: str = Field(min_length=5, max_length=20, default='My movie')
    overview: str = Field(min_length=20, max_length=200)
    year: int = Field(ge=1900, le=datetime.date.today().year)
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=3, max_length=15)

    # gt greater than = mayor que.
    # ge greater than or equal to = mayor o igual que.
    # lt less than = menor que.
    # le less than or equal = menor que o igual.

    class Config():
        json_schema_extra = {
            "example": {
                "name": "The Walking dead",
                "overview": "A group of survivors must band together to stay alive in a post-apocalyptic world.",
                "year": 2010,
                "rating": 8.1,
                "category": "Horror"
            }
        }

    @field_validator('name')
    def validate(cls, value):
        if len(value) < 5:
            raise ValueError("Name must be at least 5 characters long")
        return value
        