---
declaration: lemma
origin: cited
lean: MellinOfSmooth1c
statement: formalized
proof: formalized
---

# MellinOfSmooth1c

At $s=1$, we have

$$
\mathcal{M}(\widetilde{1_{\epsilon}})(1) = 1+O(\epsilon)).
$$

## Depends on

- [Smooth1](smooth1.md)

## Proof depends on

- [MellinOfDeltaSpikeAt1-asymp](mellinofdeltaspikeat1-asymp.md)
- [MellinOfSmooth1a](mellinofsmooth1a.md)

## Proof

Follows from Lemmas [MellinOfSmooth1a](mellinofsmooth1a.md), [MellinOfDeltaSpikeAt1](mellinofdeltaspikeat1.md) and [MellinOfDeltaSpikeAt1-asymp](mellinofdeltaspikeat1-asymp.md).

## Lean

Formalized as [`MellinOfSmooth1c`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/MellinOfSmooth1c).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MellinCalculus.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/MellinCalculus.lean)
