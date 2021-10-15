# Xlsx Validator

```
Thanks to pydantic, we got a nicer way to extract & validate data from Excel files.
```


### 1. Define a template model

```python
# templates.py
from typing import Optional
from datetime import datetime

from pydantic import Field
from xlsx_validator import SheetTemplate, ImageCell


class ProductSheet(SheetTemplate):
    # using alias can easily handle header label
    sku: str = Field(alias='#SKU')
    created_at: Optional[datetime] = Field(alias='CreatedAt')
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