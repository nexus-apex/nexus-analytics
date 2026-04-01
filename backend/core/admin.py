from django.contrib import admin
from .models import Dashboard, Report, DataSource

@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "owner", "widgets", "status", "created_at"]
    list_filter = ["category", "status"]
    search_fields = ["name", "owner"]

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ["title", "dashboard_name", "report_type", "data_source", "schedule", "created_at"]
    list_filter = ["report_type", "schedule"]
    search_fields = ["title", "dashboard_name", "data_source"]

@admin.register(DataSource)
class DataSourceAdmin(admin.ModelAdmin):
    list_display = ["name", "source_type", "connection_string", "status", "last_sync", "created_at"]
    list_filter = ["source_type", "status"]
    search_fields = ["name", "connection_string"]
