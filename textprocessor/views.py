from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .text_processor import process_text


def upload_view(request):
    """
    Display the file upload form.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered template with the upload form.
    """

    form = UploadFileForm()
    context = {"form": form,
               "title": "Upload new text file",
               "description": "Upload a text file to be processed.",
               }

    return render(request, "home.html", context)


def process_view(request):
    """
    Process the uploaded text file and display results.

    Accepts POST requests with an uploaded file, processes the text by scrambling
    words, and displays the result. For non-POST requests, redirects to home.

    Args:
        request: The HTTP request object containing the uploaded file.

    Returns:
        Rendered template with processed text on success, or form with errors on failure.
        Redirects to home page for non-POST requests.
    """

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            text = file.read().decode("utf-8")
            processed_text = process_text(text)
            context = {
                "form": form,
                "title": "Processed text",
                "description": "Processed text from uploaded file.",
                "processed_text": processed_text,
            }
            return render(request, "processed.html", context)
        else:
            # TODO: Consider refactoring due to context duplication in upload_view.
            context = {
                "form": form,
                "title": "Upload new text file",
                "description": "Upload a text file to be processed.",
                "error_message": "Please correct the errors below.",
            }
            return render(request, "home.html", context)
    else:
        return redirect("home")
