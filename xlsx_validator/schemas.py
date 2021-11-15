from PIL.Image import Image
from openpyxl.cell import Cell, ReadOnlyCell
from openpyxl.cell.read_only import EmptyCell

from pydantic import BaseModel, validator, root_validator


class SheetTemplate(BaseModel):
    @root_validator(pre=True)
    def trans_cell(cls, values):
        for k, v in values.items():
            if isinstance(v, (Cell, ReadOnlyCell, EmptyCell)):
                values[k] = v.value
        return values

    @validator('*', pre=True)
    def default(cls, v, field):
        if v is None:
            return field.get_default()
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
