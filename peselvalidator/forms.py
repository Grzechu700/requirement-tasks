from django import forms
from .pesel_validator import validate_pesel


class PeselForm(forms.Form):
    """
    Form for PESEL number validation.

    Validates PESEL format, checksum, and extracts birth date and gender.
    """

    pesel = forms.CharField(
        label="PESEL Number",
        max_length=11,
        min_length=11,
        required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "00000000000",
            "class": "form-control",
        })
    )

    def clean_pesel(self):
        pesel = self.cleaned_data["pesel"]
        result = validate_pesel(pesel)

        if not result["valid"]:
            raise forms.ValidationError(result["error"])

        return pesel
