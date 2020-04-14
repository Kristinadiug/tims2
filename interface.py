import tkinter.ttk as ttk
import tkinter as tk
from paphra_tktable import table as tktable
from distribution import *


class Table(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.show()

    def show(self):
        lb1 = tk.Label(self, text=f"Frequency table", width=30, bd=10, font='Times 15')
        lb1.pack(side=tk.TOP)


class ShowSummary(tk.Toplevel):
    def __init__(self, d):
        super().__init__()
        self.distribution = d
        self.summary()

    def summary(self):
        header = ["Ranges", 'n_i', "p_i*n"]
        F1 = tk.Frame(self)
        for h in header:
            lb1 = tk.Label(F1, text=h, width=15, bd=10, font='Times 15')
            lb1.pack(side=tk.LEFT)
        F1.pack(side=tk.TOP)
        for r in self.distribution.ranges:
            F = tk.Frame(self)
            lbr = tk.Label(F, text=r.get_range(), width=15, bd=10, font='Times 15')
            lbr.pack(side=tk.LEFT)
            lbv = tk.Label(F, text=str(r.val), width=15, bd=10, font='Times 15')
            lbv.pack(side=tk.LEFT)
            lbp = tk.Label(F, text=str(round(r.get_normal()*self.distribution.n, 5)), width=25, bd=10, font='Times 15')
            lbp.pack(side=tk.LEFT)
            F.pack(side=tk.TOP)

        x = self.distribution.xi()
        critical = self.distribution.table[(len(self.distribution.ranges) - 1, self.distribution.a)]

        xi = tk.Label(self, text="Xi2 = " + str(x), width=30, bd=10, font='Times 15')
        xi.pack()
        c = tk.Label(self, text="Critical = " + str(critical), width=15, bd=10, font='Times 15')
        c.pack()
        res =""
        if self.distribution.check():
            res = "hypothesis is right"
        else:
            res = "hypothesis is wrong"
        r = tk.Label(self, text=res, width=15, bd=10, font='Times 15')
        r.pack()


def set_text(l, text):
    l['text'] = text


class Message(tk.Toplevel):
    def __init__(self, txt):
        super().__init__()
        self.txt = str(txt)
        self.init_m()

    def init_m(self):
        lb = tk.Label(self, text=self.txt)
        lb.pack(side=tk.TOP)


class Continuous(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("350x350+200+200")
        self.read()

    def check(self, filename, mu, sig2, a):
        d = Distribution(mu, sig2, a)
        d.read_continuous(filename)
        ShowSummary(d)
        self.destroy()

    def read(self):
        lb1 = tk.Label(self, text=f"Check Continuous Distribution", width=30, bd=10, font='Times 15')
        lb1.pack(side=tk.TOP)

        f_lb = tk.Label(self, text=f"Enter filename: ", font='Times 13')
        f_lb.pack()
        f_entr = tk.Entry(self)
        f_entr.insert(0, "continuous.txt")
        f_entr.pack()

        lb3 = tk.Label(self, text=f"Enter alpha", width=30, bd=10, font='Times 13')
        lb3.pack()

        a_lb = tk.Label(self, text=f"\u03BC: ", font='Times 12')
        a_lb.pack()
        a_entr = tk.Entry(self, width=15)
        a_entr.insert(0, "0.05")
        a_entr.pack()

        lb2 = tk.Label(self, text=f"Enter parameters", width=30, bd=10, font='Times 13')
        lb2.pack()

        mu_lb = tk.Label(self, text=f"\u03BC: ", font='Times 12')
        mu_lb.pack()
        mu_entr = tk.Entry(self, width=15)
        mu_entr.insert(0, "0")
        mu_entr.pack()

        s_lb = tk.Label(self, text=f"\u03C3\u00b2: ", font='Times 12')
        s_lb.pack()
        s_entr = tk.Entry(self, width=15)
        s_entr.insert(0, "1")
        s_entr.pack()

        submit = tk.Button(self, text="Submit", font='Times 13')
        submit.pack(side=tk.TOP)
        submit.bind('<Button-1>', lambda event: self.check(str(f_entr.get()), float(mu_entr.get()), float(s_entr.get()), float(a_entr.get())))


class Discrete(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.geometry("350x350+200+200")
        self.read()

    def check(self, filename, n, mu, sig2, a):
        d = Distribution(mu, sig2, a)
        d.read_discrete(filename, n)
        ShowSummary(d)
        self.destroy()

    def read(self):
        lb1 = tk.Label(self, text=f"Check Discrete Distribution", width=30, bd=10, font='Times 15')
        lb1.pack(side=tk.TOP)

        f_lb = tk.Label(self, text=f"Enter filename: ", font='Times 13')
        f_lb.pack()
        f_entr = tk.Entry(self)
        f_entr.insert(0, "discrete.txt")
        f_entr.pack()

        lb3 = tk.Label(self, text=f"Enter alpha", width=30, bd=10, font='Times 13')
        lb3.pack()

        a_lb = tk.Label(self, text=f"\u03BC: ", font='Times 12')
        a_lb.pack()
        a_entr = tk.Entry(self, width=15)
        a_entr.insert(0, "0.05")
        a_entr.pack()

        n_lb = tk.Label(self, text=f"\nEnter number of ranges to split the sequence: ", font='Times 13')
        n_lb.pack()
        n_entr = tk.Entry(self, width=15)
        n_entr.insert(0, "5")
        n_entr.pack()

        lb2 = tk.Label(self, text=f"Enter parameters", width=30, bd=10, font='Times 13')
        lb2.pack()

        mu_lb = tk.Label(self, text=f"\u03BC: ", font='Times 12')
        mu_lb.pack()
        mu_entr = tk.Entry(self, width=15)
        mu_entr.insert(0, "0")
        mu_entr.pack()

        s_lb = tk.Label(self, text=f"\u03C3\u00b2: ", font='Times 12')
        s_lb.pack()
        s_entr = tk.Entry(self, width=15)
        s_entr.insert(0, "1")
        s_entr.pack()

        submit = tk.Button(self, text="Submit", font='Times 13')
        submit.pack(side=tk.TOP)
        submit.bind('<Button-1>', lambda event: self.check(str(f_entr.get()), int(n_entr.get()), float(mu_entr.get()), float(s_entr.get())), float(a_entr.get()))


class Main(tk.Frame):
    def __init__(self, root):
        self.r = root
        super().__init__(root)
        self.init_main()

    def init_main(self):
        toolbar = tk.Frame(bd=5)
        toolbar.pack(side=tk.TOP)

        lb1 = tk.Label(toolbar, text=f"Check Normal Distribution", width=30, bd=10, font='Times 15')
        lb1.pack(side=tk.TOP)

        lb2 = tk.Label(toolbar, text=f"With parameters", width=30, bd=10, font='Times 14')
        lb2.pack(side=tk.TOP)

        add = tk.Button(toolbar, text="Continuous", width='20', command=Continuous)
        add.pack(side=tk.BOTTOM)

        add = tk.Button(toolbar, text="Discrete", width='20', command=Discrete)
        add.pack(side=tk.BOTTOM)


if __name__ == "__main__":
    root = tk.Tk()
    w = Main(root)
    w.pack()
    root.title("Check Normal Distribution")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
