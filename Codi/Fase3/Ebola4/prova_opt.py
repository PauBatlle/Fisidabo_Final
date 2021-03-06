import numpy as np
from scipy.optimize import fmin_bfgs

def rosen(X, info): #Rosenbrock function
    res = (1.0 - X[0])**2 + 100.0 * (X[1] - X[0]**2)**2 + \
           (1.0 - X[1])**2 + 100.0 * (X[2] - X[1]**2)**2


    # display information
    if info['Nfeval']%10 == 0:
        print ('{0:4d}   {1: 3.6f}   {2: 3.6f}   {3: 3.6f}   {4: 3.6f}'.format(info['Nfeval'], X[0], X[1], X[2], res))
    info['Nfeval'] += 1
    return res

print ('{0:4s}   {1:9s}   {2:9s}   {3:9s}   {4:9s}'.format('Iter', ' X1', ' X2', ' X3', 'f(X)'))
x0 = np.array([1.1, 1.1, 1.1], dtype=np.double)
[xopt, fopt, gopt, Bopt, func_calls, grad_calls, warnflg] = \
    fmin_bfgs(rosen, 
              x0, 
              args=({'Nfeval':0},), 
              maxiter=1000, 
              full_output=True, 
              retall=False,
              )