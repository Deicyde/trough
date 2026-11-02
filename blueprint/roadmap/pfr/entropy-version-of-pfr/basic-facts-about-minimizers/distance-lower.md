---
declaration: lemma
origin: cited
lean: distance_ge_of_min
statement: formalized
proof: formalized
---

# Distance lower bound

For any $G$-valued random variables $X'_1,X'_2$, one has

$$
d[X'_1;X'_2] \geq k - \eta (d[X^0_1;X'_1] - d[X^0_1;X_1] ) - \eta (d[X^0_2;X'_2] - d[X^0_2;X_2] ).
$$

## Depends on

- [$\tau$-minimizer](../tau-min-def.md)

## Proof depends on

- [$\tau$ functional](../tau-def.md)
- [$\tau$ has minimum](../tau-min.md)

## Proof

Immediate from [$\tau$ functional](../tau-def.md) and [$\tau$ has minimum](../tau-min.md).

## Lean

Formalized as [`distance_ge_of_min`](https://teorth.github.io/pfr/docs/find/#doc/distance_ge_of_min).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 48](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy_pfr.tex#L48)
