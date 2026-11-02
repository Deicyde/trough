---
declaration: lemma
origin: cited
lean: ZHat.nontrivial
statement: formalized
proof: formalized
---

# ZHat.nontrivial

$0\not=1$ in $\widehat{\mathbb{Z}}$.

## Depends on

- [ZHat.commRing](zhat-commring.md)

## Proof

Recall that you can evaluate an element of $\widehat{\mathbb{Z}}$ at a positive integer. Evaluating $0$ at 2 gives $0$, and evaluating $1$ at $2$ gives $1$, and these are distinct elements of $\mathbb{Z}/2\mathbb{Z}$, so $0\not=1$ in $\widehat{\mathbb{Z}}$.

## Lean

Formalized as [`ZHat.nontrivial`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/ZHat.nontrivial).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch05automorphicformexample.tex, line 108](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch05automorphicformexample.tex#L108)
