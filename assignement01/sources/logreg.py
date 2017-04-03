#!/usr/bin/env python
import numpy as np
from logreg_toolbox import sig

__author__ = 'bellec, subramoney'

"""
Computational Intelligence TU - Graz
Assignment: Linear and Logistic Regression
Section: Gradient descent (GD) (Logistic Regression)
TODO Fill the cost function and the gradient
"""
def safe_ln(x, minval=0.0000000001):
    return np.log(x.clip(min=minval))

def sigmoid(X):
    return 1. / (1 + np.exp(-X))

def cost(theta, x, y):
    """
    Cost of the logistic regression function.

    :param theta: parameter(s)
    :param x: sample(s)
    :param y: target(s)
    :return: cost
    """

    N, n = x.shape
    
    yPred = sigmoid(x.dot(theta))
    cost = -y.T.dot(safe_ln(yPred)) - (1 - y).T.dot(safe_ln(1 - yPred))

    #print("coût: {}".format(cost))

    return cost/N


def grad(theta, x, y):
    """

    Compute the gradient of the cost of logistic regression

    :param theta: parameter(s)
    :param x: sample(s)
    :param y: target(s)
    :return: gradient
    """
    N, n = x.shape
    g = np.zeros(theta.shape)
    # matrice multiplication solution
    yPred = sigmoid(x.dot(theta))
    for i in range(n):
        g[i] = (1/N)*np.sum((yPred - y).dot(x[:,i]));

    return g
