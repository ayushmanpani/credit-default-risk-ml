from pydantic import BaseModel
from typing import Optional

class CreditApplication(BaseModel):
    AMT_INCOME_TOTAL: float
    AMT_CREDIT: float
    AMT_ANNUITY: float
    DAYS_BIRTH: int
    DAYS_EMPLOYED: int
    CODE_GENDER: Optional[str] = None
    NAME_INCOME_TYPE: Optional[str] = None
    FLAG_OWN_CAR: Optional[str] = None
    FLAG_OWN_REALTY: Optional[str] = None
