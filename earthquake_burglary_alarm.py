"""
Earthquake Burglary Alarm - Bayesian Network
Classic AI Probabilistic Inference Problem
"""

# ─────────────────────────────────────────
#  Conditional Probability Tables (CPTs)
# ─────────────────────────────────────────

P = {
    # Priors
    'B':  0.001,          # P(Burglary)
    'E':  0.002,          # P(Earthquake)

    # P(Alarm | Burglary, Earthquake)
    'A|B,E':   0.95,
    'A|B,~E':  0.94,
    'A|~B,E':  0.29,
    'A|~B,~E': 0.001,

    # P(JohnCalls | Alarm)
    'J|A':  0.90,
    'J|~A': 0.05,

    # P(MaryCalls | Alarm)
    'M|A':  0.70,
    'M|~A': 0.01,
}


def p_alarm(b: bool, e: bool) -> float:
    """P(Alarm=True | Burglary=b, Earthquake=e)"""
    key = f"A|{'B' if b else '~B'},{'E' if e else '~E'}"
    return P[key]


def joint_prob(b: bool, e: bool, a: bool, j: bool, m: bool) -> float:
    """Full joint probability of all variables."""
    pb  = P['B']  if b else 1 - P['B']
    pe  = P['E']  if e else 1 - P['E']
    pa  = p_alarm(b, e) if a else 1 - p_alarm(b, e)
    pj  = (P['J|A'] if a else P['J|~A']) if j else \
          (1 - P['J|A'] if a else 1 - P['J|~A'])
    pm  = (P['M|A'] if a else P['M|~A']) if m else \
          (1 - P['M|A'] if a else 1 - P['M|~A'])
    return pb * pe * pa * pj * pm


def enumeration_ask(query_var: str, evidence: dict) -> dict:
    """
    Exact inference by enumeration over all hidden variables.
    Returns normalized probability distribution for query_var.
    """
    vars_order = ['B', 'E', 'A', 'J', 'M']
    hidden = [v for v in vars_order
              if v != query_var and v not in evidence]

    dist = {}
    for qval in [True, False]:
        total = 0.0
        # Enumerate all combinations of hidden variables
        n = len(hidden)
        for mask in range(1 << n):
            assignment = {query_var: qval, **evidence}
            for i, hv in enumerate(hidden):
                assignment[hv] = bool((mask >> i) & 1)
            total += joint_prob(
                assignment['B'], assignment['E'],
                assignment['A'], assignment['J'], assignment['M']
            )
        dist[qval] = total

    # Normalize
    total_sum = dist[True] + dist[False]
    return {k: v / total_sum for k, v in dist.items()}


# ─────────────────────────────────────────
#  Queries
# ─────────────────────────────────────────

def run_queries():
    print("=" * 55)
    print("   EARTHQUAKE BURGLARY ALARM — BAYESIAN NETWORK")
    print("=" * 55)

    queries = [
        ("P(Burglary | JohnCalls=T, MaryCalls=T)",
         'B', {'J': True,  'M': True}),
        ("P(Alarm   | JohnCalls=T, MaryCalls=T)",
         'A', {'J': True,  'M': True}),
        ("P(Burglary | JohnCalls=T)",
         'B', {'J': True}),
        ("P(Earthquake | Alarm=T)",
         'E', {'A': True}),
        ("P(Alarm   | Burglary=T)",
         'A', {'B': True}),
    ]

    for label, var, ev in queries:
        result = enumeration_ask(var, ev)
        print(f"\n{label}")
        print(f"  P(True)  = {result[True]:.6f}")
        print(f"  P(False) = {result[False]:.6f}")

    print("\n" + "=" * 55)


if __name__ == "__main__":
    run_queries()
