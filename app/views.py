from django.shortcuts import render

def demand(request):
    return render(request, "demand.html")


def main(request):
    return render(request, "main.html")


def geography(request):
    return render(request, "geography.html")


def skills(request):
    return render(request, "skills.html")


def last_vacansies(request):
    return render(request, "last_vacancies.html")