def getP(l, X, c):
    total = len(l)
    
    count_c = sum(1 for i in l if i[-1] == c)
    
    prob_c = count_c / total
    
    prob_x_given_c = 1.0
    for xi in X:
        count_xi_given_c = sum(1 for i in l if xi in i[:-1] and i[-1] == c)
        prob_xi_given_c = count_xi_given_c / count_c
        prob_x_given_c *= prob_xi_given_c
    
    posterior_prob = prob_c * prob_x_given_c
    
    return posterior_prob