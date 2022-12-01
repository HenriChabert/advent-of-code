raw_inp = """CHBBKPHCPHPOKNSNCOVB

SP -> K
BB -> H
BH -> S
BS -> H
PN -> P
OB -> S
ON -> C
HK -> K
BN -> V
OH -> F
OF -> C
SN -> N
PF -> H
CF -> F
HN -> S
SK -> F
SS -> C
HH -> C
SO -> B
FS -> P
CB -> V
NK -> F
KK -> P
VN -> H
KF -> K
PS -> B
HP -> B
NP -> P
OO -> B
FB -> V
PO -> B
CN -> O
HC -> B
NN -> V
FV -> F
BK -> K
VC -> K
KV -> V
VF -> V
FO -> O
FK -> B
HS -> C
OV -> F
PK -> F
VV -> S
NH -> K
SH -> H
VB -> H
NF -> P
OK -> B
FH -> F
CO -> V
BC -> K
PP -> S
OP -> V
VO -> C
NC -> F
PB -> F
KO -> O
BF -> C
VS -> K
KN -> P
BP -> F
KS -> V
SB -> H
CH -> N
HF -> O
CV -> P
NB -> V
FF -> H
OS -> S
CS -> S
KC -> F
NS -> N
NV -> O
SV -> V
BO -> V
BV -> V
CC -> F
CK -> H
KP -> C
KH -> H
KB -> F
PH -> P
VP -> P
OC -> F
FP -> N
HV -> P
HB -> H
PC -> N
VK -> H
HO -> V
CP -> F
SF -> N
FC -> P
NO -> K
VH -> S
FN -> F
PV -> O
SC -> N"""

pattern = raw_inp.split("\n\n")[0]
md = {k: v for k, v in [x.split(" -> ") for x in raw_inp.split("\n\n")[1].split("\n")]}

inp = {}
for i in range(len(pattern) - 1):
    inp[pattern[i:i+2]] = inp.get(pattern[i:i+2], 0) + 1


N_TICKS = 40

for n in range(N_TICKS):
	ninp = {}
	for k, v in inp.items():

		ninp[k[0] + md[k]] = ninp.get(k[0] + md[k], 0) + v

		ninp[md[k] + k[1]] = ninp.get(md[k] + k[1], 0) + v
	inp = ninp
	
def calc_score(ip):
    np = {}
    for k, v in ip.items():
        np[k[0]] = np.get(k[0], 0) + v

        np[k[1]] = np.get(k[1], 0) + v
    np[pattern[0]] += 1
    np[pattern[-1]] += 1

    mx = max(np, key=lambda x: np[x])
    mn = min(np, key=lambda x: np[x])
	
    return (np[mx] // 2 ) - (np[mn] // 2)
	
print(calc_score(inp))
