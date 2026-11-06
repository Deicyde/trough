---
declaration: theorem
origin: cited
lean: IsDedekindDomain.FiniteAdeleRing.baseChangeAlgEquiv
statement: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/243
---

# IsDedekindDomain.FiniteAdeleRing.baseChangeAlgEquiv

This natural map $L\otimes_K\mathbb{A}_{A,K}^\infty\to\mathbb{A}_{B,L}^\infty$ is an isomorphism.

## Depends on

- [IsDedekindDomain.HeightOneSpectrum.range\_baseChange\_comp\_tensorAdicCompletionTo\_eq\_pi](isdedekinddomain-heightonespectrum-range-basecha.md)
- [IsDedekindDomain.AKLB.tensorProduct\_module\_algEquiv](isdedekinddomain-aklb-tensorproduct-module-algeq.md)

## Proof

Follows immediately from theorem [IsDedekindDomain.FiniteAdeleRing.baseChangeIntegralAlgEquiv](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L579) and theorem [IsDedekindDomain.AKLB.tensorProduct\_module\_algEquiv](isdedekinddomain-aklb-tensorproduct-module-algeq.md).

## Lean

Formalized as [`IsDedekindDomain.FiniteAdeleRing.baseChangeAlgEquiv`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/IsDedekindDomain.FiniteAdeleRing.baseChangeAlgEquiv).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 388](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L388)
