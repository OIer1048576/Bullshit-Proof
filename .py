from copy import deepcopy
from random import *


Alphabet = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "\\alpha", "\\beta", "\\gamma", "\\delta", "\\epsilon", "\\zeta", "\\eta", "\\theta", "\\iota", "\\kappa", "\\lambda", "\\mu", "\\nu", "\\xi", "\\pi", "\\rho", "\\sigma", "\\tau", "\\upsilon", "\\phi", "\\chi", "\\psi", "\\omega",
    "\\varepsilon", "\\vartheta", "\\varpi", "\\varrho", "\\varsigma", "\\varphi",
    "\\Gamma", "\\Theta", "\\Lambda", "\\Xi", "\\Pi", "\\Sigma", "\\Upsilon", "\\Phi", "\\Psi", "\\Omega",
]

Operators = [
    "1+2", "1-2", "1\\times 2", "1\\div 2", "1^{2}", "\\frac{1}{2}",
    "\\sum_{0=(1)}^{2} (3)", "\\prod_{0=1}^{2} (3)", "\\bigoplus_{0=1}^{2} (3)", "\\bigotimes_{0=1}^{2} (3)",
    "\\int_{1}^{2} (3)", "\\oint_{1}^{2} (3)"
]

Statement_Operators = [
    " \\le ", " \\ge ", " < ", " > ", " \\ne ", " = ",
]


Statement_To_Statements = [
    " \\wedge ", " \\vee ", " \\rightarrow ", " \\implies ", " \\iff ",
]


constants = []


def ___generate_number(depth):
    if depth == 0:
        if random() > 0.5:
            return "{" + f"Eve \\times Qwq^{'{R}'}" + "}"
        else:
            ch = choice(Alphabet)
            ch = ch + "_{Eve}"
            constants.append(ch)
            return ch
    else:
        return choice(Operators).replace("0", choice(Alphabet)) \
            .replace("1", ___generate_number(randrange(depth))) \
            .replace("2", ___generate_number(randrange(depth))) \
            .replace("3", ___generate_number(randrange(depth))) \



def generate_number(depth):
    s = ___generate_number(depth).replace("Qwq", "10")
    while "Eve" in s:
        s = s.replace("Eve", f"{randint(1, 9)}", 1)
    while "R" in s:
        s = s.replace("R", f"{randint(1, 99)}", 1)
    return s


def generate_statement(depth, number_depth):
    if depth == 0:
        return f"({generate_number(number_depth)}) {choice(Statement_Operators)} ({generate_number(number_depth)})"
    else:
        return f"({generate_statement(randrange(depth), number_depth)}) {choice(Statement_To_Statements)} ({generate_statement(randrange(depth), number_depth)})"


fp = open("test.tex", "w")
print("""\\begin{array} \n \\huge{\\text{Proof Of 3x+1 Problem}} \\\\
    \\tiny{\\text{1048576's Bot}} \\\\ \\\\""", file=fp)
e = 114514
proof_depth = int(input())
statement_depth = int(input())
number_depth = int(input())
for gen in range(1, proof_depth+1):
    constants = []
    if gen > 2:
        print("\\text{Cause}", "\\text{ and }".join(
            map(lambda x: f"({x})", sample(range(1, gen), 2))), file=fp)
    print("" if random() > 0.5 else "\\text{Trivally }",
          generate_statement(statement_depth, number_depth), f"& ({gen})", file=fp)
    print("\\\\", file=fp)
    e = generate_statement(statement_depth-1, number_depth-1)
    print(
        "\\text{Thus, }"+e+"\\text{ Can Complete The Proof.} \\\\", file=fp)
print("\\text{Trivally } ", e, " \\text{ is Right.} \\\\", file=fp)
print("\\text{That completes the proof.} \\Box \n \\end{array}", file=fp)
