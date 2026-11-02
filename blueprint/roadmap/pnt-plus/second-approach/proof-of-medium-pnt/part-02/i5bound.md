---
declaration: lemma
origin: cited
lean: I5Bound
statement: formalized
proof: formalized
---

# I5Bound

We have that

$$
\left|I_5(\nu,\epsilon,X,\sigma_2)\right|\ll\frac{X^{\sigma_2}}{\epsilon}.
$$

## Depends on

- [I₅](../part-01/i5.md)

## Proof depends on

- [Smooth1](../../mellin-transforms/part-01/smooth1.md)
- [MellinOfSmooth1b](../../mellin-transforms/part-01/mellinofsmooth1b.md)

## Proof

Here $\zeta'/\zeta$ is absolutely bounded on the compact interval $\sigma_2 + i [-3,3]$, and $X^s$ is bounded by $X^{\sigma_2}$. Using Theorem [MellinOfSmooth1b](../../mellin-transforms/part-01/mellinofsmooth1b.md) gives the bound $1/(\epsilon |s|^2)$, which is bounded by $C'/\epsilon$. Putting these together gives the result.

## Lean

Formalized as [`I5Bound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/I5Bound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MediumPNT.lean)
