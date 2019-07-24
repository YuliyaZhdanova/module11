from datetime import datetime, timezone

from django.core.management import BaseCommand
from django.contrib.auth.models import User
from tasks.models import TodoItem
import collections

class Command(BaseCommand):
    help = u"Dump all task dates"

    def add_arguments(self, parser):
        parser.add_argument(
            '--warning-days', dest='warn_days', type=int, default=5)

    def handle(self, *args, **options):
        done_tasks = 0
        c = collections.Counter()
        for u in User.objects.all():
            for t in u.tasks.filter(is_completed=False):
                c[u] += 1
                done_tasks += 1
        n = 0
        for i in c:
            if c[i] < 20:
                n += 1
                
        print(c.most_common(2)[1])
