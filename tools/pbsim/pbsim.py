import random

from collections import Counter
from collections import namedtuple

PITCH_WEIGHTS = {
    "strike": 0.60,
    "ball": 0.39,
    "balk": 0.01
}

PlateAppearanceResult = namedtuple(
    "PlateAppearance",
    field_names=["pitcher", "batter", "outcome", "pitches_thrown"]
)


player_pitcher = {
    "name": "Jim Pitcher",
    "confidence": 0,
    "energy": 100,  # 1 pitch == 1 energy point
    "velocity": 100,
    "pitches": [
        {
            "name": "4FB",
            "movement": 0,
            "command": 0,
            "control": 0,
            "confidence": 0,
        },
        {
            "name": "2FB",
            "movement": 0,
            "command": 0,
            "control": 0,
            "confidence": 0,
        },
        {
            "name": "CHG",
            "movement": 0,
            "command": 0,
            "control": 0,
            "confidence": 0,
        },
    ]
}

player_batter = {
    "name": "Joe Hitter"
}


def bases_are_empty(bases):
    return bases == [None, None, None]


def compute_intentional_walk(manager, pitcher, current_batter, next_batter, bases):
    return False


def compute_balk_probability(pitcher, inning, bases):

    """Compute the probability of a balk.

    The balk in baseball is designed to protect runners from being deceived by the pitcher. However, there are a lot of
    reasons why a pitcher might balk and most of them usually do not have bad intent. Instead pitcher's balk because
    of pressure or tiredness and umpires that are jerks.

    Tired or rattled pitchers are prone to balking slightly more (but it should still be *really* rare).

    Balks are rare: "Since 2000, there have only been 100-200 balks per season, which is roughly one every 12 to 24
                    games (or 648 to 1296 innings pitched) in a full 2430-game season."

    For our purposes we want to know the probability of a balk being called per any given pitch.

    Let's go with 120 balks per season as our baseline.

    Games: 160
    Teams: 24
    Innings Per Game: 9
    Average Pitches Per Inning: ~20

    prob_balk = 120 / ((160 * 24) * (9 * 20))

    That is the unmodified probability. Tired and slightly nervous pitchers are prone to balking more (total guess), but
    let's assume that's true because fuck it.
    """

    return False


def select_pitch(pitcher, thrown_pitches):

    thrown_pitches_count = Counter(thrown_pitches)
    pitch = random.choices(pitcher["pitches"], weights=[(p.confidence + p.level) for p in pitcher["pitches"]], k=1)

    return pitch


def deliver_pitch(pitcher, pitch, batter, bases):

    #
    # check the state of the bases first...
    #   - if the bases are empty compute the outcome for the delivered pitch
    #   - if the bases are not empty then we need to do some things
    #
    # **NOTE** Bases empty balks are exceptionally rare and result in a ball.
    #
    events = ["strike:swinging", "strike:looking", "ball", "hbp"]


    # 1. Decide if the pitcher is going to balk as the first thing we do. If he's going to balk then two things occur:



    # https://sports.stackexchange.com/questions/5000/is-a-balk-scored-differently-from-a-base-on-balls
    return "strike"


def sim_matchup(pitcher, batter, bases):

    # these are the high-level outcomes for a single matchup between a pitcher and a batter:
    #
    # 1. Out
    #   - strikeout
    #   - fly out
    #   - ground out
    # 2. Hit
    #   - single
    #   - double
    #   - triple
    #   - home run
    #   - inside the park home run
    # 3. Walk
    # 4. Intentional Walk
    # 5. Balk
    # 6. Hit by Pitch

    outcome = None
    strikes = 0
    balls = 0
    pitches_thrown = []

    # Determine if the pitcher should intentionally walk the batter before throwing any pitches.
    if compute_intentional_walk(None, pitcher, batter, None, []):
        pitches_thrown = [None, None, None, None]
        return PlateAppearanceResult(pitcher, batter, {"id": "INTENTIONAL_WALK"}, pitches_thrown)

    while True:
        pitch = select_pitch(pitcher, [])
        pitch_result = deliver_pitch(pitcher, pitch, batter)
        pitches_thrown.append(pitch)

        if pitch_result.startswith("strike") or (pitch_result == "foul" and strikes < 2):
            strikes += 1
            if strikes == 3:
                return PlateAppearanceResult(pitcher, batter, {"id": "STRIKEOUT"}, pitches_thrown)
        elif pitch_result.startswith("ball"):
            balls += 1
            if balls == 4:
                return PlateAppearanceResult(pitcher, batter, {"id": "WALK"}, pitches_thrown)
        elif pitch_result == "balk": # balks are fucking stupid
            if balls == 4:
                return PlateAppearanceResult(pitcher, batter, {"id": "BALK"}, pitches_thrown)

        if pitch_result == "strike" or (pitch_result == "foul" and strikes < 2):
            strikes += 1
        elif pitch_result == "ball":
            balls += 1

    return result


if __name__ == "__main__":
    random.seed(a="IAmTheWalrus")

