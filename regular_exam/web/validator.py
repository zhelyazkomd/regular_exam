from django.core.exceptions import ValidationError


def min_length_validator(value):
    MIN_VALUE_LENGTH = 2
    VALIDATION_ERROR_MESSAGE = f'The username must be a minimum of {MIN_VALUE_LENGTH} chars'
    if len(value) < MIN_VALUE_LENGTH:
        raise ValidationError(VALIDATION_ERROR_MESSAGE)


def min_and_max_year_validation(value):
    MAX_YEAR_OLD = 2049
    MIN_YEAR_OLD = 1980
    VALIDATION_ERROR_MESSAGE = f'Year must be between {MIN_YEAR_OLD} and {MAX_YEAR_OLD}'

    if int(value) < MIN_YEAR_OLD or int(value) > MAX_YEAR_OLD:
        raise ValidationError(VALIDATION_ERROR_MESSAGE)

def min_length_username(value):
    pass