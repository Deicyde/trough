---
declaration: proposition
origin: cited
lean: Eq1729.enlarge_S'_induction
statement: formalized
proof: formalized
---

# Enlarging $S'$ with induction hypothesis

Suppose one has a partial solution in which $S'x$ is undefined for some $x \in N$, but $S'y$ is defined for all $y < x$. (This hypothesis is vacuous for $x=1$.) Then one can extend the partial solution so that $S'x$ is now defined.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Enlarging $L'_0$ many times](enlarge-l0-many.md)
- [Enlarging $S'$ with induction hypothesis and axioms](enlarge-s-induct-axioms.md)

## Proof

Let $y_0$ be the parent of $x$, that is to say the unique neighbor of $x$ in the path to $1$ (this is only defined for $x \neq 1$), then by axiom (i”) $y_0$ is the unique neighbor for which $S'y_0$ is defined, and we either have $x = R'_a y_0$ or $R'_a x = y_0$ for some unique $a \in SM$.

By using [Enlarging $L'_0$ many times](enlarge-l0-many.md), we may impose axioms (A), (B), (C) without loss of generality, as this only imposes a finite set of conditions. The claim now follows from [Enlarging $S'$ with induction hypothesis and axioms](enlarge-s-induct-axioms.md).

## Lean

Formalized as [`Eq1729.enlarge_S'_induction`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1729.enlarge_S'_induction).

## Sources

- [Equational Theories blueprint: chapter/1729.tex, line 254](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/1729.tex#L254)
