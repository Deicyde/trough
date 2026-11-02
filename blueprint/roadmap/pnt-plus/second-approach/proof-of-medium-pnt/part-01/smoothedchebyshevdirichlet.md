---
declaration: theorem
origin: cited
lean: SmoothedChebyshevDirichlet
statement: formalized
proof: formalized
---

# SmoothedChebyshevDirichlet

We have that

$$
\psi_{\epsilon}(X) = \sum_{n=1}^\infty \Lambda(n)\widetilde{1_{\epsilon}}(n/X).
$$

## Depends on

- [SmoothedChebyshev](smoothedchebyshev.md)
- [Smooth1](../../mellin-transforms/part-01/smooth1.md)

## Proof depends on

- [Smooth1Nonneg](../../mellin-transforms/part-01/smooth1nonneg.md)
- [Smooth1Properties-above](../../mellin-transforms/part-01/smooth1properties-above.md)
- [Smooth1ContinuousAt](../../mellin-transforms/part-01/smooth1continuousat.md)
- [SmoothedChebyshevDirichlet-aux-integrable](smoothedchebyshevdirichlet-aux-integrable.md)
- [LogDerivativeDirichlet](logderivativedirichlet.md)
- [Smooth1LeOne](../../mellin-transforms/part-01/smooth1leone.md)
- [SmoothedChebyshevDirichlet-aux-tsum-integral](smoothedchebyshevdirichlet-aux-tsum-integral.md)

## Proof

We have that

$$
\psi_{\epsilon}(X) = \frac{1}{2\pi i}\int_{(2)}\sum_{n=1}^\infty \frac{\Lambda(n)}{n^s}
\mathcal{M}(\widetilde{1_{\epsilon}})(s)
X^{s}ds.
$$

We have enough decay (thanks to quadratic decay of $\mathcal{M}(\widetilde{1_{\epsilon}})$) to justify the interchange of summation and integration. We then get

$$
\psi_{\epsilon}(X) =
\sum_{n=1}^\infty \Lambda(n)\frac{1}{2\pi i}\int_{(2)}
\mathcal{M}(\widetilde{1_{\epsilon}})(s)
(n/X)^{-s}
ds
$$

and apply the Mellin inversion formula.

## Lean

Formalized as [`SmoothedChebyshevDirichlet`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/SmoothedChebyshevDirichlet).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MediumPNT.lean)
