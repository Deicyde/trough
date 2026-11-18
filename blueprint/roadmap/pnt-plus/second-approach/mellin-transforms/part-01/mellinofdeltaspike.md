---
declaration: theorem
origin: cited
lean: MellinOfDeltaSpike
statement: formalized
proof: formalized
---

# MellinOfDeltaSpike

For any $\epsilon>0$, the Mellin transform of $\nu_\epsilon$ is

$$
\mathcal{M}(\nu_\epsilon)(s) = \mathcal{M}(\nu)\left(\epsilon s\right).
$$

## Depends on

- [DeltaSpike](deltaspike.md)

## Proof

Substitute $y=x^{1/\epsilon}$, use Haar measure; direct calculation.

## Lean

Formalized as [`MellinOfDeltaSpike`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/MellinOfDeltaSpike).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MellinCalculus.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/MellinCalculus.lean)
