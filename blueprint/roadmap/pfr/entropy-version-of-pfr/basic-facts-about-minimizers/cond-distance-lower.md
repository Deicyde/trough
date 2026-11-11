---
declaration: lemma
origin: cited
lean: condRuzsaDistance_ge_of_min
statement: formalized
proof: formalized
---

# Conditional distance lower bound

For any $G$-valued random variables $X'_1,X'_2$ and random variables $Z,W$, one has

$$
d[X'_1|Z;X'_2|W] \geq k - \eta (d[X^0_1;X'_1|Z] - d[X^0_1;X_1] ) - \eta (d[X^0_2;X'_2|W] - d[X^0_2;X_2] ).
$$

## Depends on

- [$\tau$-minimizer](../tau-min-def.md)
- [Conditioned Ruzsa distance](../../entropic-ruzsa-calculus/part-01/cond-dist-def.md)

## Proof depends on

- [Distance lower bound](distance-lower.md)

## Proof

Apply [Distance lower bound](distance-lower.md) to conditioned random variables and then average.

## Lean

Formalized as [`condRuzsaDistance_ge_of_min`](https://teorth.github.io/pfr/docs/find/#doc/condRuzsaDistance_ge_of_min).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 60](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy_pfr.tex#L60)
