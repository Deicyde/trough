---
declaration: corollary
origin: cited
lean: rdist_of_hom_le
statement: formalized
proof: formalized
---

# fibring-ineq

If $\pi:G\to H$ is a homomorphism of additive groups and $X,Y$ are $G$-valued random variables then

$$
d[X;Y]\geq d[\pi(X);\pi(Y)].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [General fibring identity](fibring-ident.md)
- [Distance nonnegative](../entropic-ruzsa-calculus/part-01/ruzsa-nonneg.md)

## Proof

By [General fibring identity](fibring-ident.md) and the nonnegativity of conditional Ruzsa distance (from [Distance nonnegative](../entropic-ruzsa-calculus/part-01/ruzsa-nonneg.md)) we have

$$
d[X;Y]\geq d[\pi(X);\pi(Y)]+d[X\mid \pi(X);Y\mid \pi(Y)].
$$

The inequality follows from $d[X\mid \pi(X);Y\mid \pi(Y)]\geq 0$ ([Distance nonnegative](../entropic-ruzsa-calculus/part-01/ruzsa-nonneg.md)).

## Lean

Formalized as [`rdist_of_hom_le`](https://teorth.github.io/pfr/docs/find/#doc/rdist_of_hom_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/fibring.tex, line 37](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/fibring.tex#L37)
