---
declaration: lemma
origin: cited
lean: Perron.vertIntBound
statement: formalized
proof: formalized
---

# vertIntBound

Let $x>0$ and $\sigma>1$. Then

$$
\left|
\int_{(\sigma)}\frac{x^s}{s(s+1)}ds\right| \leq
x^\sigma \int_\mathbb{R}\frac{1}{|(1+t ^ 2)(2+t ^ 2)|^{1/2}}dt.
$$

## Depends on

- [VerticalIntegral](../../residue-calculus-on-rectangles/verticalintegral.md)

## Proof depends on

- [integralPosAux](integralposaux.md)

## Proof

Triangle inequality and pointwise estimate.

## Lean

Formalized as [`Perron.vertIntBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Perron.vertIntBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/PerronFormula.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/PerronFormula.lean)
