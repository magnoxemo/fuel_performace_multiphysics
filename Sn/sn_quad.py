import numpy as np
import scipy as sp
def Sn_quadrature(n):
    
    def newton_raphson(n, x0, tol=1e-11, max_iter=10000):
        coeffs=sp.special.legendre(n)
        for _ in range(max_iter):
            f = np.polyval(coeffs, x0)
            f_prime = np.polyval(np.polyder(coeffs), x0)
            x1 = x0 - f / f_prime
            if abs(x1 - x0) < tol:
                return x1
            x0 = x1
        
        raise ValueError("Did not converge within the maximum number of iterations")

    x=np.linspace(-1,1,n)
    """this program only works when n is n=2
    
    I think the main reason is the polynomial solver. And the problem is caused by the initial guess.
    aparently the solution of legendre polynomial --> nodes aren't unifromly distributed within the interval of [-1,1] """
    angles=np.zeros(n)
    weights=np.zeros(n)
    for _ in range(n):
        angles[_]=(newton_raphson(n, x0=x[_]))
        weights[_]=(2*(1-angles[_]**2))/((n+1)*(np.polyval(sp.special.legendre(n+1),angles[_])))**2
    return angles,weights


