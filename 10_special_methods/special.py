class ClassParser(object):
    def __init__(self, string):
        self._string = string
        self._name = self.getName()
        self._fields = self._populatefields()

    def __getattr__(self, item):
        if item in self._fields:
            return self._fields[item]
        return "Property does not exist"

    def __getitem__(self, item):
        return self._fields[item]

    def __setitem__(self, key, value):
        self._string += '''
    def {}(self, args):
        {}
'''.format(key, value)
        self._populatefields()

    def __lt__(self, other):
        return len(self.getMethods()) < len(other.getMethods())

    def __gt__(self, other):
        return len(self.getMethods()) > len(other.getMethods())

    def __eq__(self, other):
        return len(self.getMethods()) == len(other.getMethods())

    def __str__(self):
        return 'class {} with methods {}'.format(self._name, ", ".join(sorted(self.getMethods())))

    def __repr__(self):
        methods = '{}'.format(sorted(self.getMethods()))
        return "{}{} : {}{}".format('{', self._name, methods.replace("'", ""), '}')

    def getName(self):
        return self._string.splitlines()[1].split(' ')[1].split('(')[0]

    def getMethods(self):
        return [x.split('(')[0] for x in
                [x.split(' ')[1] for x in
                 [x.strip() for x in
                  [line for line in self._string.splitlines() if 'def' in line]]]]

    def _populatefields(self):
        items = {'name': self._name, 'methods': self.getMethods(), 'method_count': len(self.getMethods())}
        items.update(zip([x.split(' ')[5].split('(')[0] for x in self._string.splitlines() if 'def' in x],
                         [x.strip() for x in self._string.splitlines() if '        ' in x]))
        return items
