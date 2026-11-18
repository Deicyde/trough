---
declaration: theorem
origin: cited
lean: ShiftZeroBound
statement: formalized
proof: formalized
---

# ShiftZeroBound

For all $\delta\in(0,1)$ we have

$$
-\Re \left(\frac{\zeta'}{\zeta}(1+\delta)\right)\leq\frac{1}{\delta}+O(1).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [BddAbove-to-IsBigO](../../../second-approach/zeta-bounds/part-01/bddabove-to-isbigo.md)
- [riemannZetaLogDerivResidue](../../../second-approach/zeta-bounds/part-01/riemannzetalogderivresidue.md)

## Proof

From Theorem [riemannZetaLogDerivResidue](../../../second-approach/zeta-bounds/part-01/riemannzetalogderivresidue.md) we know that

$$
-\frac{\zeta'}{\zeta}(s)=\frac{1}{s-1}+O(1).
$$

Changing variables $s\mapsto 1+\delta$ and applying the triangle inequality we have that

$$
-\Re \left(\frac{\zeta'}{\zeta}(1+\delta)\right)\leq\left|
-\frac{\zeta'}{\zeta}(1+\delta)\right|\leq\frac{1}{\delta}+O(1).
$$

## Lean

Formalized as [`ShiftZeroBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ShiftZeroBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/StrongPNT.lean)
