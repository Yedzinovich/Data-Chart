import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


height_weight_age = [70, 170, 40]
height_weight_age_1 = [90, 180, 37]
grades = [95, 80, 75, 62]
grades_1 = [98, 99, 60]

#add two vectors
def vector_add(v, w):
    return [v_i + w_i 
            for v_i, w_i in zip(v, w)]

#subtract two vectors
def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

#sum of all elemnts in vector
def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
        return result

#scalar multiply: vector by scala
def scalar_multyply(c, vectors):
    return [c*i for i in vectors]    

#componentwise mean of the list(vector)
def vector_mean(vectors):
    n = len(vectors)
    return scalar_multyply(1/n, vector_sum(vectors))

def printVector(vectors):
    for v in vectors:
        print(v)
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))
