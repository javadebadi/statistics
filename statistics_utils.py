#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import scipy as sp

class Statistics_utils(object):
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import scipy as sp
    
    def __init__(self):
        print("course object is created!")

        

        
        
    # Chapter: sample mean and sample variance
    def distributions_example_sample_mean_and_sample_variance_generated_die_data(self,size=1):
        """
        input: size=sampel size
        output: 100000 data which average of size times rolling a die
        a function that generate 100000 data for die roll with sample size = size
        """

        die_min = 1    # minimum value a die can return
        die_max = 6    # maximum value a die can return
        n_sim = 100000   # number of times we run the simulation (rolling a die)
        data=[]
        for item in xrange(n_sim):
            temp = np.random.randint(low=die_min, high=die_max+1, size=size).sum()*(1.0/size)
            data.append(temp)
        return data
        
    def distributions_example_sample_mean_and_sample_variance_make_plot_title(self,size):
        """
        set titles for the plot for die problem

        """
        plt.title("N (sample size) = "+str(size))
        plt.xlabel("die value")
        plt.ylabel("frequency (normalized)")
        plt.xlim([0,7])
        return 
        
    def distributions_example_sample_mean_and_sample_variance_plot_for_die_samples(self,sizes=[1,2,6,30], n_bins=30):


        sub_plots_list=[221,222,223,224]
        fig = plt.figure(figsize=(10,10))
        counter = 0
        for size in sizes:
            data = self.distributions_example_sample_mean_and_sample_variance_generated_die_data(size=size)       
            plt.subplot(sub_plots_list[counter])
            #ax = fig.add_subplot(sub_plots_list[counter])
            self.distributions_example_sample_mean_and_sample_variance_make_plot_title(size)
            counter += 1
            # plot the histogram
            sns.distplot(data,bins=n_bins,kde=False)
        plt.tight_layout(h_pad=2.0,w_pad=2.0)
  










        
    # Chapter: P-Value (p-value)
    ## P-value: example: die
    ### a dictionry whcih contains probability of each outcome
    p_value_example_die_distiribution = {"1":1./2,"2":1./8,"3":1./8,"4":1./8,"5":1./16,"6":1./16}
    def p_value_example_die_distiribution_plot(self):
        die = self.p_value_example_die_distiribution
        # code for drawing probability density function
        fig = plt.figure(figsize=(6,4))
        ax = fig.add_axes()
        plt.xlabel("die roll value")
        plt.ylabel("probablity density")
        plt.title("Probability density function of the roll (null hypothesis)")
        x,y=zip(*sorted(die.items()))
        plt.plot(x,y,'bo')
        plt.show()

