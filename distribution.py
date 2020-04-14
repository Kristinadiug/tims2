import math


class Range:
    def __init__(self, l, r, val=0, mu=0, sig2=1.0):
        self.l = l
        self.r = r
        self.val = val
        self.mu = mu
        self.sig2 = sig2

    def normal(self, x):
        return (1 + math.exp((x - self.mu)/math.sqrt(2*self.sig2)))/2

    def get_normal(self):
        return self.normal(self.r) - self.normal(self.l)

    def unite(self, y):
        self.r = y.r
        self.val += y.val

    def too_small(self):
        return self.val < 5 or self.get_normal() < 5

    def get_range(self):
        return "[{left} - {right}]".format(left=self.l, right=self.r)


class Distribution:
    def __init__(self, mu=0, sig2=1.0, a=0.05):
        self.ranges = list()
        self.n = 0
        self.table = dict()
        self.mu = mu
        self.sig2 = sig2
        self.a = a

        f = open("table.txt", "r")
        lines = f.readlines()
        prob = map(float, lines[0].split())
        prob = list(prob)
        for i in range(1, len(lines)):
            line = map(float, lines[i].split())
            line = list(line)
            for j in range(len(line)):
                self.table[(i, prob[j])] = line[j]

    def read_continuous(self, filename="continuous.txt"):
        f = open(filename, "r")
        lines = f.readlines()
        for line in lines:
            lst = map(int, line.split())
            lst = list(lst)
            r = Range(lst[0], lst[1], lst[2], self.mu, self.sig2)
            self.ranges.append(r)
            self.n += r.val

    def read_discrete(self, filename="discrete.txt", ranges=5):
        f = open(filename, "r")
        line = f.readline()
        lst = list(map(int, line.split()))
        mn = 100000
        mx = -100000
        for x in lst:
            mn = min(mn, x)
            mx = max(mx, x)
        d = (mx - mn + ranges - 1) / ranges
        for i in range(ranges):
            rg = Range(mn, mn + d, 0, self.mu, self.sig2)
            for x in lst:
                if rg.l <= x < rg.r:
                    rg.val += 1
            self.ranges.append(rg)
        self.n = len(lst)

    def parse(self):
        for i in range(1, len(self.ranges), -1):
            print(i)
            print(len(self.ranges))
            if self.ranges[i].too_small or self.ranges[i-1].too_small:
                self.ranges[i-1].unite(self.ranges[i])
                self.ranges.remove(self.ranges[i])

    def xi(self):
        sum = 0
        for r in self.ranges:
            p = r.get_normal()
            sum += ((r.val - self.n * p)**2) / (self.n * p)
        return sum

    def check(self):
        alpha = self.a
        self.parse()
        x = self.xi()
        critical = self.table[(len(self.ranges)-1, alpha)]

        if x <= critical:
            return True
        else:
            return False


if __name__ == "__main__":
    m = -200
    while m < 200:
        a = 0.47
        while a < 10.0:
            d = Distribution(m, a)
            d.read_continuous()
            if d.check():
                print(d.mu)
                print(d.sig2)
                was = 1
                break
            a += 0.01
        m += 0.1



