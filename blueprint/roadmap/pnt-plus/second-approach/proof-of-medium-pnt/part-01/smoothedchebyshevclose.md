---
declaration: theorem
origin: cited
lean: SmoothedChebyshevClose
statement: formalized
proof: formalized
---

# SmoothedChebyshevClose

We have that

$$
\psi_{\epsilon}(X) = \psi(X) + O(\epsilon X \log X).
$$

## Depends on

- [SmoothedChebyshev](smoothedchebyshev.md)

## Proof depends on

- [Smooth1Nonneg](../../mellin-transforms/part-01/smooth1nonneg.md)
- [SmoothedChebyshevDirichlet](smoothedchebyshevdirichlet.md)
- [Smooth1Properties-above](../../mellin-transforms/part-01/smooth1properties-above.md)
- [Smooth1Properties-below](../../mellin-transforms/part-01/smooth1properties-below.md)
- [Smooth1](../../mellin-transforms/part-01/smooth1.md)
- [Smooth1LeOne](../../mellin-transforms/part-01/smooth1leone.md)

## Proof

Take the difference. By Lemma [Smooth1Properties-above](../../mellin-transforms/part-01/smooth1properties-above.md) and [Smooth1Properties-below](../../mellin-transforms/part-01/smooth1properties-below.md), the sums agree except when $1-c \epsilon \leq n/X \leq 1+c \epsilon$. This is an interval of length $\ll \epsilon X$, and the summands are bounded by $\Lambda(n) \ll \log X$.

## Lean

Formalized as [`SmoothedChebyshevClose`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/SmoothedChebyshevClose).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MediumPNT.lean)
