import sys, math, util

"""
f_k is a counter where the key are k
a list of f_k represents the passage of time
where the index is t
"""
def forward(model, emissions):
    f = util.Counter()
    for state in model.getStates():
        f[state] = model.p(state)*model.e(state, emissions[0])  
    for b in emissions[1:]:
        f_next = util.Counter()
        for state_l in model.getStates():
            f_next[state_l] = model.e(state_l, b) * sum([model.a(state_k, state_l)*f[state_k] for state_k in model.getStates()])
        f = f_next.copy()
    return f.totalCount()
    
    
def backward(model, emissions):
    b = util.Counter()
    #minor initialization nuance
    for state in model.getStates() : b[state] = 1
    emissions.reverse()
    for q in emissions[len(emissions)-1]:
        b_prev = util.Counter()
        for state_k in model.getStates():
            b_prev[state_k] = sum([model.a(state_k, state_l)*model.e(state_l, q)*b[state_l] for state_l in model.getStates()])
        b = b_prev.copy()
    for state in model.getStates():
        b[state] = model.p(state)*model.e(state, emissions[len(emissions)-1])*b[state]
    return b.totalCount()
    
    

