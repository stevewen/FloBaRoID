import numpy as np
from math import sin, cos

#robotran generated model for one arm of walk-man
#writes (numeric) dynamics regressor for one system state into PHI_t

def idinvbar(PHI_t, q, qd, qdd):
    #double PHI_t[7][48], double q[10],double qd[10], double qdd[10]

    # points of the kinematic chain
    #(whats this?)
    d = np.array(
        [
        [  0.,	 0.,	0., 	0.,    	0.,		0.,     0.,			0.,		0.,		0.],
        [  0.,	 0.,    0., 	0.,     0.,     0.,  0.036,		-0.075,		0.,		0.],
        [  0.,	 0.,	0., 	0.,-0.10914,	0., 	0.,			0.,		0.,		0.],
        [  0.,	 0.,	0., 	0., -0.053,	-0.222,  -0.15,	   -0.1955,	    0.,	-0.092]
        ]
    )

    # gravity
    g = [0.0, 0.0, -9.81, 0.0]
    PHI = np.zeros((10, 49))

    # Trigonometric Variables
    S1 = sin(q[1])
    C1 = cos(q[1])
    S2 = sin(q[2])
    C2 = cos(q[2])
    S3 = sin(q[3])
    C3 = cos(q[3])
    S4 = sin(q[4])
    C4 = cos(q[4])
    S5 = sin(q[5])
    C5 = cos(q[5])
    S6 = sin(q[6])
    C6 = cos(q[6])
    S7 = sin(q[7])
    C7 = cos(q[7])
    S8 = sin(q[8])
    C8 = cos(q[8])
    S9 = sin(q[9])
    C9 = cos(q[9])

    # Forward Kinematics

    ALS21 = -g[3]*S1
    ALS31 = -g[3]*C1
    ALS12 = ALS21*S2
    ALS22 = ALS21*C2
    BS93 = -qd[3]*qd[3]
    ALS13 = ALS12*C3-ALS31*S3
    ALS33 = ALS12*S3+ALS31*C3
    OM24 = qd[3]*C4
    OM34 = -qd[3]*S4
    OMP24 = -qd[3]*qd[4]*S4+qdd[3]*C4
    OMP34 = -qd[3]*qd[4]*C4-qdd[3]*S4
    BS24 = qd[4]*OM24
    BS34 = qd[4]*OM34
    BS54 = -qd[4]*qd[4]-OM34*OM34
    BS64 = OM24*OM34
    BS94 = -qd[4]*qd[4]-OM24*OM24
    BETA24 = BS24-OMP34
    BETA34 = BS34+OMP24
    BETA64 = -qdd[4]+BS64
    BETA84 = qdd[4]+BS64
    ALS14 = ALS13+qdd[3]*d[3][4]
    ALS24 = ALS22*C4+S4*(ALS33+BS93*d[3][4])
    ALS34 = -ALS22*S4+C4*(ALS33+BS93*d[3][4])
    OM15 = qd[4]*C5+OM24*S5
    OM25 = -qd[4]*S5+OM24*C5
    OM35 = qd[5]+OM34
    OMP15 = C5*(qdd[4]+qd[5]*OM24)+S5*(OMP24-qd[4]*qd[5])
    OMP25 = C5*(OMP24-qd[4]*qd[5])-S5*(qdd[4]+qd[5]*OM24)
    OMP35 = qdd[5]+OMP34
    BS15 = -OM25*OM25-OM35*OM35
    BS25 = OM15*OM25
    BS35 = OM15*OM35
    BS55 = -OM15*OM15-OM35*OM35
    BS65 = OM25*OM35
    BS95 = -OM15*OM15-OM25*OM25
    BETA25 = BS25-OMP35
    BETA35 = BS35+OMP25
    BETA45 = BS25+OMP35
    BETA65 = BS65-OMP15
    BETA75 = BS35-OMP25
    BETA85 = BS65+OMP15
    ALS15 = C5*(ALS14+BETA34*d[3][5])+S5*(ALS24+BETA64*d[3][5])
    ALS25 = C5*(ALS24+BETA64*d[3][5])-S5*(ALS14+BETA34*d[3][5])
    ALS35 = ALS34+BS94*d[3][5]
    OM16 = OM15*C6-OM35*S6
    OM26 = qd[6]+OM25
    OM36 = OM15*S6+OM35*C6
    OMP16 = C6*(OMP15-qd[6]*OM35)-S6*(OMP35+qd[6]*OM15)
    OMP26 = qdd[6]+OMP25
    OMP36 = C6*(OMP35+qd[6]*OM15)+S6*(OMP15-qd[6]*OM35)
    BS16 = -OM26*OM26-OM36*OM36
    BS26 = OM16*OM26
    BS36 = OM16*OM36
    BS66 = OM26*OM36
    BS96 = -OM16*OM16-OM26*OM26
    BETA36 = BS36+OMP26
    BETA46 = BS26+OMP36
    BETA66 = BS66-OMP16
    BETA76 = BS36-OMP26
    ALS16 = C6*(ALS15+BETA35*d[3][6]+BS15*d[1][6])-S6*(ALS35+BETA75*d[1][6]+BS95*d[3][6])
    ALS26 = ALS25+BETA45*d[1][6]+BETA65*d[3][6]
    ALS36 = C6*(ALS35+BETA75*d[1][6]+BS95*d[3][6])+S6*(ALS15+BETA35*d[3][6]+BS15*d[1][6])
    OM17 = OM16*C7+OM26*S7
    OM27 = -OM16*S7+OM26*C7
    OM37 = qd[7]+OM36
    OMP17 = C7*(OMP16+qd[7]*OM26)+S7*(OMP26-qd[7]*OM16)
    OMP27 = C7*(OMP26-qd[7]*OM16)-S7*(OMP16+qd[7]*OM26)
    OMP37 = qdd[7]+OMP36
    BS17 = -OM27*OM27-OM37*OM37
    BS27 = OM17*OM27
    BS37 = OM17*OM37
    BS57 = -OM17*OM17-OM37*OM37
    BS67 = OM27*OM37
    BETA27 = BS27-OMP37
    BETA47 = BS27+OMP37
    BETA77 = BS37-OMP27
    BETA87 = BS67+OMP17
    ALS17 = C7*(ALS16+BETA36*d[3][7]+BS16*d[1][7])+S7*(ALS26+BETA46*d[1][7]+BETA66*d[3][7])
    ALS27 = C7*(ALS26+BETA46*d[1][7]+BETA66*d[3][7])-S7*(ALS16+BETA36*d[3][7]+BS16*d[1][7])
    ALS37 = ALS36+BETA76*d[1][7]+BS96*d[3][7]
    OM18 = OM17*C8-OM37*S8
    OM28 = qd[8]+OM27
    OM38 = OM17*S8+OM37*C8
    OMP18 = C8*(OMP17-qd[8]*OM37)-S8*(OMP37+qd[8]*OM17)
    OMP28 = qdd[8]+OMP27
    OMP38 = C8*(OMP37+qd[8]*OM17)+S8*(OMP17-qd[8]*OM37)
    BS18 = -OM28*OM28-OM38*OM38
    BS28 = OM18*OM28
    BS38 = OM18*OM38
    BS68 = OM28*OM38
    BS98 = -OM18*OM18-OM28*OM28
    BETA38 = BS38+OMP28
    BETA48 = BS28+OMP38
    BETA68 = BS68-OMP18
    BETA78 = BS38-OMP28
    ALS18 = ALS17*C8-ALS37*S8
    ALS38 = ALS17*S8+ALS37*C8
    OM19 = qd[9]+OM18
    OM29 = OM28*C9+OM38*S9
    OM39 = -OM28*S9+OM38*C9
    OMP19 = qdd[9]+OMP18
    OMP29 = C9*(OMP28+qd[9]*OM38)+S9*(OMP38-qd[9]*OM28)
    OMP39 = C9*(OMP38-qd[9]*OM28)-S9*(OMP28+qd[9]*OM38)
    BS29 = OM19*OM29
    BS39 = OM19*OM39
    BS59 = -OM19*OM19-OM39*OM39
    BS69 = OM29*OM39
    BS99 = -OM19*OM19-OM29*OM29
    BETA29 = BS29-OMP39
    BETA39 = BS39+OMP29
    BETA69 = BS69-OMP19
    BETA89 = BS69+OMP19
    ALS19 = ALS18+BETA38*d[3][9]
    ALS29 = C9*(ALS27+BETA68*d[3][9])+S9*(ALS38+BS98*d[3][9])
    ALS39 = C9*(ALS38+BS98*d[3][9])-S9*(ALS27+BETA68*d[3][9])

    # Backward Dynamics

    pd55CF19 = OMP29-OM19*OM39
    pd56CF19 = OMP39+OM19*OM29
    pd57CF19 = -2.000*OM29*OM39
    pd58CF19 = OM29*OM29-OM39*OM39
    pd54CF29 = OM19*OM39
    pd55CF29 = OMP19+OM29*OM39
    pd56CF29 = -OM19*OM19+OM39*OM39
    pd57CF29 = OMP29+OM19*OM39
    pd58CF29 = OMP39-OM19*OM29
    pd54CF39 = -OM19*OM29
    pd55CF39 = OM19*OM19-OM29*OM29
    pd56CF39 = OMP19-OM29*OM39
    pd57CF39 = -OMP39+OM19*OM29
    pd58CF39 = OMP29+OM19*OM39
    pd52GS28 = -BETA89*S9+BS59*C9
    pd53GS28 = BETA69*C9-BS99*S9
    pd52GS38 = BETA89*C9+BS59*S9
    pd53GS38 = BETA69*S9+BS99*C9
    pd46CF18 = OMP28-OM18*OM38
    pd47CF18 = OMP38+OM18*OM28
    pd48CF18 = -OM28*OM38
    pd49CF18 = OM28*OM28-OM38*OM38
    pd50CF18 = -OMP18+OM28*OM38
    pd52CF18 = ALS39-d[3][9]*(-BETA89*S9+BS59*C9)
    pd53CF18 = -ALS29-d[3][9]*(BETA69*C9-BS99*S9)
    pd46CF28 = OMP18+OM28*OM38
    pd47CF28 = -OM18*OM18+OM38*OM38
    pd49CF28 = OMP38-OM18*OM28
    pd50CF28 = -2.000*OM18*OM38
    pd52CF28 = ALS19*S9+BETA29*d[3][9]
    pd53CF28 = ALS19*C9+BETA39*d[3][9]
    pd54CF28 = pd54CF29*C9-pd54CF39*S9
    pd55CF28 = pd55CF29*C9-pd55CF39*S9
    pd56CF28 = pd56CF29*C9-pd56CF39*S9
    pd57CF28 = pd57CF29*C9-pd57CF39*S9
    pd58CF28 = pd58CF29*C9-pd58CF39*S9
    pd46CF38 = OM18*OM18-OM28*OM28
    pd47CF38 = OMP18-OM28*OM38
    pd48CF38 = OM18*OM28
    pd49CF38 = OMP28+OM18*OM38
    pd50CF38 = OMP38+OM18*OM28
    pd52CF38 = -ALS19*C9
    pd53CF38 = ALS19*S9
    pd54CF38 = pd54CF29*S9+pd54CF39*C9
    pd55CF38 = pd55CF29*S9+pd55CF39*C9
    pd56CF38 = pd56CF29*S9+pd56CF39*C9
    pd57CF38 = pd57CF29*S9+pd57CF39*C9
    pd58CF38 = pd58CF29*S9+pd58CF39*C9
    pd44GS17 = BETA78*S8+BS18*C8
    pd45GS17 = BETA38*C8+BS98*S8
    pd52GS17 = BETA29*C8+pd52GS38*S8
    pd53GS17 = BETA39*C8+pd53GS38*S8
    pd44GS37 = BETA78*C8-BS18*S8
    pd45GS37 = -BETA38*S8+BS98*C8
    pd52GS37 = -BETA29*S8+pd52GS38*C8
    pd53GS37 = -BETA39*S8+pd53GS38*C8
    pd38CF17 = OMP17+OM27*OM37
    pd39CF17 = OMP27-OM17*OM37
    pd40CF17 = OMP37+OM17*OM27
    pd41CF17 = OM27*OM27-OM37*OM37
    pd42CF17 = OM27*OM37
    pd44CF17 = ALS27*S8
    pd45CF17 = -ALS27*C8
    pd46CF17 = pd46CF18*C8+pd46CF38*S8
    pd47CF17 = pd47CF18*C8+pd47CF38*S8
    pd48CF17 = pd48CF18*C8+pd48CF38*S8
    pd49CF17 = pd49CF18*C8+pd49CF38*S8
    pd50CF17 = pd50CF18*C8+pd50CF38*S8
    pd52CF17 = pd52CF18*C8+pd52CF38*S8
    pd53CF17 = pd53CF18*C8+pd53CF38*S8
    pd54CF17 = OMP19*C8+pd54CF38*S8
    pd55CF17 = pd55CF19*C8+pd55CF38*S8
    pd56CF17 = pd56CF19*C8+pd56CF38*S8
    pd57CF17 = pd57CF19*C8+pd57CF38*S8
    pd58CF17 = pd58CF19*C8+pd58CF38*S8
    pd38CF27 = -OMP27+OM17*OM37
    pd39CF27 = OMP17+OM27*OM37
    pd40CF27 = -OM17*OM17+OM37*OM37
    pd41CF27 = OMP37-OM17*OM27
    pd42CF27 = -OM17*OM37
    pd38CF37 = -2.000*OM17*OM27
    pd39CF37 = OM17*OM17-OM27*OM27
    pd40CF37 = OMP17-OM27*OM37
    pd41CF37 = OMP27+OM17*OM37
    pd44CF37 = ALS27*C8
    pd45CF37 = ALS27*S8
    pd46CF37 = -pd46CF18*S8+pd46CF38*C8
    pd47CF37 = -pd47CF18*S8+pd47CF38*C8
    pd48CF37 = -pd48CF18*S8+pd48CF38*C8
    pd49CF37 = -pd49CF18*S8+pd49CF38*C8
    pd50CF37 = -pd50CF18*S8+pd50CF38*C8
    pd52CF37 = -pd52CF18*S8+pd52CF38*C8
    pd53CF37 = -pd53CF18*S8+pd53CF38*C8
    pd54CF37 = -OMP19*S8+pd54CF38*C8
    pd55CF37 = -pd55CF19*S8+pd55CF38*C8
    pd56CF37 = -pd56CF19*S8+pd56CF38*C8
    pd57CF37 = -pd57CF19*S8+pd57CF38*C8
    pd58CF37 = -pd58CF19*S8+pd58CF38*C8
    pd36GS16 = -BETA47*S7+BS17*C7
    pd37GS16 = BETA27*C7-BS57*S7
    pd44GS16 = -BETA48*S7+pd44GS17*C7
    pd45GS16 = -BETA68*S7+pd45GS17*C7
    pd52GS16 = pd52GS17*C7-pd52GS28*S7
    pd53GS16 = pd53GS17*C7-pd53GS28*S7
    pd36GS26 = BETA47*C7+BS17*S7
    pd37GS26 = BETA27*S7+BS57*C7
    pd44GS26 = BETA48*C7+pd44GS17*S7
    pd45GS26 = BETA68*C7+pd45GS17*S7
    pd52GS26 = pd52GS17*S7+pd52GS28*C7
    pd53GS26 = pd53GS17*S7+pd53GS28*C7
    pd30CF16 = OMP26-OM16*OM36
    pd31CF16 = OMP36+OM16*OM26
    pd32CF16 = -OM26*OM36
    pd33CF16 = OM26*OM26-OM36*OM36
    pd34CF16 = -OMP16+OM26*OM36
    pd36CF16 = ALS37*S7-d[3][7]*(BETA47*C7+BS17*S7)
    pd37CF16 = ALS37*C7-d[3][7]*(BETA27*S7+BS57*C7)
    pd38CF16 = pd38CF17*C7-pd38CF27*S7
    pd39CF16 = pd39CF17*C7-pd39CF27*S7
    pd40CF16 = pd40CF17*C7-pd40CF27*S7
    pd41CF16 = pd41CF17*C7-pd41CF27*S7
    pd42CF16 = pd42CF17*C7-pd42CF27*S7
    pd44CF16 = ALS38*S7+pd44CF17*C7-d[3][7]*(BETA48*C7+pd44GS17*S7)
    pd45CF16 = -ALS18*S7+pd45CF17*C7-d[3][7]*(BETA68*C7+pd45GS17*S7)
    pd46CF16 = pd46CF17*C7-pd46CF28*S7
    pd47CF16 = pd47CF17*C7-pd47CF28*S7
    pd48CF16 = -OMP28*S7+pd48CF17*C7
    pd49CF16 = pd49CF17*C7-pd49CF28*S7
    pd50CF16 = pd50CF17*C7-pd50CF28*S7
    pd52CF16 = pd52CF17*C7-pd52CF28*S7-d[3][7]*(pd52GS17*S7+pd52GS28*C7)
    pd53CF16 = pd53CF17*C7-pd53CF28*S7-d[3][7]*(pd53GS17*S7+pd53GS28*C7)
    pd54CF16 = pd54CF17*C7-pd54CF28*S7
    pd55CF16 = pd55CF17*C7-pd55CF28*S7
    pd56CF16 = pd56CF17*C7-pd56CF28*S7
    pd57CF16 = pd57CF17*C7-pd57CF28*S7
    pd58CF16 = pd58CF17*C7-pd58CF28*S7
    pd30CF26 = OMP16+OM26*OM36
    pd31CF26 = -OM16*OM16+OM36*OM36
    pd33CF26 = OMP36-OM16*OM26
    pd34CF26 = -2.000*OM16*OM36
    pd36CF26 = -ALS37*C7-BETA77*d[1][7]+d[3][7]*(-BETA47*S7+BS17*C7)
    pd37CF26 = ALS37*S7-BETA87*d[1][7]+d[3][7]*(BETA27*C7-BS57*S7)
    pd38CF26 = pd38CF17*S7+pd38CF27*C7
    pd39CF26 = pd39CF17*S7+pd39CF27*C7
    pd40CF26 = pd40CF17*S7+pd40CF27*C7
    pd41CF26 = pd41CF17*S7+pd41CF27*C7
    pd42CF26 = pd42CF17*S7+pd42CF27*C7
    pd44CF26 = -ALS38*C7+pd44CF17*S7-pd44GS37*d[1][7]+d[3][7]*(-BETA48*S7+pd44GS17*C7)
    pd45CF26 = ALS18*C7+pd45CF17*S7-pd45GS37*d[1][7]+d[3][7]*(-BETA68*S7+pd45GS17*C7)
    pd46CF26 = pd46CF17*S7+pd46CF28*C7
    pd47CF26 = pd47CF17*S7+pd47CF28*C7
    pd48CF26 = OMP28*C7+pd48CF17*S7
    pd49CF26 = pd49CF17*S7+pd49CF28*C7
    pd50CF26 = pd50CF17*S7+pd50CF28*C7
    pd52CF26 = pd52CF17*S7+pd52CF28*C7-pd52GS37*d[1][7]+d[3][7]*(pd52GS17*C7-pd52GS28*S7)
    pd53CF26 = pd53CF17*S7+pd53CF28*C7-pd53GS37*d[1][7]+d[3][7]*(pd53GS17*C7-pd53GS28*S7)
    pd54CF26 = pd54CF17*S7+pd54CF28*C7
    pd55CF26 = pd55CF17*S7+pd55CF28*C7
    pd56CF26 = pd56CF17*S7+pd56CF28*C7
    pd57CF26 = pd57CF17*S7+pd57CF28*C7
    pd58CF26 = pd58CF17*S7+pd58CF28*C7
    pd30CF36 = OM16*OM16-OM26*OM26
    pd31CF36 = OMP16-OM26*OM36
    pd32CF36 = OM16*OM26
    pd33CF36 = OMP26+OM16*OM36
    pd34CF36 = OMP36+OM16*OM26
    pd36CF36 = ALS27+d[1][7]*(BETA47*C7+BS17*S7)
    pd37CF36 = -ALS17+d[1][7]*(BETA27*S7+BS57*C7)
    pd44CF36 = pd44CF37+d[1][7]*(BETA48*C7+pd44GS17*S7)
    pd45CF36 = pd45CF37+d[1][7]*(BETA68*C7+pd45GS17*S7)
    pd52CF36 = pd52CF37+d[1][7]*(pd52GS17*S7+pd52GS28*C7)
    pd53CF36 = pd53CF37+d[1][7]*(pd53GS17*S7+pd53GS28*C7)
    pd28GS15 = BETA76*S6+BS16*C6
    pd29GS15 = BETA36*C6+BS96*S6
    pd36GS15 = BETA77*S6+pd36GS16*C6
    pd37GS15 = BETA87*S6+pd37GS16*C6
    pd44GS15 = pd44GS16*C6+pd44GS37*S6
    pd45GS15 = pd45GS16*C6+pd45GS37*S6
    pd52GS15 = pd52GS16*C6+pd52GS37*S6
    pd53GS15 = pd53GS16*C6+pd53GS37*S6
    pd28GS35 = BETA76*C6-BS16*S6
    pd29GS35 = -BETA36*S6+BS96*C6
    pd36GS35 = BETA77*C6-pd36GS16*S6
    pd37GS35 = BETA87*C6-pd37GS16*S6
    pd44GS35 = -pd44GS16*S6+pd44GS37*C6
    pd45GS35 = -pd45GS16*S6+pd45GS37*C6
    pd52GS35 = -pd52GS16*S6+pd52GS37*C6
    pd53GS35 = -pd53GS16*S6+pd53GS37*C6
    pd22CF15 = OMP15+OM25*OM35
    pd23CF15 = OMP25-OM15*OM35
    pd24CF15 = OMP35+OM15*OM25
    pd25CF15 = OM25*OM25-OM35*OM35
    pd26CF15 = OM25*OM35
    pd28CF15 = ALS26*S6-BETA46*d[3][6]
    pd29CF15 = -ALS26*C6-BETA66*d[3][6]
    pd30CF15 = pd30CF16*C6+pd30CF36*S6
    pd31CF15 = pd31CF16*C6+pd31CF36*S6
    pd32CF15 = pd32CF16*C6+pd32CF36*S6
    pd33CF15 = pd33CF16*C6+pd33CF36*S6
    pd34CF15 = pd34CF16*C6+pd34CF36*S6
    pd36CF15 = pd36CF16*C6+pd36CF36*S6-pd36GS26*d[3][6]
    pd37CF15 = pd37CF16*C6+pd37CF36*S6-pd37GS26*d[3][6]
    pd38CF15 = pd38CF16*C6+pd38CF37*S6
    pd39CF15 = pd39CF16*C6+pd39CF37*S6
    pd40CF15 = pd40CF16*C6+pd40CF37*S6
    pd41CF15 = pd41CF16*C6+pd41CF37*S6
    pd42CF15 = OMP37*S6+pd42CF16*C6
    pd44CF15 = pd44CF16*C6+pd44CF36*S6-pd44GS26*d[3][6]
    pd45CF15 = pd45CF16*C6+pd45CF36*S6-pd45GS26*d[3][6]
    pd46CF15 = pd46CF16*C6+pd46CF37*S6
    pd47CF15 = pd47CF16*C6+pd47CF37*S6
    pd48CF15 = pd48CF16*C6+pd48CF37*S6
    pd49CF15 = pd49CF16*C6+pd49CF37*S6
    pd50CF15 = pd50CF16*C6+pd50CF37*S6
    pd52CF15 = pd52CF16*C6+pd52CF36*S6-pd52GS26*d[3][6]
    pd53CF15 = pd53CF16*C6+pd53CF36*S6-pd53GS26*d[3][6]
    pd54CF15 = pd54CF16*C6+pd54CF37*S6
    pd55CF15 = pd55CF16*C6+pd55CF37*S6
    pd56CF15 = pd56CF16*C6+pd56CF37*S6
    pd57CF15 = pd57CF16*C6+pd57CF37*S6
    pd58CF15 = pd58CF16*C6+pd58CF37*S6
    pd22CF25 = -OMP25+OM15*OM35
    pd23CF25 = OMP15+OM25*OM35
    pd24CF25 = -OM15*OM15+OM35*OM35
    pd25CF25 = OMP35-OM15*OM25
    pd26CF25 = -OM15*OM35
    pd28CF25 = -ALS36-d[1][6]*(BETA76*C6-BS16*S6)+d[3][6]*(BETA76*S6+BS16*C6)
    pd29CF25 = ALS16-d[1][6]*(-BETA36*S6+BS96*C6)+d[3][6]*(BETA36*C6+BS96*S6)
    pd36CF25 = pd36CF26-d[1][6]*(BETA77*C6-pd36GS16*S6)+d[3][6]*(BETA77*S6+pd36GS16*C6)
    pd37CF25 = pd37CF26-d[1][6]*(BETA87*C6-pd37GS16*S6)+d[3][6]*(BETA87*S6+pd37GS16*C6)
    pd44CF25 = pd44CF26-d[1][6]*(-pd44GS16*S6+pd44GS37*C6)+d[3][6]*(pd44GS16*C6+pd44GS37*S6)
    pd45CF25 = pd45CF26-d[1][6]*(-pd45GS16*S6+pd45GS37*C6)+d[3][6]*(pd45GS16*C6+pd45GS37*S6)
    pd52CF25 = pd52CF26-d[1][6]*(-pd52GS16*S6+pd52GS37*C6)+d[3][6]*(pd52GS16*C6+pd52GS37*S6)
    pd53CF25 = pd53CF26-d[1][6]*(-pd53GS16*S6+pd53GS37*C6)+d[3][6]*(pd53GS16*C6+pd53GS37*S6)
    pd22CF35 = -2.000*OM15*OM25
    pd23CF35 = OM15*OM15-OM25*OM25
    pd24CF35 = OMP15-OM25*OM35
    pd25CF35 = OMP25+OM15*OM35
    pd28CF35 = ALS26*C6+BETA46*d[1][6]
    pd29CF35 = ALS26*S6+BETA66*d[1][6]
    pd30CF35 = -pd30CF16*S6+pd30CF36*C6
    pd31CF35 = -pd31CF16*S6+pd31CF36*C6
    pd32CF35 = -pd32CF16*S6+pd32CF36*C6
    pd33CF35 = -pd33CF16*S6+pd33CF36*C6
    pd34CF35 = -pd34CF16*S6+pd34CF36*C6
    pd36CF35 = -pd36CF16*S6+pd36CF36*C6+pd36GS26*d[1][6]
    pd37CF35 = -pd37CF16*S6+pd37CF36*C6+pd37GS26*d[1][6]
    pd38CF35 = -pd38CF16*S6+pd38CF37*C6
    pd39CF35 = -pd39CF16*S6+pd39CF37*C6
    pd40CF35 = -pd40CF16*S6+pd40CF37*C6
    pd41CF35 = -pd41CF16*S6+pd41CF37*C6
    pd42CF35 = OMP37*C6-pd42CF16*S6
    pd44CF35 = -pd44CF16*S6+pd44CF36*C6+pd44GS26*d[1][6]
    pd45CF35 = -pd45CF16*S6+pd45CF36*C6+pd45GS26*d[1][6]
    pd46CF35 = -pd46CF16*S6+pd46CF37*C6
    pd47CF35 = -pd47CF16*S6+pd47CF37*C6
    pd48CF35 = -pd48CF16*S6+pd48CF37*C6
    pd49CF35 = -pd49CF16*S6+pd49CF37*C6
    pd50CF35 = -pd50CF16*S6+pd50CF37*C6
    pd52CF35 = -pd52CF16*S6+pd52CF36*C6+pd52GS26*d[1][6]
    pd53CF35 = -pd53CF16*S6+pd53CF36*C6+pd53GS26*d[1][6]
    pd54CF35 = -pd54CF16*S6+pd54CF37*C6
    pd55CF35 = -pd55CF16*S6+pd55CF37*C6
    pd56CF35 = -pd56CF16*S6+pd56CF37*C6
    pd57CF35 = -pd57CF16*S6+pd57CF37*C6
    pd58CF35 = -pd58CF16*S6+pd58CF37*C6
    pd20GS14 = -BETA45*S5+BS15*C5
    pd21GS14 = BETA25*C5-BS55*S5
    pd28GS14 = -BETA46*S5+pd28GS15*C5
    pd29GS14 = -BETA66*S5+pd29GS15*C5
    pd36GS14 = pd36GS15*C5-pd36GS26*S5
    pd37GS14 = pd37GS15*C5-pd37GS26*S5
    pd44GS14 = pd44GS15*C5-pd44GS26*S5
    pd45GS14 = pd45GS15*C5-pd45GS26*S5
    pd52GS14 = pd52GS15*C5-pd52GS26*S5
    pd53GS14 = pd53GS15*C5-pd53GS26*S5
    pd20GS24 = BETA45*C5+BS15*S5
    pd21GS24 = BETA25*S5+BS55*C5
    pd28GS24 = BETA46*C5+pd28GS15*S5
    pd29GS24 = BETA66*C5+pd29GS15*S5
    pd36GS24 = pd36GS15*S5+pd36GS26*C5
    pd37GS24 = pd37GS15*S5+pd37GS26*C5
    pd44GS24 = pd44GS15*S5+pd44GS26*C5
    pd45GS24 = pd45GS15*S5+pd45GS26*C5
    pd52GS24 = pd52GS15*S5+pd52GS26*C5
    pd53GS24 = pd53GS15*S5+pd53GS26*C5
    pd15CF14 = OMP24-qd[4]*OM34
    pd16CF14 = OMP34+qd[4]*OM24
    pd17CF14 = -2.000*OM24*OM34
    pd18CF14 = OM24*OM24-OM34*OM34
    pd20CF14 = ALS35*S5-d[3][5]*(BETA45*C5+BS15*S5)
    pd21CF14 = ALS35*C5-d[3][5]*(BETA25*S5+BS55*C5)
    pd22CF14 = pd22CF15*C5-pd22CF25*S5
    pd23CF14 = pd23CF15*C5-pd23CF25*S5
    pd24CF14 = pd24CF15*C5-pd24CF25*S5
    pd25CF14 = pd25CF15*C5-pd25CF25*S5
    pd26CF14 = pd26CF15*C5-pd26CF25*S5
    pd28CF14 = pd28CF15*C5-pd28CF25*S5-d[3][5]*(BETA46*C5+pd28GS15*S5)
    pd29CF14 = pd29CF15*C5-pd29CF25*S5-d[3][5]*(BETA66*C5+pd29GS15*S5)
    pd30CF14 = pd30CF15*C5-pd30CF26*S5
    pd31CF14 = pd31CF15*C5-pd31CF26*S5
    pd32CF14 = -OMP26*S5+pd32CF15*C5
    pd33CF14 = pd33CF15*C5-pd33CF26*S5
    pd34CF14 = pd34CF15*C5-pd34CF26*S5
    pd36CF14 = pd36CF15*C5-pd36CF25*S5-d[3][5]*(pd36GS15*S5+pd36GS26*C5)
    pd37CF14 = pd37CF15*C5-pd37CF25*S5-d[3][5]*(pd37GS15*S5+pd37GS26*C5)
    pd38CF14 = pd38CF15*C5-pd38CF26*S5
    pd39CF14 = pd39CF15*C5-pd39CF26*S5
    pd40CF14 = pd40CF15*C5-pd40CF26*S5
    pd41CF14 = pd41CF15*C5-pd41CF26*S5
    pd42CF14 = pd42CF15*C5-pd42CF26*S5
    pd44CF14 = pd44CF15*C5-pd44CF25*S5-d[3][5]*(pd44GS15*S5+pd44GS26*C5)
    pd45CF14 = pd45CF15*C5-pd45CF25*S5-d[3][5]*(pd45GS15*S5+pd45GS26*C5)
    pd46CF14 = pd46CF15*C5-pd46CF26*S5
    pd47CF14 = pd47CF15*C5-pd47CF26*S5
    pd48CF14 = pd48CF15*C5-pd48CF26*S5
    pd49CF14 = pd49CF15*C5-pd49CF26*S5
    pd50CF14 = pd50CF15*C5-pd50CF26*S5
    pd52CF14 = pd52CF15*C5-pd52CF25*S5-d[3][5]*(pd52GS15*S5+pd52GS26*C5)
    pd53CF14 = pd53CF15*C5-pd53CF25*S5-d[3][5]*(pd53GS15*S5+pd53GS26*C5)
    pd54CF14 = pd54CF15*C5-pd54CF26*S5
    pd55CF14 = pd55CF15*C5-pd55CF26*S5
    pd56CF14 = pd56CF15*C5-pd56CF26*S5
    pd57CF14 = pd57CF15*C5-pd57CF26*S5
    pd58CF14 = pd58CF15*C5-pd58CF26*S5
    pd14CF24 = qd[4]*OM34
    pd15CF24 = qdd[4]+OM24*OM34
    pd16CF24 = -qd[4]*qd[4]+OM34*OM34
    pd17CF24 = OMP24+qd[4]*OM34
    pd18CF24 = OMP34-qd[4]*OM24
    pd20CF24 = -ALS35*C5+d[3][5]*(-BETA45*S5+BS15*C5)
    pd21CF24 = ALS35*S5+d[3][5]*(BETA25*C5-BS55*S5)
    pd22CF24 = pd22CF15*S5+pd22CF25*C5
    pd23CF24 = pd23CF15*S5+pd23CF25*C5
    pd24CF24 = pd24CF15*S5+pd24CF25*C5
    pd25CF24 = pd25CF15*S5+pd25CF25*C5
    pd26CF24 = pd26CF15*S5+pd26CF25*C5
    pd28CF24 = pd28CF15*S5+pd28CF25*C5+d[3][5]*(-BETA46*S5+pd28GS15*C5)
    pd29CF24 = pd29CF15*S5+pd29CF25*C5+d[3][5]*(-BETA66*S5+pd29GS15*C5)
    pd30CF24 = pd30CF15*S5+pd30CF26*C5
    pd31CF24 = pd31CF15*S5+pd31CF26*C5
    pd32CF24 = OMP26*C5+pd32CF15*S5
    pd33CF24 = pd33CF15*S5+pd33CF26*C5
    pd34CF24 = pd34CF15*S5+pd34CF26*C5
    pd36CF24 = pd36CF15*S5+pd36CF25*C5+d[3][5]*(pd36GS15*C5-pd36GS26*S5)
    pd37CF24 = pd37CF15*S5+pd37CF25*C5+d[3][5]*(pd37GS15*C5-pd37GS26*S5)
    pd38CF24 = pd38CF15*S5+pd38CF26*C5
    pd39CF24 = pd39CF15*S5+pd39CF26*C5
    pd40CF24 = pd40CF15*S5+pd40CF26*C5
    pd41CF24 = pd41CF15*S5+pd41CF26*C5
    pd42CF24 = pd42CF15*S5+pd42CF26*C5
    pd44CF24 = pd44CF15*S5+pd44CF25*C5+d[3][5]*(pd44GS15*C5-pd44GS26*S5)
    pd45CF24 = pd45CF15*S5+pd45CF25*C5+d[3][5]*(pd45GS15*C5-pd45GS26*S5)
    pd46CF24 = pd46CF15*S5+pd46CF26*C5
    pd47CF24 = pd47CF15*S5+pd47CF26*C5
    pd48CF24 = pd48CF15*S5+pd48CF26*C5
    pd49CF24 = pd49CF15*S5+pd49CF26*C5
    pd50CF24 = pd50CF15*S5+pd50CF26*C5
    pd52CF24 = pd52CF15*S5+pd52CF25*C5+d[3][5]*(pd52GS15*C5-pd52GS26*S5)
    pd53CF24 = pd53CF15*S5+pd53CF25*C5+d[3][5]*(pd53GS15*C5-pd53GS26*S5)
    pd54CF24 = pd54CF15*S5+pd54CF26*C5
    pd55CF24 = pd55CF15*S5+pd55CF26*C5
    pd56CF24 = pd56CF15*S5+pd56CF26*C5
    pd57CF24 = pd57CF15*S5+pd57CF26*C5
    pd58CF24 = pd58CF15*S5+pd58CF26*C5
    pd14CF34 = -qd[4]*OM24
    pd15CF34 = qd[4]*qd[4]-OM24*OM24
    pd16CF34 = qdd[4]-OM24*OM34
    pd17CF34 = -OMP34+qd[4]*OM24
    pd18CF34 = OMP24+qd[4]*OM34
    pd9CF13 = qd[3]*qd[3]
    pd12CF13 = ALS34+d[2][4]*(BETA84*C4+BS54*S4)-d[3][4]*(-BETA84*S4+BS54*C4)
    pd13CF13 = -ALS24+d[2][4]*(BETA64*S4+BS94*C4)-d[3][4]*(BETA64*C4-BS94*S4)
    pd20CF13 = pd20CF14+d[2][4]*(BETA75*C4+pd20GS24*S4)-d[3][4]*(-BETA75*S4+pd20GS24*C4)
    pd21CF13 = pd21CF14+d[2][4]*(BETA85*C4+pd21GS24*S4)-d[3][4]*(-BETA85*S4+pd21GS24*C4)
    pd28CF13 = pd28CF14+d[2][4]*(pd28GS24*S4+pd28GS35*C4)-d[3][4]*(pd28GS24*C4-pd28GS35*S4)
    pd29CF13 = pd29CF14+d[2][4]*(pd29GS24*S4+pd29GS35*C4)-d[3][4]*(pd29GS24*C4-pd29GS35*S4)
    pd36CF13 = pd36CF14+d[2][4]*(pd36GS24*S4+pd36GS35*C4)-d[3][4]*(pd36GS24*C4-pd36GS35*S4)
    pd37CF13 = pd37CF14+d[2][4]*(pd37GS24*S4+pd37GS35*C4)-d[3][4]*(pd37GS24*C4-pd37GS35*S4)
    pd44CF13 = pd44CF14+d[2][4]*(pd44GS24*S4+pd44GS35*C4)-d[3][4]*(pd44GS24*C4-pd44GS35*S4)
    pd45CF13 = pd45CF14+d[2][4]*(pd45GS24*S4+pd45GS35*C4)-d[3][4]*(pd45GS24*C4-pd45GS35*S4)
    pd52CF13 = pd52CF14+d[2][4]*(pd52GS24*S4+pd52GS35*C4)-d[3][4]*(pd52GS24*C4-pd52GS35*S4)
    pd53CF13 = pd53CF14+d[2][4]*(pd53GS24*S4+pd53GS35*C4)-d[3][4]*(pd53GS24*C4-pd53GS35*S4)
    pd12CF23 = ALS14*S4+BETA24*d[3][4]
    pd13CF23 = ALS14*C4+BETA34*d[3][4]
    pd14CF23 = pd14CF24*C4-pd14CF34*S4
    pd15CF23 = pd15CF24*C4-pd15CF34*S4
    pd16CF23 = pd16CF24*C4-pd16CF34*S4
    pd17CF23 = pd17CF24*C4-pd17CF34*S4
    pd18CF23 = pd18CF24*C4-pd18CF34*S4
    pd20CF23 = -ALS25*S4+pd20CF24*C4+pd20GS14*d[3][4]
    pd21CF23 = ALS15*S4+pd21CF24*C4+pd21GS14*d[3][4]
    pd22CF23 = pd22CF24*C4-pd22CF35*S4
    pd23CF23 = pd23CF24*C4-pd23CF35*S4
    pd24CF23 = pd24CF24*C4-pd24CF35*S4
    pd25CF23 = pd25CF24*C4-pd25CF35*S4
    pd26CF23 = -OMP35*S4+pd26CF24*C4
    pd28CF23 = pd28CF24*C4-pd28CF35*S4+pd28GS14*d[3][4]
    pd29CF23 = pd29CF24*C4-pd29CF35*S4+pd29GS14*d[3][4]
    pd30CF23 = pd30CF24*C4-pd30CF35*S4
    pd31CF23 = pd31CF24*C4-pd31CF35*S4
    pd32CF23 = pd32CF24*C4-pd32CF35*S4
    pd33CF23 = pd33CF24*C4-pd33CF35*S4
    pd34CF23 = pd34CF24*C4-pd34CF35*S4
    pd36CF23 = pd36CF24*C4-pd36CF35*S4+pd36GS14*d[3][4]
    pd37CF23 = pd37CF24*C4-pd37CF35*S4+pd37GS14*d[3][4]
    pd38CF23 = pd38CF24*C4-pd38CF35*S4
    pd39CF23 = pd39CF24*C4-pd39CF35*S4
    pd40CF23 = pd40CF24*C4-pd40CF35*S4
    pd41CF23 = pd41CF24*C4-pd41CF35*S4
    pd42CF23 = pd42CF24*C4-pd42CF35*S4
    pd44CF23 = pd44CF24*C4-pd44CF35*S4+pd44GS14*d[3][4]
    pd45CF23 = pd45CF24*C4-pd45CF35*S4+pd45GS14*d[3][4]
    pd46CF23 = pd46CF24*C4-pd46CF35*S4
    pd47CF23 = pd47CF24*C4-pd47CF35*S4
    pd48CF23 = pd48CF24*C4-pd48CF35*S4
    pd49CF23 = pd49CF24*C4-pd49CF35*S4
    pd50CF23 = pd50CF24*C4-pd50CF35*S4
    pd52CF23 = pd52CF24*C4-pd52CF35*S4+pd52GS14*d[3][4]
    pd53CF23 = pd53CF24*C4-pd53CF35*S4+pd53GS14*d[3][4]
    pd54CF23 = pd54CF24*C4-pd54CF35*S4
    pd55CF23 = pd55CF24*C4-pd55CF35*S4
    pd56CF23 = pd56CF24*C4-pd56CF35*S4
    pd57CF23 = pd57CF24*C4-pd57CF35*S4
    pd58CF23 = pd58CF24*C4-pd58CF35*S4
    pd6CF33 = -qd[3]*qd[3]
    pd12CF33 = -ALS14*C4-BETA24*d[2][4]
    pd13CF33 = ALS14*S4-BETA34*d[2][4]
    pd14CF33 = pd14CF24*S4+pd14CF34*C4
    pd15CF33 = pd15CF24*S4+pd15CF34*C4
    pd16CF33 = pd16CF24*S4+pd16CF34*C4
    pd17CF33 = pd17CF24*S4+pd17CF34*C4
    pd18CF33 = pd18CF24*S4+pd18CF34*C4
    pd20CF33 = ALS25*C4+pd20CF24*S4-pd20GS14*d[2][4]
    pd21CF33 = -ALS15*C4+pd21CF24*S4-pd21GS14*d[2][4]
    pd22CF33 = pd22CF24*S4+pd22CF35*C4
    pd23CF33 = pd23CF24*S4+pd23CF35*C4
    pd24CF33 = pd24CF24*S4+pd24CF35*C4
    pd25CF33 = pd25CF24*S4+pd25CF35*C4
    pd26CF33 = OMP35*C4+pd26CF24*S4
    pd28CF33 = pd28CF24*S4+pd28CF35*C4-pd28GS14*d[2][4]
    pd29CF33 = pd29CF24*S4+pd29CF35*C4-pd29GS14*d[2][4]
    pd30CF33 = pd30CF24*S4+pd30CF35*C4
    pd31CF33 = pd31CF24*S4+pd31CF35*C4
    pd32CF33 = pd32CF24*S4+pd32CF35*C4
    pd33CF33 = pd33CF24*S4+pd33CF35*C4
    pd34CF33 = pd34CF24*S4+pd34CF35*C4
    pd36CF33 = pd36CF24*S4+pd36CF35*C4-pd36GS14*d[2][4]
    pd37CF33 = pd37CF24*S4+pd37CF35*C4-pd37GS14*d[2][4]
    pd38CF33 = pd38CF24*S4+pd38CF35*C4
    pd39CF33 = pd39CF24*S4+pd39CF35*C4
    pd40CF33 = pd40CF24*S4+pd40CF35*C4
    pd41CF33 = pd41CF24*S4+pd41CF35*C4
    pd42CF33 = pd42CF24*S4+pd42CF35*C4
    pd44CF33 = pd44CF24*S4+pd44CF35*C4-pd44GS14*d[2][4]
    pd45CF33 = pd45CF24*S4+pd45CF35*C4-pd45GS14*d[2][4]
    pd46CF33 = pd46CF24*S4+pd46CF35*C4
    pd47CF33 = pd47CF24*S4+pd47CF35*C4
    pd48CF33 = pd48CF24*S4+pd48CF35*C4
    pd49CF33 = pd49CF24*S4+pd49CF35*C4
    pd50CF33 = pd50CF24*S4+pd50CF35*C4
    pd52CF33 = pd52CF24*S4+pd52CF35*C4-pd52GS14*d[2][4]
    pd53CF33 = pd53CF24*S4+pd53CF35*C4-pd53GS14*d[2][4]
    pd54CF33 = pd54CF24*S4+pd54CF35*C4
    pd55CF33 = pd55CF24*S4+pd55CF35*C4
    pd56CF33 = pd56CF24*S4+pd56CF35*C4
    pd57CF33 = pd57CF24*S4+pd57CF35*C4
    pd58CF33 = pd58CF24*S4+pd58CF35*C4
    pd4CF12 = ALS22*S3
    pd5CF12 = -ALS22*C3
    pd6CF12 = qdd[3]*C3+pd6CF33*S3
    pd9CF12 = qdd[3]*S3+pd9CF13*C3
    pd12CF12 = pd12CF13*C3+pd12CF33*S3
    pd13CF12 = pd13CF13*C3+pd13CF33*S3
    pd14CF12 = qdd[4]*C3+pd14CF33*S3
    pd15CF12 = pd15CF14*C3+pd15CF33*S3
    pd16CF12 = pd16CF14*C3+pd16CF33*S3
    pd17CF12 = pd17CF14*C3+pd17CF33*S3
    pd18CF12 = pd18CF14*C3+pd18CF33*S3
    pd20CF12 = pd20CF13*C3+pd20CF33*S3
    pd21CF12 = pd21CF13*C3+pd21CF33*S3
    pd22CF12 = pd22CF14*C3+pd22CF33*S3
    pd23CF12 = pd23CF14*C3+pd23CF33*S3
    pd24CF12 = pd24CF14*C3+pd24CF33*S3
    pd25CF12 = pd25CF14*C3+pd25CF33*S3
    pd26CF12 = pd26CF14*C3+pd26CF33*S3
    pd28CF12 = pd28CF13*C3+pd28CF33*S3
    pd29CF12 = pd29CF13*C3+pd29CF33*S3
    pd30CF12 = pd30CF14*C3+pd30CF33*S3
    pd31CF12 = pd31CF14*C3+pd31CF33*S3
    pd32CF12 = pd32CF14*C3+pd32CF33*S3
    pd33CF12 = pd33CF14*C3+pd33CF33*S3
    pd34CF12 = pd34CF14*C3+pd34CF33*S3
    pd36CF12 = pd36CF13*C3+pd36CF33*S3
    pd37CF12 = pd37CF13*C3+pd37CF33*S3
    pd38CF12 = pd38CF14*C3+pd38CF33*S3
    pd39CF12 = pd39CF14*C3+pd39CF33*S3
    pd40CF12 = pd40CF14*C3+pd40CF33*S3
    pd41CF12 = pd41CF14*C3+pd41CF33*S3
    pd42CF12 = pd42CF14*C3+pd42CF33*S3
    pd44CF12 = pd44CF13*C3+pd44CF33*S3
    pd45CF12 = pd45CF13*C3+pd45CF33*S3
    pd46CF12 = pd46CF14*C3+pd46CF33*S3
    pd47CF12 = pd47CF14*C3+pd47CF33*S3
    pd48CF12 = pd48CF14*C3+pd48CF33*S3
    pd49CF12 = pd49CF14*C3+pd49CF33*S3
    pd50CF12 = pd50CF14*C3+pd50CF33*S3
    pd52CF12 = pd52CF13*C3+pd52CF33*S3
    pd53CF12 = pd53CF13*C3+pd53CF33*S3
    pd54CF12 = pd54CF14*C3+pd54CF33*S3
    pd55CF12 = pd55CF14*C3+pd55CF33*S3
    pd56CF12 = pd56CF14*C3+pd56CF33*S3
    pd57CF12 = pd57CF14*C3+pd57CF33*S3
    pd58CF12 = pd58CF14*C3+pd58CF33*S3
    pd4CF32 = ALS22*C3
    pd5CF32 = ALS22*S3
    pd6CF32 = -qdd[3]*S3+pd6CF33*C3
    pd9CF32 = qdd[3]*C3-pd9CF13*S3
    pd12CF32 = -pd12CF13*S3+pd12CF33*C3
    pd13CF32 = -pd13CF13*S3+pd13CF33*C3
    pd14CF32 = -qdd[4]*S3+pd14CF33*C3
    pd15CF32 = -pd15CF14*S3+pd15CF33*C3
    pd16CF32 = -pd16CF14*S3+pd16CF33*C3
    pd17CF32 = -pd17CF14*S3+pd17CF33*C3
    pd18CF32 = -pd18CF14*S3+pd18CF33*C3
    pd20CF32 = -pd20CF13*S3+pd20CF33*C3
    pd21CF32 = -pd21CF13*S3+pd21CF33*C3
    pd22CF32 = -pd22CF14*S3+pd22CF33*C3
    pd23CF32 = -pd23CF14*S3+pd23CF33*C3
    pd24CF32 = -pd24CF14*S3+pd24CF33*C3
    pd25CF32 = -pd25CF14*S3+pd25CF33*C3
    pd26CF32 = -pd26CF14*S3+pd26CF33*C3
    pd28CF32 = -pd28CF13*S3+pd28CF33*C3
    pd29CF32 = -pd29CF13*S3+pd29CF33*C3
    pd30CF32 = -pd30CF14*S3+pd30CF33*C3
    pd31CF32 = -pd31CF14*S3+pd31CF33*C3
    pd32CF32 = -pd32CF14*S3+pd32CF33*C3
    pd33CF32 = -pd33CF14*S3+pd33CF33*C3
    pd34CF32 = -pd34CF14*S3+pd34CF33*C3
    pd36CF32 = -pd36CF13*S3+pd36CF33*C3
    pd37CF32 = -pd37CF13*S3+pd37CF33*C3
    pd38CF32 = -pd38CF14*S3+pd38CF33*C3
    pd39CF32 = -pd39CF14*S3+pd39CF33*C3
    pd40CF32 = -pd40CF14*S3+pd40CF33*C3
    pd41CF32 = -pd41CF14*S3+pd41CF33*C3
    pd42CF32 = -pd42CF14*S3+pd42CF33*C3
    pd44CF32 = -pd44CF13*S3+pd44CF33*C3
    pd45CF32 = -pd45CF13*S3+pd45CF33*C3
    pd46CF32 = -pd46CF14*S3+pd46CF33*C3
    pd47CF32 = -pd47CF14*S3+pd47CF33*C3
    pd48CF32 = -pd48CF14*S3+pd48CF33*C3
    pd49CF32 = -pd49CF14*S3+pd49CF33*C3
    pd50CF32 = -pd50CF14*S3+pd50CF33*C3
    pd52CF32 = -pd52CF13*S3+pd52CF33*C3
    pd53CF32 = -pd53CF13*S3+pd53CF33*C3
    pd54CF32 = -pd54CF14*S3+pd54CF33*C3
    pd55CF32 = -pd55CF14*S3+pd55CF33*C3
    pd56CF32 = -pd56CF14*S3+pd56CF33*C3
    pd57CF32 = -pd57CF14*S3+pd57CF33*C3
    pd58CF32 = -pd58CF14*S3+pd58CF33*C3
    pd2CF11 = ALS31*C2
    pd4CF11 = ALS33*S2+pd4CF12*C2
    pd5CF11 = -ALS13*S2+pd5CF12*C2
    pd6CF11 = pd6CF12*C2
    pd8CF11 = -qdd[3]*S2
    pd9CF11 = pd9CF12*C2
    pd12CF11 = pd12CF12*C2-pd12CF23*S2
    pd13CF11 = pd13CF12*C2-pd13CF23*S2
    pd14CF11 = pd14CF12*C2-pd14CF23*S2
    pd15CF11 = pd15CF12*C2-pd15CF23*S2
    pd16CF11 = pd16CF12*C2-pd16CF23*S2
    pd17CF11 = pd17CF12*C2-pd17CF23*S2
    pd18CF11 = pd18CF12*C2-pd18CF23*S2
    pd20CF11 = pd20CF12*C2-pd20CF23*S2
    pd21CF11 = pd21CF12*C2-pd21CF23*S2
    pd22CF11 = pd22CF12*C2-pd22CF23*S2
    pd23CF11 = pd23CF12*C2-pd23CF23*S2
    pd24CF11 = pd24CF12*C2-pd24CF23*S2
    pd25CF11 = pd25CF12*C2-pd25CF23*S2
    pd26CF11 = pd26CF12*C2-pd26CF23*S2
    pd28CF11 = pd28CF12*C2-pd28CF23*S2
    pd29CF11 = pd29CF12*C2-pd29CF23*S2
    pd30CF11 = pd30CF12*C2-pd30CF23*S2
    pd31CF11 = pd31CF12*C2-pd31CF23*S2
    pd32CF11 = pd32CF12*C2-pd32CF23*S2
    pd33CF11 = pd33CF12*C2-pd33CF23*S2
    pd34CF11 = pd34CF12*C2-pd34CF23*S2
    pd36CF11 = pd36CF12*C2-pd36CF23*S2
    pd37CF11 = pd37CF12*C2-pd37CF23*S2
    pd38CF11 = pd38CF12*C2-pd38CF23*S2
    pd39CF11 = pd39CF12*C2-pd39CF23*S2
    pd40CF11 = pd40CF12*C2-pd40CF23*S2
    pd41CF11 = pd41CF12*C2-pd41CF23*S2
    pd42CF11 = pd42CF12*C2-pd42CF23*S2
    pd44CF11 = pd44CF12*C2-pd44CF23*S2
    pd45CF11 = pd45CF12*C2-pd45CF23*S2
    pd46CF11 = pd46CF12*C2-pd46CF23*S2
    pd47CF11 = pd47CF12*C2-pd47CF23*S2
    pd48CF11 = pd48CF12*C2-pd48CF23*S2
    pd49CF11 = pd49CF12*C2-pd49CF23*S2
    pd50CF11 = pd50CF12*C2-pd50CF23*S2
    pd52CF11 = pd52CF12*C2-pd52CF23*S2
    pd53CF11 = pd53CF12*C2-pd53CF23*S2
    pd54CF11 = pd54CF12*C2-pd54CF23*S2
    pd55CF11 = pd55CF12*C2-pd55CF23*S2
    pd56CF11 = pd56CF12*C2-pd56CF23*S2
    pd57CF11 = pd57CF12*C2-pd57CF23*S2
    pd58CF11 = pd58CF12*C2-pd58CF23*S2

    # Symbolic Outputs

    PHI[1][1] = pd2CF11
    PHI[1][2] = pd4CF11
    PHI[1][3] = pd5CF11
    PHI[1][4] = pd6CF11
    PHI[1][5] = pd8CF11
    PHI[1][6] = pd9CF11
    PHI[1][7] = pd12CF11
    PHI[1][8] = pd13CF11
    PHI[1][9] = pd14CF11
    PHI[1][10] = pd15CF11
    PHI[1][11] = pd16CF11
    PHI[1][12] = pd17CF11
    PHI[1][13] = pd18CF11
    PHI[1][14] = pd20CF11
    PHI[1][15] = pd21CF11
    PHI[1][16] = pd22CF11
    PHI[1][17] = pd23CF11
    PHI[1][18] = pd24CF11
    PHI[1][19] = pd25CF11
    PHI[1][20] = pd26CF11
    PHI[1][21] = pd28CF11
    PHI[1][22] = pd29CF11
    PHI[1][23] = pd30CF11
    PHI[1][24] = pd31CF11
    PHI[1][25] = pd32CF11
    PHI[1][26] = pd33CF11
    PHI[1][27] = pd34CF11
    PHI[1][28] = pd36CF11
    PHI[1][29] = pd37CF11
    PHI[1][30] = pd38CF11
    PHI[1][31] = pd39CF11
    PHI[1][32] = pd40CF11
    PHI[1][33] = pd41CF11
    PHI[1][34] = pd42CF11
    PHI[1][35] = pd44CF11
    PHI[1][36] = pd45CF11
    PHI[1][37] = pd46CF11
    PHI[1][38] = pd47CF11
    PHI[1][39] = pd48CF11
    PHI[1][40] = pd49CF11
    PHI[1][41] = pd50CF11
    PHI[1][42] = pd52CF11
    PHI[1][43] = pd53CF11
    PHI[1][44] = pd54CF11
    PHI[1][45] = pd55CF11
    PHI[1][46] = pd56CF11
    PHI[1][47] = pd57CF11
    PHI[1][48] = pd58CF11
    PHI[2][1] = -ALS12
    PHI[2][2] = pd4CF32
    PHI[2][3] = pd5CF32
    PHI[2][4] = pd6CF32
    PHI[2][6] = pd9CF32
    PHI[2][7] = pd12CF32
    PHI[2][8] = pd13CF32
    PHI[2][9] = pd14CF32
    PHI[2][10] = pd15CF32
    PHI[2][11] = pd16CF32
    PHI[2][12] = pd17CF32
    PHI[2][13] = pd18CF32
    PHI[2][14] = pd20CF32
    PHI[2][15] = pd21CF32
    PHI[2][16] = pd22CF32
    PHI[2][17] = pd23CF32
    PHI[2][18] = pd24CF32
    PHI[2][19] = pd25CF32
    PHI[2][20] = pd26CF32
    PHI[2][21] = pd28CF32
    PHI[2][22] = pd29CF32
    PHI[2][23] = pd30CF32
    PHI[2][24] = pd31CF32
    PHI[2][25] = pd32CF32
    PHI[2][26] = pd33CF32
    PHI[2][27] = pd34CF32
    PHI[2][28] = pd36CF32
    PHI[2][29] = pd37CF32
    PHI[2][30] = pd38CF32
    PHI[2][31] = pd39CF32
    PHI[2][32] = pd40CF32
    PHI[2][33] = pd41CF32
    PHI[2][34] = pd42CF32
    PHI[2][35] = pd44CF32
    PHI[2][36] = pd45CF32
    PHI[2][37] = pd46CF32
    PHI[2][38] = pd47CF32
    PHI[2][39] = pd48CF32
    PHI[2][40] = pd49CF32
    PHI[2][41] = pd50CF32
    PHI[2][42] = pd52CF32
    PHI[2][43] = pd53CF32
    PHI[2][44] = pd54CF32
    PHI[2][45] = pd55CF32
    PHI[2][46] = pd56CF32
    PHI[2][47] = pd57CF32
    PHI[2][48] = pd58CF32
    PHI[3][2] = -ALS33
    PHI[3][3] = ALS13
    PHI[3][5] = qdd[3]
    PHI[3][7] = pd12CF23
    PHI[3][8] = pd13CF23
    PHI[3][9] = pd14CF23
    PHI[3][10] = pd15CF23
    PHI[3][11] = pd16CF23
    PHI[3][12] = pd17CF23
    PHI[3][13] = pd18CF23
    PHI[3][14] = pd20CF23
    PHI[3][15] = pd21CF23
    PHI[3][16] = pd22CF23
    PHI[3][17] = pd23CF23
    PHI[3][18] = pd24CF23
    PHI[3][19] = pd25CF23
    PHI[3][20] = pd26CF23
    PHI[3][21] = pd28CF23
    PHI[3][22] = pd29CF23
    PHI[3][23] = pd30CF23
    PHI[3][24] = pd31CF23
    PHI[3][25] = pd32CF23
    PHI[3][26] = pd33CF23
    PHI[3][27] = pd34CF23
    PHI[3][28] = pd36CF23
    PHI[3][29] = pd37CF23
    PHI[3][30] = pd38CF23
    PHI[3][31] = pd39CF23
    PHI[3][32] = pd40CF23
    PHI[3][33] = pd41CF23
    PHI[3][34] = pd42CF23
    PHI[3][35] = pd44CF23
    PHI[3][36] = pd45CF23
    PHI[3][37] = pd46CF23
    PHI[3][38] = pd47CF23
    PHI[3][39] = pd48CF23
    PHI[3][40] = pd49CF23
    PHI[3][41] = pd50CF23
    PHI[3][42] = pd52CF23
    PHI[3][43] = pd53CF23
    PHI[3][44] = pd54CF23
    PHI[3][45] = pd55CF23
    PHI[3][46] = pd56CF23
    PHI[3][47] = pd57CF23
    PHI[3][48] = pd58CF23
    PHI[4][7] = ALS34
    PHI[4][8] = -ALS24
    PHI[4][9] = qdd[4]
    PHI[4][10] = pd15CF14
    PHI[4][11] = pd16CF14
    PHI[4][12] = pd17CF14
    PHI[4][13] = pd18CF14
    PHI[4][14] = pd20CF14
    PHI[4][15] = pd21CF14
    PHI[4][16] = pd22CF14
    PHI[4][17] = pd23CF14
    PHI[4][18] = pd24CF14
    PHI[4][19] = pd25CF14
    PHI[4][20] = pd26CF14
    PHI[4][21] = pd28CF14
    PHI[4][22] = pd29CF14
    PHI[4][23] = pd30CF14
    PHI[4][24] = pd31CF14
    PHI[4][25] = pd32CF14
    PHI[4][26] = pd33CF14
    PHI[4][27] = pd34CF14
    PHI[4][28] = pd36CF14
    PHI[4][29] = pd37CF14
    PHI[4][30] = pd38CF14
    PHI[4][31] = pd39CF14
    PHI[4][32] = pd40CF14
    PHI[4][33] = pd41CF14
    PHI[4][34] = pd42CF14
    PHI[4][35] = pd44CF14
    PHI[4][36] = pd45CF14
    PHI[4][37] = pd46CF14
    PHI[4][38] = pd47CF14
    PHI[4][39] = pd48CF14
    PHI[4][40] = pd49CF14
    PHI[4][41] = pd50CF14
    PHI[4][42] = pd52CF14
    PHI[4][43] = pd53CF14
    PHI[4][44] = pd54CF14
    PHI[4][45] = pd55CF14
    PHI[4][46] = pd56CF14
    PHI[4][47] = pd57CF14
    PHI[4][48] = pd58CF14
    PHI[5][14] = ALS25
    PHI[5][15] = -ALS15
    PHI[5][16] = pd22CF35
    PHI[5][17] = pd23CF35
    PHI[5][18] = pd24CF35
    PHI[5][19] = pd25CF35
    PHI[5][20] = OMP35
    PHI[5][21] = pd28CF35
    PHI[5][22] = pd29CF35
    PHI[5][23] = pd30CF35
    PHI[5][24] = pd31CF35
    PHI[5][25] = pd32CF35
    PHI[5][26] = pd33CF35
    PHI[5][27] = pd34CF35
    PHI[5][28] = pd36CF35
    PHI[5][29] = pd37CF35
    PHI[5][30] = pd38CF35
    PHI[5][31] = pd39CF35
    PHI[5][32] = pd40CF35
    PHI[5][33] = pd41CF35
    PHI[5][34] = pd42CF35
    PHI[5][35] = pd44CF35
    PHI[5][36] = pd45CF35
    PHI[5][37] = pd46CF35
    PHI[5][38] = pd47CF35
    PHI[5][39] = pd48CF35
    PHI[5][40] = pd49CF35
    PHI[5][41] = pd50CF35
    PHI[5][42] = pd52CF35
    PHI[5][43] = pd53CF35
    PHI[5][44] = pd54CF35
    PHI[5][45] = pd55CF35
    PHI[5][46] = pd56CF35
    PHI[5][47] = pd57CF35
    PHI[5][48] = pd58CF35
    PHI[6][21] = -ALS36
    PHI[6][22] = ALS16
    PHI[6][23] = pd30CF26
    PHI[6][24] = pd31CF26
    PHI[6][25] = OMP26
    PHI[6][26] = pd33CF26
    PHI[6][27] = pd34CF26
    PHI[6][28] = pd36CF26
    PHI[6][29] = pd37CF26
    PHI[6][30] = pd38CF26
    PHI[6][31] = pd39CF26
    PHI[6][32] = pd40CF26
    PHI[6][33] = pd41CF26
    PHI[6][34] = pd42CF26
    PHI[6][35] = pd44CF26
    PHI[6][36] = pd45CF26
    PHI[6][37] = pd46CF26
    PHI[6][38] = pd47CF26
    PHI[6][39] = pd48CF26
    PHI[6][40] = pd49CF26
    PHI[6][41] = pd50CF26
    PHI[6][42] = pd52CF26
    PHI[6][43] = pd53CF26
    PHI[6][44] = pd54CF26
    PHI[6][45] = pd55CF26
    PHI[6][46] = pd56CF26
    PHI[6][47] = pd57CF26
    PHI[6][48] = pd58CF26
    PHI[7][28] = ALS27
    PHI[7][29] = -ALS17
    PHI[7][30] = pd38CF37
    PHI[7][31] = pd39CF37
    PHI[7][32] = pd40CF37
    PHI[7][33] = pd41CF37
    PHI[7][34] = OMP37
    PHI[7][35] = pd44CF37
    PHI[7][36] = pd45CF37
    PHI[7][37] = pd46CF37
    PHI[7][38] = pd47CF37
    PHI[7][39] = pd48CF37
    PHI[7][40] = pd49CF37
    PHI[7][41] = pd50CF37
    PHI[7][42] = pd52CF37
    PHI[7][43] = pd53CF37
    PHI[7][44] = pd54CF37
    PHI[7][45] = pd55CF37
    PHI[7][46] = pd56CF37
    PHI[7][47] = pd57CF37
    PHI[7][48] = pd58CF37
    PHI[8][35] = -ALS38
    PHI[8][36] = ALS18
    PHI[8][37] = pd46CF28
    PHI[8][38] = pd47CF28
    PHI[8][39] = OMP28
    PHI[8][40] = pd49CF28
    PHI[8][41] = pd50CF28
    PHI[8][42] = pd52CF28
    PHI[8][43] = pd53CF28
    PHI[8][44] = pd54CF28
    PHI[8][45] = pd55CF28
    PHI[8][46] = pd56CF28
    PHI[8][47] = pd57CF28
    PHI[8][48] = pd58CF28
    PHI[9][42] = ALS39
    PHI[9][43] = -ALS29
    PHI[9][44] = OMP19
    PHI[9][45] = pd55CF19
    PHI[9][46] = pd56CF19
    PHI[9][47] = pd57CF19
    PHI[9][48] = pd58CF19

    #	Number of continuation lines = 0
    # /!\ start at 3 because PHI[1][*] and PHI[2][*] are regressor of blocked joints. So they should be discard.
    for i in range(1+2, 10):
        for j in range(1, 49):
            PHI_t[i-3, j-1] = PHI[i][j]
