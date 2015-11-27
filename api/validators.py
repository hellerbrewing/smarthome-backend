from django.core.exceptions import ValidationError

def removeJavascriptKeyword(value):
    if "javascript:" in value:
        raise ValidationError('sting contains javascript')
