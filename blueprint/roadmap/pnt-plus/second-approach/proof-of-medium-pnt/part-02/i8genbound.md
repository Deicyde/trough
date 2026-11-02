---
declaration: lemma
origin: cited
lean: I8GenBound
statement: formalized
proof: formalized
---

# I8GenBound

Assuming a bound of the form of Definition [LogDerivZetaHasBound](../part-01/logderivzetahasbound.md), we have that

$$
\left|I_8(\nu,\epsilon,X,T)\right|\ll\frac{X}{\epsilon T}.
$$

## Depends on

- [LogDerivZetaHasBound](../part-01/logderivzetahasbound.md)
- [I₈](../part-01/i8.md)

## Proof depends on

- [I₂](../part-01/i2.md)
- [I2GenBound](i2genbound.md)
- [I8I2](i8i2.md)

## Proof

We deduce this from the corresponding bound for $I_2$, using the symmetry between $I_2$ and $I_8$.

## Lean

Formalized as [`I8GenBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/I8GenBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MediumPNT.lean)
