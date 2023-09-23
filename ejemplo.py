from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig1 = plt.figure()
plt.plot([2, 1, 7, 1, 2], color='red', lw=5)

fig2 = plt.figure()
plt.plot([3, 5, 1, 5, 3], color='green', lw=5)


def save_multi_image(filename):
    pp = PdfPages(filename)
    fig_nums = plt.get_fignums()
    figs = [plt.figure(n) for n in fig_nums]
    for fig in figs:
        fig.savefig(pp, format='pdf')
    pp.close()


filename = "multi.pdf"
save_multi_image(filename)
