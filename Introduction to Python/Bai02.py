class Bai2:
    def nhap(self):
        return int(input('Nhap n = '))

    def list(self, n):
        a = []
        if n <= 0:
            exit()
        for i in range(0, n):
            a.append(int(input('a[%d] = ' % (i + 1))))
        return a
        # return [int(input(f'a[{i}] = ')) for i in range(n)]

    # def max_positive(a):
    #     pos = [x for x in a if x > 0]
    #     return '*' if len(pos) == 0 else max(pos)
    #
    # def count_occ(a):
    #     for x in set(a):
    #         print(f'So {x} xuat hien {a.count(x)} lan')
    def MaxMin(self, a):
        m1 = max(a)
        m2 = min(a)
        if m1 < 0:
            print('So duong lon nhat: *')
        else:
            print('So duong lon nhat: ', m1)
        if m2 > 0:
            print('So am be nhat: *')
        else:
            print('So am be nhat: ', m2)


if __name__ == '__main__':
    b = Bai2()
    n = b.nhap()
    a = b.list(n)
    print(a)
    b.MaxMin(a)
    # a.sort(reverse=True)
    # print(a)
