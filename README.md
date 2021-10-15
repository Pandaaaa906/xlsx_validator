# Xlsx Validator

```
Thanks to pydantic, we got a nicer way to extra & validate rows from Excel files.
```


### 1. define a template model

```python
# templates.py
from typing import Optional

from pydantic import Field
from xlsx_validator import SheetTemplate, ImageCell


class ProductSheet(SheetTemplate):
    sku: Optional[str] = Field(alias='#SKU')
    img: Optional[ImageCell] = Field(alias='#IMG')  # Image also supported

```

### 2. Extract data

```python
from pathlib import Path
from xlsx_validator import validate_xlsx

from .templates import ProductSheet

fp = Path('/path/to/excel_file.xlsx')
for row in validate_xlsx(fp, ProductSheet):
    # do whatever you want to your row
    pass
```