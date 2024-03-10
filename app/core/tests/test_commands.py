"""
Test custom Django management commands
"""
from unittest.mock import patch

from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError

from django.core.management import call_command
from django.test import SimpleTestCase


# patched_anyVarName is overriding of default action of provided  functions
# e.g. patched_sleep - make it work only in production, not in dev environment
# e.g. patched_check - check database is UP without making actual requrests
#      to DB

# This is the mock command that is coming from our made function
@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test Commands"""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database ready"""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """Test waiting for database when getting OperationalError"""

        # Psycopg2Error = Return this 2 times
        #                 (as per testing results when starting DB)
        # OperationalError = Return this 3 times

        patched_check.side_effect = [Psycopg2Error] * 2 + \
                                    [OperationalError] * 3 + \
                                    [True]

        call_command('wait_for_db')

        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
