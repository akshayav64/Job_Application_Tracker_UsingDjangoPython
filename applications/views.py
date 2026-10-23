from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Count
from .models import JobApplication
from .forms import ApplicationForm


@login_required
def dashboard(request):
    apps = JobApplication.objects.filter(user=request.user)
    q = request.GET.get('q')
    if q:
        apps = apps.filter(company__icontains=q)
    stats = apps.values('status').annotate(total=Count('id'))

    status_names = dict(JobApplication.STATUS_CHOICES)
    chart_data = {
        'labels': [status_names[s['status']] for s in stats],
        'values': [s['total'] for s in stats],
    }
    return render(request, 'applications/dashboard.html', {
        'apps': apps,
        'stats': stats,
        'chart_data': chart_data,
    })


@login_required
def add_application(request):
    form = ApplicationForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        return redirect('dashboard')
    return render(request, 'applications/form.html', {'form': form})


@login_required
def edit_application(request, pk):
    obj = get_object_or_404(JobApplication, pk=pk, user=request.user)
    form = ApplicationForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'applications/form.html', {'form': form})


@login_required
def delete_application(request, pk):
    obj = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == 'POST':
        obj.delete()
        return redirect('dashboard')
    return render(request, 'applications/confirm_delete.html', {'obj': obj})


def signup(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request, 'registration/signup.html', {'form': form})