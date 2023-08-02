from enum import Enum


class RegExEnum(Enum):
    BRAND = (
        r'^[A-Z][a-zA-Z\d]{1,24}$',
        'First letter uppercase, min 2 max 25 characters'
    )
    PASSWORD = (
        r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=(?:.*[`~!@#$%^&*()\-_+=\\\|\'\"\;\:\/?.>,<\[\]\{\}]){2,})[a-zA-Z\d`~!@#$%^&*()\-_+=\\\|\'\"\;\:\/?.>,<\[\]\{\}]{8,30}$',
        [
            'min 1 lowercase',
            'min 1 uppercase',
            'min 2 digits',
            'min 1 special character',
            'length 8-30 characters'
        ]
    )
    NAME = (
        r'^[А-ЯЁІЇЄҐ][А-яёЁіІїЇєЄґҐ]{1,49}$',
        [
            'Only cyrillic',
            'First letter uppercase',
            'Length 2-50 characters'

        ]
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
