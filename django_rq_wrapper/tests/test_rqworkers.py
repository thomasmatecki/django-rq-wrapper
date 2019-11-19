from django.test import TestCase
from django.core.management import call_command

class RqWorkersTest(TestCase):

    def test_command_runs(self):
        call_command('rqworkers', 'high', 'default', 'low')
