---
declaration: definition
origin: cited
lean: Eq1729.PartialSolution
statement: formalized
---

# Partial solution

A *partial solution* $(L'_0, \diamond', S', {\mathcal I})$ is a collection of the following data:

- A partially defined function $L'_0: N \to N$, defined on a finite union of right cosets of $\langle e_0\rangle$;
- A partially defined operation $\diamond': N \times N \to M$, defined on a finite set;
- A partially defined function $S': N \to SM$, defined on a finite set; and
- A finite collection ${\mathcal I}$ of “pending identities” $I[x,y,z]$, which one can think of either as ordered triples of elements $x,y,z \in N$, or as formal strings of the form “$z \diamond' x = (R'_{2S'x})^{-1} L'_0 R'_0 R'_{S'x} y$” for some $x,y,z \in N$.

Furthermore, the following axioms are satisfied:

- (i”) $L'_0 x$ is defined and equal to $y$, then we have the identities [(6)](README.md), [(7)](README.md) for all $n\in \mathbb{Z}$.
- (S) If $S'x$ is defined for some $x \in N$, then $S'y$ is defined for all $y \leq x$.
- (iii”) If $R'_a x = y$ for some $a \in SM$ and some $x,y \in N$, and $S'x, S'y$ are defined, then $(R'_{S'y})^{-1} L'_0 R'_{2S'y} (R'_{a-S'x})^{-1} L'_0 R'_{2(a-S'x)} y$ is defined and equal to $x$.
- (iv”) If $x \in N$ is such that $S'x$ is defined, then $(R'_{S'x})^{-1} L'_0 R'_{2S'x} (R'_{S'x})^{-1} L'_0 R'_{2S'x} x$ is defined and equal to $x$.
- (v”) If $x \in N$ and $x \diamond' x$ is defined, then $S'x$ is defined and equal to $x \diamond' x$.
- (vi”) For all $y \in N$ and $a \in SM$, if $R'_a y \diamond' y$ is defined, then $a - S'y$ is defined and equal to $R'_a y \diamond' y$.
- (vii”) For all $x,y \in N$ and $x$ is not equal to $y$ or $R'_a y$ for any $a \in SM$, and $x \diamond' y$ is defined, then it is equal to some $z \in N$. Furthermore, either $I[x,y,z]$ is a pending identity, or else $z \diamond' x$ and $(R'_{2S'x})^{-1} L'_0 R'_0 R'_{S'x} y$ are defined and equal to each other.
- (P) If $I[x,y,z]$ is a pending identity, then $x,y,z \in N$, and $Sx$ and $z \diamond' x$ are undefined. Furthermore, $z$ is not equal to $x$ or $R'_a x$ for any $a \in SM$, and $y$ is not of the form $(R'_0)^n x$ or $(R'_0)^n y_0$ for any $n$, where $y_0$ is the parent of $x$.
- (P') If $I[x,y,z]$ and $I[x,y',z]$ are pending identities, then $y=y'$.
- (P”) If $I[x,y,z]$ is a pending identity, then $x \diamond' y = z$.
- (L) If $y$ is the parent of $x$ with $x = R'_a y$, and $(R'_{a-S'y})^{-1} L'_0 R'_{2(a-S'y)} x$ is defined, then it is not equal to $x$.

We say that one partial solution $(\tilde L'_0, \tilde \diamond', \tilde S', \tilde {\mathcal I})$ *extends* another if $(L'_0, \diamond', S', {\mathcal I})$ if $\tilde L'$ is an extension of $L'_0$, $\tilde \diamond'$ is an extension of $\diamond'$, and $\tilde S'$ is an extension of $S'$. (No constraint is imposed on the final components $\tilde {\mathcal I}, {\mathcal I}$.) This is a preordering.

## Depends on

- [Definition of $SM$](sm-def.md)
- [Definition of $N$](n-def.md)

## Lean

Formalized as [`Eq1729.PartialSolution`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1729.PartialSolution).

## Sources

- [Equational Theories blueprint: chapter/1729.tex, line 156](https://github.com/teorth/equational_theories/blob/8b87204d5b201e1cf6c69b8dcabb0558109bee00/blueprint/src/chapter/1729.tex#L156)
