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

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 153](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/distance.tex#L153)
