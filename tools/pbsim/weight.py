import random

OUTCOMES = {
    "O_STRIKE_LOOKING": 1000,
    "O_STRIKE_SWINGING": 1000,
    "O_FOUL": 1000,
    "O_BALL_IN_PLAY": 1000,
    "O_BALL": 1000,
    "O_BALK": 1
}

if __name__ == "__main__":
    random.seed()
    it = 0
    max_it = 1000000

    results = dict()
    while it < max_it:
        outcome = random.choices(list(OUTCOMES.keys()), OUTCOMES.values())[0]
        if outcome not in results:
            results[outcome] = 0

        results[outcome] += 1
        it += 1

    for outcome_name, count in results.items():
        print("{0}:".format(outcome_name).ljust(20), end="")
        print("{0} - {1:.10f}".format(count, (count / max_it)))
