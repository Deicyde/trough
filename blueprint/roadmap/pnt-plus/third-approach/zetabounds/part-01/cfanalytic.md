---
declaration: lemma
origin: cited
lean: CfAnalytic
statement: formalized
proof: formalized
---

# CfAnalytic

If $f:\mathbb{C}\to\mathbb{C}$ is analytic on $\overline{\mathbb{D}_1}$ then so too is $C_f$.

## Depends on

- [CFunction](cfunction.md)

## Proof depends on

- [ZeroFactorization](zerofactorization.md)
- [SetOfZeros](setofzeros.md)
- [ZeroFactor](zerofactor.md)

## Proof

Look at the definition of $C_f$ and apply ZeroFactorization.

## Lean

Formalized as [`CfAnalytic`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/CfAnalytic).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/StrongPNT.lean)
