---
declaration: definition
origin: cited
lean: Smooth1
statement: formalized
proof: formalized
---

# Smooth1

Let $\epsilon>0$. Then we define the smooth function $\widetilde{1_{\epsilon}}$ from $\mathbb{R}_{>0}$ to $\mathbb{C}$ by

$$
\widetilde{1_{\epsilon}} = 1_{(0,1]}\ast\nu_\epsilon.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [DeltaSpike](deltaspike.md)
- [MellinConvolution](mellinconvolution.md)

## Proof

Let $c:=2^\epsilon > 1$, in terms of which we wish to prove

$$
-1 < c \log c - c .
$$

Letting $f(x):=x\log x - x$, we can rewrite this as $f(1) < f(c)$. Since

$$
\frac {d}{dx}f(x) = \log x > 0 ,
$$

$f$ is monotone increasing on [1, $\infty$), and we are done.

## Lean

Formalized as [`Smooth1`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Smooth1).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MellinCalculus.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MellinCalculus.lean)
