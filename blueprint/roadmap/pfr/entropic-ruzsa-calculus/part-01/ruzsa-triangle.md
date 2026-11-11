---
declaration: lemma
origin: cited
lean: rdist_triangle
statement: formalized
proof: formalized
---

# Ruzsa triangle inequality

If $X,Y,Z$ are $G$-valued random variables, then

$$
d[X ;Y] \leq d[X ;Z] + d[Z;Y].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Copy preserves Ruzsa distance](ruz-copy.md)
- [Ruzsa distance in independent case](ruz-indep.md)
- [Existence of independent copies](independent-exist.md)
- [Improved Ruzsa triangle inequality](ruzsa-triangle-improved.md)

## Proof

By [Copy preserves Ruzsa distance](ruz-copy.md) and Lemmas [Existence of independent copies](independent-exist.md), [Ruzsa distance in independent case](ruz-indep.md), it suffices to prove this inequality assuming that $X,Y,Z$ are defined on the same space and are independent. But then the claim follows from [Improved Ruzsa triangle inequality](ruzsa-triangle-improved.md) and [Ruzsa distance](ruz-dist-def.md).

## Lean

Formalized as [`rdist_triangle`](https://teorth.github.io/pfr/docs/find/#doc/rdist_triangle).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 211](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/distance.tex#L211)
