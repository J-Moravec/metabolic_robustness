# metabolic_robustness/utils/normdist.py

from scipy.stats import truncnorm
from scipy.stats import norm
from math import sqrt


def truncnorm_pdf(x, mean, var, min, max):
    a, b = _truncnorm_params_transform(mean, var, min, max)
    val = truncnorm.pdf(
        x, a, b,
        loc = mean,
        scale = sqrt(var),
        )
    return(val)


def truncnorm_sample(mean, var, min, max):
    a, b = _truncnorm_params_transform(mean, var, min, max)
    val = truncnorm.rvs(
        a, b,
        loc = mean,
        scale = sqrt(var),
        )
    return(val)


def _truncnorm_params_transform(mean, var, min, max):
    a = (min - mean) / sqrt(var)
    b = (max - mean) / sqrt(var)
    return(a, b)


def norm_pdf(x, mean, var):
    val = norm.pdf(x, loc=mean, scale=sqrt(var))
    return(val)


def norm_sample(mean, var):
    val = norm.rvs(
        loc = mean,
        scale = sqrt(var)
        )
    return(val)
