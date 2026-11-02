---
declaration: lemma
origin: cited
lean: SmoothedChebyshevDirichlet_aux_integrable
statement: formalized
proof: formalized
---

# SmoothedChebyshevDirichlet-aux-integrable

Fix a nonnegative, continuously differentiable function $F$ on $\mathbb{R}$ with support in $[1/2,2]$, and total mass one, $\int_{(0,\infty)} F(x)/x dx = 1$. Then for any $\epsilon>0$, and $\sigma\in (1, 2]$, the function

$$
x \mapsto\mathcal{M}(\widetilde{1_{\epsilon}})(\sigma + ix)
$$

is integrable on $\mathbb{R}$.

## Depends on

- [Smooth1](../../mellin-transforms/part-01/smooth1.md)

## Proof depends on

- [Smooth1Nonneg](../../mellin-transforms/part-01/smooth1nonneg.md)
- [Smooth1Properties-above](../../mellin-transforms/part-01/smooth1properties-above.md)
- [Smooth1ContinuousAt](../../mellin-transforms/part-01/smooth1continuousat.md)
- [Smooth1LeOne](../../mellin-transforms/part-01/smooth1leone.md)
- [MellinOfSmooth1b](../../mellin-transforms/part-01/mellinofsmooth1b.md)

## Proof

By Lemma [MellinOfSmooth1b](../../mellin-transforms/part-01/mellinofsmooth1b.md) the integrand is $O(1/t^2)$ as $t\rightarrow \infty$ and hence the function is integrable.

## Lean

Formalized as [`SmoothedChebyshevDirichlet_aux_integrable`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/SmoothedChebyshevDirichlet_aux_integrable).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MediumPNT.lean)
