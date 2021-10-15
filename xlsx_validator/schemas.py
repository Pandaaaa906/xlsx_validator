from PIL.Image import Image
from openpyxl.cell import Cell, ReadOnlyCell
from openpyxl.cell.read_only import EmptyCell

from pydantic import BaseModel, validator


class SheetTemplate(BaseModel):
    @validator('*', pre=True)
    def trans_cell(cls, v):
        if not isinstance(v, (Cell, ReadOnlyCell, EmptyCell)):
            value = v
        else:
            value = v.value
        return value

    @validator('*')
    def default(cls, v, field):
        if v is None:
            return field.default
        return v

    class Config:
        validate_assignment = True


class ImageCell(Image):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if v is None:
            return
        if v and not isinstance(v, Image):
            raise ValueError(f'Not an Image: {v}')
        return v
