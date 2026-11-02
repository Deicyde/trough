---
declaration: lemma
origin: cited
lean: SmoothedChebyshevDirichlet_aux_tsum_integral
statement: formalized
proof: formalized
---

# SmoothedChebyshevDirichlet-aux-tsum-integral

Fix a nonnegative, continuously differentiable function $F$ on $\mathbb{R}$ with support in $[1/2,2]$, and total mass one, $\int_{(0,\infty)} F(x)/x dx = 1$. Then for any $\epsilon>0$ and $\sigma\in(1,2]$, the function $x \mapsto \sum_{n=1}^\infty \frac{\Lambda(n)}{n^{\sigma+it}} \mathcal{M}(\widetilde{1_{\epsilon}})(\sigma+it) x^{\sigma+it}$ is equal to $\sum_{n=1}^\infty \int_{(0,\infty)} \frac{\Lambda(n)}{n^{\sigma+it}} \mathcal{M}(\widetilde{1_{\epsilon}})(\sigma+it) x^{\sigma+it}$.

## Depends on

- [Smooth1](../../mellin-transforms/part-01/smooth1.md)

## Proof depends on

- [Smooth1Nonneg](../../mellin-transforms/part-01/smooth1nonneg.md)
- [Smooth1Properties-above](../../mellin-transforms/part-01/smooth1properties-above.md)
- [Smooth1ContinuousAt](../../mellin-transforms/part-01/smooth1continuousat.md)
- [SmoothedChebyshevDirichlet-aux-integrable](smoothedchebyshevdirichlet-aux-integrable.md)
- [Smooth1LeOne](../../mellin-transforms/part-01/smooth1leone.md)

## Proof

Interchange of summation and integration.

## Lean

Formalized as [`SmoothedChebyshevDirichlet_aux_tsum_integral`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/SmoothedChebyshevDirichlet_aux_tsum_integral).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MediumPNT.lean)
