from django.shortcuts import render

def dashboard(request):
    """
    Renders the main dashboard page.
    """
    context = {
        # Placeholders for now, will be populated by AI model later
    }
    return render(request, 'core/dashboard.html', context)
