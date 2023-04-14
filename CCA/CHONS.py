import numpy as np

def CHONS(TS, VS, LP, PR, SU, LG, HCE, BD):
    c = [0.069, 0.135, 0.001, 0.123, -0.034, -0.069, 0.088, 2.175, 25.154]
    n = [6.76e-5, 0.012, 0.030, 0.174, 0.032, 0.023, -0.006, -3.401, 0.701]
    h = [0.003, 0.025, 0.015, 0.011, 6.06e-4, 0.012, 0.024, -0.170, 3.261]
    o = [-0.072, -0.179, -0.051, -0.352, -0.008, 0.029, -0.108, 1.491, 71.351]

    if type(TS) == type(0):
        pass
    elif type(TS) == type(0.1):
        pass
    else:
        assert len(TS)  == len(VS)
        assert len(VS)  == len(LP)
        assert len(LP)  == len(PR)
        assert len(PR)  == len(SU)
        assert len(SU)  == len(LG)
        assert len(LG)  == len(HCE)
        assert len(HCE) == len(BD)
    
        C = np.empty(shape = (len(VS), 1))
        H = np.empty(shape = (len(VS), 1))
        O = np.empty(shape = (len(VS), 1))
        N = np.empty(shape = (len(VS), 1))
        S = np.empty(shape = (len(VS), 1))

        for i in range(len(VS)):
            C[i] = TS[i]*c[0] + VS[i]*c[1] + LP[i]*c[2] + PR[i]*c[3] + SU[i]*c[4] + LG[i]*c[5] + HCE[i]*c[6] + BD[i]*c[7] + c[8]
            H[i] = TS[i]*h[0] + VS[i]*h[1] + LP[i]*h[2] + PR[i]*h[3] + SU[i]*h[4] + LG[i]*h[5] + HCE[i]*h[6] + BD[i]*h[7] + h[8]
            O[i] = TS[i]*o[0] + VS[i]*o[1] + LP[i]*o[2] + PR[i]*o[3] + SU[i]*o[4] + LG[i]*o[5] + HCE[i]*o[6] + BD[i]*o[7] + o[8]
            N[i] = TS[i]*n[0] + VS[i]*n[1] + LP[i]*n[2] + PR[i]*n[3] + SU[i]*n[4] + LG[i]*n[5] + HCE[i]*n[6] + BD[i]*n[7] + n[8]
            S[i] = 100 - C[i] - H[i] - O[i] - N[i]
            
    C = TS*c[0] + VS*c[1] + LP*c[2] + PR*c[3] + SU*c[4] + LG*c[5] + HCE*c[6] + BD*c[7] + c[8]
    H = TS*h[0] + VS*h[1] + LP*h[2] + PR*h[3] + SU*h[4] + LG*h[5] + HCE*h[6] + BD*h[7] + h[8]
    O = TS*o[0] + VS*o[1] + LP*o[2] + PR*o[3] + SU*o[4] + LG*o[5] + HCE*o[6] + BD*o[7] + o[8]
    N = TS*n[0] + VS*n[1] + LP*n[2] + PR*n[3] + SU*n[4] + LG*n[5] + HCE*n[6] + BD*n[7] + n[8]
    S = 100 - C - H - O - N
    
    dict = {
    'C': C,
    'H': H,
    'O': O,
    'N': N,
    'S': S
    }
    
    return dict