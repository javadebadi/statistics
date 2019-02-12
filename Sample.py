
# coding: utf-8

# # Sample Class
# a class that computes the sample mean and sample variance of an observation of

# In[64]:


class Sample(object):
    
    # Class Object Attributes
    
    # initializer
    def __init__(self, data):
        self.data = data     # we assume that data is a list
    # deconstructer
    def __del__(self):
        pass
    
    def merge_two_data(self, other_data):
        for item in other_data:
            (self.data).append(item)
    
    def set_data(self, new_data):
        self.data = new_data
        
    def get_data(self):
        return self.data
    
    def length(self):
        return len(self.data)
    
    def sample_mean(self):
        temp = 0.0
        for item in self.data:
            temp = temp + item
        temp = (1.0*temp)/(self.length())
        return temp
    
    def sample_variance(self):
        temp = 0.0
        for X in self.data:
            temp = 0
            Xbar = self.sample_mean()
            temp = temp + (X - Xbar)**2
        temp = (1.0*temp)/(self.length()-1)
        return temp
            


# In[73]:


new = Sample([1,2,3])


# In[74]:


new.length()


# In[75]:


new.sample_mean()


# In[76]:


new.sample_variance()


# In[77]:


new.get_data()


# In[78]:


new.merge_two_data([5,6,9])


# In[79]:


new.get_data()


# In[80]:


del new

