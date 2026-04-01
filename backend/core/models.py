from django.db import models

class Dashboard(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=[("sales", "Sales"), ("marketing", "Marketing"), ("finance", "Finance"), ("operations", "Operations"), ("hr", "HR")], default="sales")
    owner = models.CharField(max_length=255, blank=True, default="")
    widgets = models.IntegerField(default=0)
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("draft", "Draft"), ("archived", "Archived")], default="active")
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Report(models.Model):
    title = models.CharField(max_length=255)
    dashboard_name = models.CharField(max_length=255, blank=True, default="")
    report_type = models.CharField(max_length=50, choices=[("chart", "Chart"), ("table", "Table"), ("kpi", "KPI"), ("funnel", "Funnel")], default="chart")
    data_source = models.CharField(max_length=255, blank=True, default="")
    schedule = models.CharField(max_length=50, choices=[("none", "None"), ("daily", "Daily"), ("weekly", "Weekly"), ("monthly", "Monthly")], default="none")
    last_run = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class DataSource(models.Model):
    name = models.CharField(max_length=255)
    source_type = models.CharField(max_length=50, choices=[("database", "Database"), ("api", "API"), ("csv", "CSV"), ("spreadsheet", "Spreadsheet")], default="database")
    connection_string = models.CharField(max_length=255, blank=True, default="")
    status = models.CharField(max_length=50, choices=[("connected", "Connected"), ("disconnected", "Disconnected"), ("error", "Error")], default="connected")
    last_sync = models.DateField(null=True, blank=True)
    records = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
