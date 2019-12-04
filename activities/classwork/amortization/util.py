import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Amortization(object):

    def __init__(self, amount, interest, n):
        self.amount = amount
        self.interest = interest
        self.n = n

    def annuity(self): #self: Cuando un objeto hace referencia a sí mismo
        annuity = self.amount / ((1-(1+self.interest)**(-self.n))/self.interest)
        return annuity

    def get_table(self):
        Annuity = self.annuity()
        Principal_ = [0]
        Interest_ = [0]
        Annuity_ = [Annuity]
        Loan_Val_ = [self.amount]

        for j in range(self.n):
            Annuity_.append(Annuity_[-1])
            Interest_.append(Loan_Val_[-1])*(self.interest)
            Principal_.append(Annuity_[-1]-Interest_[-1])
            Loan_Val_.append(Loan_Val_[-1]-Principal_[-1])

            table = pd.DataFrame([Principal_, Interest_, Annuity_, Loan_Val_]).transpose()
            table = table.rename(columns={0: 'Principal', 1: 'Interest', 2: 'Annuity', 3: 'Loan Value'})
            return table

    def get_plot(self):
        table = self.get_table()
        fig = plt.figure(1)
        plt.subplot(2, 2, 1)
        plt.plot(list(np.arange(self.n)+1), list(table.iloc[1:,0]))
        plt.title('Principal')
        plt.xlabel('Periods')
        plt.ylabel('$ Amount')
        plt.subplot(2, 2, 2)
        plt.plot(list(np.arange(self.n)+1), list(table.iloc[1:,1]))
        plt.title('Interest')
        plt.xlabel('Periods')
        plt.ylabel('$ Interest')
        plt.subplot(2, 2, 3)
        plt.plot(list(np.arange(self.n)+1), list(table.iloc[1:,3]))
        plt.title('Loan Value')
        plt.xlabel('Periods')
        plt.ylabel('$ Loan Value')
        plt.show()
        return fig






