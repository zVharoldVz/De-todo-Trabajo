from django.core.exceptions import ValidationError,MaxValueValidator

class MaxLengthIntegerValidator(MaxValueValidator):
    def __init__(self, length):
        max_value = 10**length-1
        super(MaxLengthIntegerValidator, self).__init__(max_value)