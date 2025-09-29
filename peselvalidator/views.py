from django.shortcuts import render
from .forms import PeselForm
from .pesel_validator import validate_pesel


def pesel_validate_view(request):
    if request.method == "POST":
        form = PeselForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data["pesel"]
            result = validate_pesel(pesel)
            context = {
                "form": form,
                "title": "PESEL Validation Result",
                "result": result
            }
            return render(request, "pesel_form.html", context)
        else:
            context = {
                "form": form,
                "title": "Pesel Validator",
            }
            return render(request, "pesel_form.html", context)
    else:
        form = PeselForm()
        context = {
            "form": form,
            "title": "Pesel Validator",
            "description": "Enter PESEL number to validate."
        }
        return render(request, "pesel_form.html", context)
