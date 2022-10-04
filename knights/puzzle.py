from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

and_true = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    
    Not(And(AKnight, AKnave)), #can be only of them
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave))
    
)
# Puzzle 0
# A says "I am both a knight and a knave."  #impossible to be both ----> implication
                                            # T -> F == T
                                            # F -> T == F

knowledge0 = And(
    and_true,
    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(BKnight, BKnave)))

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.

knowledge1 = And(
    and_true,

    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    and_true,
    #same kind
   Implication(AKnight, Or(And(AKnight, BKnight), 
                           And(AKnave, BKnave))),
   Implication(AKnave, Not(Or(And(AKnave, BKnave), 
                              And(AKnight, BKnight)))),

   #different kinds
   Implication (BKnight, Or(And(BKnight, AKnave), 
                            And(BKnave, AKnight))),
   Implication(BKnave, Not(Or(And(BKnave, AKnight), 
                              And(BKnight, AKnave))))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    and_true,
    #a
    Implication(AKnight, Or(AKnight, AKnave)),
    Implication(AKnave, Not(Or(AKnight, AKnave))),

    #b
    Implication(BKnight, And(Implication(AKnight, AKnave),
                            Implication(AKnave, Not(AKnave)))),

    Implication(BKnight, CKnight),
    Implication(BKnave, Not(CKnave)),

    #c
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)

def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
