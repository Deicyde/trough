---
declaration: lemma
origin: cited
lean: Real.log_le_const_mul_rpow
statement: formalized
proof: formalized
---

# Real.log-le-const-mul-rpow

For all $0\lt c$ and $0\lt x$ we have that

$$
\log x\leq cx^{1/c}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By `Real.log_le_sub_one_of_pos` we know that $\log y\leq y-1$. If we set $y=x^{1/c}$ this becomes

$$
\frac{\log x}{c}\leq x^{1/c}-1.
$$

Multiplying through by $c$ we have

$$
\log x\leq cx^{1/c}-c\leq cx^{1/c}
$$

as desired.

## Lean

Formalized as [`Real.log_le_const_mul_rpow`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Real.log_le_const_mul_rpow).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/MediumPNT.lean)
