---
declaration: theorem
origin: cited
lean: TauCeti.gaussNorm_amiceRadius_le_amiceDualNorm
statement: formalized
proof: formalized
---

# `S_h ≤ D_h`

The Gauss norm at the radius `r_h` is at most the dual stage norm at level
`h`, provided the latter is the supremum of a bounded family.

```lean
TauCeti.gaussNorm_amiceRadius_le_amiceDualNorm.{u_1} {p : ℕ} [hp : Fact (Nat.Prime p)]
  {K : Type u_1} [NormedRing K] {F : PowerSeries K} {h : ℕ}
  (hF : BddAbove (Set.range fun n => ‖(PowerSeries.coeff n) F‖ * ‖↑(n / p ^ h).factorial‖)) :
  PowerSeries.gaussNorm norm (TauCeti.amiceRadius p h) F ≤ TauCeti.amiceDualNorm p h F
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.gaussNorm_amiceRadius_le_amiceDualNorm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Norm.html#TauCeti.gaussNorm_amiceRadius_le_amiceDualNorm).

## Sources

- [Tau Ceti documentation: `TauCeti.gaussNorm_amiceRadius_le_amiceDualNorm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Norm.html#TauCeti.gaussNorm_amiceRadius_le_amiceDualNorm)
- [Source of `TauCeti.gaussNorm_amiceRadius_le_amiceDualNorm` in TauCeti/NumberTheory/Padics/Distribution/Amice/Norm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/Distribution/Amice/Norm.lean#L287)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
