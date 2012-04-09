import sys, math

def forward(HMM, emissions):
    f = {}
    f[0] = {}
    f[0][0] = 1
    for k in HMM.getS:
        f[l] = {}
        f[k][0] = 0
    for t in range(1, len(emissions)+1):
        for l in HMM.getS:
            sum = 0.0
            for k in HMM.getS:
                sum += (f[k][t-1]*HMM.a(k,l))
            f[l][t] = HMM.e(l,emissions[t])*

