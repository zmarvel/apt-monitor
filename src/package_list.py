
import re


pattern = re.compile('([A-Za-z0-9\\-_]+)\\/([A-Za-z]+) ([0-9\\.\\-]+) '
                     '([a-z0-9]+) \\[upgradable from: (.*)\\]')


class PackageList():
    def __init__(self, packages=[]):
        self.packages = self.parse_packages(packages)

    def parse_packages(self, packages):
        package_list = []
        for line in packages:
            match = pattern.match(line)
            if match is not None:
                # ignore arch for now
                package_list.append(Package(match.group(1), match.group(2),
                                            match.group(3), match.group(5)))
        return package_list


class Package():
    def __init__(self, name, source, new, old):
        self.name = name
        self.source = source
        self.new = new
        self.old = old


def test():
    case = ['aptitude/stable 0.8.7-1 i386 [upgradable from: 0.6.11-1+b1]']
    match = pattern.match(case[0])
    assert match is not None
    print(match)
    assert match.group(1) == 'aptitude'
    assert match.group(2) == 'stable'
    assert match.group(3) == '0.8.7-1'
    assert match.group(4) == 'i386'
    assert match.group(5) == '0.6.11-1+b1'
    package_list = PackageList(case)
    assert len(package_list.packages) == 1
    pkg = package_list.packages[0]
    assert pkg.name == 'aptitude'
    assert pkg.source == 'stable'
    assert pkg.new == '0.8.7-1'
    assert pkg.old == '0.6.11-1+b1'


if __name__ == '__main__':
    test()
