---
declaration: definition
origin: cited
lean: SmoothedChebyshev
statement: formalized
---

# SmoothedChebyshev

Fix $\epsilon>0$, and a bumpfunction supported in $[1/2,2]$. Then we define the smoothed Chebyshev function $\psi_{\epsilon}$ from $\mathbb{R}_{>0}$ to $\mathbb{C}$ by

$$
\psi_{\epsilon}(X) = \frac{1}{2\pi i}\int_{(\sigma)}\frac{-\zeta'(s)}{\zeta(s)}
\mathcal{M}(\widetilde{1_{\epsilon}})(s)
X^{s}ds,
$$

where we'll take $\sigma = 1 + 1 / \log X$.

## Depends on

- [Smooth1](../../mellin-transforms/part-01/smooth1.md)
- [VerticalIntegral](../../residue-calculus-on-rectangles/verticalintegral.md)

## Lean

Formalized as [`SmoothedChebyshev`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/SmoothedChebyshev).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/MediumPNT.lean)
