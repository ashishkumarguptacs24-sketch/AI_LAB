
"""
Week-6 AI Lab: Truth-table enumeration for propositional entailment (TT-ENTAILS).

Name:ASHISH KUMAR GUPTA
USN: 1WA24CS063
"""

from itertools import product


# Logical connectives
def NOT(a):
    return not a

def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def IMPLIES(a, b):
    return (not a) or b

def IFF(a, b):
    return a == b


# Evaluate propositional sentence
def pl_true(sentence, model):
    env = {
        "NOT": NOT,
        "AND": AND,
        "OR": OR,
        "IMPLIES": IMPLIES,
        "IFF": IFF
    }
    env.update(model)

    return bool(eval(sentence, {"__builtins__": {}}, env))


# Check whether KB is true
def kb_true(kb, model):
    return all(pl_true(s, model) for s in kb)


# Truth-table entailment
def tt_entails(kb, alpha, symbols):
    return tt_check_all(kb, alpha, list(symbols), {})


def tt_check_all(kb, alpha, symbols, model):

    if not symbols:
        if kb_true(kb, model):
            return pl_true(alpha, model)
        return True

    first, rest = symbols[0], symbols[1:]

    return (
        tt_check_all(kb, alpha, rest,
                     {**model, first: True})
        and
        tt_check_all(kb, alpha, rest,
                     {**model, first: False})
    )


# Print truth table
def print_truth_table(kb, queries, symbols):

    cols = list(symbols) + kb + list(queries) + ["KB"]

    widths = [max(len(c), 5) for c in cols]

    line = " | ".join(
        c.ljust(w) for c, w in zip(cols, widths)
    )

    print(line)
    print("-" * len(line))

    t = lambda b: "T" if b else "F"

    for vals in product([True, False], repeat=len(symbols)):

        m = dict(zip(symbols, vals))

        row = (
            [t(v) for v in vals]
            + [t(pl_true(s, m)) for s in kb]
            + [t(pl_true(q, m)) for q in queries]
            + [t(kb_true(kb, m))]
        )

        print(" | ".join(
            c.ljust(w) for c, w in zip(row, widths)
        ))


# Main program
if __name__ == "__main__":

    print("Name: Ayush Kumar")
    print("USN : 1WA24CS074\n")

    symbols = ["P", "Q", "R"]

    kb = [
        "IMPLIES(Q, P)",
        "IMPLIES(P, NOT(Q))",
        "OR(Q, R)"
    ]

    queries = {
        "R": "R",
        "R -> P": "IMPLIES(R, P)",
        "Q -> R": "IMPLIES(Q, R)"
    }

    print_truth_table(kb, list(queries.values()), symbols)

    print("\nModels of KB:")

    for vals in product([True, False], repeat=len(symbols)):

        m = dict(zip(symbols, vals))

        if kb_true(kb, m):
            print("  ", m)

    print()

    for name, q in queries.items():
        print(
            f"KB entails {name:7s}? "
            f"{tt_entails(kb, q, symbols)}"
        )
