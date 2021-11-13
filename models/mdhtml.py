from typing import Optional
from pydantic import BaseModel


class HTMLStr(BaseModel):
    html: str
