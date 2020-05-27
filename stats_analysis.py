import numpy as np
from scipy.stats import ttest_ind
from scipy.stats import shapiro
from scipy.stats import normaltest
import seaborn as sns 
import matplotlib.pyplot as plt

#check sample for normal distribution using shapiro-wilk test and D'Agostinos's K^2 test
#note gaussian means normal distribution 
def check_normality(sample):
    #using an alpha of 5% for 95% confidence
    alpha = 0.05
    print('H0: sample is normally distributed')
    print('H1: sample is not normally distributed')
    print('Sample size=%.3f' % (len(sample)))
    print('Using an Alpha of %.2f' % (alpha))
    #shapiro-wilk test
    stat, p = shapiro(sample)
    print('shapiro-wilk Statistics=%.3f, p=%.3f' % (stat, p))
    if p > alpha:
        print('wilk-shaprio test: fail to reject H0, sample appears to be gaussian')
    else:
        print('wilk-shaprio test: reject H0, sample not gaussian')
        
    #D'Agostino's K^2 test
    if len(sample) >= 20:
        stat, p = normaltest(sample)
        print('D Agostinos K^2 test Statistics=%.3f, p=%.3f' % (stat, p))
        if p > alpha:
            print('D Agostinos K^2 test: fail to reject H0, sample appears to be gaussian')
        else:
            print('D Agostinos K^2 test: reject H0, sample not gaussian')
    else:
        print('Not enough samples for D Agostinos K^2 test')


#t-test, two tailed for difference of means between two independent samples
#alpha of 5% for 95% confidence
#not assuming equal variance in samples
def students_two_tailed(sample_1, sample_2):
    print('H0: sample 1 mean = sample 2 mean')
    print('H1: sample 1 mean != sample 2 mean')
    alpha = 0.05
    print('sample 1: mean=%.3f stdv=%.3f' % (np.mean(sample_1), np.std(sample_1)))
    print('sample 2: mean=%.3f stdv=%.3f' % (np.mean(sample_2), np.std(sample_2)))
    stat, p = ttest_ind(sample_1, sample_2, equal_var=False)
    print('Using an alpha of: %.2f' % (alpha))
    print('T Statistics=%.3f, p=%.3f' % (stat, p))
    if p > alpha:
        print('fail to reject H0, sample means are equal')
    else:
        print('reject H0, samples means are not equal')


#t-test, one tailed test to see if sample 1 mean > sample 2 mean
#using standard alpha of 5% for 95% confidence
#scipy.stats.ttest_ind is a two tailed test, so we divide the p-value(probability)/2 for one tailed test result
#not assuming equal variance in samples
def students_one_tailed(sample_1, sample_2):
    print('H0: sample 1 mean <= sample 2 mean')
    print('H1: sample 1 mean > sample 2 mean')
    alpha = 0.05
    print('sample 1: mean=%.3f stdv=%.3f' % (np.mean(sample_1), np.std(sample_1)))
    print('sample 2: mean=%.3f stdv=%.3f' % (np.mean(sample_2), np.std(sample_2)))
    stat, p = ttest_ind(sample_1, sample_2, equal_var=False)
    p_2 = p/2
    print('Using an alpha of: %.2f' % (alpha))
    print('T Statistics=%.3f, p=%.3f' % (stat, p_2))
    if p_2 > alpha:
        print('fail to reject H0, sample 1 mean <= sample 2 mean')
    else:
        print('reject H0, sample 1 mean > sample 2 mean')

#plot two seaborn distplots side by side
#inputs are pandas series for experiment and control
#font size for title font
def side_by_side_distplt(experiment_data, control_data, font_size):
    fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=True)
    ax1.set_title('Experiment')
    ax2.set_title('Control')
    sns.distplot(experiment_data, ax=ax1)
    sns.distplot(control_data, ax=ax2)
