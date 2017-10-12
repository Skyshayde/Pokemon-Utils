from enum import Enum


class Nature(Enum):
    HARDY = 0
    LONELY = 1
    BRAVE = 2
    ADAMANT = 3
    NAUGHTY = 4
    BOLD = 5
    DOCILE = 6
    RELAXED = 7
    IMPISH = 8
    LAX = 9
    TIMID = 10
    HASTY = 11
    SERIOUS = 12
    JOLLY = 13
    NAIVE = 14
    MODEST = 15
    MILD = 16
    QUIET = 17
    BASHFUL = 18
    RASH = 19
    CALM = 20
    GENTLE = 21
    SASSY = 22
    CAREFUL = 23
    QUIRKY = 24

    def stat(nature):
        "Returns the stats affected by a nature in +, - order tuple.  Null natures are represented by dual empty strings.  Input should be the nature enum.  "
        plus = ""
        minus = ""

        if (nature in (Nature.LONELY, Nature.BRAVE, Nature.ADAMANT, Nature.ADAMANT)):
            plus = "atk"
        if (nature in (Nature.BOLD, Nature.RELAXED, Nature.IMPISH, Nature.LAX)):
            plus = "def"
        if (nature in (Nature.TIMID, Nature.HASTY, Nature.JOLLY, Nature.NAIVE)):
            plus = "spe"
        if (nature in (Nature.MODEST, Nature.MILD, Nature.QUIET, Nature.RASH)):
            plus = "spatk"
        if (nature in (Nature.CALM, Nature.GENTLE, Nature.SASSY, Nature.CAREFUL)):
            plus = "spdef"

        if (nature in (Nature.BOLD, Nature.TIMID, Nature.MODEST, Nature.CALM)):
            minus = "atk"
        if (nature in (Nature.LONELY, Nature.HASTY, Nature.MILD, Nature.GENTLE)):
            minus = "def"
        if (nature in (Nature.ADAMANT, Nature.IMPISH, Nature.JOLLY, Nature.CAREFUL)):
            minus = "spatk"
        if (nature in (Nature.NAUGHTY, Nature.LAX, Nature.NAIVE, Nature.RASH)):
            minus = "spdef"
        if (nature in (Nature.BRAVE, Nature.RELAXED, Nature.QUIET, Nature.SASSY0)):
            minus = "spe"

        return (plus, minus)