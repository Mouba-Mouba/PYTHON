# Islam md Shariful 1720601
# MOHAMED MOUBARAK MOHAMED MISBAHOU MKOUBOI 1820705

obs = ('Practicing', 'Islam', 'beautifies' , 'individual' , 'character')
states = ('N' ,'V' ,  'DT')
start_p = {'N':0.5 ,  'V':0.1  , 'DT':0.4}
trans_p = { 'N' : {'N': 0.5, 'V': 0.4 , 'P':0.1, 'ADV':0 ,'DT' : 0},
            'P' : {'V':0, 'P':0, 'ADV':0,'DT' : 0.6, 'N' : 0.4} ,
            'V' : {'DT': 0.3, 'N': 0.4, 'P':0.1, 'V': 0.1, 'P' :0},
            'ADV':{'N':0.5, 'V':0.3, 'P':0 , 'DT':0 , 'ADV':0, 'ADJ':0.1},
            'DT' : {'N': 0.8, 'V': 0.1 , 'ADV':0.1, 'P':0 , 'DT' :0}}

emit_p = {'N' : {'character': 0.2, 'Islam': 0.1, 'Practicing':0, 'beautifies' : 0 , 'individual':0},
          'P':{'individual' : 0.0,'beautifies' : 0, 'Practicing' : 0, 'character' : 0 , 'Islam':0 },
          'V' :{'character' : 0.5 , 'Islam':0.1 , 'beautifies' : 0.1, 'Practicing':0,  'individual':0},
          'ADV' : {'individual' : 0.2,'beautifies' : 0, 'Practicing' : 0, 'character' : 0 , 'Islam':0 },
          'DT' : {'beautifies' : 0.4 , 'Practicing' : 0.3, 'character' : 0 , 'Islam':0 , 'individual' :0}}


def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    for st in states:
        V[0][st] = {"prob": start_p[st] * emit_p[st][obs[0]], "prev": None}

    print(V)

    # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        V.append({})
        for st in states:
            max_tr_prob = max(V[t-1][prev_st]["prob"]*trans_p[prev_st][st] for prev_st in states)
            for prev_st in states:
                if V[t-1][prev_st]["prob"] * trans_p[prev_st][st] == max_tr_prob:
                    max_prob = max_tr_prob * emit_p[st][obs[t]]
                    V[t][st] = {"prob": max_prob, "prev": prev_st}
                    break
    for line in dptable(V):
        print(line)
    opt = []
    
# The highest probability
    max_prob = max(value["prob"] for value in V[-1].values())
    previous = None
    # Get most probable state and its backtrack
    for st, data in V[-1].items():
        if data["prob"] == max_prob:
            opt.append(st)
            previous = st
            break

    # Follow the backtrack till the first observation
    for t in range(len(V) - 2, -1, -1):
        opt.insert(0, V[t + 1][previous]["prev"])
        previous = V[t + 1][previous]["prev"]

    print('The steps of states are ' + ' '.join(opt) + ' with highest probability of %s' % max_prob)

def dptable(V):
    # Print a table of steps from dictionary
    yield " ".join(("%12d" % i) for i in range(len(V)))
    for state in V[0]:
        yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v[state]["prob"]) for v in V)

viterbi(obs, states, start_p, trans_p, emit_p)