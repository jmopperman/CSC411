import scipy.optimize
import numpy as np
import timeit
from random import gauss


def add_noise(ydata, sigma):
    sig = np.linspace(0,sigma,10)  # specifying sigma determines the range 
                                    # of noise to be invesitgated, with 10 variations each time.
    otpts = ydata                   # The clean data is returned here for simplicity later.            
    for s in sig:
        noise = []
        for i in range(len(ydata)):
            noise.append(gauss(1,s))
        yn = ydata + noise
        otpts = np.vstack((otpts, yn)) # stacked arrays of output data with varying degeres of noise
    return otpts, sig

def ARX(A, B, Y, U):
    return A.dot(Y) + B.dot(U)

def OF_gen(ydata, udata, m, n):
    ydev = ydata - ydata[0]
    udev = udata - udata[0]
    def OF(x):
        A, B = x[:m], x[m:]

        ydev_app = np.concatenate([[0]*m, ydev])
        udev_app = np.concatenate([[0]*n, udev]) 

        summ = 0
        for j in range(len(ydev)):
            k = j + m
            l = j + n

            Y = np.flip(ydev_app[j:k])
            U = np.flip(udev_app[j:l])
            yt = ARX(A, B, Y, U)
            summ += (ydev[j] - yt)**2

        return summ
    return OF

def simulate(coefficients, Uinput, m, n):
    udev = Uinput - Uinput[0]
    A, B = coefficients[:m], coefficients[m:]
    Youtput = []
    for i in range(len(udev)):
        if i < len(B):
            U = [0]*(len(B) - i) + list(udev[:i])
        else:
            j = i - len(B)
            U = list(udev[j:i])
        U.reverse()

        if i < len(A):
            Y = [0]*(len(A) - len(Youtput)) + Youtput
        else:
            Y = Youtput[-len(A):]
        Y.reverse()

        yt =ARX(A, B, Y, U)
        Youtput.append(yt)
    return Youtput

def DE_rt_coeffs(bounds, ydata, udata, m, n):
    OF = OF_gen(ydata, udata, m, n)        
    
    start = timeit.default_timer()
    coeff = scipy.optimize.differential_evolution(OF, bounds).x
    end = timeit.default_timer()
    
    runtime = end - start
       
    return runtime, coeff

def MIN_rt_coeffs(ig, ydata, udata, m, n, met=None): #ig = initial guess and met=method
    OF = OF_gen(ydata, udata, m, n)        
    
    start = timeit.default_timer()
    coeff = scipy.optimize.minimize(OF, ig, method=met).x
    end = timeit.default_timer()
    
    runtime = end - start
       
    return runtime, coeff

def LSTSQ_rt_coeffs(ig, ydata, udata, m, n): #ig = initial guess and met=method
    OF = OF_gen(ydata, udata, m, n)        
    
    start = timeit.default_timer()
    coeff = scipy.optimize.least_squares(OF, ig).x
    end = timeit.default_timer()
    
    runtime = end - start
       
    return runtime, coeff

ID_techs= [DE_rt_coeffs, MIN_rt_coeffs, LSTSQ_rt_coeffs]


