from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('dashboards/', views.dashboard_list, name='dashboard_list'),
    path('dashboards/create/', views.dashboard_create, name='dashboard_create'),
    path('dashboards/<int:pk>/edit/', views.dashboard_edit, name='dashboard_edit'),
    path('dashboards/<int:pk>/delete/', views.dashboard_delete, name='dashboard_delete'),
    path('reports/', views.report_list, name='report_list'),
    path('reports/create/', views.report_create, name='report_create'),
    path('reports/<int:pk>/edit/', views.report_edit, name='report_edit'),
    path('reports/<int:pk>/delete/', views.report_delete, name='report_delete'),
    path('datasources/', views.datasource_list, name='datasource_list'),
    path('datasources/create/', views.datasource_create, name='datasource_create'),
    path('datasources/<int:pk>/edit/', views.datasource_edit, name='datasource_edit'),
    path('datasources/<int:pk>/delete/', views.datasource_delete, name='datasource_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
