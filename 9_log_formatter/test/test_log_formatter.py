import unittest
import difflib
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from log_formatter import RadioLogFormatter, ConsoleLogFormatter, CsvLogFormatter


class _WithPrintouts(object):

    def _assert_printout(self, actual, expected):
        if(actual != expected):
            differences = list(difflib.Differ().compare(expected.splitlines(True), actual.splitlines(True)))
            self.fail(''.join(differences))


text_log_data = '''\
06:54:56  Doors               Central locking opened
06:55:22  Engine              Started, coolant temp +2C
06:55:27  Rear radar          Activated
06:56:00  Rear radar          Collision warning, distance 100cm
06:56:05  Rear radar          Collision warning, distance 100cm
06:56:10  Rear radar          Collision warning, distance 50cm
06:57:30  Lights              Hi-Beam activated
06:57:35  Lights              Automated Hi-Beam/Lo-Beam switching activated
06:57:30  Lights              Hi-Beam activated
07:05:11  Windscreen wipers   Rain detected, speed 1
07:06:05  Engine              Engine reached normal temperature, Oil temp 95C, Coolant 81C
07:20:10  Windscreen wipers   Rain stopped, keeping speed 1 for 10 sec
07:20:20  Windscreen wipers   Speed 0
07:25:10  Brakes              ABS activated, emergency assist active, speed 55km/h
07:25:15  Brakes              ABS deactivated, speed 0km/h
07:31:20  Engine              Engine stopped
07:31:33  Doors               Central locking closed
'''


class TestLogFormatForRadioDisplay(unittest.TestCase, _WithPrintouts):

    def test_radio_display_showing_first_4_lines(self):
        rf = RadioLogFormatter(text_log_data)
        self._assert_printout(rf.next_screen(),
'''*** Event log: Entries 1-4 of 17
06:54:56  Doors               Central locking opened
06:55:22  Engine              Started, coolant temp +2C
06:55:27  Rear radar          Activated
06:56:00  Rear radar          Collision warning, distance 100cm
*** PRESS > for next screen''')

    def test_radio_display_showing_second_4_line_group(self):
        rf = RadioLogFormatter(text_log_data)
        rf.next_screen()
        self._assert_printout(rf.next_screen(),
'''*** Event log: Entries 5-8 of 17
06:56:05  Rear radar          Collision warning, distance 100cm
06:56:10  Rear radar          Collision warning, distance 50cm
06:57:30  Lights              Hi-Beam activated
06:57:35  Lights              Automated Hi-Beam/Lo-Beam switching activated
*** PRESS > for next screen''')

    def test_radio_display_showing_last_line(self):
        rf = RadioLogFormatter(text_log_data)
        for _ in range(4):
            rf.next_screen()
        self._assert_printout(rf.next_screen(),
'''*** Event log: Entries 17-17 of 17
07:31:33  Doors               Central locking closed
*** PRESS < to exit''')


class TestLogFormatForConsoleDisplay(unittest.TestCase, _WithPrintouts):

    '''
    Read about template method design pattern:
    http://en.wikipedia.org/wiki/Template_method_pattern

    Implement log formatting for console display using Template Method pattern.
    Only one event should be shown at time.
    Time, event source and event description should be under eachother.
    Hint: first refactor the algorithm part (next_screen) of RadioLogFormatter to
    base class LogFormatter
'''
    def test_console_display_showing_first_event(self):
        cf = ConsoleLogFormatter(text_log_data)
        self._assert_printout(cf.next_screen(),
'''*** Event log: Entry 1 of 17
06:54:56
Doors
Central locking opened
*** PRESS > for next screen''')


class TestLogFormatForCsvFile(unittest.TestCase, _WithPrintouts):

    ''' Implement formatting log into comma separated values '''
    def test_console_display_showing_first_event(self):
        csvf = CsvLogFormatter(text_log_data)
        self._assert_printout(csvf.next_screen(),
'''\
06:54:56, Doors, Central locking opened
06:55:22, Engine, Started, coolant temp +2C
06:55:27, Rear radar, Activated
06:56:00, Rear radar, Collision warning, distance 100cm
06:56:05, Rear radar, Collision warning, distance 100cm
06:56:10, Rear radar, Collision warning, distance 50cm
06:57:30, Lights, Hi-Beam activated
06:57:35, Lights, Automated Hi-Beam/Lo-Beam switching activated
06:57:30, Lights, Hi-Beam activated
07:05:11, Windscreen wipers, Rain detected, speed 1
07:06:05, Engine, Engine reached normal temperature, Oil temp 95C, Coolant 81C
07:20:10, Windscreen wipers, Rain stopped, keeping speed 1 for 10 sec
07:20:20, Windscreen wipers, Speed 0
07:25:10, Brakes, ABS activated, emergency assist active, speed 55km/h
07:25:15, Brakes, ABS deactivated, speed 0km/h
07:31:20, Engine, Engine stopped
07:31:33, Doors, Central locking closed
''')


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
