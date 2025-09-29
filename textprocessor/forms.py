import django.forms


class UploadFileForm(django.forms.Form):
    """
    Form for uploading text files to be processed.

    Attributes:
        file: A file upload field that accepts text files for processing.
    """

    file = django.forms.FileField(label="Choose text file", required=True)
