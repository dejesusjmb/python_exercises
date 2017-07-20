from abc import ABCMeta, abstractmethod

class LogFormatter(object):

    __metaclass__ = ABCMeta

    def __init__(self, log_lines):
        self._lines = log_lines
        self._total_lines = len(log_lines.splitlines())
        self._current_first = 0

    @abstractmethod
    def next_screen(self):
        pass

    @abstractmethod
    def _do_header(self):
        pass

    @abstractmethod
    def _do_footer(self):
        pass

    @abstractmethod
    def _has_more_entries(self):
        pass

    @abstractmethod
    def _next_screen_first(self):
        pass


class RadioLogFormatter(LogFormatter):

    def __init__(self, log_lines):
        super(RadioLogFormatter, self).__init__(log_lines)

    def next_screen(self):
        content = self._do_header()
        content += ''.join(self._lines.splitlines(True)[self._current_first:self._next_screen_first()])
        content += self._do_footer()
        self._current_first += 4
        return content

    def _do_header(self):
        first = self._current_first + 1
        if self._has_more_entries():
            last = self._next_screen_first()
        else:
            last = self._total_lines
        return '*** Event log: Entries {}-{} of {}\n'.format(first, last, self._total_lines)

    def _do_footer(self):
        if self._has_more_entries():
            return '*** PRESS > for next screen'
        else:
            return '*** PRESS < to exit'

    def _has_more_entries(self):
        return self._next_screen_first() < self._total_lines

    def _next_screen_first(self):
        return self._current_first + 4

class ConsoleLogFormatter(LogFormatter):

    def __init__(self, log_lines):
        super(ConsoleLogFormatter, self).__init__(log_lines)

    def next_screen(self):
        content = self._do_header()
        content += '\n'.join(filter(None, [x.strip() for x in self._lines.splitlines(True)[0].split('  ')]))
        content += '\n'
        content += self._do_footer()
        self._current_first += 1
        return content

    def _do_header(self):
        first = self._current_first + 1
        return '*** Event log: Entry {} of {}\n'.format(first, self._total_lines)

    def _do_footer(self):
        if self._has_more_entries():
            return '*** PRESS > for next screen'
        else:
            return '*** PRESS < to exit'

    def _has_more_entries(self):
        return self._next_screen_first() < self._total_lines

    def _next_screen_first(self):
        return self._current_first + 1


class CsvLogFormatter(LogFormatter):

    def __init__(self, log_lines):
        super(CsvLogFormatter, self).__init__(log_lines)

    def next_screen(self):
        content = ''
        for line in self._lines.splitlines(True):
            content += ', '.join(filter(None, [x.strip() for x in line.split('  ')]))
            content += '\n'
        return content

    def _do_header(self):
        pass

    def _do_footer(self):
        pass

    def _has_more_entries(self):
        pass

    def _next_screen_first(self):
        pass
