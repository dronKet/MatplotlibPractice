import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerPatch
from matplotlib.legend_handler import HandlerLine2D
from numpy.random import randn

def task1():
    red_patch = mpatches.Patch(color='red', label='The red data')
    plt.legend(handles=[red_patch])
    plt.show()


def task2():
    blue_line = mlines.Line2D([], [], color='blue', marker='*',
                              markersize=15, label='Blue stars')
    plt.legend(handles=[blue_line])
    plt.show()

def task3():
    plt.subplot(211)
    plt.plot([1,2,3], label="test1")
    plt.plot([3,2,1], label="test2")
    # Place a legend above this subplot, expanding itself to
    # fully use the given bounding box.
    plt.legend(bbox_to_anchor=(0., 1.01, 1.1, .102), loc=3,
               ncol=2, mode="expand", borderaxespad=0.)

    plt.subplot(223)
    plt.plot([1,2,3], label="test1")
    plt.plot([3,2,1], label="test2")
    # Place a legend to the right of this smaller subplot.
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()

def task4():

    line1, = plt.plot([1,2,3], label="Line 1", linestyle='--')
    line2, = plt.plot([3,2,1], label="Line 2", linewidth=4)

    # Create a legend for the first line.
    first_legend = plt.legend(handles=[line1], loc=1)

    # Add the legend manually to the current Axes.
    ax = plt.gca().add_artist(first_legend)

    # Create another legend for the second line.
    plt.legend(handles=[line2], loc=4)
    plt.show()

def task5():
    line1, = plt.plot([3,2,1], marker='o', label='Line 1')
    line2, = plt.plot([1,2,3], marker='o', label='Line 2')

    plt.legend(handler_map={line1: HandlerLine2D(numpoints=4)})
    plt.show()
def task6():
    z = randn(10)

    red_dot, = plt.plot(z, "ro", markersize=15)
    # Put a white cross over some of the data.
    white_cross, = plt.plot(z[:10], "w+", markeredgewidth=3, markersize=15)

    plt.legend([red_dot, (red_dot, white_cross)], ["Attr A", "Attr A+B"])
    plt.show()
def task7():
    class AnyObject(object):
        pass

    class AnyObjectHandler(object):
        def legend_artist(self, legend, orig_handle, fontsize, handlebox):
            x0, y0 = handlebox.xdescent, handlebox.ydescent
            width, height = handlebox.width, handlebox.height
            patch = mpatches.Rectangle([x0, y0], width, height, facecolor='red',
                                       edgecolor='black', hatch='xx', lw=3,
                                       transform=handlebox.get_transform())
            handlebox.add_artist(patch)
            return patch

    plt.legend([AnyObject()], ['My first handler'],
               handler_map={AnyObject: AnyObjectHandler()})
    plt.show()
def task8():
    class HandlerEllipse(HandlerPatch):
        def create_artists(self, legend, orig_handle,
                           xdescent, ydescent, width, height, fontsize, trans):
            center = 0.5 * width - 0.5 * xdescent, 0.5 * height - 0.5 * ydescent
            p = mpatches.Ellipse(xy=center, width=width + xdescent,
                                 height=height + ydescent)
            self.update_prop(p, orig_handle, legend)
            p.set_transform(trans)
            return [p]


    c = mpatches.Circle((0.5, 0.5), 0.25, facecolor="green",
                        edgecolor="red", linewidth=3)
    plt.gca().add_patch(c)

    plt.legend([c], ["An ellipse, not a rectangle"],
               handler_map={mpatches.Circle: HandlerEllipse()})
    plt.show()
task1()
task2()
task3()
task4()
task5()
task6()
task7()
task8()


