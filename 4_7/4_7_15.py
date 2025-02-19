class StrExtension:

    @staticmethod
    def remove_vowels(line):
        return ''.join(i for i in line if i.lower() not in "aeiouy")

    @staticmethod
    def leave_alpha(line):
        return ''.join(i for i in line if i.isalpha() and isinstance(i, str))

    @staticmethod
    def replace_all(line, chars, char):
        return ''.join(char if i in chars else i for i in line)



print(StrExtension.remove_vowels('Python'))
print(StrExtension.remove_vowels('Stepik'))
print(StrExtension.leave_alpha('Python111'))
print(StrExtension.leave_alpha('__Stepik__()'))
print(StrExtension.replace_all('Python', 'Ptn', '-'))
print(StrExtension.replace_all('Stepik', 'stk', '#'))