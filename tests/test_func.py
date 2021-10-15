from datetime import datetime
from pathlib import Path
from typing import Optional
from unittest import TestCase

from pydantic import Field

from xlsx_validator import validate_xlsx, SheetTemplate, ImageCell


class TestSheet(SheetTemplate):
    text: Optional[str] = Field(alias='TextValue', default='default value')
    number: str = Field(alias='NumericValue')
    date: datetime = Field(alias='DateValue')
    img: Optional[ImageCell] = Field(alias='Image')


class Test(TestCase):
    def test_validate_xlsx(self):
        fp = Path('./samples/test.xlsx')
        for row in validate_xlsx(fp, TestSheet):
            print(row)
