from django.db.models import TextChoices


class GenderChoiceType(TextChoices):
    MALE = 'male', 'male'
    FEMALE = 'female', 'female'
    OTHER = 'other', 'other'
