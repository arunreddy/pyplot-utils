import matplotlib.pyplot  as plt

class Plot(object):
    '''Plot a helper class to plot using Matplotlib.'''


    def __init__(self):
        self.name = 'Plot Utils- Plot'


    def setPlotParams(self,params):
        pass

    def plot(self,X,Y,title='',xlabel='',ylabel='',legend=[],save=False,fileName=''):
        '''Helper function to plot using matplotlib'''

        plt.plot(X,Y)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        if(len(legend>0)):
            plt.legend(legend)

        if save :
            plt.show()
        else:
            plt.savefig(fileName,dpi=300)
