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

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 153](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/distance.tex#L153)
