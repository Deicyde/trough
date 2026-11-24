---
declaration: lemma
origin: cited
lean: rdist_nonneg
statement: formalized
proof: formalized
---

# Distance nonnegative

If $X,Y$ are $G$-valued random variables, then

$$
d[X ;Y] \geq 0.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Distance controls entropy difference](ruzsa-diff.md)

## Proof

Immediate from [Distance controls entropy difference](ruzsa-diff.md).

## Lean

Formalized as [`rdist_nonneg`](https://teorth.github.io/pfr/docs/find/#doc/rdist_nonneg).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 153](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/distance.tex#L153)
