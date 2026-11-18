---
declaration: lemma
origin: cited
lean: SmoothedChebyshevPull1_aux_integrable
statement: formalized
proof: formalized
---

# SmoothedChebyshevPull1-aux-integrable

The integrand

$$
\zeta'(s)/\zeta(s)\mathcal{M}(\widetilde{1_{\epsilon}})(s)X^{s}
$$

is integrable on the contour $\sigma_0 + t i$ for $t \in \mathbb{R}$ and $\sigma_0 > 1$.

## Depends on

- [Smooth1](../../mellin-transforms/part-01/smooth1.md)

## Proof depends on

- [dlog-riemannZeta-bdd-on-vertical-lines](dlog-riemannzeta-bdd-on-vertical-lines.md)
- [SmoothedChebyshevDirichlet-aux-integrable](smoothedchebyshevdirichlet-aux-integrable.md)

## Proof

The $\zeta'(s)/\zeta(s)$ term is bounded, as is $X^s$, and the smoothing function $\mathcal{M}(\widetilde{1_{\epsilon}})(s)$ decays like $1/|s|^2$ by Theorem [MellinOfSmooth1b](../../mellin-transforms/part-01/mellinofsmooth1b.md). Actually, we already know that $\mathcal{M}(\widetilde{1_{\epsilon}})(s)$ is integrable from Theorem [SmoothedChebyshevDirichlet-aux-integrable](smoothedchebyshevdirichlet-aux-integrable.md), so we should just need to bound the rest.

## Lean

Formalized as [`SmoothedChebyshevPull1_aux_integrable`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/SmoothedChebyshevPull1_aux_integrable).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/MediumPNT.lean)
