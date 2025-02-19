class CaseHelper:

    @staticmethod
    def is_snake(line):
        if "_" not in line:
            for i in line:
                if i.isalpha() and i.islower():
                    pass
                else:
                    return False
        elif line[0] == "_" or line[-1] == "_":
            return False
        elif "_" in line[1:-1]:
            for i in line:
                if i.isalpha() and i.islower() or i == "_":
                    pass
                else:
                    return False
        else:
            return False
        return True

    @staticmethod
    def is_upper_camel(line):
        if line[0].isupper():
            for i in line:
                if i.isalpha():
                    pass
                else:
                    return False
        else:
            return False
        return True

    @staticmethod
    def to_snake(line):
        res = line[0].lower()
        for i in line[1:]:
            res += '_' + i.lower() if i.isupper() else i
        return res

    @staticmethod
    def to_upper_camel(line):
        res = line[0].upper()
        for i in range(1, len(line)):
            if line[i] == '_':
                pass
            else:
                if line[i - 1] == "_":
                    res += line[i].upper()
                else:
                    res += line[i]
        return res

cases = ['assert_equal', 'tear_down', '__init__', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup', 'its_wednesday_my_dudes']

for case in cases:
    print(CaseHelper.is_snake(case))