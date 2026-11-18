---
declaration: theorem
origin: cited
lean: ZetaAltFormula
statement: formalized
proof: formalized
---

# ZetaAltFormula

We have that

$$
\zeta(s)=\zeta_1(s)
$$

for all $s\in S$ with $S=\{s\in\mathbb{C}:0\lt \mathfrak{R}s,\,s\neq 1\}$.

## Depends on

- [riemannZeta1](riemannzeta1.md)

## Proof depends on

- [riemannZeta0](../../../second-approach/zeta-bounds/part-01/riemannzeta0.md)
- [Zeta1AltFormula](zeta1altformula.md)
- [Zeta0EqZeta](../../../second-approach/zeta-bounds/part-02/zeta0eqzeta.md)

## Proof

This immediately follows from Lemmas [Zeta1AltFormula](zeta1altformula.md) and [Zeta0EqZeta](../../../second-approach/zeta-bounds/part-02/zeta0eqzeta.md).

## Lean

Formalized as [`ZetaAltFormula`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaAltFormula).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/StrongPNT.lean)
