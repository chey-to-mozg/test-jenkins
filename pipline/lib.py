import os.path
import subprocess
import sys


class lib(object):
    def __init__(self):
        self._sut_path = os.path.join(os.path.dirname(__file__), 'main.py')
        print(self._sut_path)
        self._status = ''


    def compare(self, number):
        self._run_command('compare', number)


    def status_should_be(self, expected_status):
        if expected_status != self._status:
            raise AssertionError("Expected status to be '%s' but was '%s'."
                                 % (expected_status, self._status))

    def _run_command(self, command, *args):
        command = [sys.executable, self._sut_path, command] + list(args)
        process = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        self._status = process.communicate()[0].strip()
