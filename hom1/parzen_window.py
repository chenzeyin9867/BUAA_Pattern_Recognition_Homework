import random
import numpy as np
import matplotlib.pyplot as plt

'''
This program was coded by SY2006312 chenzeyin
'''

def gaussian_probability_diff(x, mu, std):
    return 1.0/(np.sqrt(2 * np.pi * std * std)) * np.exp(np.square(x - mu)/(-2 * np.square(std)))


def parzen_density_estimation(x, xi_list, mu, std):
    n = len(xi_list)
    sum = 0.0
    for t in xi_list:
        sum += gaussian_probability_diff(x, t, std)
    return sum / n

if __name__ == "__main__":
    seed = int(input("random_seed:"))
    np.random.seed(seed)
    mu, std = float(input("mu:")), float(input("std:"))
    
    sampleNum = int(input("num of samples:"))
    sampled_data = np.random.normal(mu, std, sampleNum)
    # print(sampled_data)
    # plt.hist(sampled_data, 30, normed=True)
    # plt.show()
    sampled_data = sorted(sampled_data)
    min_d = -20
    max_d = 20
    pdf = []
    for t in range(min_d, max_d):
        pdf.append(parzen_density_estimation(t, sampled_data, mu, std))
    
    x = np.arange(min_d, max_d)
    # plt.plot(x,pdf)
    # plt.show()    
    
    x_true = np.arange(min_d, max_d)
    pdf_true = []
    for t in range(min_d, max_d):
        pdf_true.append(gaussian_probability_diff(t, mu, std))
    
    plt.figure(figsize = (10,5))

    plt.subplot(1,2,1)
    plt.title("Gaussian hist mu:" + str(mu) + " std:" + str(std))
    plt.hist(sampled_data, 30, normed=True)

    plt.subplot(1,2,2)
    plt.title("Gaussian distribution")
    plt.plot(x, pdf_true, c='r',label='True gaussian distribution')
     
    # plt.subplot(1,3,3)
    # plt.title("Parzen Window Estimation:")
    plt.plot(x, pdf, c='g', label='Parzen Window Estimation')
    plt.legend()
    plt.savefig('./result2.png')
    plt.show()
    