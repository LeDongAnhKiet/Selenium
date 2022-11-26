class Bai1:

    def nhap(self):
        return int(input('Nhap n = '))

    def HinhVuong(self, n):
        print(('* ' * n + '\n') * n)
        # for i in range(0, n):
        #     print('* ' * n)
        # print('\n')
        # i = 0
        # while i < n:
        #     print('* ' * n)
        #     i += 1

    def TamGiacVuongTrai(self, n):
        for i in range(1, n + 1):
            print('* ' * i)

    def TamGiacVuongPhai(self, n):
        for i in range(1, n + 1):
            print('  ' * (n - i) + '* ' * i)

    def TamGiacVuongCan(self, n):
        for i in range(1, n + 1):
            n2 = n - i
            if n2 % 2 == 0:
                print('  ' * round(n2 / 2) + '* ' * i)
        # for i in range(1, n + 1, 2):
        #     print(('*' * i).center(n))


a = Bai1()
n = a.nhap()
a.HinhVuong(n)
a.TamGiacVuongTrai(n)
a.TamGiacVuongPhai(n)
a.TamGiacVuongCan(n)
