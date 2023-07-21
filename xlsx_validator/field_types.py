from PIL.Image import Image
from openpyxl.cell import Cell, ReadOnlyCell
from openpyxl.cell.read_only import EmptyCell
from openpyxl_image_loader import SheetImageLoader


class TextCell(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if v and not isinstance(v, (Cell, ReadOnlyCell, EmptyCell)):
            return v
        return v.value


class ImageCell(Image):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if v is None:
            return
        if v and not isinstance(v, (Cell, ReadOnlyCell, EmptyCell)):
            return v
        sheet = v.parent
        img_loader = SheetImageLoader(sheet)
        coord = f'{v.column_letter}{v.row}'
        if not img_loader.image_in(coord):
            return
        return img_loader.get(coord)

