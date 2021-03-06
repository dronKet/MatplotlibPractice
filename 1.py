import matplotlib.pyplot as plt
import numpy as np

def task1():
    plt.plot([1,2,3,4,-1])
    plt.ylabel('y')
    plt.xlabel('x')
    plt.show()

def task2():
    plt.plot([1, 5, 6, 8], [10, 4, 9, 16])
    plt.show()

def task3():

    plt.plot([1,2,3,4], [1,4,9,16], 'ro')
    plt.axis([0, 7, 0, 25])
    plt.show()

def task4():
    t = np.arange(0., 5., 0.2)

    plt.plot(t, t*np.e, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.show()

def task5():
    plt.plot([1, 5, 6, 8], [10, 4, 9, 16], linewidth=10.0)
    plt.show()

def task6():
    line, = plt.plot([1, 5, 6, 8], [10, 4, 9, 16], '-')
    line.set_antialiased(False) # turn off antialising
    plt.show()

def task7():
    x1=[1, 5, 6, 8]
    y1=[10, 4, 9, 16]
    x2=[1,2,3,4]
    y2= [1,4,9,16]
    lines = plt.plot(x1, y1, x2, y2)
    # use keyword args
    plt.setp(lines, color='r', linewidth=2.0)
    plt.show()
    plt.setp(lines)

def task8():
    def f(t):
        return np.exp(-t) * np.cos(2*np.pi*t)

    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

    plt.subplot(212)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
    plt.show()

def task9():
    import matplotlib.pyplot as plt
    plt.figure(1)                # the first figure
    plt.subplot(211)             # the first subplot in the first figure
    plt.plot([1, 2, 3])
    plt.subplot(212)             # the second subplot in the first figure
    plt.plot([4, 5, 6])


    plt.figure(2)                # a second figure
    plt.plot([4, 5, 6])          # creates a subplot(111) by default

    plt.figure(1)                # figure 1 current; subplot(212) still current
    plt.subplot(211)             # make subplot(211) in figure1 current
    plt.title('Easy as 1, 2, 3') # subplot 211 title
    plt.show()

def task10():
    np.random.seed(19680801)
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)
    n, bins, patches = plt.hist(x, 50, density =1, facecolor='g', alpha=0.75)
    t = plt.xlabel('my data', fontsize=14, color='red')
    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    plt.title(r'$\sigma_i=15$')
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()

def task11():
    ax = plt.subplot(111)

    t = np.arange(0.0, 5.0, 0.01)
    print(t)
    s = np.cos(2*np.pi*t)
    line, = plt.plot(t, s, lw=2)

    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                arrowprops=dict(facecolor='black', shrink=0.05),
                )

    plt.ylim(-2,2)
    plt.show()

def task12():
    from matplotlib.ticker import NullFormatter  # useful for `logit` scale

    # Fixing random state for reproducibility
    np.random.seed(19680801)

    # make up some data in the interval ]0, 1[
    y = np.random.normal(loc=0.5, scale=0.4, size=1000)
    y = y[(y > 0) & (y < 1)]
    y.sort()
    x = np.arange(len(y))

    plt.figure(1)
    plt.subplot(221)
    plt.plot(x, y)
    plt.yscale('linear')
    plt.title('linear')
    plt.grid(True)
    plt.subplot(222)
    plt.plot(x, y)
    plt.yscale('log')
    plt.title('log')
    plt.grid(True)
    plt.subplot(223)
    plt.plot(x, y - y.mean())
    plt.yscale('symlog', linthreshy=0.01)
    plt.title('symlog')
    plt.grid(True)
    plt.subplot(224)
    plt.plot(x, y)
    plt.yscale('logit')
    plt.title('logit')
    plt.grid(True)
    plt.gca().yaxis.set_minor_formatter(NullFormatter())
    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                        wspace=0.35)
    plt.show()
task1()
task2()
task3()
task4()
task5()
task6()
task7()
task8()
task9()
task10()
task11()
task12()
