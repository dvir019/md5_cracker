class Code(object):
    char_to_num = {chr(i): i - ord('a') for i in range(ord('a'), ord('z') + 1)}
    num_to_char = {i - ord('a'): chr(i) for i in range(ord('a'), ord('z') + 1)}

    def __init__(self, str_or_code):
        self.string = str_or_code if type(str_or_code) == str else str_or_code.string

    def inc(self, st):
        index = 0
        for i in range(len(st) - 1, -1, -1):
            if st[i] != 'z':
                index = i
                break
        inc_str = st[:index] + chr(ord(st[index]) + 1) + 'a' * (len(st) - (index + 1))
        return inc_str

    def __add__(self, add):
        self.string = Code.convert_from_decimal(self.convert_to_decimal() + add).string
        return self

    def __sub__(self, other):
        # if self.string==other.string:
        #     return 0
        # length = len(self.string)
        # count = 1
        # for i in range(length - 1, -1, -1):
        #     dif = ord(self.string[i]) - ord(other.string[i])
        #     count += dif * (26 ** (length - i - 1))
        # return count
        # print other.convert_to_decimal()
        # print self.convert_to_decimal()
        return self.convert_to_decimal() - other.convert_to_decimal() + 1

    def __le__(self, other):
        return self.convert_to_decimal() < other.convert_to_decimal()

    def convert_to_decimal(self):
        decimal = 0
        for i in range(len(self.string) - 1, -1, -1):
            if ':' in self.string:
                print self.string
            decimal += Code.char_to_num[self.string[i]] * (26 ** (len(self.string) - i - 1))
        return decimal

    @staticmethod
    def convert_from_decimal(num, lenght=6):
        st = ''
        while num != 0:
            st = Code.num_to_char[num % 26] + st
            num /= 26
        st = 'a' * (lenght - len(st)) + st
        return Code(st)

    def __repr__(self):
        return self.string


# a1 = Code('aaaaaa')
# a2 = Code('aaaabb')
# print a2-a1
# a1+=3369876
# print a1

# print a1.convert_to_decimal()
# print a2.convert_to_decimal()
# print Code.convert_from_decimal(1000)
# print Code('aaabmm').convert_to_decimal()

# print a1
# a1+=5
# print a1
#x=Code('aaaaaa')
#x2=Code('zzzzzz')
#print x<=x2
