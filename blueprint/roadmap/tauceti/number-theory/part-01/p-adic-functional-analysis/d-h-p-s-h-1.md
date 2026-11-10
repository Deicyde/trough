---
declaration: theorem
origin: cited
lean: TauCeti.amiceDualNorm_le_mul_gaussNorm_amiceRadius_succ
statement: formalized
proof: formalized
---

# `D_h ≤ p S_{h+1}`

The dual stage norm at level `h` is at most `p` times the Gauss norm at
the radius `r_{h+1}`, provided the latter is the supremum of a bounded family.

```lean
TauCeti.amiceDualNorm_le_mul_gaussNorm_amiceRadius_succ.{u_1} {p : ℕ} [hp : Fact (Nat.Prime p)]
  {K : Type u_1} [NormedRing K] {F : PowerSeries K} {h : ℕ}
  (hF : PowerSeries.HasGaussNorm norm (TauCeti.amiceRadius p (h + 1)) F) :
  TauCeti.amiceDualNorm p h F ≤ ↑p * PowerSeries.gaussNorm norm (TauCeti.amiceRadius p (h + 1)) F
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.amiceDualNorm_le_mul_gaussNorm_amiceRadius_succ`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Norm.html#TauCeti.amiceDualNorm_le_mul_gaussNorm_amiceRadius_succ).

## Sources

- [Tau Ceti documentation: `TauCeti.amiceDualNorm_le_mul_gaussNorm_amiceRadius_succ`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Norm.html#TauCeti.amiceDualNorm_le_mul_gaussNorm_amiceRadius_succ)
- [Source of `TauCeti.amiceDualNorm_le_mul_gaussNorm_amiceRadius_succ` in TauCeti/NumberTheory/Padics/Distribution/Amice/Norm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/Distribution/Amice/Norm.lean#L295)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
