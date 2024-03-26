import numpy as np
#import random

#Define the conversion rates and nr of samples
conversion_rates = [0.05, 0.13, 0.09, 0.16, 0.11, 0.04, 0.22, 0.08, 0.21]
n = 10000
d = len(conversion_rates)

#creating the dataset
x = np.zeros((n,d))
for i in range(n):
    for j in range(d):
        if np.random.rand() <= conversion_rates[j]:
            x[i][j]=1
#print(x)
            
#make arrays to count the subscriptions and non subscriptions
n_pos_reward = np.zeros(d)
n_neg_reward = np.zeros(d)

#using beta distribution to pick the best strategy and update the reward values
for i in range(n):
    selected = 0
    max_random = 0
    for j in range(0,d):
        random_beta = np.random.beta(n_pos_reward[j] + 1, n_neg_reward[j] + 1)
        #random_beta = random.betavariate(n_pos_reward[j] + 1, n_neg_reward[j] + 1)
        if random_beta > max_random:
            max_random = random_beta
            selected = j
    if x[i][selected]==1:
        n_pos_reward[selected]+=1
    else:
        n_neg_reward[selected]+=1
        
#showing which strategy is considered to be the best
n_selected = n_pos_reward + n_neg_reward
for i in range(d):
    print("Strategy nr " + str(i+1) + " was selected " + str(n_selected[i]) + " times.")
print("Conclusion: Best strategy is strategy number " + str(np.argmax(n_selected) + 1))
