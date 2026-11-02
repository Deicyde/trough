---
declaration: lemma
origin: cited
lean: Perron.integralPosAux
statement: formalized
proof: formalized
---

# integralPosAux

The integral

$$
\int_\mathbb{R}\frac{1}{|(1+t^2)(2+t^2)|^{1/2}}dt
$$

is positive (and hence convergent - since a divergent integral is zero in Lean, by definition).

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This integral is between $\frac{1}{2}$ and $1$ of the integral of $\frac{1}{1+t^2}$, which is $\pi$.

## Lean

Formalized as [`Perron.integralPosAux`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Perron.integralPosAux).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/PerronFormula.lean)
