---
declaration: proposition
origin: cited
lean: Eq1729.enlarge_S'
statement: formalized
proof: formalized
---

# Enlarging $S'$

Suppose one has a partial solution in which $S'x$ is undefined for some $x \in N$. Then one can extend the partial solution so that $S'x$ is now defined.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Enlarging $S'$ with induction hypothesis](enlarge-s-induct.md)

## Proof

Obtained by induction from Proposition [Enlarging $S'$ with induction hypothesis](enlarge-s-induct.md), using the fact that there are no infinite descending chains in $N$.

## Lean

Formalized as [`Eq1729.enlarge_S'`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1729.enlarge_S').

## Sources

- [Equational Theories blueprint: chapter/1729.tex, line 266](https://github.com/teorth/equational_theories/blob/8b87204d5b201e1cf6c69b8dcabb0558109bee00/blueprint/src/chapter/1729.tex#L266)
