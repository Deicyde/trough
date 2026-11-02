---
declaration: theorem
origin: cited
lean: MellinOfPsi
statement: formalized
proof: formalized
---

# MellinOfPsi

The Mellin transform of $\nu$ is

$$
\mathcal{M}(\nu)(s) =  O\left(\frac{1}{|s|}\right),
$$

as $|s|\to\infty$ with $\sigma_1 \le \Re(s) \le 2$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [PartialIntegration](partialintegration.md)

## Proof

Integrate by parts:

$$
\left|\int_0^\infty \nu(x)x^s\frac{dx}{x}\right| =
\left|-\int_0^\infty \nu'(x)\frac{x^{s}}{s}dx\right|
$$

$$
\le \frac{1}{|s|} \int_{1/2}^2|\nu'(x)|x^{\Re(s)}dx.
$$

Since $\Re(s)$ is bounded, the right-hand side is bounded by a constant times $1/|s|$.

## Lean

Formalized as [`MellinOfPsi`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/MellinOfPsi).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MellinCalculus.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MellinCalculus.lean)
