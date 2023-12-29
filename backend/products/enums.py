from enum import IntEnum


class ProductEnums(IntEnum):
    TITLE_MAX_LEN = 64
    TITLE_MIN_LEN = 2
    DESCRIPTION_MAX_LEN = 4096
    PRICE_MAX_DIGITS = 10
    PRICE_DECIMAL_PLACES = 2
    MEASUREMENT_UNIT_MAX_LEN = 16


class BrandEnums(IntEnum):
    TITLE_MAX_LEN = 128
    TITLE_MIN_LEN = 2
    DESCRIPTION_MAX_LEN = 4096
