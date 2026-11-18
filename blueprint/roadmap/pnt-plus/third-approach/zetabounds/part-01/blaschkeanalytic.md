---
declaration: lemma
origin: cited
lean: BlaschkeAnalytic
statement: formalized
proof: formalized
---

# BlaschkeAnalytic

If $f:\mathbb{C}\to\mathbb{C}$ is analytic on $\overline{\mathbb{D}_R}$ then so too is $B_f$.

## Depends on

- [BlaschkeB](blaschkeb.md)
- [SetOfZeros](setofzeros.md)

## Proof depends on

- [CFunction](cfunction.md)
- [CfAnalytic](cfanalytic.md)

## Proof

Expand out $B_f$ as a product, and observe that each part is analytic on $\overline{\mathbb{D}_R}$.

## Lean

Formalized as [`BlaschkeAnalytic`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/BlaschkeAnalytic).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/StrongPNT.lean)
