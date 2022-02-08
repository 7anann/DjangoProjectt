from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
from django.db.models import Avg
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


# Create your views here.


# home views

def index(request):
    projects = Project.objects.all()
    ProjectRate = Project.objects.annotate(avg=Avg("rate__rate")).order_by('-avg')[:5]
    lastProject = Project.objects.order_by('-id')[:5]
    featureProjects = FeatureProjects.objects.all()
    categories = Categories.objects.all()
    context = {
        "projects": projects,
        "ProjectRate": ProjectRate,
        "lastProject": lastProject,
        "featureProjects": featureProjects,
        "categories": categories
    }
    return render(request, "projects/projectHome.html", context)


def view(request, cid):
    projects = get_object_or_404(Categories, id=cid)
    categories = Categories.objects.all()
    context = {
        "projects": projects.project,
        "categories": categories,
        "categoryName": projects.name
    }

    return render(request, "projects/view.html", context)


def search(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        mode = form.cleaned_data.get("mode")
        searching = form.cleaned_data.get("search")
        if mode == "1":
            projects = ProjectTage.objects.filter(tage=searching)
            if projects:
                projects = projects[0].project_all()
        else:
            projects = Project.objects.filter(title=searching)
    categories = Categories.objects.all()
    context = {
        "projects": projects,
        "categories": categories,
        "categieName": searching
    }
    return render(request, "projects/view.html", context)


def details(request, pid):
    categories = Categories.objects.all()
    project = get_object_or_404(Project, id=pid)

    context = {
        "categories": categories,
        "images": project.allImage(),
        "project": project,
        "relativesProject": project.relativeProject(),
        "commentcount": project.comments().count()
    }
    return render(request, "projects/details.html", context)



