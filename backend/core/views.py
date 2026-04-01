import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Dashboard, Report, DataSource


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['dashboard_count'] = Dashboard.objects.count()
    ctx['dashboard_sales'] = Dashboard.objects.filter(category='sales').count()
    ctx['dashboard_marketing'] = Dashboard.objects.filter(category='marketing').count()
    ctx['dashboard_finance'] = Dashboard.objects.filter(category='finance').count()
    ctx['report_count'] = Report.objects.count()
    ctx['report_chart'] = Report.objects.filter(report_type='chart').count()
    ctx['report_table'] = Report.objects.filter(report_type='table').count()
    ctx['report_kpi'] = Report.objects.filter(report_type='kpi').count()
    ctx['datasource_count'] = DataSource.objects.count()
    ctx['datasource_database'] = DataSource.objects.filter(source_type='database').count()
    ctx['datasource_api'] = DataSource.objects.filter(source_type='api').count()
    ctx['datasource_csv'] = DataSource.objects.filter(source_type='csv').count()
    ctx['recent'] = Dashboard.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def dashboard_list(request):
    qs = Dashboard.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(category=status_filter)
    return render(request, 'dashboard_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def dashboard_create(request):
    if request.method == 'POST':
        obj = Dashboard()
        obj.name = request.POST.get('name', '')
        obj.category = request.POST.get('category', '')
        obj.owner = request.POST.get('owner', '')
        obj.widgets = request.POST.get('widgets') or 0
        obj.status = request.POST.get('status', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/dashboards/')
    return render(request, 'dashboard_form.html', {'editing': False})


@login_required
def dashboard_edit(request, pk):
    obj = get_object_or_404(Dashboard, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.category = request.POST.get('category', '')
        obj.owner = request.POST.get('owner', '')
        obj.widgets = request.POST.get('widgets') or 0
        obj.status = request.POST.get('status', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/dashboards/')
    return render(request, 'dashboard_form.html', {'record': obj, 'editing': True})


@login_required
def dashboard_delete(request, pk):
    obj = get_object_or_404(Dashboard, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/dashboards/')


@login_required
def report_list(request):
    qs = Report.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(report_type=status_filter)
    return render(request, 'report_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def report_create(request):
    if request.method == 'POST':
        obj = Report()
        obj.title = request.POST.get('title', '')
        obj.dashboard_name = request.POST.get('dashboard_name', '')
        obj.report_type = request.POST.get('report_type', '')
        obj.data_source = request.POST.get('data_source', '')
        obj.schedule = request.POST.get('schedule', '')
        obj.last_run = request.POST.get('last_run') or None
        obj.save()
        return redirect('/reports/')
    return render(request, 'report_form.html', {'editing': False})


@login_required
def report_edit(request, pk):
    obj = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '')
        obj.dashboard_name = request.POST.get('dashboard_name', '')
        obj.report_type = request.POST.get('report_type', '')
        obj.data_source = request.POST.get('data_source', '')
        obj.schedule = request.POST.get('schedule', '')
        obj.last_run = request.POST.get('last_run') or None
        obj.save()
        return redirect('/reports/')
    return render(request, 'report_form.html', {'record': obj, 'editing': True})


@login_required
def report_delete(request, pk):
    obj = get_object_or_404(Report, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/reports/')


@login_required
def datasource_list(request):
    qs = DataSource.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(source_type=status_filter)
    return render(request, 'datasource_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def datasource_create(request):
    if request.method == 'POST':
        obj = DataSource()
        obj.name = request.POST.get('name', '')
        obj.source_type = request.POST.get('source_type', '')
        obj.connection_string = request.POST.get('connection_string', '')
        obj.status = request.POST.get('status', '')
        obj.last_sync = request.POST.get('last_sync') or None
        obj.records = request.POST.get('records') or 0
        obj.save()
        return redirect('/datasources/')
    return render(request, 'datasource_form.html', {'editing': False})


@login_required
def datasource_edit(request, pk):
    obj = get_object_or_404(DataSource, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.source_type = request.POST.get('source_type', '')
        obj.connection_string = request.POST.get('connection_string', '')
        obj.status = request.POST.get('status', '')
        obj.last_sync = request.POST.get('last_sync') or None
        obj.records = request.POST.get('records') or 0
        obj.save()
        return redirect('/datasources/')
    return render(request, 'datasource_form.html', {'record': obj, 'editing': True})


@login_required
def datasource_delete(request, pk):
    obj = get_object_or_404(DataSource, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/datasources/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['dashboard_count'] = Dashboard.objects.count()
    data['report_count'] = Report.objects.count()
    data['datasource_count'] = DataSource.objects.count()
    return JsonResponse(data)
