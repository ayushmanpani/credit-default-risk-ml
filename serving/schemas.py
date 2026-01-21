from pydantic import BaseModel
from typing import Optional


class CreditApplication(BaseModel):
    # ===============================
    # Core client-provided features
    # ===============================
    NAME_CONTRACT_TYPE: Optional[str] = None
    CODE_GENDER: Optional[str] = None
    FLAG_OWN_CAR: Optional[str] = None
    FLAG_OWN_REALTY: Optional[str] = None

    CNT_CHILDREN: Optional[int] = None
    CNT_FAM_MEMBERS: Optional[int] = None

    AMT_INCOME_TOTAL: float
    AMT_CREDIT: float
    AMT_GOODS_PRICE: Optional[float] = None

    NAME_TYPE_SUITE: Optional[str] = None
    NAME_INCOME_TYPE: Optional[str] = None
    NAME_EDUCATION_TYPE: Optional[str] = None
    NAME_FAMILY_STATUS: Optional[str] = None
    NAME_HOUSING_TYPE: Optional[str] = None
    OCCUPATION_TYPE: Optional[str] = None

    DAYS_BIRTH: int
    DAYS_EMPLOYED: int
    DAYS_LAST_PHONE_CHANGE: Optional[int] = None
    OWN_CAR_AGE: Optional[float] = None

    # ===============================
    # Contact & communication flags
    # ===============================
    FLAG_MOBIL: Optional[int] = None
    FLAG_EMP_PHONE: Optional[int] = None
    FLAG_WORK_PHONE: Optional[int] = None
    FLAG_CONT_MOBILE: Optional[int] = None
    FLAG_PHONE: Optional[int] = None
    FLAG_EMAIL: Optional[int] = None

    # ===============================
    # Internal system-set features
    # ===============================
    AMT_ANNUITY: Optional[float] = None
    ORGANIZATION_TYPE: Optional[str] = None
    WEEKDAY_APPR_PROCESS_START: Optional[str] = None
    HOUR_APPR_PROCESS_START: Optional[int] = None

    REG_REGION_NOT_LIVE_REGION: Optional[int] = None
    REG_REGION_NOT_WORK_REGION: Optional[int] = None
    LIVE_REGION_NOT_WORK_REGION: Optional[int] = None

    REG_CITY_NOT_LIVE_CITY: Optional[int] = None
    REG_CITY_NOT_WORK_CITY: Optional[int] = None
    LIVE_CITY_NOT_WORK_CITY: Optional[int] = None

    # ===============================
    # Static third-party reference features
    # ===============================
    REGION_POPULATION_RELATIVE: Optional[float] = None
    REGION_RATING_CLIENT: Optional[int] = None
    REGION_RATING_CLIENT_W_CITY: Optional[int] = None

    # ---- Housing / property (AVG) ----
    APARTMENTS_AVG: Optional[float] = None
    BASEMENTAREA_AVG: Optional[float] = None
    YEARS_BEGINEXPLUATATION_AVG: Optional[float] = None
    YEARS_BUILD_AVG: Optional[float] = None
    COMMONAREA_AVG: Optional[float] = None
    ELEVATORS_AVG: Optional[float] = None
    ENTRANCES_AVG: Optional[float] = None
    FLOORSMAX_AVG: Optional[float] = None
    FLOORSMIN_AVG: Optional[float] = None
    LANDAREA_AVG: Optional[float] = None
    LIVINGAPARTMENTS_AVG: Optional[float] = None
    LIVINGAREA_AVG: Optional[float] = None
    NONLIVINGAPARTMENTS_AVG: Optional[float] = None
    NONLIVINGAREA_AVG: Optional[float] = None

    # ---- Housing / property (MODE) ----
    APARTMENTS_MODE: Optional[float] = None
    BASEMENTAREA_MODE: Optional[float] = None
    YEARS_BEGINEXPLUATATION_MODE: Optional[float] = None
    YEARS_BUILD_MODE: Optional[float] = None
    COMMONAREA_MODE: Optional[float] = None
    ELEVATORS_MODE: Optional[float] = None
    ENTRANCES_MODE: Optional[float] = None
    FLOORSMAX_MODE: Optional[float] = None
    FLOORSMIN_MODE: Optional[float] = None
    LANDAREA_MODE: Optional[float] = None
    LIVINGAPARTMENTS_MODE: Optional[float] = None
    LIVINGAREA_MODE: Optional[float] = None
    NONLIVINGAPARTMENTS_MODE: Optional[float] = None
    NONLIVINGAREA_MODE: Optional[float] = None

    # ---- Housing / property (MEDI) ----
    APARTMENTS_MEDI: Optional[float] = None
    BASEMENTAREA_MEDI: Optional[float] = None
    YEARS_BEGINEXPLUATATION_MEDI: Optional[float] = None
    YEARS_BUILD_MEDI: Optional[float] = None
    COMMONAREA_MEDI: Optional[float] = None
    ELEVATORS_MEDI: Optional[float] = None
    ENTRANCES_MEDI: Optional[float] = None
    FLOORSMAX_MEDI: Optional[float] = None
    FLOORSMIN_MEDI: Optional[float] = None
    LANDAREA_MEDI: Optional[float] = None
    LIVINGAPARTMENTS_MEDI: Optional[float] = None
    LIVINGAREA_MEDI: Optional[float] = None
    NONLIVINGAPARTMENTS_MEDI: Optional[float] = None
    NONLIVINGAREA_MEDI: Optional[float] = None

    # ---- Property classification ----
    FONDKAPREMONT_MODE: Optional[str] = None
    HOUSETYPE_MODE: Optional[str] = None
    TOTALAREA_MODE: Optional[float] = None
    WALLSMATERIAL_MODE: Optional[str] = None
    EMERGENCYSTATE_MODE: Optional[str] = None

    # ===============================
    # Document flags
    # ===============================
    FLAG_DOCUMENT_2: Optional[int] = None
    FLAG_DOCUMENT_3: Optional[int] = None
    FLAG_DOCUMENT_4: Optional[int] = None
    FLAG_DOCUMENT_5: Optional[int] = None
    FLAG_DOCUMENT_6: Optional[int] = None
    FLAG_DOCUMENT_7: Optional[int] = None
    FLAG_DOCUMENT_8: Optional[int] = None
    FLAG_DOCUMENT_9: Optional[int] = None
    FLAG_DOCUMENT_10: Optional[int] = None
    FLAG_DOCUMENT_11: Optional[int] = None
    FLAG_DOCUMENT_12: Optional[int] = None
    FLAG_DOCUMENT_13: Optional[int] = None
    FLAG_DOCUMENT_14: Optional[int] = None
    FLAG_DOCUMENT_15: Optional[int] = None
    FLAG_DOCUMENT_16: Optional[int] = None
    FLAG_DOCUMENT_17: Optional[int] = None
    FLAG_DOCUMENT_18: Optional[int] = None
    FLAG_DOCUMENT_19: Optional[int] = None
    FLAG_DOCUMENT_20: Optional[int] = None
    FLAG_DOCUMENT_21: Optional[int] = None
