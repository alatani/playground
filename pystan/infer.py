import pystan

schools_dat = {'J': 8,
               'y': [28,  8, -3,  7, -1,  1, 18, 12],
               'sigma': [15, 10, 16, 11,  9, 11, 10, 18]}

if __name__=="__main__":

    model = pystan.StanModel("./8schools.stan")
    fit = model.sampling(data=schools_dat, iter=1000, chains=4)

    la = fit.extract(permuted=True)  # return a dictionary of arrays
    mu = la['mu']

    ## return an array of three dimensions: iterations, chains, parameters
    a = fit.extract(permuted=False)
    print(fit)
    print("mu",mu)
    print("a",a)
    pass
