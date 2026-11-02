---
declaration: lemma
origin: cited
lean: DeltaSpikeMass
statement: formalized
proof: formalized
---

# DeltaSpikeMass

For any $\epsilon>0$, we have

$$
\int_0^\infty \nu_\epsilon(x)\frac{dx}{x} = 1.
$$

## Depends on

- [DeltaSpike](deltaspike.md)

## Proof

Substitute $y=x^{1/\epsilon}$, and use the fact that $\nu$ has mass one, and that $dx/x$ is Haar measure.

## Lean

Formalized as [`DeltaSpikeMass`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/DeltaSpikeMass).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MellinCalculus.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MellinCalculus.lean)
