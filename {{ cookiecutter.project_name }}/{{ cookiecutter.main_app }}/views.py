from django.shortcuts import render


def index(request):
    """ The view that will render the home page """
    return render(request, '{{ cookiecutter.main_app }}/home.html', context={})
