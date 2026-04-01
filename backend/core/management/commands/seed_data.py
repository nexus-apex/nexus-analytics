from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Dashboard, Report, DataSource
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusAnalytics with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusanalytics.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Dashboard.objects.count() == 0:
            for i in range(10):
                Dashboard.objects.create(
                    name=f"Sample Dashboard {i+1}",
                    category=random.choice(["sales", "marketing", "finance", "operations", "hr"]),
                    owner=f"Sample {i+1}",
                    widgets=random.randint(1, 100),
                    status=random.choice(["active", "draft", "archived"]),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Dashboard records created'))

        if Report.objects.count() == 0:
            for i in range(10):
                Report.objects.create(
                    title=f"Sample Report {i+1}",
                    dashboard_name=f"Sample Report {i+1}",
                    report_type=random.choice(["chart", "table", "kpi", "funnel"]),
                    data_source=f"Sample {i+1}",
                    schedule=random.choice(["none", "daily", "weekly", "monthly"]),
                    last_run=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 Report records created'))

        if DataSource.objects.count() == 0:
            for i in range(10):
                DataSource.objects.create(
                    name=f"Sample DataSource {i+1}",
                    source_type=random.choice(["database", "api", "csv", "spreadsheet"]),
                    connection_string=f"Sample {i+1}",
                    status=random.choice(["connected", "disconnected", "error"]),
                    last_sync=date.today() - timedelta(days=random.randint(0, 90)),
                    records=random.randint(1, 100),
                )
            self.stdout.write(self.style.SUCCESS('10 DataSource records created'))
